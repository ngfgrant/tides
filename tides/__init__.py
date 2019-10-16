import os

from tides.provider import TideProvider
from tides.exceptions import MissingApiKeyError


class Tides(object):
    def __init__(self, provider_name):
        self.provider = provider_name
        self.TIDE_KEY = os.environ.get('TIDE_KEY', None)
        if self.TIDE_KEY is None:
            raise MissingApiKeyError("API Key for tide provider not set.")

    @property
    def provider(self):
        return self.__provider

    @provider.setter
    def provider(self, provider_name):
        self.__provider = TideProvider.get_provider(provider_name)
