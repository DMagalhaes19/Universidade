from aed_ds.trees.nodes.binary_nodes import BinaryTreeNode
from aed_ds.exceptions import EmptyTreeException
from aed_ds.trees.adt_tree import Tree


class BinaryTree(Tree):
    root: BinaryTreeNode
    num_elements: int

    def __init__(self):
        self.root = None
        self.num_elements = 0

    def get_root(self) -> object:
        """Returns the root element of the tree.
        Throws EmptyTreeException"""
        if self.root is None:
            raise EmptyTreeException()
        return self.root.get_element()

    def size(self) -> int:
        """Returns the number of elements in the tree."""
        return self.num_elements

    def height(self) -> int:
        """Returns the height of the tree."""
        if self.is_empty():
            raise EmptyTreeException()
        return self.node_height(self.root)

    def node_height(self, node: BinaryTreeNode) -> int:
        """Calculate the height of a single node."""
        if node is None:
            return 0
        return 1 + max(
            self.node_height(node.get_left_child()),
            self.node_height(node.get_right_child()),
        )

    def is_empty(self) -> bool:
        """Returns True if the tree is empty."""
        return self.size() == 0

    def is_full(self) -> bool:
        """Returns True if the tree is full."""
        return False

    def str_tree(self, root: BinaryTreeNode) -> str:
        if root is None:
            return "" + self.str_node(root)
        return (
            self.str_node(root)
            + "["
            + self.str_tree(root.get_left_child())
            + "]"
            + "["
            + self.str_tree(root.get_right_child())
            + "]"
        )

    def str_node(self, node: BinaryTreeNode) -> str:
        if node is None:
            return "X"
        else:
            return "(" + str(node.get_key()) + ")"

    def __str__(self) -> str:
        return self.str_tree(self.root)