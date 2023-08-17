from aed_ds.adt_iterator import Iterator
from aed_ds.lists.nodes import SingleListNode
from aed_ds.lists.adt_list import List
from aed_ds.exceptions import EmptyListException,InvalidPositionException,NoSuchElementException

class SinglyLinkedList(List): 
    def __init__(self):
        self.head = None
        self.tail = None
        self.next_node = None
        self.num_elements = 0
        
    def is_empty(self) -> bool:
        """Returns true iff the list contains no elements."""
        if(self.num_elements == 0):
            return True
        else:
            return False

    def size(self) -> int:
        """Returns the number of elements in the list."""
        return self.num_elements

    def get_first(self) -> object:
        """Returns the first element of the list.
        Throws EmptyListException."""
        if(self.head is  None):
            raise EmptyListException("Executing non empty list methods on an empty list.")
        else:
            return self.head
    
    def get_last(self) -> object:
        """Returns the last element of the list.
        Throws EmptyListException."""
        if(self.tail is None):
            raise EmptyListException("Executing non empty list methods on an empty list.")
        else:
            return self.tail

    def get(self, position: int) -> object:
        """Returns the element at the specified position in the list.
        Range of valid positions: 0, ..., size()-1."""
        idx = 0
        node = SingleListNode(self.head,self.tail)
        if(position < 0 or position > self.num_elements):
            raise InvalidPositionException("Accessing positions smaller or greater then the number of elements")
        while node != None:
            if(idx==position):
                return node.get_element()
            idx += 1
            node = node.get_next_node()

    def find(self, element: object) -> int:
        idx = 0
        node = SingleListNode(self.head,element)
        while(idx <=  self.num_elements):
            if(SingleListNode.get_next_node(node) == element):
                return idx
            else:
                node = SingleListNode.get_next_node(node)
                idx+=1
        """Returns the position in the list of the first occurrence of the
        specified element, or -1 if the specified element does not occur in the
        list."""
    
    def insert_first(self, element: object) -> None:
        """Inserts the specified element at the first position in the list."""
        node = SingleListNode(self.head,self.tail)
        if self.head != None:
            element = node.get_next_node(self)
        self.head = element
        self.num_elements += 1

            
    def insert_last(self, element: object) -> None:
        """Inserts the specified element at the last position in the list."""
        node = SingleListNode(self.head,element)
        i = 0
        while node != None:
            if(i == self.num_elements):
                node = SingleListNode.set_element(node,element)
            i += 1
        self.num_elements += 1
            
    def insert(self, element: object, position: int) -> None:
        """Inserts the specified element at the specified position in the list.
        Range of valid positions: 0, ..., size().
        If the specified position is 0, insert corresponds to insertFirst.
        If the specified position is size(), insert corresponds to insertLast.
        Throws InvalidPositionException."""
        i = 0
        node = self.head
        if(position < 0 or position > self.num_elements):
            raise InvalidPositionException("Accessing positions smaller or greater then the number of elements")
        elif position == 0:
            self.insert_first(element)
        elif position == self.num_elements:
            self.insert_last(element)
        else:
            while node != None:
                if(i == position):
                    node = SingleListNode.set_element(self,element)
                i += 1
        self.num_elements += 1
        
    def remove_first(self) -> object:
        """Removes and returns the element at the first position in the list.
        Throws EmptyListException."""
        aux = self.head
        if(self.head is None):
            raise EmptyListException("Executing non empty list methods on an empty list.")
        node = SingleListNode(self.head,self.tail)
        self.head = node.next_node
        return aux
            

    def remove_last(self) -> object:
        """Removes and returns the element at the last position in the list.
        Throws EmptyListException."""
        node = SingleListNode(self.head,self.tail)
        aux = self.tail
        idx = 0 
        while idx <= self.num_elements:
            if(idx == self.num_elements-1):
                self.tail = node
            idx += 1
            node = SingleListNode.get_next_node(self)
        return aux

    def remove(self, position: int) -> object:
        """Removes and returns the element at the specified position in the
        list.
        Range of valid positions: 0, ..., size()-1.
        Throws InvalidPositionException."""
        i = 0
        node = self.head
        if position > 0 and position != self.num_elements:
            if position == 0:
                self.remove_first(self)
            elif position==self.num_elements:
                self.remove_last(self)
            else:
                while node != None:
                    if(i == position):
                        node.set_element()
                        return node.get_element()
                    node.get_next_node()
                    i += 1

    def make_empty(self) -> None:
        """Removes all elements from the list."""
        """for i in range(0, len(self)-1): #v1
            self.element[i] = None"""
        self.head = None 
        self.tail = None
        self.num_elements = 0

    def iterator(self) -> Iterator:
        """Returns an iterator of the elements in the list (in proper
        sequence)."""