from aed_ds.stacks.adt_stack import Stack
from aed_ds.lists.singly_linked_list import SinglyLinkedList
from aed_ds.exceptions import EmptyStackException


class ListStack(Stack):
    def __init__(self):
        self.list = SinglyLinkedList()

    def is_empty(self) -> bool:
        return self.list.is_empty()

    def is_full(self) -> bool:
        return False

    def size(self) -> int:
        return self.list.size()

    def top(self) -> object:
        if self.is_empty():
            raise EmptyStackException()
        return self.list.get_first()

    def push(self, element: object) -> None:
        self.list.insert_first(element)

    def pop(self) -> object:
        if self.is_empty():
            raise EmptyStackException()
        return self.list.remove_first()