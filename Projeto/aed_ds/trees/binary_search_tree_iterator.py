from aed_ds.exceptions import NoSuchElementException, DuplicatedKeyException, EmptyTreeException
from aed_ds.trees.binary_tree import BinaryTree
from ..dictionaries.adt_ordered_dictionary import OrderedDictionary
from aed_ds.trees.nodes.binary_nodes import BinarySearchTreeNode
from aed_ds.adt_iterator import Iterator
from aed_ds.stacks.array_stack import ArrayStack

class BinarySearchTreeIterator(Iterator):
    def __init__(self, root, num_elements):
        self.root = root
        self.num_elements = num_elements
        self.rewind()

    def setup(self, node):
        if node is not None:
            if node.get_right_child() is not None:
                self.setup(node.get_right_child())
            self.stack.push(node)
            if node.get_left_child() is not None:
                self.setup(node.get_left_child())
    
    def has_next(self):
        return not self.stack.is_empty()

    def get_next(self):
        if not self.has_next():
            raise NoSuchElementException()
        return self.stack.pop()

    def rewind(self):
        self.stack = ArrayStack(self.num_elements)
        self.setup(self.root)