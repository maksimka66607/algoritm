import pytest
from structures.linked_list import LinkedList


def test_append_prepend_and_remove():
    values = LinkedList()
    values.append(2)
    values.prepend(1)
    values.append(3)
    values.append(2)
    assert list(values) == [1, 2, 3, 2]
    values.remove(2)
    assert list(values) == [1, 3, 2]
    values.remove(1)
    values.remove(2)
    assert len(values) == 1
    assert values.tail is values.head
    values.remove(3)
    assert values.head is values.tail is None
    assert len(values) == 0
    values.prepend(4)
    values.append(5)
    assert list(values) == [4, 5]


def test_missing_value_and_empty_iteration():
    values = LinkedList()
    assert list(values) == []
    with pytest.raises(ValueError):
        values.remove(1)
    values.append(2)
    with pytest.raises(ValueError):
        values.remove(1)
    assert list(values) == [2]
    assert len(values) == 1
