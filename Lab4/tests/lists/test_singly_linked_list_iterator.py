import unittest

from aed_ds.lists.singly_linked_list import SinglyLinkedList
from aed_ds.exceptions import NoSuchElementException


class TestSinglyLinkedListIterator(unittest.TestCase):
    def setUp(self):
        pass

    def test_has_next(self):
        singly_linked_list = SinglyLinkedList()
        it = singly_linked_list.iterator()
        self.assertFalse(it.has_next())
        singly_linked_list.insert_last("element 1")
        singly_linked_list.insert_last("element 2")
        singly_linked_list.insert_last("element 3")
        it = singly_linked_list.iterator()
        self.assertTrue(it.has_next())
        it.get_next()
        self.assertTrue(it.has_next())
        it.get_next()
        self.assertTrue(it.has_next())
        it.get_next()
        self.assertFalse(it.has_next())

    def test_next(self):
        singly_linked_list = SinglyLinkedList()
        it = singly_linked_list.iterator()
        with self.assertRaises(NoSuchElementException):
            it.get_next()
        singly_linked_list.insert_last("element 1")
        singly_linked_list.insert_last("element 2")
        singly_linked_list.insert_last("element 3")
        it = singly_linked_list.iterator()
        self.assertEqual(it.get_next(), "element 1")
        self.assertEqual(it.get_next(), "element 2")
        self.assertEqual(it.get_next(), "element 3")
        with self.assertRaises(NoSuchElementException):
            it.get_next()

    def test_rewind(self):
        singly_linked_list = SinglyLinkedList()
        singly_linked_list.insert_last("element 1")
        singly_linked_list.insert_last("element 2")
        singly_linked_list.insert_last("element 3")
        it = singly_linked_list.iterator()
        self.assertEqual(it.get_next(), "element 1")
        self.assertEqual(it.get_next(), "element 2")
        it.rewind()
        self.assertEqual(it.get_next(), "element 1")


if __name__ == "__main__":
    unittest.main()