#!/usr/bin/env python3
"""Regenerate every generated file from the JSON sources.

Sources of truth:
  data/datasets.json                          global, cross-country datasets
  topics/<topic>/topic.json                   topic title and description
  topics/<topic>/<country>/dataset-NN.json    one file per country-specific dataset
  data/countries.json                         ISO 3166-1 alpha-2 -> display name

Generated (never edit by hand):
  README.md            block between the GENERATED markers
  topics/<topic>/README.md
  data/datasets.csv
  data/country-datasets.csv
"""

from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
TOPICS = ROOT / "topics"
README = ROOT / "README.md"

BEGIN = "<!-- BEGIN GENERATED - edit the JSON sources and run scripts/build.py -->"
END = "<!-- END GENERATED -->"

SUMMARY_BEGIN = "<!-- BEGIN LICENSE-SUMMARY - generated, do not edit -->"
SUMMARY_END = "<!-- END LICENSE-SUMMARY -->"

ACCESS_LABEL = {
    "open": "Direct download",
    "registration": "Free account required",
    "agreement": "Signed agreement required",
    "credentialed": "Credentialed access required",
}
COMMERCIAL_LABEL = {
    "yes": "Commercial use permitted",
    "no": "Non-commercial only",
    "check": "Commercial use: check terms",
}

GLOBAL_COLUMNS = [
    "id", "name", "topic", "url", "description", "provider", "formats",
    "size", "records", "languages", "license", "license_url", "access",
    "commercial_use", "cite",
]
COUNTRY_COLUMNS = [
    "id", "name", "topic", "country", "country_name", "url", "description",
    "provider", "formats", "size", "records", "license", "license_url",
    "access", "commercial_use", "cite", "path",
]


def anchor(title: str) -> str:
    slug = "".join(ch for ch in title.lower() if ch.isalnum() or ch in " -")
    return "#" + slug.replace(" ", "-")


def meta_line(ds: dict) -> str:
    return " · ".join([
        ds["provider"],
        ", ".join(ds["formats"]),
        ds["size"],
        ds["records"],
        f"[{ds['license']}]({ds['license_url']})",
        ACCESS_LABEL[ds["access"]],
        COMMERCIAL_LABEL[ds["commercial_use"]],
    ])


def entry(ds: dict) -> list[str]:
    return [
        f"- [{ds['name']}]({ds['url']}) - {ds['description']}",
        f"  <br><sub>{meta_line(ds)}</sub>",
    ]


def load_country_tree(countries: dict[str, str]) -> list[dict]:
    """Return topics in directory order, each with its countries and datasets."""
    out = []
    for tdir in sorted(TOPICS.iterdir()):
        if not tdir.is_dir():
            continue
        topic = json.loads((tdir / "topic.json").read_text())
        topic["path"] = tdir
        topic["by_country"] = {}
        for cc in topic["countries"]:
            cdir = tdir / cc
            files = sorted(cdir.glob("dataset-*.json"))
            topic["by_country"][cc] = [json.loads(f.read_text()) | {"path": str(f.relative_to(ROOT))}
                                       for f in files]
        out.append(topic)
    return out


def render_root(global_catalog: dict, tree: list[dict], countries: dict[str, str]) -> str:
    by_topic: dict[str, list[dict]] = {}
    for ds in global_catalog["datasets"]:
        by_topic.setdefault(ds["topic"], []).append(ds)

    lines: list[str] = ["## Contents", ""]
    lines.append("**[Global datasets](#global-datasets)** - not tied to one country.")
    lines.append("")
    for topic in global_catalog["topics"]:
        lines.append(f"- [{topic['title']}]({anchor(topic['title'])})")
    lines.append("")
    lines.append("**[By country](#by-country)** - the same domains split by where the data comes from.")
    lines.append("")

    lines.append("## Global datasets")
    lines.append("")
    for topic in global_catalog["topics"]:
        lines.append(f"### {topic['title']}")
        lines.append("")
        lines.append(topic["description"])
        lines.append("")
        for ds in by_topic.get(topic["slug"], []):
            lines.extend(entry(ds))
        lines.append("")

    total = sum(len(v) for t in tree for v in t["by_country"].values())
    lines.append("## By country")
    lines.append("")
    lines.append(
        f"{total} datasets across {len(tree)} topics and {len(countries)} countries, "
        "two countries per topic. Each topic links to its own page."
    )
    lines.append("")
    lines.append("| Topic | Countries | Datasets |")
    lines.append("| --- | --- | --- |")
    for topic in tree:
        names = ", ".join(countries[cc] for cc in topic["countries"])
        n = sum(len(v) for v in topic["by_country"].values())
        lines.append(f"| [{topic['title']}](topics/{topic['slug']}/) | {names} | {n} |")
    lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_topic(topic: dict, countries: dict[str, str]) -> str:
    lines = [f"# {topic['title']}", ""]
    lines.append(f"> {topic['description']}")
    lines.append("")
    lines.append("Part of [Awesome Datasets](../../README.md). "
                 "Entries here are generated from the `dataset-*.json` files in this "
                 "directory - edit those, then run `python3 scripts/build.py`.")
    lines.append("")
    lines.append("## Contents")
    lines.append("")
    for cc in topic["countries"]:
        lines.append(f"- [{countries[cc]}](#{countries[cc].lower().replace(' ', '-')})")
    lines.append("")
    for cc in topic["countries"]:
        lines.append(f"## {countries[cc]}")
        lines.append("")
        for ds in topic["by_country"][cc]:
            lines.extend(entry(ds))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_license_summary(rows: list[dict]) -> str:
    """Live counts, so the warning above cannot drift out of date."""
    com = Counter(r["commercial_use"] for r in rows)
    acc = Counter(r["access"] for r in rows)
    total = len(rows)
    return (
        f"Of the {total} datasets listed here, **{com['yes']} permit commercial use**, "
        f"**{com['no']} are non-commercial only**, and **{com['check']} have mixed or unclear terms** "
        f"that you have to check yourself. {acc['open']} are a direct download, "
        f"{acc['registration']} need a free account, and {acc['agreement']} need a signed agreement."
    )


def write_csv(path: Path, columns: list[str], rows: list[dict]) -> None:
    # lineterminator="\n": the csv module defaults to CRLF per RFC 4180, but
    # .gitattributes normalises *.csv to LF, so writing CRLF makes git warn on
    # every commit. Emit LF directly instead.
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            flat = dict(row)
            for key in ("formats", "languages"):
                if isinstance(flat.get(key), list):
                    flat[key] = "; ".join(flat[key])
            writer.writerow({c: flat.get(c, "") for c in columns})


def main() -> int:
    global_catalog = json.loads((DATA / "datasets.json").read_text())
    countries = json.loads((DATA / "countries.json").read_text())
    tree = load_country_tree(countries)

    country_rows = [
        ds | {"country_name": countries[ds["country"]]}
        for topic in tree for cc in topic["countries"] for ds in topic["by_country"][cc]
    ]
    all_rows = global_catalog["datasets"] + country_rows

    text = README.read_text()
    for marker in (BEGIN, END, SUMMARY_BEGIN, SUMMARY_END):
        if marker not in text:
            print(f"README.md is missing the marker {marker!r}", file=sys.stderr)
            return 1

    head, rest = text.split(BEGIN, 1)
    _, tail = rest.split(END, 1)
    text = f"{head}{BEGIN}\n\n{render_root(global_catalog, tree, countries)}\n{END}{tail}"

    head, rest = text.split(SUMMARY_BEGIN, 1)
    _, tail = rest.split(SUMMARY_END, 1)
    text = f"{head}{SUMMARY_BEGIN}\n{render_license_summary(all_rows)}\n{SUMMARY_END}{tail}"

    README.write_text(text)

    for topic in tree:
        (topic["path"] / "README.md").write_text(render_topic(topic, countries))

    write_csv(DATA / "datasets.csv", GLOBAL_COLUMNS, global_catalog["datasets"])
    write_csv(DATA / "country-datasets.csv", COUNTRY_COLUMNS, country_rows)

    print(f"README.md + {len(tree)} topic pages + 2 CSVs "
          f"({len(global_catalog['datasets'])} global, {len(country_rows)} country datasets)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
