# Earthquakes & Natural Hazards

> Seismic catalogues, ground motion records, flood and wildfire extents and disaster loss databases.

Part of [Awesome Datasets](../../README.md). Entries here are generated from the `dataset-*.json` files in this directory - edit those, then run `python3 scripts/build.py`.

## Contents

- [European Union](#european-union)
- [Japan](#japan)
- [United States](#united-states)

## European Union

- [EMSC Euro-Mediterranean Seismological Centre](https://www.emsc-csem.org/) - Real-time and archived earthquake locations for the Euro-Mediterranean region, with felt reports, moment tensors and a public API.
  <br><sub>European-Mediterranean Seismological Centre · REST API, JSON, QuakeML, CSV · ~20 GB · Millions of located events · [Free for research and public use with attribution](https://www.emsc-csem.org/) · Direct download · Commercial use: check terms</sub>
- [ORFEUS EIDA Seismic Waveforms](https://www.orfeus-eu.org/) - Federated access to continuous seismic waveform archives from European networks, with standard FDSN web services for stations and events.
  <br><sub>ORFEUS and European seismic networks · miniSEED, StationXML, FDSN web services · Petabyte-scale · Thousands of stations across Europe · [Mostly CC BY 4.0; varies by network](https://www.orfeus-eu.org/) · Direct download · Commercial use: check terms</sub>
- [Copernicus Emergency Management Service](https://emergency.copernicus.eu/) - Rapid mapping and risk products for floods, wildfires, earthquakes and storms, with delineation and damage assessment layers for activated events.
  <br><sub>European Commission and Copernicus · GeoTIFF, Shapefile, GeoJSON, PDF · Multi-TB · 700+ activations since 2012 · [Copernicus open licence, free reuse with attribution](https://emergency.copernicus.eu/) · Direct download · Commercial use permitted</sub>
- [European Flood Awareness System](https://www.efas.eu/) - Pan-European probabilistic flood forecasts, river discharge reanalysis and historical flood event data at continental scale.
  <br><sub>Copernicus Emergency Management Service and JRC · NetCDF, GRIB, Web · ~50 TB · Continental coverage with daily forecasts · [Copernicus open licence, free reuse with attribution](https://www.efas.eu/) · Free account required · Commercial use permitted</sub>
- [EFEHR European Seismic Hazard Model](https://www.efehr.org/) - The harmonised European seismic hazard and risk model with ground motion exceedance maps, fault databases and national hazard comparisons.
  <br><sub>European Facilities for Earthquake Hazard and Risk · GeoTIFF, CSV, XML · ~20 GB · Pan-European hazard grids and fault catalogues · [CC BY 4.0](https://www.efehr.org/) · Direct download · Commercial use permitted</sub>

## Japan

- [Japan Meteorological Agency Earthquake Information](https://www.jma.go.jp/jma/en/Activities/earthquake.html) - Official Japanese seismic monitoring products including hypocentre catalogues, seismic intensity observations and tsunami warnings.
  <br><sub>Japan Meteorological Agency · CSV, XML, PDF · Varies by product · Catalogues spanning over a century · [JMA terms of use, free reuse with attribution](https://www.jma.go.jp/jma/en/copyright.html) · Direct download · Commercial use permitted</sub>
- [NIED K-NET and KiK-net Strong Motion](https://www.kyoshin.bosai.go.jp/) - Strong-motion accelerograms from over a thousand nationwide seismographs, the reference ground motion dataset for earthquake engineering research.
  <br><sub>National Research Institute for Earth Science and Disaster Resilience · ASCII, SAC, ZIP · Multi-TB · 1,000+ stations recording since 1996 · [Free for research with registration and attribution](https://www.kyoshin.bosai.go.jp/) · Free account required · Commercial use: check terms</sub>
- [NIED Hi-net High Sensitivity Seismograph Network](https://www.hinet.bosai.go.jp/) - Continuous waveform data and automatic hypocentre determinations from Japan's dense high-sensitivity borehole seismometer network.
  <br><sub>National Research Institute for Earth Science and Disaster Resilience · WIN32, SEED, CSV · Petabyte-scale · 800+ stations with continuous recording · [Free for research with registration and attribution](https://www.hinet.bosai.go.jp/) · Free account required · Commercial use: check terms</sub>
- [e-Stat Portal of Official Statistics of Japan](https://www.e-stat.go.jp/en) - Japan's unified statistics portal covering population, economy, disaster damage, housing and land use, with a documented API and bulk downloads.
  <br><sub>Statistics Bureau of Japan · CSV, XLSX, REST API · Varies by table · Hundreds of thousands of statistical tables · [Japan Government Standard Terms of Use, CC BY compatible](https://www.e-stat.go.jp/en/terms-of-use) · Free account required · Commercial use permitted</sub>
- [GSI Geospatial Information Authority of Japan](https://www.gsi.go.jp/ENGLISH/index.html) - National mapping data including elevation models, base maps, crustal deformation observations from GNSS and hazard-related geospatial layers.
  <br><sub>Geospatial Information Authority of Japan · GeoTIFF, Shapefile, XML, Tiles · Terabyte-scale · National coverage of Japan · [GSI terms of use, free reuse with attribution](https://www.gsi.go.jp/ENGLISH/page_e30286.html) · Direct download · Commercial use permitted</sub>

## United States

- [USGS Earthquake Catalog](https://earthquake.usgs.gov/earthquakes/search/) - Global catalogue of located earthquakes with magnitude, depth, coordinates, origin time and moment tensors, served through a documented query API.
  <br><sub>US Geological Survey · GeoJSON, CSV, QuakeML, REST API · ~10 GB · 4 million+ located events · [US Government public domain](https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits) · Direct download · Commercial use permitted</sub>
- [USGS ShakeMap and Ground Motion](https://earthquake.usgs.gov/data/shakemap/) - Near-real-time maps of ground shaking intensity, peak acceleration and velocity generated for significant earthquakes, with grid downloads for loss modelling.
  <br><sub>US Geological Survey · GeoTIFF, XML, GeoJSON, KML · Varies by event · Thousands of mapped events · [US Government public domain](https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits) · Direct download · Commercial use permitted</sub>
- [FEMA OpenFEMA](https://www.fema.gov/about/openfema/data-sets) - Disaster declarations, individual and public assistance awards, flood insurance claims and policy records published as open datasets with an API.
  <br><sub>Federal Emergency Management Agency · CSV, JSON, Parquet, REST API · ~50 GB · Millions of claims and assistance records · [US Government public domain](https://www.fema.gov/about/openfema/terms-conditions) · Direct download · Commercial use permitted</sub>
- [NOAA Billion-Dollar Weather and Climate Disasters](https://www.ncei.noaa.gov/access/billions/) - A curated record of US weather and climate disasters exceeding one billion dollars in damage, with CPI-adjusted cost, deaths and event geography since 1980.
  <br><sub>NOAA NCEI · CSV, JSON · ~50 MB · 400+ billion-dollar events since 1980 · [US Government public domain](https://www.ncei.noaa.gov/) · Direct download · Commercial use permitted</sub>
- [NASA FIRMS Active Fire Data](https://firms.modaps.eosdis.nasa.gov/) - Near-real-time satellite detections of active fires and thermal anomalies from MODIS and VIIRS, with archive downloads and a fire information API.
  <br><sub>NASA · CSV, Shapefile, KML, REST API · ~100 GB archive · Global detections since 2000 · [NASA open data policy, free and open](https://firms.modaps.eosdis.nasa.gov/) · Free account required · Commercial use permitted</sub>
