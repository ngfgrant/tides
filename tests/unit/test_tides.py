import pytest
from mock import patch

from tides import Tides
from tides.provider import TideProvider
from tides.exceptions import MissingApiKeyError


class TestTides(object):
    def test_missing_api_key_raises_missing_api_key_error(self):
        with pytest.raises(MissingApiKeyError):
            Tides('admiralty')

    @patch.dict('os.environ', {'TIDE_KEY': 'ABC123'})
    def test_tides_instantiates_with_api_key(self):
        tides = Tides('admiralty')
        assert tides.TIDE_KEY == 'ABC123'

    @patch.dict('os.environ', {'TIDE_KEY': 'ABC123'})
    def test_set_provider(self):
        tides = Tides('admiralty')
        assert isinstance(tides.provider, TideProvider)
        assert tides.provider.name == 'admiralty'
