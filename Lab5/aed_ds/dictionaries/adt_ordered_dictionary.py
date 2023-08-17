from abc import abstractmethod

from aed_ds.dictionaries.adt_dictionary import Dictionary
from aed_ds.adt_iterator import Iterator


class OrderedDictionary(Dictionary):
    @abstractmethod
    def iterator(self) -> Iterator:
        """Returns an iterator of the elements in the dictionary."""

    @abstractmethod
    def get_min_element(self) -> object:
        """Returns the element with the smallest key."""

    @abstractmethod
    def get_max_element(self) -> object:
        """Returns the element with the largest key."""