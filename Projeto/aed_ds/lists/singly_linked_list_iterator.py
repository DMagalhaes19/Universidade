from aed_ds.adt_iterator import Iterator
from aed_ds.exceptions import NoSuchElementException


class SinglyLinkedListIterator(Iterator):

    def __init__(self, head):
        self.head = head
        self.current_node = None


    def has_next(self) -> bool:
        """Returns true iff the iteration has more elements. In other words,
        returns true next would return an element rather than throwing an
        exception."""
        if self.head is None:
            return False
        elif self.current_node is not None:
            if self.current_node.get_next_node() is None:
                return False
            else:
                return True
        else:
            return True

    def get_next(self) -> object:
        """Returns the next element in the iteration.
        Throws NoSuchElementException"""
        if self.head == None:
            raise NoSuchElementException()
        elif self.current_node != None and self.current_node.get_next_node() == None:
            raise NoSuchElementException()
        elif self.current_node == None:
            self.current_node = self.head
            return self.current_node.get_element()
        else:
            return self.current_node.get_next_node().get_element()


    def rewind(self) -> None:
        """Restarts the iteration. After rewind, if the iteration is not empty,
        next will return the first element in the iteration."""
        self.current_node = None