import pytest
from structures.array import DynamicArray


def test_growth_read_write_and_pop():
    array = DynamicArray()
    for value in range(100):
        array.append(value)
    assert len(array) == 100
    assert list(array) == list(range(100))
    array[50] = -1
    assert array[50] == -1
    assert [array.pop() for _ in range(49)] == list(range(99, 50, -1))
    assert array.pop() == -1
    for _ in range(50):
        array.pop()
    assert len(array) == 0
    array.append(None)
    assert array.pop() is None


@pytest.mark.parametrize('index', [-1, 0, 10])
def test_empty_index(index):
    array = DynamicArray()
    with pytest.raises(IndexError):
        _ = array[index]
    with pytest.raises(IndexError):
        array[index] = 5


def test_empty_pop_and_upper_bound():
    array = DynamicArray()
    with pytest.raises(IndexError):
        array.pop()
    array.append('a')
    with pytest.raises(IndexError):
        _ = array[1]
