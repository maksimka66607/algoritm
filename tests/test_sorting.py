import random
import pytest
from sorting.bubble_sort import bubble_sort
from sorting.quick_sort import quick_sort


@pytest.mark.parametrize('sort', [bubble_sort, quick_sort])
@pytest.mark.parametrize('values', [[], [1], [2, 1], [1, 2, 3], [3, 2, 1],
                                   [5] * 20, [0, -1, 2, -1, 0], ['z', 'a', 'b']])
def test_edge_cases(sort, values):
    original = values.copy()
    assert sort(values) == sorted(values)
    assert values == original
    assert sort(iter(values)) == sorted(values)


@pytest.mark.parametrize('sort', [bubble_sort, quick_sort])
def test_random_inputs(sort):
    rng = random.Random(42)
    for size in range(100):
        values = [rng.randrange(-50, 51) for _ in range(size)]
        assert sort(values) == sorted(values)


def test_quick_sort_large_inputs():
    for values in [list(range(10000)), list(range(10000, 0, -1)), [1] * 10000]:
        assert quick_sort(values) == sorted(values)
