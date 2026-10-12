"""Дек на двусвязных узлах; операции с концами за O(1)."""
from dataclasses import dataclass


@dataclass
class Node:
    value: object
    prev: 'Node | None' = None
    next: 'Node | None' = None


class Deque:
    def __init__(self):
        self.head = self.tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def append(self, value):
        node = Node(value, prev=self.tail)
        if self.tail:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node
        self._size += 1

    def appendleft(self, value):
        node = Node(value, next=self.head)
        if self.head:
            self.head.prev = node
        else:
            self.tail = node
        self.head = node
        self._size += 1

    def pop(self):
        if self.tail is None:
            raise IndexError('empty deque')
        value = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self._size -= 1
        return value

    def popleft(self):
        if self.head is None:
            raise IndexError('empty deque')
        value = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self._size -= 1
        return value
