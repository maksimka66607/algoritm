import random
import pytest
from structures.avl_tree import AVLTree


def check_tree(tree, expected):
    def visit(node, lower=None, upper=None):
        if node is None:
            return 0
        assert lower is None or lower < node.key
        assert upper is None or node.key < upper
        left = visit(node.left, lower, node.key)
        right = visit(node.right, node.key, upper)
        assert abs(left - right) <= 1
        assert node.height == 1 + max(left, right)
        return node.height
    visit(tree.root)
    assert list(tree) == sorted(expected)
    assert len(tree) == len(expected)


@pytest.mark.parametrize('keys', [[3, 2, 1], [1, 2, 3], [3, 1, 2], [1, 3, 2]])
def test_all_rotation_types(keys):
    tree = AVLTree()
    for key in keys:
        tree.insert(key)
    assert tree.root.key == 2
    check_tree(tree, {1, 2, 3})


def test_duplicates_search_and_missing_delete():
    tree = AVLTree()
    with pytest.raises(KeyError):
        tree.remove(7)
    tree.insert(7)
    tree.insert(7)
    assert 7 in tree
    assert 8 not in tree
    with pytest.raises(KeyError):
        tree.remove(8)
    check_tree(tree, {7})
    tree.remove(7)
    check_tree(tree, set())


def test_insert_and_delete_rebalance():
    tree = AVLTree()
    expected = set()
    keys = list(range(200))
    for key in keys:
        tree.insert(key)
        expected.add(key)
        check_tree(tree, expected)
    random.Random(42).shuffle(keys)
    for key in keys:
        tree.remove(key)
        expected.remove(key)
        check_tree(tree, expected)


def test_random_mixed_operations():
    rng = random.Random(2026)
    tree, expected = AVLTree(), set()
    for _ in range(1000):
        key = rng.randrange(-100, 100)
        if rng.randrange(2):
            tree.insert(key)
            expected.add(key)
        elif key in expected:
            tree.remove(key)
            expected.remove(key)
        else:
            with pytest.raises(KeyError):
                tree.remove(key)
        assert (key in tree) == (key in expected)
        check_tree(tree, expected)
