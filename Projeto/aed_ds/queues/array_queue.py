import ctypes

from aed_ds.queues.adt_queue import Queue
from aed_ds.exceptions import EmptyQueueException, FullQueueException


class ArrayQueue(Queue):
    def __init__(self, max_size):
        self.max_size = max_size
        self.array = (ctypes.py_object * self.max_size)()
        self.num_elements = 0
        self.start = 0
        self.end = 0

    def is_empty(self) -> bool:
        return self.num_elements == 0

    def is_full(self) -> bool:
        return self.num_elements == self.max_size

    def size(self) -> int:
        return self.num_elements

    def enqueue(self, element: object) -> None:
        if self.is_full():
            raise FullQueueException()
        self.array[self.end] = element
        self.end = (self.end + 1) % self.max_size
        self.num_elements += 1

    def dequeue(self) -> object:
        if self.is_empty():
            raise EmptyQueueException()
        element = self.array[self.start]
        self.start = (self.start + 1) % self.max_size
        self.num_elements -= 1
        return element