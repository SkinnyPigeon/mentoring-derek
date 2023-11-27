# A Binary Search Tree API with recursive methods in standard library

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left_child = None
        self.right_child = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if node is None:
            return Node(key, value)
        if key < node.key:
            node.left_child = self._insert(node.left_child, key, value)
        elif key > node.key:
            node.right_child = self._insert(node.right_child, key, value)
        else:
            node.value = value
        return node
    
    def search(self, key):
        return self._search(self.root, key)
    
    def _search(self, node, key):
        if node is None:
            return None
        if key < node.key:
            return self._search(node.left_child, key)
        elif key > node.key:
            return self._search(node.right_child, key)
        else:
            return node.value

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left_child = self._delete(node.left_child, key)
        elif key > node.key:
            node.right_child = self._delete(node.right_child, key)
        else:
            if node.left_child is None:
                return node.right_child
            elif node.right_child is None:
                return node.left_child
            else:
                node.key, node.value = self._find_min(node.right_child)
                node.right_child = self._delete(node.right_child, node.key)
        return node
    
    def _find_min(self, node):
        while node.left_child is not None:
            node = node.left_child
        return node.key, node.value
