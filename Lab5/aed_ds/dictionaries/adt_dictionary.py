from abc import ABC, abstractmethod
from aed_ds.lists.adt_list import List


class Dictionary(ABC):
    @abstractmethod
    def size(self) -> int:
        """Returns the number of elements in the dictionary."""

    @abstractmethod
    def is_full(self) -> bool:
        """Returns true if the dictionary is full.
        Throws NoSuchElementException"""

    @abstractmethod
    def get(self, k: object) -> object:
        """Returns the value associated with key k.
        Throws NoSuchElementException"""

    @abstractmethod
    def insert(self, k: object, v: object) -> None:
        """Inserts a new value, associated with key k.
        Throws DuplicatedKeyException"""

    @abstractmethod
    def update(self, k: object, v: object) -> None:
        """Updates the value associated with key k.
        Throws NoSuchElementException"""

    @abstractmethod
    def remove(self, k: object) -> object:
        """Removes the item with key k, and returns the value associated with it.
        Throws NoSuchElementException"""

    @abstractmethod
    def keys(self) -> List:
        """Returns a List with all the keys in the dictionary."""

    @abstractmethod
    def values(self) -> List:
        """Returns a List with all the values in the dictionary."""

    @abstractmethod
    def items(self) -> List:
        """Returns a List with all the key value pairs in the dictionary."""