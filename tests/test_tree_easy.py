from ast import For

from leetcode.tree_easy import create_tree_from_list, is_symmetric, level_order, sorted_array_to_BST, visit, Order, max_depth, is_valid_BST


def test_is_valid_BST():
    assert is_valid_BST(create_tree_from_list([2, 1, 3])) == True
    assert is_valid_BST(create_tree_from_list(
        [5, 1, 4, None, None, 3, 6])) == False
    assert is_valid_BST(create_tree_from_list(
        [5, 4, 6, None, None, 3, 7])) == False
    assert is_valid_BST(create_tree_from_list([1, 1])) == False
    assert is_valid_BST(create_tree_from_list([1])) == True
    assert is_valid_BST(create_tree_from_list([])) == True


def test_max_depth():
    assert max_depth(create_tree_from_list([3, 9, 30, None, None, 15, 7])) == 3
    assert max_depth(create_tree_from_list([1, None, 2])) == 2


def test_is_symmetric():
    assert is_symmetric(create_tree_from_list(
        [1, 2, 2, 3, 4, 4, 3, 5, None, None, 6, 6, None, None, 5])) == True
    assert is_symmetric(create_tree_from_list([1, 2, 2, 3, 4, 4, 3])) == True
    assert is_symmetric(create_tree_from_list(
        [1, 2, 2, None, 3, None, 3])) == False
    assert is_symmetric(create_tree_from_list(
        [1, 2, 2, None, 3, 3, None])) == True


def test_level_order():
    assert level_order(create_tree_from_list([3, 9, 20, None, None, 15, 7])) == [
        [3], [9, 20], [15, 7]]
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
        [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    visit(root, order=Order.LEVELORDER, callback=lambda n: print(f'v: {n}'))


#####################
# Util Methods
#####################


def test_build_tree_from_list():
    node0 = create_tree_from_list(
        [0, 1, 2, 3, 4, None, 5, 6, 7, None, None, None, None, 8, 9])

    assert node0.val == 0
    assert node0.left.val == 1
    assert node0.right.val == 2

    node1 = node0.left
    assert node1.val == 1
    assert node1.left.val == 3
    assert node1.right.val == 4

    node2 = node0.right
    assert node2.val == 2
    assert node2.left is None
    assert node2.right.val == 5

    node3 = node0.left.left
    assert node3.val == 3
    assert node3.left.val == 6
    assert node3.right.val == 7

    node4 = node0.left.right
    assert node4.val == 4
    assert node4.left is None
    assert node4.right is None

    node6 = node0.left.left.left
    assert node6.val == 6
    assert node6.left is None
    assert node6.right is None

    visit(node0, order=Order.LEVELORDER, callback=lambda n: print(f'v: {n}'))


def test_build_tree_from_list_2():
    node3 = create_tree_from_list([3, 9, 20, None, None, 15, 7])

    assert node3.val == 3
    assert node3.left.val == 9
    assert node3.right.val == 20

    node9 = node3.left
    assert node9.val == 9
    assert node9.left is None
    assert node9.right is None

    node20 = node3.right
    assert node20.val == 20
    assert node20.left.val == 15
    assert node20.right.val == 7

    node15 = node20.left
    assert node15.val == 15
    assert node15.left is None
    assert node15.right is None

    visit(node3, order=Order.LEVELORDER, callback=lambda n: print(f'v: {n}'))


def test_build_tree_from_list_3():
    node = create_tree_from_list([3, 1])
    assert node.left is not None
    assert node.right is None

    node2 = create_tree_from_list([1])
    assert node2.left is None
    assert node2.right is None

    node3 = create_tree_from_list([])
    assert node3 is None
