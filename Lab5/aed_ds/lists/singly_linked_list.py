from aed_ds.lists.singly_linked_list_iterator import SinglyLinkedListIterator
from aed_ds.lists.nodes import SingleListNode
from aed_ds.lists.adt_list import List
from aed_ds.exceptions import EmptyListException,InvalidPositionException,NoSuchElementException

class SinglyLinkedList(List): 
    def __init__(self):
        self.head = None
        self.tail = None
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
        if self.is_empty():
            raise EmptyListException()
        return self.head.get_element()
    
    def get_last(self) -> object:
        """Returns the last element of the list.
        Throws EmptyListException."""
        if self.is_empty():
           raise EmptyListException()
        return self.tail.get_element()

    def get(self, position: int) -> object:
        """Returns the element at the specified position in the list.
        Range of valid positions: 0, ..., size()-1."""
        idx = 0
        node = self.head
        if(position < 0 or position > self.num_elements):
            raise InvalidPositionException("Accessing positions smaller or greater then the number of elements")
        if(position == 0):
            return self.get_first()
        elif(position == self.num_elements-1):
            return self.get_last()
        while idx < position:
            idx += 1
            node = node.get_next_node()
        return node.get_element()

    def find(self, element: object) -> int:
        if self.is_empty():
            return -1
        node = self.head
        idx = 0
        while node != None:
            if node.get_element()==element:
                return idx
            node=node.next_node
            idx+=1
        return -1
        """Returns the position in the list of the first occurrence of the
        specified element, or -1 if the specified element does not occur in the
        list."""
    
    def insert_first(self, element: object) -> None:
        """Inserts the specified element at the first position in the list."""
        newNode = SingleListNode(element,None)
        newNode.next_node = self.head
        self.head = newNode
        if self.tail is None:
        	self.tail = newNode
        self.num_elements+=1
		

            
    def insert_last(self, element: object) -> None:
        """Inserts the specified element at the last position in the list."""
        node = SingleListNode(element,None)
        if(self.tail is not None):
        	self.tail.set_next_node(node)
        self.tail = node
        if(self.head is None):
            self.head = self.tail
        self.num_elements += 1
            
    def insert(self, element: object, position: int) -> None:
        """Inserts the specified element at the specified position in the list.
        Range of valid positions: 0, ..., size().
        If the specified position is 0, insert corresponds to insertFirst.
        If the specified position is size(), insert corresponds to insertLast.
        Throws InvalidPositionException."""
        idx = 0
        node = self.head
        if(position < 0 or position > self.num_elements):
            raise InvalidPositionException("Accessing positions smaller or greater then the number of elements")
        elif position == 0:
            self.insert_first(element)
        elif position == self.num_elements:
            self.insert_last(element)
        else:
            while idx < position-1:
                node = node.next_node
                idx += 1
            newNode = SingleListNode(element, node.next_node)
            node.next_node = newNode
            self.num_elements +=1
        
    def remove_first(self) -> object:
        """Removes and returns the element at the first position in the list.
        Throws EmptyListException."""
        if(self.num_elements == 0):
            raise EmptyListException()
        else:
            node = self.head.get_element()
            self.head = self.head.next_node
            self.num_elements -= 1
            return node 
                    
    def remove_last(self) -> object:
        """Removes and returns the element at the last position in the list.
        Throws EmptyListException."""
        node = self.head
        idx = self.num_elements-2
        if self.num_elements == 0:
            raise EmptyListException("Executing non empty list methods on an empty list.")
        else:
            while idx > 0:
                node= node.next_node
                idx-=1
            node2 = self.tail.get_element()
            node.next_node = None
            self.tail = node
            self.num_elements -= 1
        return node2

    def remove(self, position: int) -> object:
        """Removes and returns the element at the specified position in the
        list.
        Range of valid positions: 0, ..., size()-1.
        Throws InvalidPositionException."""
        if position > self.size() or position < 0 or self.is_empty():
             raise InvalidPositionException()
        else:
            if position == 0:
                return self.remove_first()
            elif position == self.size()-1:
                return self.remove_last()
            else:
                node = self.head
                position -= 1
                idx = position
                while idx >0:
                     node = node.get_next_node()
                     idx -= 1
                saveNode = node.next_node.get_element()
                node.set_next_node(node.next_node.next_node)
                self.num_elements -= 1
                return saveNode
            
                    

    def make_empty(self) -> None:
        """Removes all elements from the list."""
        """for i in range(0, len(self)-1): #v1
            self.element[i] = None"""
        self.head = None 
        self.num_elements = 0

    def iterator(self):
        it= SinglyLinkedListIterator(self.head)
        return it
        """Returns an iterator of the elements in the list (in proper
        sequence)."""