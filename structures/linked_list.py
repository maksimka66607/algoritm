"""Односвязный список."""
from dataclasses import dataclass


@dataclass
class Node:
    value: object
    next: 'Node | None' = None


class LinkedList:
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
        node = Node(value)
        if self.tail:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node
        self._size += 1

    def prepend(self, value):
        self.head = Node(value, self.head)
        if self.tail is None:
            self.tail = self.head
        self._size += 1

    def remove(self, value):
        previous, node = None, self.head
        while node:
            if node.value == value:
                if previous:
                    previous.next = node.next
                else:
                    self.head = node.next
                if node is self.tail:
                    self.tail = previous
                self._size -= 1
                return
            previous, node = node, node.next
        raise ValueError(value)
