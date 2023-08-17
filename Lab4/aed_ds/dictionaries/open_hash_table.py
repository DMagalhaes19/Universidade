from aed_ds.dictionaries.adt_dictionary import Dictionary
from aed_ds.lists.singly_linked_list import SinglyLinkedList
from aed_ds.dictionaries.item import Item
from aed_ds.exceptions import EmptyListException,InvalidPositionException,NoSuchElementException,EmptyStackException,FullStackException,EmptyQueueException,FullQueueException,DuplicatedKeyException,EmptyDictionaryException,EmptyTreeException
import ctypes

class OpenHashTable(Dictionary,SinglyLinkedList):
    def __init__(self, size):
        self.quantity = size
        self.buckets = (self.quantity * ctypes.py_object)()
        for i in range(self.quantity):
            self.buckets[i] = SinglyLinkedList()
        self.lenght = 0
        
    def size(self) -> int:
        return self.lenght
        """Returns the number of elements in the dictionary."""

    
    def is_full(self) -> bool:
        for i in range(self.quantity):
            if self.buckets[i].is_empty():
                return False
        return True
        """Returns true if the dictionary is full.
        Throws NoSuchElementException"""

    
    def get(self, k: object) -> object:
        index=self.hash(k)
        it=self.buckets[index].iterator()
        while it.has_next():
            item=it.get_next()
            if item.get_key()==k:
                return item.get_value()
        raise NoSuchElementException()
        """Returns the value associated with key k.
        Throws NoSuchElementException"""

    
    def insert(self, k: object, v: object) -> None:                        
        index = self.hash(k)
        it = self.buckets[index].iterator()
        while it.has_next():
            item = it.get_next()
            if item.get_key() == k:
                raise DuplicatedKeyException
        item = Item(k,v)
        self.buckets[index].insert_last(item)
        self.lenght += 1            
        """Inserts a new value, associated with key k.
            Throws DuplicatedKeyException"""
            
    
    def update(self, k: object, v: object) -> None:     
        i = 0
        index=self.hash(k)
        it=self.buckets[index].iterator()
        while it.has_next():
            item=it.get_next()
            if item.get_key()==k:
                self.buckets[index].remove(i)
                self.buckets[index].insert(Item(k,v),i)
                return
            i += 1
        raise NoSuchElementException()
        """Updates the value associated with key k.
        """"Throws NoSuchElementException"""

    
    def remove(self, k: object) -> object:  
        i = 0
        index=self.hash(k)
        it=self.buckets[index].iterator()
        while it.has_next():
            item=it.get_next()
            if item.get_key()==k:
                self.buckets[index].remove(i)
                return item.get_value()
            i +=1
            self.lenght -= 1
        raise NoSuchElementException()                
        """Removes the item with key k, and returns the value associated with it.
        Throws NoSuchElementException"""

    
    def keys(self)->list:        
        lista=SinglyLinkedList()
        for i in self.buckets:
            it=i.iterator()
            while it.has_next():
                item=it.get_next()
                lista.insert_last(item.get_key())
        return lista
        """Returns a List with all the keys in the dictionary."""

    
    def values(self) -> list:
        lista= SinglyLinkedList()
        for i in self.buckets:
            it=i.iterator()
            while it.has_next():
                item=it.get_next()
                lista.insert_last(item.get_value())
        return lista
        """Returns a List with all the values in the dictionary."""

    def items(self) -> list:
        lista = SinglyLinkedList()
        for i in self.buckets:
            it=i.iterator()
            while it.has_next():
                item=it.get_next()
                lista.insert_last(item)
        return lista
        """Returns a List with all the key value pairs in the dictionary."""
    
    def hash(self,key):
        result = 0
        a = 127
        for b in key:
            result = (result * a + ord(b)) % self.quantity
        return result