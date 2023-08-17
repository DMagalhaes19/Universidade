from abc import ABC, abstractmethod


class Queue(ABC):
    @abstractmethod
    def is_empty(self) -> bool:
        ''' Returns true iff the queue contains no elements. '''

    @abstractmethod
    def is_full(self) -> bool:
        ''' Returns true iff the queue cannot contain more elements. '''

    @abstractmethod
    def size(self) -> int:
        ''' Returns the number of elements in the queue.'''

    @abstractmethod
    def enqueue(self, element: object) -> None:
        ''' Inserts the specified element at the rear of the queue.
        Throws FullQueueException '''

    @abstractmethod
    def dequeue(self) -> object:
        ''' Removes and returns the element at the front of the queue.
        Throws EmptyQueueException '''