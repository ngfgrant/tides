[![CircleCI](https://circleci.com/gh/ngfgrant/tides/tree/master.svg?style=svg&circle-token=a701bb98360276f425d52b21d6d0803e27e7fb78)](https://circleci.com/gh/ngfgrant/tides/tree/master) [![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=ngfgrant_tides&metric=coverage)](https://sonarcloud.io/api/project_badges/measure?project=ngfgrant_tides&metric=coverage) [![Sonarcloud
Status](https://sonarcloud.io/api/project_badges/measure?project=ngfgrant_tides&metric=ncloc)](https://sonarcloud.io/api/project_badges/measure?project=ngfgrant_tides&metric=ncloc) [![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=ngfgrant_tides&metric=sqale_rating)](https://sonarcloud.io/api/project_badges/measure?project=ngfgrant_tides&metric=sqale_rating)
[![Sonarcloud
Status](https://sonarcloud.io/api/project_badges/measure?project=ngfgrant_tides&metric=reliability_rating)](https://sonarcloud.io/api/project_badges/measure?project=ngfgrant_tides&metric=reliability_rating)
[![Sonarcloud
Status](https://sonarcloud.io/api/project_badges/measure?project=ngfgrant_tides&metric=security_rating)](https://sonarcloud.io/api/project_badges/measure?project=ngfgrant_tides&metric=security_rating)
[![Sonarcloud
Status](https://sonarcloud.io/api/project_badges/measure?project=ngfgrant_tides&metric=sqale_index)](https://sonarcloud.io/api/project_badges/measure?project=ngfgrant_tides&metric=sqale_index)
[![Sonarcloud
Status](https://sonarcloud.io/api/project_badges/measure?project=ngfgrant_tides&metric=vulnerabilities)](https://sonarcloud.io/api/project_badges/measure?project=ngfgrant_tides&metric=vulnerabilities)

# Tides

This module acts as a wrapper around the Tidal Data providers such as Admiralty
(UK Tide provider).

# Usage

Using tides is pretty straightforward. You will need to have your
TideProvider's (currently on only Admiralty is implemented) access token set as
an environment variable named `TIDE_KEY`.

```python
tides = Tides('admiralty')
tides.provider.get_tides(station="Leith")
```

The TideProvdier interface defines the following methods:

```python
def get_all_stations():

def get_station_by_id():

def get_station_by_name():

def get_tides():

def next_tide():

def time_to_next_tide():
```

# Install

```shell
$pip install tides
```

# Contributing

See the [Contributing Guide](CONTRIBUTING.md)
