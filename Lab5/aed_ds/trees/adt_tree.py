from abc import ABC, abstractmethod

from aed_ds.trees.nodes.binary_nodes import BinarySearchTreeNode


class Tree(ABC):
    @abstractmethod
    def get_root(self) -> object:
        """Returns the root of the tree."""

    @abstractmethod
    def size(self) -> int:
        """Returns the number of elements in the tree."""

    @abstractmethod
    def height(self) -> int:
        """Returns the height of the tree."""

    @abstractmethod
    def is_empty(self) -> bool:
        """Returns True if the tree is empty."""

    @abstractmethod
    def is_full(self) -> bool:
        """Returns True if the tree is full."""