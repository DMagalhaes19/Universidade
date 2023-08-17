import unittest

from aed_ds.dictionaries.open_hash_table import OpenHashTable
from aed_ds.exceptions import NoSuchElementException, DuplicatedKeyException


class TestOpenHashTable(unittest.TestCase):
    def setUp(self):
        self.table = OpenHashTable(size=11)

    def insert_items(self, quantity, shift=0):
        for i in range(quantity):
            k = f"key_{i+1+shift}"
            v = f"value_{i+1+shift}"
            self.table.insert(k, v)

    def remove_items(self, quantity, shift=0):
        for i in range(quantity):
            k = f"key_{i+1+shift}"
            self.table.remove(k)

    def test_size_of_empty_table(self):
        self.assertEqual(self.table.size(), 0)

    def test_size(self):
        self.insert_items(5)
        self.assertEqual(self.table.size(), 5)

    def test_is_full_of_empty_table(self):
        self.assertFalse(self.table.is_full())

    def test_is_full(self):
        self.table = OpenHashTable(size=7)
        self.assertFalse(self.table.is_full())
        self.insert_items(7)
        self.assertTrue(self.table.is_full())
        self.remove_items(1)
        self.assertFalse(self.table.is_full())

    def test_get_from_empty_table(self):
        with self.assertRaises(NoSuchElementException):
            self.table.get("missing_key")

    def test_get_after_insert_removed(self):
        self.insert_items(5)
        self.remove_items(1, shift=2)
        self.insert_items(1, shift=2)
        self.assertEqual(self.table.get("key_3"), "value_3")

    def test_insert_duplicate(self):
        self.insert_items(1)
        with self.assertRaises(DuplicatedKeyException):
            self.table.insert("key_1", "value_1")

    def test_get_missing_key(self):
        self.insert_items(5)
        with self.assertRaises(NoSuchElementException):
            self.table.get("missing_key")

    def test_get_after_insert_single(self):
        self.insert_items(1)
        self.assertEqual(self.table.get("key_1"), "value_1")

    def test_get_after_insert_multiple(self):
        self.insert_items(5)
        self.assertEqual(self.table.get("key_3"), "value_3")

    def test_get_after_remove(self):
        self.insert_items(5)
        self.remove_items(1, shift=2)
        with self.assertRaises(NoSuchElementException):
            self.table.get("key_3")

    def test_update_missing_key(self):
        with self.assertRaises(NoSuchElementException):
            self.table.update("key_1", "new_value_1")

    def test_get_after_update(self):
        self.insert_items(1)
        self.table.update("key_1", "new_value_1")
        self.assertEqual(self.table.get("key_1"), "new_value_1")

    def test_remove_missing_key(self):
        with self.assertRaises(NoSuchElementException):
            self.table.remove("missing_key")

    def test_remove_from_single_element_table(self):
        self.insert_items(1)
        self.assertEqual(self.table.remove("key_1"), "value_1")

    def test_remove_from_larger_table(self):
        self.insert_items(5)
        self.assertEqual(self.table.remove("key_3"), "value_3")

    def test_remove_twice(self):
        self.insert_items(1)
        self.table.remove("key_1")
        with self.assertRaises(NoSuchElementException):
            self.table.remove("key_1")

    def test_keys_of_empty_table(self):
        self.assertEqual(self.table.keys().size(), 0)

    def test_keys(self):
        self.insert_items(5)
        self.assertEqual(self.table.keys().size(), 5)
        self.assertNotEqual(self.table.keys().find("key_1"), -1)

    def test_values_of_empty_table(self):
        self.assertEqual(self.table.values().size(), 0)

    def test_values(self):
        self.insert_items(5)
        self.assertEqual(self.table.values().size(), 5)
        self.assertNotEqual(self.table.values().find("value_1"), -1)

    def test_items_of_empty_table(self):
        self.assertEqual(self.table.items().size(), 0)

    def test_items(self):
        self.insert_items(5)
        self.assertEqual(self.table.items().size(), 5)

    def test_iterate_items(self):
        it = self.table.items().iterator()
        while it.has_next():
            item = it.get_next()
            self.assertIn(item.get_key(), [f"key_{i+1}" for i in range(5)])
            self.assertIn(item.get_value(), [f"value_{i+1}" for i in range(5)])


if __name__ == "__main__":
    unittest.main()