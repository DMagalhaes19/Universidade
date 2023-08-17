import ctypes

from aed_ds.stacks.adt_stack import Stack
from aed_ds.exceptions import EmptyStackException, FullStackException


class ArrayStack(Stack):
    def __init__(self, max_size):
        self.max_size = max_size
        self.array = (ctypes.py_object * self.max_size)()
        self.num_elements = 0
        self.idx = 0

    def is_empty(self) -> bool:
        return self.num_elements == 0

    def is_full(self) -> bool:
        return self.num_elements == self.max_size

    def size(self) -> int:
        return self.num_elements

    def top(self) -> object:
        if self.is_empty():
            raise EmptyStackException()
        top_idx = self.get_top_idx()
        return self.array[top_idx]

    def push(self, element: object) -> None:
        if self.is_full():
            raise FullStackException()
        self.array[self.idx] = element
        self.idx = (self.idx + 1) % self.max_size
        self.num_elements += 1

    def pop(self) -> object:
        if self.is_empty():
            raise EmptyStackException()
        self.idx = self.get_top_idx()
        element = self.array[self.idx]
        self.num_elements -= 1
        return element

    def get_top_idx(self):
        idx = self.idx - 1
        if idx < 0:
            idx = self.max_size - 1
        return idx