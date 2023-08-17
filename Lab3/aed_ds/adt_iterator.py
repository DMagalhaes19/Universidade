from abc import ABC, abstractmethod


class Iterator(ABC):        
    @abstractmethod
    def has_next(self) -> bool:
        """Returns true iff the iteration has more elements. In other words,
        returns true next would return an element rather than throwing an
        exception."""
        
    @abstractmethod
    def get_next(self) -> object:
        """Returns the next element in the iteration.
        Throws NoSuchElementException"""

    @abstractmethod
    def rewind(self) -> None:
        """Restarts the iteration. After rewind, if the iteration is not empty,
        next will return the first element in the iteration."""