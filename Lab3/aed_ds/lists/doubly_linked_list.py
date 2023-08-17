from aed_ds.adt_iterator import Iterator
from aed_ds.lists.adt_list import List
from aed_ds.lists.nodes import DoubleListNode
from aed_ds.exceptions import EmptyListException,InvalidPositionException,NoSuchElementException


class DoublyLinkedList(List):
    def __init__(self):
        self.head = None
        self.tail = None
        self.previous_node = None
        self.next_node = None
        self.num_elements = 0
        
    def is_empty(self) -> bool:
        if(self.head == None):
            return True
        else:
            return False
        """Returns true iff the list contains no elements."""

    
    def size(self) -> int:
        return self.num_elements
        """Returns the number of elements in the list."""

    
    def get_first(self) -> object:
        if(self.head is None):
            raise EmptyListException()
        return self.head
        """Returns the first element of the list.
        Throws EmptyListException."""

    
    def get_last(self) -> object:
        if(self.tail is None):
            raise EmptyListException()    
        return self.tail.element
        """Returns the last element of the list.
        Throws EmptyListException."""

    
    def get(self, position: int) -> object:
        idx = 0
        node = self.head
        if(position < 0 or position > self.num_elements):
            raise InvalidPositionException()
        while node != None:
            if(idx==position):
                return node.get_element()
            idx += 1
            node = node.next_node
        """Returns the element at the specified position in the list.
        Range of valid positions: 0, ..., size()-1."""

    
    def find(self, element: object) -> bool:
        i = 0
        node = self.head
        while(i <= self.num_elements):
            if(node.get_next_node(self) == element):
                return True
            else:
                return False
            
        """Returns the position in the list of the first occurrence of the
        specified element, or -1 if the specified element does not occur in the
        list."""

    
    def insert_first(self, element: object) -> None:
        node = self.head
        if(self.head != None):
            self.head = node.next_node
        self.num_elements += 1
        """Inserts the specified element at the first position in the list."""

    
    def insert_last(self, element: object) -> None:
        """Inserts the specified element at the last position in the list."""
        node = self.tail
        while (self.tail != None):
            node.previous_node = self.tail
        self.tail = element
        self.num_elements += 1
        
    
    def insert(self, element: object, position: int) -> None:
        """Inserts the specified element at the specified position in the list.
        Range of valid positions: 0, ..., size().
        If the specified position is 0, insert corresponds to insertFirst.
        If the specified position is size(), insert corresponds to insertLast.
        Throws InvalidPositionException."""
        i = 0
        node = self.head
        if position == 0:
            self.insert_first(self,element)
        elif position == self.num_elements:
            self.insert_last(self,element)
        else:
            node.set_next_node(self,current_node.next_node)
            node.set_previous_node(self,current_node)
            if(current_node.next_node != None):
                current_node.next_node.set_previous_node(self,node)
            current_node.set_next_node(self,node)
            
                
            
            
    
    def remove_first(self) -> object:
        """Removes and returns the element at the first position in the list.
        Throws EmptyListException."""
        self.head = self.element.next_node
        return self.head
    
    
    def remove_last(self) -> object:
        """Removes and returns the element at the last position in the list.
        Throws EmptyListException."""
        self.tail = self.element.previous_node
        return self.tail
   
    def remove(self, position: int) -> object:
        """Removes and returns the element at the specified position in the
        list.
        Range of valid positions: 0, ..., size()-1.
        Throws InvalidPositionException."""
        current_node = self.head
        if(position == 0):
            self.remove_first(self)
        elif(position == self.num_elements):
            self.remove_last(self)
        else:
            i = 1
            while(current_node != None and i < position):
                current_node.next_node
                i = i + 1
            if(current_node.next_node != None):
                current_node.next_node.previous_node = current_node.previous_node
            if(current_node.previous_node != None):
                current_node.previous_node.next_node = current_node.next_node    
        return current_node
            
    
    def make_empty(self) -> None:
        self.head = None
        self.tail = None
        self.num_elements = 0
        """Removes all elements from the list."""

    
    def iterator(self) -> Iterator:
        """Returns an iterator of the elements in the list (in proper
        sequence)."""
