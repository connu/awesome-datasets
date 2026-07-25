# Addresses & Geocoding

> Authoritative address points, postcode registers, administrative boundaries and geocoding services.

Part of [Awesome Datasets](../../README.md). Entries here are generated from the `dataset-*.json` files in this directory - edit those, then run `python3 scripts/build.py`.

## Contents

- [Germany](#germany)
- [France](#france)
- [United States](#united-states)

## Germany

- [BKG Geodatenzentrum Open Data](https://gdz.bkg.bund.de/) - Germany's national geodata centre distributing administrative boundaries, digital terrain models, topographic base data and gazetteers as free open data.
  <br><sub>Bundesamt für Kartographie und Geodäsie · Shapefile, GeoPackage, GeoTIFF, WMS, WFS · Terabyte-scale · National coverage of Germany · [DL-DE-BY-2.0 for open products](https://www.govdata.de/dl-de/by-2-0) · Direct download · Commercial use permitted</sub>
- [basemap.de](https://basemap.de/) - The official German web map service built from state survey data, offering raster and vector tiles for cartographic base layers.
  <br><sub>Arbeitsgemeinschaft der Vermessungsverwaltungen (AdV) · Vector tiles, WMTS, WMS · Tile service · National coverage at all zoom levels · [DL-DE-BY-2.0](https://www.govdata.de/dl-de/by-2-0) · Direct download · Commercial use permitted</sub>
- [OpenPLZ API](https://www.openplzapi.org/) - A free API resolving German, Austrian, Swiss and Liechtenstein postal codes to localities, districts, states and street lists.
  <br><sub>OpenPLZ API project · REST API, JSON · API · Postal code and street coverage for four countries · [ODbL 1.0 (data from OpenStreetMap and official sources)](https://www.openplzapi.org/) · Direct download · Commercial use permitted</sub>
- [Geoportal.de](https://www.geoportal.de/) - The federal spatial data infrastructure portal indexing geodata services from all German states and agencies, with INSPIRE-compliant metadata.
  <br><sub>Bundesamt für Kartographie und Geodäsie · WMS, WFS, Atom, Metadata · Varies by service · 100,000+ registered geodata resources · [Varies by provider; commonly DL-DE-BY-2.0](https://www.geoportal.de/) · Direct download · Commercial use: check terms</sub>
- [Destatis Regionalatlas](https://regionalatlas.statistikportal.de/) - Small-area German statistics mapped to administrative geographies, covering population, economy, labour, health and infrastructure indicators.
  <br><sub>Statistische Ämter des Bundes und der Länder · CSV, XLSX, WMS · ~2 GB · 400+ indicators at district level · [DL-DE-BY-2.0](https://www.govdata.de/dl-de/by-2-0) · Direct download · Commercial use permitted</sub>

## France

- [Base Adresse Nationale](https://adresse.data.gouv.fr/) - France's authoritative address database with geolocated address points, street names and INSEE codes, plus a free geocoding and reverse-geocoding API.
  <br><sub>DINUM and IGN · CSV, GeoJSON, REST API · ~2 GB · 26 million+ addresses · [Licence Ouverte 2.0](https://www.etalab.gouv.fr/licence-ouverte-open-licence/) · Direct download · Commercial use permitted</sub>
- [data.gouv.fr](https://www.data.gouv.fr/) - France's central open data platform hosting government, local authority and community datasets across every policy domain with a full API.
  <br><sub>DINUM / Etalab · CSV, JSON, GeoJSON, Shapefile, REST API · Varies by dataset · 50,000+ datasets · [Mostly Licence Ouverte 2.0](https://www.etalab.gouv.fr/licence-ouverte-open-licence/) · Direct download · Commercial use permitted</sub>
- [IGN Géoservices](https://geoservices.ign.fr/) - National mapping agency data including cadastral parcels, topographic databases, orthophotography, elevation models and administrative boundaries.
  <br><sub>Institut national de l'information géographique et forestière · Shapefile, GeoPackage, GeoTIFF, WMS, WFS · Terabyte-scale · National coverage of France and overseas territories · [Licence Ouverte 2.0 for open products](https://geoservices.ign.fr/) · Direct download · Commercial use permitted</sub>
- [INSEE Code Officiel Géographique](https://www.insee.fr/fr/information/2560452) - The official register of French communes, departments, regions and countries with historical changes, the canonical join key for French administrative data.
  <br><sub>Institut national de la statistique et des études économiques · CSV, XLSX · ~50 MB · 35,000+ communes with historical revisions · [Licence Ouverte 2.0](https://www.etalab.gouv.fr/licence-ouverte-open-licence/) · Direct download · Commercial use permitted</sub>
- [Demandes de Valeurs Foncières](https://www.data.gouv.fr/datasets/demandes-de-valeurs-foncieres) - Every French property transaction registered by the tax administration, with price, date, surface area, parcel reference and property type.
  <br><sub>Direction générale des finances publiques · CSV, TXT · ~5 GB · 20 million+ transactions since 2014 · [Licence Ouverte 2.0](https://www.etalab.gouv.fr/licence-ouverte-open-licence/) · Direct download · Commercial use permitted</sub>

## United States

- [Census Geocoder](https://geocoding.geo.census.gov/geocoder/) - A free official geocoding service returning coordinates plus census tract, block and congressional district for any US address, in single or batch mode.
  <br><sub>US Census Bureau · REST API, CSV · API · National address coverage · [US Government public domain](https://www.census.gov/about/policies/open-gov.html) · Direct download · Commercial use permitted</sub>
- [National Address Database](https://www.transportation.gov/gis/national-address-database) - A federal aggregation of state and local authoritative address points with coordinates, address components and jurisdiction identifiers.
  <br><sub>US Department of Transportation · CSV, Geodatabase, Shapefile · ~10 GB · 80 million+ address points · [US Government public domain and contributing agency terms](https://www.transportation.gov/gis/national-address-database) · Direct download · Commercial use permitted</sub>
- [USGS National Map](https://www.usgs.gov/programs/national-geospatial-program/national-map) - Authoritative national geospatial layers covering elevation, hydrography, transportation, boundaries, structures and land cover.
  <br><sub>US Geological Survey · GeoTIFF, Shapefile, GeoPackage, REST API · Petabyte-scale · National coverage across 8 data themes · [US Government public domain](https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits) · Direct download · Commercial use permitted</sub>
- [GeoNames](https://www.geonames.org/) - A global gazetteer of place names with coordinates, population, elevation, feature class, alternate names and administrative hierarchy, free to download in full.
  <br><sub>GeoNames · TXT, ZIP, REST API · ~2 GB · 12 million+ place names worldwide · [CC BY 4.0](https://www.geonames.org/about.html) · Direct download · Commercial use permitted</sub>
- [Overture Maps Foundation Data](https://overturemaps.org/) - Open map data releases covering places, buildings, transportation, addresses and administrative divisions, published as cloud-native GeoParquet.
  <br><sub>Overture Maps Foundation · GeoParquet, PMTiles · ~500 GB · Billions of features worldwide · [CDLA Permissive 2.0 and ODbL depending on theme](https://docs.overturemaps.org/attribution/) · Direct download · Commercial use permitted</sub>
