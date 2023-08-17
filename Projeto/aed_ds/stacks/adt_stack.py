from abc import ABC, abstractmethod


class Stack(ABC):
    @abstractmethod
    def is_empty(self) -> bool:
        ''' Returns true iff the stack contains no elements. '''

    @abstractmethod
    def is_full(self) -> bool:
        ''' Returns true iff the stack cannot contain more elements. '''

    @abstractmethod
    def size(self) -> int:
        ''' Returns the number of elements in the stack. '''

    @abstractmethod
    def top(self) -> object:
        ''' Returns the element at the top of the stack.
        Throws EmptyStackException '''

    @abstractmethod
    def push(self, element: object) -> None:
        ''' Inserts the specified element onto the top of the stack.
        Throws FullStackException '''

    @abstractmethod
    def pop(self) -> object:
        ''' Removes and returns the element at the top of the stack.
        Throws EmptyStackException '''