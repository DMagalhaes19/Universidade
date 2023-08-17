from abc import abstractmethod

from aed_ds.adt_iterator import Iterator


class TwoWayIterator(Iterator):
    @abstractmethod
    def has_previous(self) -> bool:
        """Returns true iff the iteration has more elements in the reverse
        direction. In other words, returns true if previous would return an
        element rather than throwing an exception."""

    @abstractmethod
    def get_previous(self) -> object:
        """Returns the previous element in the iteration.
        Throws NoSuchElementException"""

    @abstractmethod
    def full_forward(self) -> None:
        """Restarts the iteration in the reverse direction. After fullForward,
        if the iteration is not empty, previous will return the last element in
        the iteration."""