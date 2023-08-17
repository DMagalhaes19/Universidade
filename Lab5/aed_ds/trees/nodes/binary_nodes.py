from __future__ import annotations


class BinaryTreeNode:
    def __init__(self, element=None, left_child=None, right_child=None):
        self.element = element
        self.left_child = left_child
        self.right_child = right_child

    def get_element(self) -> object:
        return self.element

    def set_element(self, element: object) -> None:
        self.element = element

    def get_left_child(self) -> BinaryTreeNode:
        return self.left_child

    def set_left_child(self, left_child: BinaryTreeNode) -> None:
        self.left_child = left_child

    def get_right_child(self) -> BinaryTreeNode:
        return self.right_child

    def set_right_child(self, right_child: BinaryTreeNode) -> None:
        self.right_child = right_child

    def is_leaf(self) -> bool:
        return self.left_child is None and self.right_child is None


class BinarySearchTreeNode(BinaryTreeNode):
    def __init__(
        self,
        key: object = None,
        element: object = None,
        left_child: BinarySearchTreeNode = None,
        right_child: BinarySearchTreeNode = None,
    ):
        BinaryTreeNode.__init__(self, element, left_child, right_child)
        self.key = key

    def get_key(self) -> object:
        return self.key