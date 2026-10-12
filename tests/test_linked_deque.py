from collections import deque
import random
import pytest
from structures.deque import Deque


@pytest.mark.parametrize('push', ['append', 'appendleft'])
@pytest.mark.parametrize('pop', ['pop', 'popleft'])
def test_single_element_reuse(push, pop):
    values = Deque()
    for value in [None, 0, -5, 'hello']:
        getattr(values, push)(value)
        assert len(values) == 1
        assert getattr(values, pop)() == value
        assert len(values) == 0
        assert values.head is values.tail is None
    with pytest.raises(IndexError):
        getattr(values, pop)()


def test_random_operations_against_standard_deque():
    rng = random.Random(42)
    actual, expected = Deque(), deque()
    for _ in range(1000):
        operation = rng.choice(['append', 'appendleft', 'pop', 'popleft'])
        if operation.startswith('append'):
            value = rng.randrange(-100, 100)
            getattr(actual, operation)(value)
            getattr(expected, operation)(value)
        elif expected:
            assert getattr(actual, operation)() == getattr(expected, operation)()
        else:
            with pytest.raises(IndexError):
                getattr(actual, operation)()
        assert list(actual) == list(expected)
        assert len(actual) == len(expected)
