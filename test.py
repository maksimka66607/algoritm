import numpy as np
from zxc import deque


def test_add_to_tail():
    d = deque(5)

    d.addToTail(np.int32(10))
    d.addToTail(np.int32(20))
    d.addToTail(np.int32(30))

    assert d.accessByIndex(0) == 10
    assert d.accessByIndex(1) == 20
    assert d.accessByIndex(2) == 30


def test_add_to_head():
    d = deque(5)

    d.addToHead(np.int32(10))
    d.addToHead(np.int32(20))
    d.addToHead(np.int32(30))

    assert d.accessByIndex(0) == 30
    assert d.accessByIndex(1) == 20
    assert d.accessByIndex(2) == 10


def test_remove_from_head():
    d = deque(5)

    d.addToTail(np.int32(10))
    d.addToTail(np.int32(20))

    assert d.removeFromHead() == 10
    assert d.accessByIndex(0) == 20


def test_remove_from_tail():
    d = deque(5)

    d.addToTail(np.int32(10))
    d.addToTail(np.int32(20))

    assert d.removeFromTail() == 20
    assert d.accessByIndex(0) == 10