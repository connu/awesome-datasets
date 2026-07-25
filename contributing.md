# Contributing

Thanks for helping keep this list accurate. Corrections are as welcome as additions — licenses get relicensed, portals move, and record counts grow.

## The one rule that catches everyone

**`README.md` and `topics/*/README.md` are generated.** Edits made to them directly are overwritten by the next build. Change the JSON, then run the build.

| To change | Edit |
| --- | --- |
| A global dataset | `data/datasets.json` |
| A country-specific dataset | `topics/<topic>/<country>/dataset-NN.json` |
| A topic's title or blurb | `topics/<topic>/topic.json` |
| A country's display name | `data/countries.json` |

## Adding a country-specific dataset

Let the scaffolder pick the file number so you never collide with an open pull request:

```bash
python3 scripts/new_dataset.py \
  --topic vehicles-and-car-sales --country in \
  --name "Vahan Dashboard" \
  --url https://vahan.parivahan.gov.in/vahan4dashboard/
```

Fill in every `TODO`, then:

```bash
python3 scripts/validate.py --links
python3 scripts/build.py
```

Commit the JSON file **and** the regenerated `README.md`, topic `README.md` and CSVs together. CI fails if they are out of sync.

Adding a new country to an existing topic needs `--new-country`. Adding a whole new topic needs `--title` and `--topic-description`, and the topic must end up with at least two countries before it will validate.

## Adding a global dataset

Append to the `datasets` array in `data/datasets.json`, at the end of the entries for its topic, then run the same two commands.

## What belongs here

- **Publicly obtainable.** Anyone can get it, even if that means a free account or accepting terms. Paywalled or contract-only data does not qualify.
- **Legally distributed.** The host has the right to publish it. Rejected: mirrors of paywalled or licensed content, leaked corpora, and data whose origin nobody will state.
- **Automated collection is not disqualifying on its own.** Projects that systematically gather court filings, election affidavits, company registrations or transit feeds from official sources belong here — public records are published to be used, and the collector is doing the tedious part. Data gathered from a private company's site without its agreement is judged case by case, and needs all three of: a named publisher who stands behind it, a stated license, and established use by researchers or regulators. [Inside Airbnb](https://insideairbnb.com/get-the-data/) is the standing example of something that clears that bar; a one-off anonymous dump of the same data would not.
- **Maintained and documented.** There is a data dictionary, a schema, or a paper describing collection.
- **Substantial.** Widely used as a benchmark, or large and well-constructed enough to be worth someone's bandwidth.
- **Not a duplicate.** One entry per dataset per country. If a better-licensed or better-documented host exists for something already listed, propose swapping the URL rather than adding a second entry.

## Field conventions

- `url` and `license_url` must be **https**. An http-only source is rejected — if the publisher has no TLS, find another host or leave it out.
- `description` is one sentence, starts with a capital, ends with a period, and says what the data *is* — not that it is popular or useful. No marketing language.
- `size` and `records` are approximate and human-readable (`~20 GB`, `2,000,000 functions`). Say what you measured.
- `license` names the actual license, including the awkward cases. `Research use only, no redistribution` is more useful than `Custom`.
- `license_url` points at the terms themselves, not the dataset home page, whenever a distinct terms page exists.
- `commercial_use` is `check` when the dataset bundles third-party content under its original terms. **Do not guess `yes`.**
- `access` is `registration` if a free account is needed, `agreement` if you must sign something, `credentialed` if identity or ethics vetting applies.
- `cite` is the paper or attribution statement the authors request.
- `id` is a lowercase slug, unique within its country folder.

Full field documentation lives in [`data/schema.json`](data/schema.json).

## Country codes

Lowercase ISO 3166-1 alpha-2, and it must already exist in [`data/countries.json`](data/countries.json) — add it there in the same pull request if not. `eu` is used for European Union-wide sources that have no single national publisher.

## Link checking

`scripts/validate.py --links` skips a small allowlist of hosts that block automated clients (Kaggle, FRED, NSE and a few others) and warns rather than fails on 403s and local TLS interception. Those entries are verified by hand. If you add a dataset on a host that blocks bots, say so in the pull request so a reviewer can check it manually.

## Please do not

- Add datasets you have not opened yourself.
- Commit generated files without the JSON change that produced them.
- Renumber existing `dataset-NN.json` files. Gaps are fine.
- Open a pull request that adds more than about ten datasets at once — smaller ones get reviewed faster.

By contributing you agree that your contributions are released under [CC0](license), like the rest of this list.
