class TideException(Exception):
    pass


class MissingApiKeyError(TideException):
    """
    Raises error when there is no Admiralty API Key set in the evironment variables.
    """
    pass
