import pytest
from mock import patch

from tides import Tides
from tides.exceptions import MissingApiKeyError


class TestTides(object):
    def test_missing_api_key_raises_missing_api_key_error(self):
        with pytest.raises(MissingApiKeyError):
            Tides()

    @patch.dict('os.environ', {'TIDE_KEY': 'ABC123'})
    def test_tides_instantiates_with_api_key(self):
        tides = Tides()
        assert tides.TIDE_KEY == 'ABC123'
