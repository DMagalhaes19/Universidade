from __future__ import annotations


class SingleListNode:
    """Represents a SinglyLinkedList node, with an element a pointer for the
    next node."""

    def __init__(self, element: object, next_node: SingleListNode):
        self.element = element
        self.next_node = next_node

    def get_element(self) -> object:
        return self.element

    def get_next_node(self) -> SingleListNode:
        return self.next_node

    def set_element(self, element: object) -> None:
        self.element = element

    def set_next_node(self, next_node: SingleListNode) -> None:
        self.next_node = next_node


class DoubleListNode(SingleListNode):
    def __init__(
        self, element: object, next_node: DoubleListNode, previous_node: DoubleListNode
    ):
        SingleListNode.__init__(self, element, next_node)
        self.previous_node = previous_node

    def get_previous_node(self) -> DoubleListNode:
        return self.previous_node

    def set_previous_node(self, previous_node: DoubleListNode) -> None:
        self.previous_node = previous_node