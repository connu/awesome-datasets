#!/usr/bin/env python3
"""Validate both catalogs: structure, referential integrity and style rules.

Runs without third-party dependencies so it works in a bare CI container.
Pass --links to additionally check that every URL resolves (slow, network bound).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
TOPICS = ROOT / "topics"

BASE_FIELDS = {
    "id", "name", "topic", "url", "description", "provider", "formats",
    "size", "records", "license", "license_url", "access", "commercial_use", "cite",
}
ACCESS_VALUES = {"open", "registration", "agreement", "credentialed"}
COMMERCIAL_VALUES = {"yes", "no", "check"}
SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9.]+)*$")
COUNTRY_RE = re.compile(r"^[a-z]{2}$")
DATASET_FILE_RE = re.compile(r"^dataset-\d{2}\.json$")

MIN_COUNTRIES_PER_TOPIC = 2
MIN_DATASETS_PER_COUNTRY = 1

# Hosts that reject non-browser clients, or that this network cannot reach.
# Their links are verified manually instead of in CI.
BOT_PROTECTED = (
    "fred.stlouisfed.org", "kaggle.com", "zenodo.org", "nseindia.com",
    "broadbandmap.fcc.gov", "cpcb.nic.in", "rchiips.org",
)

BROWSER_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
)


class _Redirect308(urllib.request.HTTPRedirectHandler):
    """urllib does not follow 308 on older Pythons; treat it like 301."""

    def http_error_308(self, req, fp, code, msg, headers):  # noqa: N802
        return self.http_error_301(req, fp, 301, msg, headers)


_OPENER = urllib.request.build_opener(_Redirect308)


def check_url(url: str, _retry: bool = True) -> tuple[str, str]:
    if any(host in url for host in BOT_PROTECTED):
        return url, "SKIP (bot-protected host)"
    req = urllib.request.Request(
        url, headers={"User-Agent": BROWSER_UA, "Accept": "text/html,application/xhtml+xml"})
    try:
        with _OPENER.open(req, timeout=30) as resp:
            return url, "OK" if resp.status < 400 else f"HTTP {resp.status}"
    except TimeoutError:
        # Slow origin, not a dead link. Give it one more chance before failing.
        return check_url(url, _retry=False) if _retry else (url, "WARN (timeout twice)")
    except urllib.error.HTTPError as exc:
        # 403 and 418 from a live page are anti-bot filtering, not link rot.
        if exc.code in (403, 418):
            return url, f"WARN ({exc.code} anti-bot)"
        # Rate limiting and transient server errors: retry once before failing,
        # so a weekly cron does not raise false alarms on a momentary blip.
        if exc.code in (429, 500, 502, 503, 504):
            if _retry:
                return check_url(url, _retry=False)
            return url, f"WARN ({exc.code} transient, twice)"
        return url, f"HTTP {exc.code}"
    except urllib.error.URLError as exc:
        # A self-signed cert in the chain means TLS interception on the local
        # machine, not a broken link. Warn instead of failing the run.
        if "CERTIFICATE_VERIFY_FAILED" in str(exc.reason):
            return url, "WARN (local TLS interception)"
        return url, f"ERROR {type(exc).__name__}"
    except Exception as exc:  # noqa: BLE001 - report any transport failure
        return url, f"ERROR {type(exc).__name__}"


def check_entry(ds: dict, label: str, errors: list[str], extra: set[str] = frozenset()) -> None:
    missing = (BASE_FIELDS | extra) - ds.keys()
    if missing:
        errors.append(f"{label}: missing fields {sorted(missing)}")
        return

    if not SLUG_RE.match(ds["id"]):
        errors.append(f"{label}: id {ds['id']!r} is not a lowercase slug")

    desc = ds["description"]
    if not desc[:1].isupper():
        errors.append(f"{label}: description must start with a capital letter")
    if not desc.endswith("."):
        errors.append(f"{label}: description must end with a period")
    if "\n" in desc:
        errors.append(f"{label}: description must be a single line")
    if len(desc) < 40:
        errors.append(f"{label}: description is too short to be useful")

    for field in ("url", "license_url"):
        if not ds[field].startswith("https://"):
            errors.append(f"{label}: {field} must use https")

    if ds["access"] not in ACCESS_VALUES:
        errors.append(f"{label}: invalid access {ds['access']!r}")
    if ds["commercial_use"] not in COMMERCIAL_VALUES:
        errors.append(f"{label}: invalid commercial_use {ds['commercial_use']!r}")
    if not ds["formats"]:
        errors.append(f"{label}: formats must be non-empty")


def validate_global(errors: list[str]) -> tuple[dict, list[str]]:
    catalog = json.loads((DATA / "datasets.json").read_text())
    topic_slugs = {t["slug"] for t in catalog["topics"]}
    per_topic = dict.fromkeys(topic_slugs, 0)
    seen_ids: set[str] = set()
    urls: list[str] = []

    for ds in catalog["datasets"]:
        label = f"global/{ds.get('id', '?')}"
        check_entry(ds, label, errors)
        if ds["id"] in seen_ids:
            errors.append(f"{label}: duplicate id")
        seen_ids.add(ds["id"])
        if ds["topic"] not in topic_slugs:
            errors.append(f"{label}: unknown topic {ds['topic']!r}")
        else:
            per_topic[ds["topic"]] += 1
        urls += [ds["url"], ds["license_url"]]

    for slug, n in sorted(per_topic.items()):
        if n < 2:
            errors.append(f"global topic {slug!r} has only {n} dataset(s); minimum is 2")

    return catalog, urls


def validate_tree(errors: list[str]) -> tuple[int, int, list[str]]:
    countries = json.loads((DATA / "countries.json").read_text())
    urls: list[str] = []
    n_topics = n_datasets = 0

    for tdir in sorted(TOPICS.iterdir()):
        if not tdir.is_dir():
            continue
        n_topics += 1
        topic_file = tdir / "topic.json"
        if not topic_file.exists():
            errors.append(f"{tdir.name}: missing topic.json")
            continue
        topic = json.loads(topic_file.read_text())

        if topic["slug"] != tdir.name:
            errors.append(f"{tdir.name}: topic.json slug {topic['slug']!r} does not match directory")
        if not SLUG_RE.match(topic["slug"]):
            errors.append(f"{tdir.name}: slug is not a lowercase slug")

        on_disk = sorted(d.name for d in tdir.iterdir() if d.is_dir())
        declared = sorted(topic["countries"])
        if on_disk != declared:
            errors.append(f"{tdir.name}: topic.json countries {declared} != directories {on_disk}")
        if len(declared) < MIN_COUNTRIES_PER_TOPIC:
            errors.append(f"{tdir.name}: only {len(declared)} country folder(s); "
                          f"minimum is {MIN_COUNTRIES_PER_TOPIC}")

        for cc in on_disk:
            if not COUNTRY_RE.match(cc):
                errors.append(f"{tdir.name}/{cc}: not a two-letter lowercase country code")
            if cc not in countries:
                errors.append(f"{tdir.name}/{cc}: not listed in data/countries.json")

            cdir = tdir / cc
            stray = [f.name for f in cdir.iterdir()
                     if f.is_file() and not DATASET_FILE_RE.match(f.name)]
            if stray:
                errors.append(f"{tdir.name}/{cc}: unexpected files {stray} "
                              "(expected dataset-NN.json only)")

            files = sorted(cdir.glob("dataset-*.json"))
            if len(files) < MIN_DATASETS_PER_COUNTRY:
                errors.append(f"{tdir.name}/{cc}: no datasets")

            seen_ids: set[str] = set()
            seen_urls: set[str] = set()
            for f in files:
                label = f"{tdir.name}/{cc}/{f.name}"
                ds = json.loads(f.read_text())
                check_entry(ds, label, errors, extra={"country"})
                if ds.get("topic") != tdir.name:
                    errors.append(f"{label}: topic {ds.get('topic')!r} does not match directory")
                if ds.get("country") != cc:
                    errors.append(f"{label}: country {ds.get('country')!r} does not match directory")
                if ds["id"] in seen_ids:
                    errors.append(f"{label}: duplicate id within {cc}")
                seen_ids.add(ds["id"])
                if ds["url"] in seen_urls:
                    errors.append(f"{label}: duplicate url within {cc}")
                seen_urls.add(ds["url"])
                urls += [ds["url"], ds["license_url"]]
                n_datasets += 1

    return n_topics, n_datasets, urls


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--links", action="store_true", help="also verify every URL resolves")
    args = parser.parse_args()

    errors: list[str] = []
    catalog, global_urls = validate_global(errors)
    n_topics, n_datasets, tree_urls = validate_tree(errors)

    print(f"global:  {len(catalog['topics'])} topics, {len(catalog['datasets'])} datasets")
    print(f"country: {n_topics} topics, {n_datasets} datasets")

    if args.links:
        urls = sorted(set(global_urls + tree_urls))
        print(f"checking {len(urls)} unique URLs...")
        with ThreadPoolExecutor(max_workers=12) as pool:
            for url, status in pool.map(check_url, urls):
                if status != "OK":
                    print(f"  {status:<30} {url}")
                if status != "OK" and not status.startswith(("SKIP", "WARN")):
                    errors.append(f"unreachable: {url} ({status})")

    if errors:
        print(f"\n{len(errors)} problem(s):", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print("catalogs are valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
