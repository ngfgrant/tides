from abc import ABC


class TideProvider(ABC):
    __registry = {}

    def __init_subclass__(cls, key, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.__registry.update({key: cls})

    @classmethod
    def get_provider(self, provider):
        cls = self.__registry.get(provider)
        return cls()


class AdmiraltyTideProvider(TideProvider, key='admiralty'):
    def __init__(self):
        self.name = 'admiralty'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
