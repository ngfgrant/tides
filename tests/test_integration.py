import pytest
from os import environ

from tides.provider import AdmiraltyTideProvider


@pytest.fixture()
def provider():
    return AdmiraltyTideProvider(environ.get('TIDE_KEY'))


class TestAdmiraltyTidesProvider:
    def test_get_stations_returns_dict(self, provider):
        all_stations = provider.get_all_stations()
        assert isinstance(all_stations, dict)

    def test_get_stations_returns_station_name_as_key(self, provider):
        all_stations = provider.get_all_stations()
        assert "Rockall" in all_stations["response"]

    def test_get_station_returns_individual_station_keyed_by_name(self, provider):
        station = provider.get_station_by_id('0001')
        assert sorted(station["response"]) == sorted({
            "ST. MARY'S": {
                "country": "England", "lat": "49.916666", "long": "-6.316666", "id": "0001"}
        })

    def test_get_station_by_name_returns_successfully(self, provider):
        station = provider.get_station_by_name('Fidra')
        assert sorted(station["response"]) == sorted(
            {
                "Fidra": {
                    "country": "Scotland",
                    "lat": "56.066666",
                    "long": "-2.783333",
                    "id": "0223"
                }
            }
        )

    def test_get_tides_by_station_name_returns_a_non_empty_result(self, provider):
        tides = provider.get_tides("Fidra", "1")
        assert len(tides) >= 1

    def test_get_next_tide(self, provider):
        tides = provider.next_tide("Fidra")
        assert "Height" in tides.keys()
