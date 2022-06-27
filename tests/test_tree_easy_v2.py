from ast import For

from leetcode.tree_easy import Order, create_tree_from_list, visit
from leetcode.tree_easy_v2 import (
    is_symmetric,
    is_valid_BST,
    level_order,
    max_depth,
    sorted_array_to_BST,
)


def test_is_valid_BST():
    assert is_valid_BST(create_tree_from_list([2, 1, 3])) == True
    assert is_valid_BST(create_tree_from_list([5, 1, 4, None, None, 3, 6])) == False
    assert is_valid_BST(create_tree_from_list([5, 4, 6, None, None, 3, 7])) == False
    assert is_valid_BST(create_tree_from_list([1, 1])) == False
    assert is_valid_BST(create_tree_from_list([1])) == True
    assert is_valid_BST(create_tree_from_list([])) == True


def test_max_depth():
    assert max_depth(create_tree_from_list([3, 9, 30, None, None, 15, 7])) == 3
    assert max_depth(create_tree_from_list([1, None, 2])) == 2


def test_is_symmetric():
    assert (
        is_symmetric(
            create_tree_from_list(
                [1, 2, 2, 3, 4, 4, 3, 5, None, None, 6, 6, None, None, 5]
            )
        )
        == True
    )
    assert is_symmetric(create_tree_from_list([1, 2, 2, 3, 4, 4, 3])) == True
    assert is_symmetric(create_tree_from_list([1, 2, 2, None, 3, None, 3])) == False
    assert is_symmetric(create_tree_from_list([1, 2, 2, None, 3, 3, None])) == True


def test_level_order():
    assert level_order(create_tree_from_list([3, 9, 20, None, None, 15, 7])) == [
        [3],
        [9, 20],
        [15, 7],
    ]
    assert level_order(create_tree_from_list([1])) == [[1]]
    assert level_order(create_tree_from_list([])) == []


def test_sorted_array_to_BST():
    node0 = sorted_array_to_BST([-10, -3, 0, 5, 9])

    assert node0.val == 0

    node10 = node0.left
    assert node10.val == -10
    node5 = node0.right
    assert node5.val == 5

    assert node10.left is None
    node3 = node10.right
    assert node3.val == -3

    assert node5.left is None
    node9 = node5.right
    assert node9.val == 9

    root = sorted_array_to_BST(
        [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    )
    visit(root, order=Order.LEVELORDER, callback=lambda n: print(f"v: {n}"))
