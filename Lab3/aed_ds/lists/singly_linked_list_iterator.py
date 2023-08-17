from aed_ds.adt_iterator import Iterator
import aed_ds.exceptions as ex

class SinglyLinkedListIterator(Iterator):
    def __init__(self, head):
        self.current = head
        
    def has_next(self) -> bool():
        if self.current == None:
            raise StopIteration
        elif self.current.next() != None:
            return True
        else:
            return False
    
    def get_next(self) -> object:
        if self.current.next() != None:
            self.current = self.current.next
            return self.current
        else:
            raise ex.NoSuchElementException
            
    def rewind(self):
        raise StopIteration
        if self.current != None:
            return self.head