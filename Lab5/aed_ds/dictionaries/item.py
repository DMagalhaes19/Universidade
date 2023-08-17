class Item:
    def __init__(self, key: object, value: object):
        self._key = key
        self._value = value

    def get_key(self) -> object:
        return self._key

    def set_key(self, key: object) -> None:
        self._key = key

    def get_value(self) -> object:
        return self._value

    def set_value(self, value: object) -> None:
        self._value = value