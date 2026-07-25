# Awesome Datasets [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Curated public data for building and evaluating software, with license, size and access terms recorded for every entry.

340 datasets: 40 global ones covering the domains software teams hit constantly — source code, defects, vulnerabilities, network traffic, logs, search, recommendations, forecasting — and 300 more split by country, because "car sales data" means something different in Delhi than in Detroit.

Every entry is a dataset you can actually obtain. The link resolves, the provider is named, and the license and access requirements are stated up front so you can tell before downloading whether you are allowed to use it. This list links and describes; it redistributes no data.

## ⚠️ Read this before you use anything here

**Browsing this list is safe. Using what it points at is where the obligations start.**

This repository contains no data — only links and factual metadata about them. Nothing you do here binds you to anyone's terms. The moment you download a dataset, however, that dataset's license applies to you in full: how you may use it, whether you may redistribute it, and whether you may build a commercial product on it.

<!-- BEGIN LICENSE-SUMMARY - generated, do not edit -->
Of the 340 datasets listed here, **264 permit commercial use**, **23 are non-commercial only**, and **53 have mixed or unclear terms** that you have to check yourself. 279 are a direct download, 59 need a free account, and 2 need a signed agreement.
<!-- END LICENSE-SUMMARY -->

So:

- **Read the license at the source before you build on a dataset**, not before you bookmark it. Terms change without notice and this list can lag behind them.
- **Treat `commercial_use: check` as "no" until you have read the terms.** It means the dataset bundles third-party content under its original license, which is common and easy to get wrong.
- **Non-commercial means non-commercial.** Several widely used entries — MovieLens, MS MARCO, Instacart, Olist among them — are research-only. Training a production model on them is a licensing decision, not a technical one.
- **Attribution is usually mandatory, not polite.** Most open government licenses and every CC BY variant require it. The `cite` field on each entry records what the publisher asks for.

The `license` and `commercial_use` fields are a starting point for your own diligence, not legal advice, and they come with no warranty — see [`license`](license). If an entry is wrong, [tell us](../../issues/new/choose); corrections are as welcome as additions.

<!-- BEGIN GENERATED - edit the JSON sources and run scripts/build.py -->

## Contents

**[Global datasets](#global-datasets)** - not tied to one country.

- [Source Code & Software Repositories](#source-code--software-repositories)
- [Software Defects & Testing](#software-defects--testing)
- [Security & Vulnerabilities](#security--vulnerabilities)
- [Network Traffic & Intrusion Detection](#network-traffic--intrusion-detection)
- [Logs & Observability](#logs--observability)
- [Databases & Query Benchmarking](#databases--query-benchmarking)
- [Web Crawl & Internet-Scale Text](#web-crawl--internet-scale-text)
- [Natural Language Processing](#natural-language-processing)
- [Computer Vision](#computer-vision)
- [Speech & Audio](#speech--audio)
- [Recommender Systems](#recommender-systems)
- [Search & Information Retrieval](#search--information-retrieval)
- [Tabular Machine Learning](#tabular-machine-learning)
- [Time Series & Forecasting](#time-series--forecasting)
- [Fraud & Anomaly Detection](#fraud--anomaly-detection)
- [Graphs & Networks](#graphs--networks)
- [Geospatial & Mapping](#geospatial--mapping)
- [Finance & Economics](#finance--economics)
- [E-commerce & Retail](#e-commerce--retail)
- [Transportation & Mobility](#transportation--mobility)

**[By country](#by-country)** - the same domains split by where the data comes from.

## Global datasets

### Source Code & Software Repositories

Corpora of source code and repository activity used to train code models and study how software is built.

- [CodeSearchNet Corpus](https://github.com/github/CodeSearchNet) - Two million functions from open-source projects in six languages, each paired with its natural-language docstring, for code search and code-summarisation models.
  <br><sub>GitHub · JSONL, GZIP · ~20 GB · 2,000,000 functions · [MIT (tooling); individual functions retain their upstream repository licenses](https://github.com/github/CodeSearchNet/blob/master/LICENSE) · Direct download · Commercial use: check terms</sub>
- [GH Archive](https://www.gharchive.org/) - Every public GitHub event since 2011, archived hourly and queryable in BigQuery, covering pushes, pull requests, issues and stars.
  <br><sub>GH Archive (Ilya Grigorik) · JSON, GZIP, BigQuery · Multi-TB, grows continuously · Billions of events · [MIT (project); event data derived from the GitHub public timeline](https://github.com/igrigorik/gharchive.org/blob/master/LICENSE.md) · Direct download · Commercial use: check terms</sub>

### Software Defects & Testing

Reproducible bugs, regressions and failing builds used for automated program repair, fault localisation and test-generation research.

- [Defects4J](https://github.com/rjust/defects4j) - A reproducible collection of real Java bugs, each with a buggy and fixed revision plus the tests that expose the failure, and a harness that checks out and builds any of them on demand.
  <br><sub>René Just et al. · Git, Java, Shell · ~2 GB after setup · 800+ bugs across 17 open-source Java projects · [MIT](https://github.com/rjust/defects4j/blob/master/license.txt) · Direct download · Commercial use permitted</sub>
- [BugSwarm](https://www.bugswarm.org/) - Fail-pass pairs of real continuous-integration builds packaged as Docker images, so a historical build failure and its fix can be reproduced exactly years later.
  <br><sub>UC Davis DECAL Lab · Docker images, JSON · Varies per artifact · 3,000+ reproducible artifacts · [MIT (client tooling); artifacts retain upstream project licenses](https://github.com/BugSwarm/bugswarm/blob/master/LICENSE) · Direct download · Commercial use: check terms</sub>

### Security & Vulnerabilities

Authoritative feeds of publicly disclosed software vulnerabilities and their severity metadata.

- [NVD Vulnerability Data Feeds](https://nvd.nist.gov/vuln/data-feeds) - The US National Vulnerability Database's enriched view of every CVE, adding CVSS severity scores, CWE weakness classes and CPE product identifiers.
  <br><sub>NIST · JSON, API · ~10 GB uncompressed · 290,000+ CVE records · [US Government public domain](https://nvd.nist.gov/general/FAQ-Sections/General-FAQs) · Direct download · Commercial use permitted</sub>
- [CVE List V5](https://github.com/CVEProject/cvelistV5) - The authoritative CVE Program record set in JSON 5.0 format, published directly to Git so every vulnerability disclosure has a full commit history.
  <br><sub>CVE Program / MITRE · JSON, Git · ~5 GB · 290,000+ CVE records · [CVE Program Terms of Use](https://www.cve.org/Legal/TermsOfUse) · Direct download · Commercial use permitted</sub>

### Network Traffic & Intrusion Detection

Labelled packet captures and flow records used to build and benchmark intrusion detection systems.

- [CIC-IDS2017](https://www.unb.ca/cic/datasets/ids-2017.html) - Five days of realistic background traffic interleaved with labelled brute-force, DoS, web-attack, infiltration and botnet scenarios, published as both raw PCAPs and extracted flow features.
  <br><sub>Canadian Institute for Cybersecurity, University of New Brunswick · PCAP, CSV · ~50 GB · 2,800,000+ labelled flows · [Free for research use with citation](https://www.unb.ca/cic/datasets/ids-2017.html) · Free account required · Non-commercial only</sub>
- [UNSW-NB15](https://research.unsw.edu.au/projects/unsw-nb15-dataset) - Synthetic-but-realistic network traffic covering nine attack families, with 49 engineered flow features and a fixed train/test split that has become a standard IDS benchmark.
  <br><sub>UNSW Canberra Cyber · PCAP, CSV · ~100 GB raw, ~500 MB feature CSVs · 2,540,044 flow records · [Free for academic research with citation](https://research.unsw.edu.au/projects/unsw-nb15-dataset) · Direct download · Non-commercial only</sub>

### Logs & Observability

Production system logs and workload traces for log parsing, anomaly detection and performance benchmarking.

- [Loghub](https://github.com/logpai/loghub) - System logs from distributed systems, supercomputers, operating systems, mobile devices and servers, with hand-labelled templates for a subset, aimed at log parsing and anomaly detection.
  <br><sub>LogPAI · Plain text, CSV · ~77 GB · 16 log collections, billions of lines · [Freely available for research; individual collections retain source terms](https://github.com/logpai/loghub#license) · Direct download · Commercial use: check terms</sub>
- [Elasticsearch Rally Tracks](https://github.com/elastic/rally-tracks) - The standard benchmarking workloads for Elasticsearch, bundling real document corpora such as HTTP server logs, geonames and NYC taxi rides with the query mixes run against them.
  <br><sub>Elastic · JSON, Bzip2 · Up to ~200 GB per track · Varies by track (millions to billions of documents) · [No single license; chosen per track, typically matching the terms of the source data](https://github.com/elastic/rally-tracks) · Direct download · Commercial use: check terms</sub>

### Databases & Query Benchmarking

Standard schemas, data generators and query workloads for comparing analytical and transactional database engines.

- [TPC-H](https://www.tpc.org/tpch/) - The decision-support benchmark that defines a fixed eight-table schema, a scalable data generator and 22 analytical queries, used to compare query engines at scale factors from 1 GB to 100 TB.
  <br><sub>Transaction Processing Performance Council · Data generator (C), SQL · Configurable (1 GB to 100 TB) · ~8.7M rows at scale factor 1 · [TPC End User License Agreement (free download)](https://www.tpc.org/tpc_documents_current_versions/current_specifications5.asp) · Direct download · Commercial use: check terms</sub>
- [ClickBench](https://github.com/ClickHouse/ClickBench) - A single wide table of anonymised web analytics hits plus 43 typical aggregation queries, designed to compare analytical databases on realistic clickstream workloads.
  <br><sub>ClickHouse · Parquet, CSV, TSV · ~15 GB Parquet (~75 GB raw) · 99,997,497 rows · [Apache-2.0](https://github.com/ClickHouse/ClickBench/blob/main/LICENSE) · Direct download · Commercial use permitted</sub>

### Web Crawl & Internet-Scale Text

Petabyte-scale crawls of the public web and the cleaned text corpora derived from them.

- [Common Crawl](https://commoncrawl.org/) - A monthly crawl of the public web hosted free on S3, published as raw WARC responses plus extracted plain text and link graphs, and the upstream source for most open LLM pretraining corpora.
  <br><sub>Common Crawl Foundation · WARC, WET, WAT, Parquet · ~100 TB per monthly crawl · ~3 billion pages per crawl · [Common Crawl Terms of Use](https://commoncrawl.org/terms-of-use) · Direct download · Commercial use: check terms</sub>
- [C4 (Colossal Clean Crawled Corpus)](https://huggingface.co/datasets/allenai/c4) - A heavily filtered English subset of Common Crawl created for training T5, with deduplication, boilerplate removal and language detection already applied.
  <br><sub>Google / AllenAI · JSON, GZIP, Parquet · ~305 GB (en) · ~365 million documents (en) · [ODC-BY 1.0; underlying text subject to Common Crawl terms](https://huggingface.co/datasets/allenai/c4#license) · Direct download · Commercial use: check terms</sub>

### Natural Language Processing

Annotated text corpora for classification, question answering and language-understanding benchmarks.

- [Large Movie Review Dataset (IMDB)](https://ai.stanford.edu/~amaas/data/sentiment/) - Polar movie reviews split evenly into positive and negative classes with a balanced train/test partition, the default smoke test for text classification pipelines.
  <br><sub>Stanford AI Lab · Plain text, TAR.GZ · ~80 MB · 50,000 labelled reviews plus 50,000 unlabelled · [Research use; see dataset README](https://ai.stanford.edu/~amaas/data/sentiment/) · Direct download · Commercial use: check terms</sub>
- [SQuAD 2.0](https://rajpurkar.github.io/SQuAD-explorer/) - Crowd-written questions over Wikipedia paragraphs, combining answerable questions with adversarially written unanswerable ones so models must learn to abstain.
  <br><sub>Stanford NLP Group · JSON · ~45 MB · 150,000 questions (100,000 answerable, 50,000 unanswerable) · [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) · Direct download · Commercial use permitted</sub>

### Computer Vision

Labelled image collections for classification, detection and segmentation.

- [COCO (Common Objects in Context)](https://cocodataset.org/) - Everyday scenes annotated with object instance masks, keypoints, panoptic segments and five captions per image, the reference benchmark for detection and segmentation.
  <br><sub>COCO Consortium · JPEG, JSON · ~25 GB (2017 splits) · 330,000 images, 1.5 million object instances, 80 categories · [CC BY 4.0 (annotations); images subject to their original Flickr terms](https://cocodataset.org/#termsofuse) · Direct download · Commercial use: check terms</sub>
- [CIFAR-10 / CIFAR-100](https://www.cs.toronto.edu/~kriz/cifar.html) - Small 32x32 colour images across 10 or 100 balanced classes, small enough to iterate on in minutes and still the standard sanity check for new architectures.
  <br><sub>University of Toronto · Pickle, Binary, TAR.GZ · ~170 MB each · 60,000 images per variant · [Research use; attribution requested](https://www.cs.toronto.edu/~kriz/cifar.html) · Direct download · Commercial use: check terms</sub>

### Speech & Audio

Transcribed speech corpora for automatic speech recognition and text-to-speech.

- [Mozilla Common Voice](https://commonvoice.mozilla.org/en/datasets) - Crowd-donated and crowd-validated read speech released into the public domain, covering more than a hundred languages including many with little other ASR data.
  <br><sub>Mozilla Foundation · MP3, TSV · Varies by language (tens of GB for English) · 30,000+ validated hours across 130+ languages · [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) · Free account required · Commercial use permitted</sub>
- [LibriSpeech](https://www.openslr.org/12) - Read English audiobook speech from LibriVox, force-aligned to its Project Gutenberg source text and split into clean and noisy subsets that define the standard ASR difficulty tiers.
  <br><sub>Johns Hopkins University / OpenSLR · FLAC, TXT, TAR.GZ · ~60 GB (all training subsets) · 1,000 hours of 16 kHz speech · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · Direct download · Commercial use permitted</sub>

### Recommender Systems

User-item interaction logs and reviews for collaborative filtering and ranking research.

- [MovieLens 25M](https://grouplens.org/datasets/movielens/) - Star ratings and free-text tags collected from the MovieLens service over 24 years, the most widely used benchmark for collaborative filtering.
  <br><sub>GroupLens Research, University of Minnesota · CSV, ZIP · ~250 MB · 25,000,095 ratings from 162,541 users on 62,423 movies · [GroupLens usage license: research use only, no redistribution, no commercial use without permission](https://files.grouplens.org/datasets/movielens/ml-25m-README.html) · Direct download · Non-commercial only</sub>
- [Amazon Reviews 2023](https://amazon-reviews-2023.github.io/) - Product reviews spanning 1996 to 2023 with ratings, review text, images and rich item metadata, organised into 33 product categories for large-scale recommendation research.
  <br><sub>McAuley Lab, UC San Diego · JSONL, Parquet · ~200 GB · 571.54 million reviews, 48.19 million items · [Research use; cite the source papers](https://amazon-reviews-2023.github.io/) · Direct download · Non-commercial only</sub>

### Search & Information Retrieval

Query-document relevance judgements for training and evaluating retrieval and reranking systems.

- [MS MARCO](https://microsoft.github.io/msmarco/) - Real anonymised Bing queries paired with human-judged passages and documents, the dataset that made neural ranking models practical to train at scale.
  <br><sub>Microsoft · TSV, JSON · ~20 GB · 1,010,916 queries, 8.8 million passages · [MS MARCO non-commercial research license](https://microsoft.github.io/msmarco/) · Direct download · Non-commercial only</sub>
- [BEIR](https://github.com/beir-cellar/beir) - A heterogeneous zero-shot retrieval benchmark that wraps 18 existing IR datasets behind one loader and evaluation protocol, so a retriever can be scored across domains without per-dataset plumbing.
  <br><sub>UKP Lab, TU Darmstadt · JSONL, TSV · ~50 GB for all subsets · 18 datasets across 9 retrieval tasks · [Apache-2.0 (toolkit); each subset retains its own license](https://github.com/beir-cellar/beir/blob/main/LICENSE) · Direct download · Commercial use: check terms</sub>

### Tabular Machine Learning

Curated repositories of small-to-medium tabular datasets used as standard classification and regression benchmarks.

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/) - The longest-running public collection of machine learning datasets, hosting the small tabular classics such as Iris, Adult, Wine Quality and Covertype behind a consistent Python API.
  <br><sub>University of California, Irvine · CSV, ARFF, Python API · Mostly under 100 MB per dataset · 670+ datasets · [CC BY 4.0 for most datasets; check per dataset](https://archive.ics.uci.edu/) · Direct download · Commercial use: check terms</sub>
- [OpenML](https://www.openml.org/search?type=benchmark) - Datasets, tasks, flows and millions of recorded experiment runs behind one REST API, including the curated CC-18 and AutoML benchmark suites for reproducible model comparison.
  <br><sub>OpenML Foundation · ARFF, Parquet, REST API · Varies by dataset · 5,000+ curated datasets, 100M+ recorded runs · [Varies per dataset; mostly CC BY or public domain](https://www.openml.org/terms) · Direct download · Commercial use: check terms</sub>

### Time Series & Forecasting

Large collections of time series with held-out horizons for reproducible forecasting evaluation.

- [M4 Competition Dataset](https://github.com/Mcompetitions/M4-methods) - One hundred thousand real series at yearly through hourly frequencies drawn from demographics, finance, industry and macro sources, with held-out horizons and every competitor's submitted forecasts.
  <br><sub>Makridakis Open Forecasting Center · CSV · ~500 MB · 100,000 time series · [Open for research and benchmarking; see repository](https://github.com/Mcompetitions/M4-methods) · Direct download · Commercial use: check terms</sub>
- [Monash Time Series Forecasting Archive](https://forecastingdata.org/) - Thirty forecasting datasets normalised into a single .tsf format with baseline results for statistical and deep models, covering tourism, traffic, electricity, weather and web traffic.
  <br><sub>Monash University · TSF, CSV, Zenodo archives · ~10 GB · 30 datasets, 100,000+ series · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · Direct download · Commercial use permitted</sub>

### Fraud & Anomaly Detection

Heavily imbalanced transaction datasets for fraud scoring and rare-event detection.

- [Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) - Two days of European cardholder transactions with PCA-anonymised features and a 0.172% positive rate, the canonical teaching example for extreme class imbalance.
  <br><sub>Machine Learning Group, ULB / Worldline · CSV · ~150 MB · 284,807 transactions, 492 frauds · [Database Contents License (DbCL) v1.0](https://opendatacommons.org/licenses/dbcl/1-0/) · Free account required · Commercial use: check terms</sub>
- [IEEE-CIS Fraud Detection](https://www.kaggle.com/competitions/ieee-fraud-detection) - Real e-commerce transactions from Vesta with 400+ engineered features spanning device, card, address and identity signals, plus a separately joined identity table.
  <br><sub>IEEE Computational Intelligence Society / Vesta Corporation · CSV · ~1.2 GB · 590,540 training transactions · [Competition rules; non-commercial research use](https://www.kaggle.com/competitions/ieee-fraud-detection/rules) · Free account required · Non-commercial only</sub>

### Graphs & Networks

Social, citation and web graphs for network analysis and graph neural network benchmarks.

- [SNAP Large Network Dataset Collection](https://snap.stanford.edu/data/) - Social, citation, collaboration, web, road and communication networks in a uniform edge-list format, ranging from thousands to billions of edges.
  <br><sub>Stanford Network Analysis Project · Edge list, TXT.GZ · KB to hundreds of GB per network · 100+ network datasets · [BSD-3-Clause (library); datasets vary, cite the source paper](https://snap.stanford.edu/snap/license.html) · Direct download · Commercial use: check terms</sub>
- [Open Graph Benchmark](https://ogb.stanford.edu/) - Large realistic graph benchmarks for node, link and graph property prediction, shipping with standardised non-random splits and an automated evaluator to stop leaderboard drift.
  <br><sub>Stanford University · Python package, NPZ, CSV · MB to ~100 GB (OGB-LSC) · 15+ datasets up to 100M+ nodes · [MIT (package); datasets carry individual licenses such as ODC-BY and CC BY](https://github.com/snap-stanford/ogb/blob/master/LICENSE) · Direct download · Commercial use: check terms</sub>

### Geospatial & Mapping

Open map data and cartographic base layers for geocoding, routing and visualisation.

- [OpenStreetMap Planet](https://planet.openstreetmap.org/) - The complete crowd-mapped world as a single weekly export of nodes, ways and relations, plus daily and minutely diffs for keeping a local mirror current.
  <br><sub>OpenStreetMap Foundation · PBF, XML.BZ2 · ~80 GB (PBF) · 9 billion+ nodes · [ODbL 1.0 (share-alike; attribution required)](https://www.openstreetmap.org/copyright) · Direct download · Commercial use permitted</sub>
- [Natural Earth](https://www.naturalearthdata.com/downloads/) - Public-domain vector and raster base maps at three cartographic scales, with boundaries, coastlines, rivers, cities and shaded relief built to line up cleanly across layers.
  <br><sub>Natural Earth / NACIS · Shapefile, GeoPackage, GeoTIFF · ~1 GB for the full set · Vector and raster layers at 1:10m, 1:50m and 1:110m · [Public domain](https://www.naturalearthdata.com/about/terms-of-use/) · Direct download · Commercial use permitted</sub>

### Finance & Economics

Official macroeconomic and development indicators published by central banks and international bodies.

- [FRED (Federal Reserve Economic Data)](https://fred.stlouisfed.org/) - Macroeconomic time series aggregated from more than a hundred official sources, covering rates, employment, prices and output, with a well-documented REST API and vintage-aware ALFRED archive.
  <br><sub>Federal Reserve Bank of St. Louis · CSV, XLS, REST API · Varies by series · 800,000+ time series · [FRED Terms of Use; many series carry upstream copyright restrictions](https://fred.stlouisfed.org/legal/) · Direct download · Commercial use: check terms</sub>
- [World Bank Open Data](https://data.worldbank.org/) - Development indicators for every country from 1960 onward, covering GDP, population, health, education, energy and trade, all available in bulk and through a free API.
  <br><sub>The World Bank · CSV, XML, REST API · ~200 MB for the full WDI archive · 1,400+ indicators, 217 economies · [CC BY 4.0](https://datacatalog.worldbank.org/public-licenses) · Direct download · Commercial use permitted</sub>

### E-commerce & Retail

Transaction and basket data for demand forecasting, market basket analysis and customer segmentation.

- [Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii) - Every transaction of a UK online gift retailer over two years, with invoice, product, quantity, price, customer and country columns, widely used for RFM segmentation and basket analysis.
  <br><sub>UCI Machine Learning Repository · XLSX, CSV · ~45 MB · 1,067,371 transactions (Dec 2009 - Dec 2011) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · Direct download · Commercial use permitted</sub>
- [Instacart Market Basket Analysis](https://www.kaggle.com/c/instacart-market-basket-analysis) - Anonymised grocery orders with per-order product sequences, reorder flags, aisle and department taxonomies, and day-of-week and hour-of-day signals for next-basket prediction.
  <br><sub>Instacart · CSV · ~700 MB · 3.4 million orders from 200,000+ users · [Instacart Data Sharing Agreement; non-commercial use](https://www.kaggle.com/c/instacart-market-basket-analysis/rules) · Free account required · Non-commercial only</sub>

### Transportation & Mobility

Trip records and transit schedules for routing, demand modelling and urban analytics.

- [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) - Every yellow taxi, green taxi, for-hire and high-volume for-hire trip in New York City since 2009, with pickup and dropoff timestamps, zones, distances and fare breakdowns.
  <br><sub>NYC Taxi and Limousine Commission · Parquet · ~50 GB for the full history · Billions of trips since 2009 · [NYC Open Data Terms of Use](https://www.nyc.gov/home/terms-of-use.page) · Direct download · Commercial use permitted</sub>
- [Mobility Database](https://mobilitydatabase.org/) - A catalogue of public transit feeds worldwide in GTFS and GTFS-Realtime, with a stable API and validation reports so schedule and vehicle-position data can be pulled without hunting agency websites.
  <br><sub>MobilityData · GTFS, GTFS-RT, REST API · Varies by feed · 2,000+ transit feeds worldwide · [Catalogue CC0; individual feeds carry their agency licenses](https://mobilitydatabase.org/terms-and-conditions) · Free account required · Commercial use: check terms</sub>

## By country

300 datasets across 30 topics and 12 countries, two countries per topic. Each topic links to its own page.

| Topic | Countries | Datasets |
| --- | --- | --- |
| [Addresses & Geocoding](topics/addresses-and-geocoding/) | France, United States | 10 |
| [Agriculture & Crops](topics/agriculture-and-crops/) | India, United States | 10 |
| [Air Quality & Pollution](topics/air-quality-and-pollution/) | India, United States | 10 |
| [Aviation & Flights](topics/aviation-and-flights/) | European Union, United States | 10 |
| [Banking & Payments](topics/banking-and-payments/) | Germany, United States | 10 |
| [Census & Demographics](topics/census-and-demographics/) | India, United States | 10 |
| [Company Registries](topics/company-registries/) | United Kingdom, India | 10 |
| [Courts & Legal](topics/courts-and-legal/) | India, United States | 10 |
| [Crime & Policing](topics/crime-and-policing/) | United Kingdom, United States | 10 |
| [Earthquakes & Natural Hazards](topics/earthquakes-and-natural-hazards/) | Japan, United States | 10 |
| [E-commerce & Retail](topics/ecommerce-and-retail/) | Brazil, United States | 10 |
| [Education & Schools](topics/education-and-schools/) | India, United States | 10 |
| [Elections & Voting](topics/elections-and-voting/) | India, United States | 10 |
| [Energy & Electricity](topics/energy-and-electricity/) | Germany, United Kingdom | 10 |
| [Financial Markets](topics/financial-markets/) | India, United States | 10 |
| [Government Spending & Budgets](topics/government-spending-and-budgets/) | United Kingdom, United States | 10 |
| [Labour & Employment](topics/labour-and-employment/) | Canada, United States | 10 |
| [Patents & Trademarks](topics/patents-and-trademarks/) | European Union, United States | 10 |
| [Public Health](topics/public-health/) | United Kingdom, United States | 10 |
| [Public Transit](topics/public-transit/) | Germany, United States | 10 |
| [Real Estate & Housing](topics/real-estate-and-housing/) | United Kingdom, United States | 10 |
| [Road Safety & Accidents](topics/road-safety-and-accidents/) | United Kingdom, United States | 10 |
| [Satellite & Earth Observation](topics/satellite-and-earth-observation/) | European Union, United States | 10 |
| [Taxi & Ride-Hailing](topics/taxi-and-ride-hailing/) | Singapore, United States | 10 |
| [Telecom & Broadband](topics/telecom-and-broadband/) | United Kingdom, United States | 10 |
| [Tourism & Hospitality](topics/tourism-and-hospitality/) | Spain, United States | 10 |
| [Trade & Customs](topics/trade-and-customs/) | India, United States | 10 |
| [Vehicles & Car Sales](topics/vehicles-and-car-sales/) | India, United States | 10 |
| [Water & Sanitation](topics/water-and-sanitation/) | India, United States | 10 |
| [Weather & Climate](topics/weather-and-climate/) | Australia, United States | 10 |

<!-- END GENERATED -->

## How this repo is laid out

```
data/datasets.json                        global datasets (source of truth)
data/countries.json                       country code -> display name
data/schema.json                          JSON Schema for both catalogs
topics/<topic>/topic.json                 topic title and description
topics/<topic>/<country>/dataset-NN.json  one file per country-specific dataset
topics/<topic>/README.md                  generated
data/*.csv                                generated
```

One dataset per file is deliberate: two people adding datasets to the same country never touch the same file, so their pull requests do not conflict.

## Using the catalog

```bash
python3 scripts/validate.py           # structure, referential integrity, style rules
python3 scripts/validate.py --links   # also verify every URL resolves
python3 scripts/build.py              # regenerate READMEs and CSVs
python3 scripts/new_dataset.py --help # scaffold a new entry
```

Load everything in a few lines:

```python
import json, pathlib

catalog = json.loads(pathlib.Path("data/datasets.json").read_text())
country = [json.loads(p.read_text())
           for p in pathlib.Path("topics").glob("*/*/dataset-*.json")]

# Everything you can use commercially without an account.
usable = [d for d in catalog["datasets"] + country
          if d["access"] == "open" and d["commercial_use"] == "yes"]
print(len(usable), "datasets are open access and commercially usable")
```

Or skip the JSON and open [`data/datasets.csv`](data/datasets.csv) and [`data/country-datasets.csv`](data/country-datasets.csv) in anything.

Field meanings are documented in [`data/schema.json`](data/schema.json). Two are worth calling out:

- **`access`** — `open` (direct download), `registration` (free account), `agreement` (signed terms), `credentialed` (identity or ethics vetting).
- **`commercial_use`** — `yes`, `no`, or `check` when terms are mixed across components, which is common for corpora that bundle third-party content under its original license.

## Contributing

Contributions are welcome, and corrections are as valuable as additions. Read [contributing.md](contributing.md) — entries are added as JSON files, never to the generated lists directly. New contributors should also read the [code of conduct](code-of-conduct.md).

## Sources and credits

Every dataset here is hosted and maintained by the organisation named in its entry. Full credit for collection, curation and hosting belongs to them.

**National statistical offices and government agencies** — the single largest source in this list. Among them: the [US Census Bureau](https://www.census.gov/), [Bureau of Labor Statistics](https://www.bls.gov/), [NOAA](https://www.ncei.noaa.gov/), [USGS](https://www.usgs.gov/), [NASA](https://www.earthdata.nasa.gov/), [EPA](https://www.epa.gov/), [NIST](https://nvd.nist.gov/), [NHTSA](https://www.nhtsa.gov/), [FCC](https://www.fcc.gov/), [SEC](https://www.sec.gov/), [USPTO](https://developer.uspto.gov/) and [USDA](https://www.nass.usda.gov/) in the United States; the [Office for National Statistics](https://www.ons.gov.uk/), [HM Land Registry](https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads), [Companies House](https://download.companieshouse.gov.uk/en_output.html), [Ofcom](https://www.ofcom.org.uk/), [NHS](https://www.england.nhs.uk/statistics/), [Ordnance Survey](https://osdatahub.os.uk/downloads/open) and the [Home Office](https://data.police.uk/data/) in the United Kingdom; the [Ministry of Statistics and Programme Implementation](https://www.mospi.gov.in/), [Reserve Bank of India](https://data.rbi.org.in/), [Election Commission of India](https://www.eci.gov.in/statistical-reports), [Central Pollution Control Board](https://airquality.cpcb.gov.in/ccr/) and the [National Informatics Centre](https://www.data.gov.in/) in India; and their counterparts in [Germany](https://www.govdata.de/), [France](https://www.data.gouv.fr/), [Spain](https://datos.gob.es/en), [Brazil](https://dados.gov.br/), [Canada](https://open.canada.ca/en/open-data), [Australia](https://data.gov.au/), [Japan](https://www.e-stat.go.jp/en) and [Singapore](https://data.gov.sg/).

**International bodies** — [Eurostat](https://ec.europa.eu/eurostat), the [European Space Agency and Copernicus programme](https://dataspace.copernicus.eu/), the [European Central Bank](https://data.ecb.europa.eu/), [EUROCONTROL](https://www.eurocontrol.int/our-data), the [European Patent Office](https://www.epo.org/en), [EUIPO](https://www.euipo.europa.eu/en/open-data), [The World Bank](https://data.worldbank.org/), the [FAO](https://www.fao.org/faostat/en/) and the [UN Statistics Division](https://comtradeplus.un.org/).

**Universities and research groups** — Stanford ([SNAP](https://snap.stanford.edu/data/), [OGB](https://ogb.stanford.edu/), [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/), [IMDB reviews](https://ai.stanford.edu/~amaas/data/sentiment/), [SEDA](https://edopportunity.org/)), Minnesota ([GroupLens](https://grouplens.org/datasets/movielens/), [IPUMS](https://usa.ipums.org/usa/)), UC Irvine ([UCI ML Repository](https://archive.ics.uci.edu/)), UC San Diego ([McAuley Lab](https://amazon-reviews-2023.github.io/)), UC Davis ([BugSwarm](https://www.bugswarm.org/)), Toronto ([CIFAR](https://www.cs.toronto.edu/~kriz/cifar.html)), Johns Hopkins ([LibriSpeech](https://www.openslr.org/12)), TU Darmstadt ([BEIR](https://github.com/beir-cellar/beir)), Monash ([Forecasting Archive](https://forecastingdata.org/)), Michigan ([ICPSR](https://www.icpsr.umich.edu/)), Harvard ([Dataverse](https://dataverse.harvard.edu/), [Caselaw Access Project](https://case.law/)), MIT ([Election Lab](https://electionlab.mit.edu/data)), Oxford ([OpenPrescribing](https://openprescribing.net/)), Imperial College ([UK-DALE](https://jack-kelly.com/data/)), Ashoka ([Lok Dhaba](https://lokdhaba.ashoka.edu.in/)), New Brunswick ([CIC](https://www.unb.ca/cic/datasets/ids-2017.html)), UNSW ([UNSW-NB15](https://research.unsw.edu.au/projects/unsw-nb15-dataset)), [ICRISAT](http://data.icrisat.org/dld/), [NIED](https://www.kyoshin.bosai.go.jp/), [Development Data Lab](https://www.devdatalab.org/), [Defects4J](https://github.com/rjust/defects4j) and [LogPAI](https://github.com/logpai/loghub).

**Companies, foundations and community projects** — [GitHub](https://github.com/github/CodeSearchNet), [Microsoft](https://microsoft.github.io/msmarco/), [Google and AllenAI](https://huggingface.co/datasets/allenai/c4), [Elastic](https://github.com/elastic/rally-tracks), [ClickHouse](https://github.com/ClickHouse/ClickBench), [Mozilla](https://commonvoice.mozilla.org/en/datasets), [Deutsche Bahn](https://data.deutschebahn.com/), [Ookla](https://registry.opendata.aws/speedtest-global-performance/), [Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce), [Instacart](https://www.kaggle.com/c/instacart-market-basket-analysis), [Vesta and IEEE-CIS](https://www.kaggle.com/competitions/ieee-fraud-detection), [Worldline and the ULB Machine Learning Group](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud), [Common Crawl](https://commoncrawl.org/), [OpenStreetMap](https://planet.openstreetmap.org/), [Overture Maps](https://overturemaps.org/), [OpenML](https://www.openml.org/), [MobilityData](https://mobilitydatabase.org/), [Natural Earth and NACIS](https://www.naturalearthdata.com/), [GeoNames](https://www.geonames.org/), [OpenAQ](https://openaq.org/), [PurpleAir](https://api.purpleair.com/), [Measurement Lab](https://www.measurementlab.net/data/), [RIPE NCC](https://atlas.ripe.net/), [OpenSky Network](https://opensky-network.org/), [Open Food Facts](https://world.openfoodfacts.org/data), [Inside Airbnb](https://insideairbnb.com/get-the-data/), [OpenCorporates](https://opencorporates.com/), [OpenSecrets](https://www.opensecrets.org/open-data/bulk-data), [Free Law Project](https://www.courtlistener.com/), [Association for Democratic Reforms](https://myneta.info/), [ASER Centre](https://asercentre.org/), the [COCO Consortium](https://cocodataset.org/), the [Makridakis Open Forecasting Center](https://github.com/Mcompetitions/M4-methods), [Open Power System Data](https://open-power-system-data.org/), [Fraunhofer ISE](https://www.energy-charts.info/) and [GH Archive](https://www.gharchive.org/).

**Hosting platforms** — [Kaggle](https://www.kaggle.com/), [Hugging Face](https://huggingface.co/datasets), [Zenodo](https://zenodo.org/), [OpenSLR](https://www.openslr.org/), [Harvard Dataverse](https://dataverse.harvard.edu/) and [AWS Open Data](https://registry.opendata.aws/) distribute several of these on behalf of their creators. Where a dataset is reachable through more than one host, the entry links to the host whose terms are clearest.

The `cite` field on each entry gives the publication its authors ask you to reference. Cite the dataset, not this list.

## Related lists

- [awesome-public-datasets](https://github.com/awesomedata/awesome-public-datasets) - Broad topic-first index of open datasets across the sciences.
- [awesome-json-datasets](https://github.com/jdorfman/awesome-json-datasets) - Public JSON endpoints and API-accessible data.
- [awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning) - Machine learning frameworks and libraries by language.
- [awesome-opensource-data-engineering](https://github.com/gunnarmorling/awesome-opensource-data-engineering) - Open-source tooling for moving and processing the data above.
