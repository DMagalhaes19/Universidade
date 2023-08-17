from aed_ds.queues.adt_queue import Queue
from aed_ds.exceptions import EmptyQueueException
from aed_ds.lists.singly_linked_list import SinglyLinkedList


class ListQueue(Queue):
    def __init__(self):
        self.queue = SinglyLinkedList()

    def is_empty(self) -> bool:
        return self.queue.is_empty()

    def is_full(self) -> bool:
        return False

    def size(self) -> int:
        return self.queue.size()

    def enqueue(self, element: object) -> None:
        self.queue.insert_last(element)

    def dequeue(self) -> object:
        if self.is_empty():
            raise EmptyQueueException()
        return self.queue.remove_first()