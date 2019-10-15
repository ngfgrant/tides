import os

from tides.exceptions import MissingApiKeyError


class Tides(object):
    def __init__(self):
        self.TIDE_KEY = os.environ.get('TIDE_KEY', None)

        if self.TIDE_KEY is None:
            raise MissingApiKeyError("API Key for tide provider not set.")
