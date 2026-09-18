import pytest

from zxc import Deque


def contents(dq):
    return [dq.get(i) for i in range(dq.count)]


def test_new_deque_is_empty():
    dq = Deque(3)

    assert dq.is_empty()
    assert not dq.is_full()
    assert dq.count == 0


@pytest.mark.parametrize(
    ("method", "expected"),
    [
        ("push_front", [30, 20, 10]),
        ("push_back", [10, 20, 30]),
    ],
)
def test_push(method, expected):
    dq = Deque(3)

    for value in [10, 20, 30]:
        getattr(dq, method)(value)

    assert contents(dq) == expected
    assert dq.count == 3
    assert dq.is_full()


@pytest.mark.parametrize(
    ("method", "expected"),
    [
        ("pop_front", [10, 20, 30]),
        ("pop_back", [30, 20, 10]),
    ],
)
def test_pop(method, expected):
    dq = Deque(3)
    for value in [10, 20, 30]:
        dq.push_back(value)

    result = [getattr(dq, method)() for _ in range(3)]

    assert result == expected
    assert dq.count == 0
    assert dq.is_empty()
    assert not dq.is_full()


@pytest.mark.parametrize("method", ["push_front", "push_back"])
def test_overflow_does_not_change_deque(method, capsys):
    dq = Deque(2)
    dq.push_back(10)
    dq.push_back(20)
    state = (dq.head, dq.tail, dq.count)

    getattr(dq, method)(99)

    assert contents(dq) == [10, 20]
    assert (dq.head, dq.tail, dq.count) == state
    assert "Дек переполнен!" in capsys.readouterr().out


@pytest.mark.parametrize("method", ["pop_front", "pop_back"])
def test_pop_empty_deque(method, capsys):
    dq = Deque(3)
    state = (dq.head, dq.tail, dq.count)

    assert getattr(dq, method)() is None
    assert (dq.head, dq.tail, dq.count) == state
    assert "Дек пуст!" in capsys.readouterr().out


@pytest.mark.parametrize("index", [-1, 2, 3, 100])
def test_invalid_index(index, capsys):
    dq = Deque(3)
    dq.push_back(10)
    dq.push_back(20)

    assert dq.get(index) is None
    assert contents(dq) == [10, 20]
    assert "Неверный индекс!" in capsys.readouterr().out


def test_get_from_empty_deque():
    assert Deque(3).get(0) is None


def test_wraparound_back():
    dq = Deque(3)
    for value in [10, 20, 30]:
        dq.push_back(value)

    assert dq.pop_front() == 10
    assert dq.pop_front() == 20

    dq.push_back(40)
    dq.push_back(50)

    assert contents(dq) == [30, 40, 50]
    assert dq.is_full()


def test_wraparound_front():
    dq = Deque(3)
    for value in [10, 20, 30]:
        dq.push_front(value)

    assert dq.pop_back() == 10
    assert dq.pop_back() == 20

    dq.push_front(40)
    dq.push_front(50)

    assert contents(dq) == [50, 40, 30]
    assert dq.is_full()


def test_mixed_operations():
    dq = Deque(4)
    dq.push_back(20)
    dq.push_front(10)
    dq.push_back(30)
    dq.push_front(0)

    assert contents(dq) == [0, 10, 20, 30]
    assert dq.pop_front() == 0
    assert dq.pop_back() == 30
    assert contents(dq) == [10, 20]


@pytest.mark.parametrize("push", ["push_front", "push_back"])
@pytest.mark.parametrize("pop", ["pop_front", "pop_back"])
def test_single_slot_reuse(push, pop):
    dq = Deque(1)

    for value in [0, -5, 42]:
        getattr(dq, push)(value)
        assert dq.is_full()
        assert dq.get(0) == value

        assert getattr(dq, pop)() == value
        assert dq.is_empty()


def test_show_empty(capsys):
    Deque(3).show()

    assert capsys.readouterr().out == "Дек пуст\n"


def test_show_nonempty(capsys):
    dq = Deque(3)
    dq.push_back(10)
    dq.push_front(20)
    capsys.readouterr()

    dq.show()

    assert capsys.readouterr().out == (
        "Дек: [20, 10]\n"
        "Размер: 2/3\n"
    )