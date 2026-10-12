"""АВЛ-дерево уникальных сравнимых ключей."""
from dataclasses import dataclass


@dataclass
class Node:
    key: object
    left: 'Node | None' = None
    right: 'Node | None' = None
    height: int = 1


def _height(node):
    return node.height if node else 0


def _update(node):
    node.height = 1 + max(_height(node.left), _height(node.right))


def _rotate_right(node):
    root = node.left
    node.left = root.right
    root.right = node
    _update(node)
    _update(root)
    return root


def _rotate_left(node):
    root = node.right
    node.right = root.left
    root.left = node
    _update(node)
    _update(root)
    return root


def _balance(node):
    _update(node)
    factor = _height(node.left) - _height(node.right)
    if factor > 1:
        if _height(node.left.left) < _height(node.left.right):
            node.left = _rotate_left(node.left)
        return _rotate_right(node)
    if factor < -1:
        if _height(node.right.right) < _height(node.right.left):
            node.right = _rotate_right(node.right)
        return _rotate_left(node)
    return node


class AVLTree:
    def __init__(self):
        self.root = None
        self._size = 0

    def __len__(self):
        return self._size

    def __contains__(self, key):
        node = self.root
        while node:
            if key == node.key:
                return True
            node = node.left if key < node.key else node.right
        return False

    def __iter__(self):
        def walk(node):
            if node:
                yield from walk(node.left)
                yield node.key
                yield from walk(node.right)
        return walk(self.root)

    def insert(self, key):
        """Добавляет ключ; повторная вставка ничего не меняет."""
        def add(node):
            if node is None:
                self._size += 1
                return Node(key)
            if key < node.key:
                node.left = add(node.left)
            elif key > node.key:
                node.right = add(node.right)
            else:
                return node
            return _balance(node)
        self.root = add(self.root)

    def remove(self, key):
        """Удаляет ключ; отсутствующий ключ вызывает KeyError."""
        def delete(node, target):
            if node is None:
                raise KeyError(target)
            if target < node.key:
                node.left = delete(node.left, target)
            elif target > node.key:
                node.right = delete(node.right, target)
            else:
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                successor = node.right
                while successor.left:
                    successor = successor.left
                node.key = successor.key
                node.right = delete(node.right, successor.key)
            return _balance(node)
        self.root = delete(self.root, key)
        self._size -= 1
