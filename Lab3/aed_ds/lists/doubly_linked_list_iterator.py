from aed_ds.adt_two_way_iterator import TwoWayIterator
from aed_ds.lists.nodes import DoubleListNode
from aed_ds.exceptions import EmptyListException,InvalidPositionException,NoSuchElementException

class DoublyLinkedListIterator(TwoWayIterator):
    def __init__(self):
        self.prev = None
        self.next = None
        
    def has_previous(self) -> bool:
        """Returns true iff the iteration has more elements in the reverse
        direction. In other words, returns true if previous would return an
        element rather than throwing an exception."""

    
    def get_previous(self) -> object:
        """Returns the previous element in the iteration.
        Throws NoSuchElementException"""

    
    def full_forward(self) -> None:
        self.prev = DoubleListNode.get_previous_node()
        DoubleListNode.get_previous_node = DoubleListNode.get_next_node()
        
        """Restarts the iteration in the reverse direction. After fullForward,
        if the iteration is not empty, previous will return the last element in
        the iteration."""
        
                