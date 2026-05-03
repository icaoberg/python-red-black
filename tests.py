import pytest
from RedBlackTree import RedBlackTree

def test_empty():
    tree = RedBlackTree()
    assert tree.is_empty()
    assert tree.size() == 0
    assert len(tree) == 0

def test_insert():
    tree = RedBlackTree()
    for i, val in enumerate([5, 3, 7, 1, 4]):
        tree.insert(val)
        assert tree.size() == i + 1
    assert not tree.is_empty()

def test_inorder():
    tree = RedBlackTree()
    for val in [5, 3, 7, 1, 4]:
        tree.insert(val)
    assert tree.inorder() == [1, 3, 4, 5, 7]

def test_min_max():
    tree = RedBlackTree()
    tree.random(10)
    assert tree.min() == 0
    assert tree.max() == 9

def test_min_max_empty():
    tree = RedBlackTree()
    assert tree.min() is None
    assert tree.max() is None

def test_min_max_single():
    tree = RedBlackTree()
    tree.insert(42)
    assert tree.min() == 42
    assert tree.max() == 42

def test_random():
    tree = RedBlackTree()
    tree.random(10)
    assert tree.size() == 10

def test_random_invalid():
    tree = RedBlackTree()
    tree.random(0)
    assert tree.is_empty()

def test_search():
    tree = RedBlackTree()
    for val in [5, 3, 7, 1, 4]:
        tree.insert(val)
    assert tree.search(3) is not None
    assert tree.search(99) is None

def test_root_is_black():
    tree = RedBlackTree()
    for val in [5, 3, 7, 1, 4]:
        tree.insert(val)
    assert tree.get_root().is_black()

def test_inorder_is_sorted():
    tree = RedBlackTree()
    tree.random(20)
    result = tree.inorder()
    assert result == sorted(result)

def test_repr():
    tree = RedBlackTree()
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    assert repr(tree) == "RedBlackTree(size=3, inorder=[1, 2, 3])"
