from aed_ds.exceptions import NoSuchElementException, DuplicatedKeyException, EmptyTreeException
from aed_ds.lists.singly_linked_list import SinglyLinkedList
from aed_ds.trees.binary_tree import BinaryTree
from aed_ds.trees.binary_search_tree_iterator import BinarySearchTreeIterator
from aed_ds.trees.nodes.binary_nodes import BinarySearchTreeNode
from aed_ds.dictionaries.adt_ordered_dictionary import OrderedDictionary

class BinarySearchTree(BinaryTree,OrderedDictionary):
    def __init__(self):
        BinaryTree.__init__(self)
        self.root = None
        self.num_elements = 0

    def get(self, k):
        return self._get(self.root, k)

    def _get(self, root, k):
        if root is None:
            raise NoSuchElementException()
        elif root.get_key() == k:
            return root.get_element()
        elif root.get_key() > k:
            return self._get(root.get_left_child(), k)
        else:
            return self._get(root.get_right_child(), k)

    def remove(self, k: object) -> object:
        self.root = self.remove_element(self.root, k)
        self.num_elements -= 1

    def remove_element(self, node, k):
        if node is None:
            raise NoSuchElementException()
        elif k > node.get_key():
            node_to_append = self.remove_element(node.get_right_child(), k)
            node.set_right_child(node_to_append)
        elif k < node.get_key():
            node_to_append = self.remove_element(node.get_left_child(), k)
            node.set_left_child(node_to_append)
        else:
            # caso com apenas elementos na esquerda
            if node.get_right_child() is None and node.get_left_child() is not None:
                temp = node.get_left_child()
                node = None
                return temp
            # caso com apenas elementos na direita
            elif node.get_left_child() is None and node.get_right_child() is not None:
                temp = node.get_right_child()
                node = None
                return temp
            # ambos none ou ambos com children
            else:
                aux_child = node
                aux = self.get_min_node(aux_child.get_right_child())
                if aux is not None:
                    append_to_child_of_current_node = aux.get_right_child()
                    aux_child.set_element(aux.get_element())
                else:
                    append_to_child_of_current_node = None
                    aux_child.set_right_child(append_to_child_of_current_node)
            return aux_child

    def remove_min_right_node(self, node):
        def get_parent_node(aux_child, key):
            if key > aux_child.get_key() and aux_child.get_right_child() is not None:
                if aux_child.get_right_child().get_key() == key:
                    return aux_child
                else:
                    return get_parent_node(aux_child.get_right_child(), key)
            elif key < aux_child.get_key() and aux_child.get_left_child() is not None:
                if aux_child.get_left_child().get_key() == key:
                    return aux_child
                else:
                    return get_parent_node(aux_child.get_left_child(), key)

        right_node = self.get_min_node(node.get_right_child())
        parent_node = get_parent_node(self.root, right_node.get_key())
        parent_node.set_left_child(self.get_min_node(right_node.get_right_child()))
        return right_node

    def insert(self, k, v):
        self.root = self.insert_element(self.root, k, v)

    def insert_element(self, root, k, v):
        if root is None:
            root = BinarySearchTreeNode(k, v)
            self.num_elements += 1
        else:
            if root.get_key() == k:
                raise DuplicatedKeyException()
            elif root.get_key() > k:
                node = self.insert_element(root.get_left_child(), k, v)
                root.set_left_child(node)
            else:
                node = self.insert_element(root.get_right_child(), k, v)
                root.set_right_child(node)
        return root

    def get_max_element(self) -> object:
        if self.is_empty():
            raise EmptyTreeException()
        return self.get_max_node(self.root).get_element()

    def get_max_node(self, node: BinarySearchTreeNode) -> BinarySearchTreeNode:
        if node.get_right_child() == None:
            return node
        return self.get_max_node(node.get_right_child())

    def get_min_element(self) -> object:
        if self.is_empty():
            raise EmptyTreeException()
        return self.get_min_node(self.root).get_element()

    def get_min_node(self, node: BinarySearchTreeNode) -> BinarySearchTreeNode:
        if node is None or (node is not None and node.get_left_child() is None):
            return node
        return self.get_min_node(node.get_left_child())

    def update(self, k, v):
        self.update_element(self.root, k, v)

    def update_element(self, node, k, v):
        if node is None:
            raise NoSuchElementException()
        if node.get_key() == k:
            node.set_element(v)
            return
        elif node.get_key() < k:
            node = self.update_element(node.get_right_child(), k, v)
            return
        else:
            node = self.update_element(node.get_left_child(), k, v)
            return

    def items(self):
        l = SinglyLinkedList()
        iterator = self.iterator()
        while iterator.has_next():
            item = iterator.get_next()
            l.insert_last(item)
        return l

    def iterator(self):
        return BinarySearchTreeIterator(self.root, self.num_elements)

    def keys(self):
        l = SinglyLinkedList()
        iterator = self.iterator()
        while iterator.has_next():
            item = iterator.get_next()
            l.insert_last(item.get_key())
        return l

    def values(self):
        l = SinglyLinkedList()
        iterator = self.iterator()
        while iterator.has_next():
            item = iterator.get_next()
            l.insert_last(item.get_element())
        return l