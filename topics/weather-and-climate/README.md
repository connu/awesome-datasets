# Weather & Climate

> Station observations, gridded reanalysis, forecasts and long-run climate records.

Part of [Awesome Datasets](../../README.md). Entries here are generated from the `dataset-*.json` files in this directory - edit those, then run `python3 scripts/build.py`.

## Contents

- [Australia](#australia)
- [United Kingdom](#united-kingdom)
- [United States](#united-states)

## Australia

- [Bureau of Meteorology Climate Data Online](https://www.bom.gov.au/climate/data/) - Daily and monthly rainfall, temperature and solar exposure observations from Australian weather stations, some with records exceeding a century.
  <br><sub>Bureau of Meteorology · CSV, TXT · Varies by station · 20,000+ stations · [CC BY 4.0](https://www.bom.gov.au/other/copyright.shtml) · Direct download · Commercial use permitted</sub>
- [BOM Australian Climate Observations Reference Network](https://www.bom.gov.au/climate/data/acorn-sat/) - The homogenised long-term temperature reference network used for official Australian climate trend analysis, with documented adjustments.
  <br><sub>Bureau of Meteorology · CSV · ~100 MB · 112 reference stations from 1910 · [CC BY 4.0](https://www.bom.gov.au/other/copyright.shtml) · Direct download · Commercial use permitted</sub>
- [data.gov.au Climate and Environment](https://data.gov.au/) - Australia's federal open data catalogue, covering weather, water, bushfire, land use and environmental monitoring published by Commonwealth and state agencies.
  <br><sub>Australian Government · CSV, JSON, GeoJSON, WMS, REST API · Varies by dataset · 80,000+ datasets · [Commonly CC BY 4.0; varies by publisher](https://data.gov.au/) · Direct download · Commercial use: check terms</sub>
- [Bureau of Meteorology Water Data Online](https://www.bom.gov.au/waterdata/) - Streamflow, water level, storage volume and water quality time series from thousands of gauging stations across Australian catchments.
  <br><sub>Bureau of Meteorology · CSV, WaterML 2.0, REST API · Multi-GB · 4,000+ monitoring sites · [CC BY 4.0](https://www.bom.gov.au/other/copyright.shtml) · Direct download · Commercial use permitted</sub>
- [Digital Earth Australia](https://www.dea.ga.gov.au/) - Analysis-ready satellite imagery and derived products for the Australian continent, including surface reflectance, water observations and coastline change.
  <br><sub>Geoscience Australia · GeoTIFF, NetCDF, Zarr, STAC API · Petabyte-scale · Continental coverage from 1986 · [CC BY 4.0](https://www.ga.gov.au/copyright) · Direct download · Commercial use permitted</sub>

## United Kingdom

- [Met Office Data Services](https://www.metoffice.gov.uk/services/data) - The UK national weather service's data offering, including site-specific forecasts, atmospheric models, observations and climate averages.
  <br><sub>Met Office · REST API, NetCDF, GRIB, CSV · Varies by product · National coverage with continuous updates · [Varies by product; open products under OGL v3.0](https://www.metoffice.gov.uk/policies/legal) · Free account required · Commercial use: check terms</sub>
- [Met Office Hadley Centre Observations](https://www.metoffice.gov.uk/hadobs/) - The HadCRUT global temperature record, HadISST sea surface temperatures and related long-run climate datasets used in IPCC assessments.
  <br><sub>Met Office Hadley Centre · NetCDF, ASCII, CSV · ~50 GB · Global series from 1850 · [Open Government Licence v3.0 for most datasets](https://www.metoffice.gov.uk/hadobs/) · Direct download · Commercial use: check terms</sub>
- [CEDA Archive](https://archive.ceda.ac.uk/) - The UK's atmospheric and earth observation data centre, hosting MIDAS surface observations, radar, satellite products and climate model output.
  <br><sub>Centre for Environmental Data Analysis · NetCDF, CSV, HDF, BADC-CSV · Multi-petabyte · Thousands of datasets including 100+ years of station data · [Varies by dataset; many under OGL v3.0](https://archive.ceda.ac.uk/) · Free account required · Commercial use: check terms</sub>
- [Environment Agency Real Time Flood Monitoring API](https://environment.data.gov.uk/flood-monitoring/doc/reference) - Live river levels, rainfall and tidal readings from thousands of Environment Agency gauges, plus current flood warnings, through a free unauthenticated API.
  <br><sub>Environment Agency · REST API, JSON, CSV, RDF · API with historical archive · 5,000+ measurement stations · [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) · Direct download · Commercial use permitted</sub>
- [Met Office HadUK-Grid](https://www.metoffice.gov.uk/research/climate/maps-and-data/data/haduk-grid/haduk-grid) - Gridded UK climate observations at 1 km resolution covering temperature, rainfall, sunshine and wind, interpolated from the station network.
  <br><sub>Met Office · NetCDF, CSV · ~20 GB · Monthly and daily grids from 1836 · [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) · Free account required · Commercial use permitted</sub>

## United States

- [NOAA Global Historical Climatology Network Daily](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily) - Daily temperature, precipitation, snowfall and wind observations from land surface stations worldwide, quality-controlled and dating back to the 1700s at some sites.
  <br><sub>NOAA National Centers for Environmental Information · CSV, Fixed-width, NetCDF · ~30 GB · 100,000+ stations, billions of observations · [US Government public domain](https://www.ncei.noaa.gov/) · Direct download · Commercial use permitted</sub>
- [NOAA National Weather Service API](https://www.weather.gov/documentation/services-web-api) - Official forecasts, active alerts, observations and gridded forecast data for the United States, free and without an API key.
  <br><sub>National Weather Service · REST API, GeoJSON, JSON-LD · API · National coverage, updated continuously · [US Government public domain](https://www.weather.gov/disclaimer) · Direct download · Commercial use permitted</sub>
- [NOAA Storm Events Database](https://www.ncdc.noaa.gov/stormevents/) - Every recorded severe weather event in the US since 1950, with type, location, timing, fatalities, injuries and property damage estimates.
  <br><sub>NOAA NCEI · CSV, GZIP · ~2 GB · 1.6 million+ events since 1950 · [US Government public domain](https://www.ncei.noaa.gov/) · Direct download · Commercial use permitted</sub>
- [NOAA Integrated Surface Database](https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database) - Hourly and sub-hourly global surface observations merged from over a hundred original sources, covering wind, visibility, pressure, temperature and sky condition.
  <br><sub>NOAA NCEI · CSV, Fixed-width · ~600 GB · 35,000+ stations since 1901 · [US Government public domain](https://www.ncei.noaa.gov/) · Direct download · Commercial use permitted</sub>
- [NOAA Open Data Dissemination on AWS](https://registry.opendata.aws/collab/noaa/) - NOAA's operational model output, radar and satellite archives staged on cloud object storage, including GFS, HRRR, NEXRAD and GOES imagery.
  <br><sub>NOAA and AWS Open Data · GRIB2, NetCDF, Zarr, Parquet · Petabyte-scale · Dozens of operational products · [US Government public domain](https://www.noaa.gov/information-technology/open-data-dissemination) · Direct download · Commercial use permitted</sub>
