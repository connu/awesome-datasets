#!/usr/bin/env python3
"""Scaffold a new country dataset entry in the right place with the right shape.

Picks the next free dataset number in the target folder so you never renumber
existing files, and never collide with someone else's open pull request.

    python3 scripts/new_dataset.py --topic vehicles-and-car-sales --country in \\
        --name "Vahan Dashboard" --url https://vahan.parivahan.gov.in/vahan4dashboard/

Creating a country folder that does not exist yet requires --new-country, and
a topic that does not exist yet requires --title and --topic-description.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOPICS = ROOT / "topics"
COUNTRIES = ROOT / "data" / "countries.json"

PLACEHOLDER = "TODO"


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def next_number(cdir: Path) -> int:
    used = {int(p.stem.split("-")[1]) for p in cdir.glob("dataset-*.json")}
    n = 1
    while n in used:
        n += 1
    return n


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--topic", required=True, help="topic slug, e.g. vehicles-and-car-sales")
    ap.add_argument("--country", required=True, help="ISO 3166-1 alpha-2, lowercase")
    ap.add_argument("--name", required=True, help="dataset name as its publisher writes it")
    ap.add_argument("--url", required=True, help="https link to the dataset landing page")
    ap.add_argument("--new-country", action="store_true",
                    help="allow creating a country folder that does not exist yet")
    ap.add_argument("--title", help="topic title, required when creating a new topic")
    ap.add_argument("--topic-description", help="topic description, required when creating a new topic")
    args = ap.parse_args()

    if not re.fullmatch(r"[a-z]{2}", args.country):
        print("error: --country must be two lowercase letters", file=sys.stderr)
        return 1
    if not args.url.startswith("https://"):
        print("error: --url must start with https://", file=sys.stderr)
        return 1

    countries = json.loads(COUNTRIES.read_text())
    if args.country not in countries:
        print(f"error: {args.country!r} is not in data/countries.json. "
              "Add it there first, with its display name.", file=sys.stderr)
        return 1

    tdir = TOPICS / args.topic
    topic_file = tdir / "topic.json"
    if not topic_file.exists():
        if not (args.title and args.topic_description):
            print(f"error: topic {args.topic!r} does not exist. To create it, pass "
                  "--title and --topic-description.", file=sys.stderr)
            return 1
        tdir.mkdir(parents=True, exist_ok=True)
        topic = {"slug": args.topic, "title": args.title,
                 "description": args.topic_description, "countries": []}
        print(f"creating new topic {args.topic!r} "
              f"(remember: a topic needs at least two countries)")
    else:
        topic = json.loads(topic_file.read_text())

    cdir = tdir / args.country
    if not cdir.exists():
        if not args.new_country:
            print(f"error: {args.topic}/{args.country} does not exist. "
                  "Pass --new-country to create it.", file=sys.stderr)
            return 1
        cdir.mkdir(parents=True)
    if args.country not in topic["countries"]:
        topic["countries"] = sorted(set(topic["countries"]) | {args.country})
    topic_file.write_text(json.dumps(topic, indent=2, ensure_ascii=False) + "\n")

    n = next_number(cdir)
    out = cdir / f"dataset-{n:02d}.json"
    out.write_text(json.dumps({
        "id": slugify(args.name),
        "name": args.name,
        "topic": args.topic,
        "country": args.country,
        "url": args.url,
        "description": f"{PLACEHOLDER} one sentence saying what the data is, ending in a period.",
        "provider": PLACEHOLDER,
        "formats": [PLACEHOLDER],
        "size": PLACEHOLDER,
        "records": PLACEHOLDER,
        "license": PLACEHOLDER,
        "license_url": args.url,
        "access": "open",
        "commercial_use": "check",
        "cite": PLACEHOLDER,
    }, indent=2, ensure_ascii=False) + "\n")

    print(f"created {out.relative_to(ROOT)}")
    print(f"\nNext: replace every {PLACEHOLDER}, then run")
    print("  python3 scripts/validate.py --links")
    print("  python3 scripts/build.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
