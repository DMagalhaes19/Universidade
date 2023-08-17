import unittest

from aed_ds.exceptions import EmptyTreeException, NoSuchElementException
from aed_ds.trees.binary_search_tree import BinarySearchTree
from aed_ds.trees.binary_search_tree_iterator import BinarySearchTreeIterator


class TestBinarySearchTreeIterator(unittest.TestCase):

    tree: BinarySearchTree
    iterator: BinarySearchTreeIterator

    def setUp(self) -> None:
        self.tree = BinarySearchTree()
        self.tree.insert(2, "value_2")
        self.tree.insert(5, "value_5")
        self.tree.insert(3, "value_3")
        self.tree.insert(4, "value_4")
        self.tree.insert(1, "value_1")
        self.iterator = self.tree.iterator()

    def test_get_root_empty_tree(self):
        self.tree = BinarySearchTree()
        with self.assertRaises(EmptyTreeException):
            self.tree.get_root()

    def test_get_root(self):
        self.assertEqual(self.tree.get_root(), "value_2")

    def test_has_next_when_empty(self):
        empty_tree = BinarySearchTree()
        iterator = empty_tree.iterator()
        self.assertFalse(iterator.has_next())

    def test_has_next_after_constructor(self):
        self.assertTrue(self.iterator.has_next())

    def test_get_next_when_empty(self):
        empty_tree = BinarySearchTree()
        iterator = empty_tree.iterator()
        with self.assertRaises(NoSuchElementException):
            iterator.get_next()

    def test_has_next_after_get_next(self):
        self.assertTrue(self.iterator.has_next())
        self.iterator.get_next()
        self.assertTrue(self.iterator.has_next())
        self.iterator.get_next()
        self.assertTrue(self.iterator.has_next())
        self.iterator.get_next()
        self.assertTrue(self.iterator.has_next())
        self.iterator.get_next()
        self.assertTrue(self.iterator.has_next())
        self.iterator.get_next()
        self.assertFalse(self.iterator.has_next())

    def test_has_next_after_rewind(self):
        for _ in range(5):
            self.iterator.get_next()
        self.assertFalse(self.iterator.has_next())
        self.iterator.rewind()
        self.assertTrue(self.iterator.has_next())