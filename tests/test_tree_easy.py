from enum import Enum


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        val = str(self.val)
        left, right = '', ''
        if self.left:
            left  = f'({self.left.val})'
        if self.right:
            right  = f'({self.right.val})'
        return f'{val}, L:{left}, R:{right}'

def build_tree_from_list():
    pass

def dump_tree():
    pass;


def test_build_tree_from_list():
    r"""
    https://web.ntnu.edu.tw/~algo/BinaryTree5.png
    PreOrder:   0125742598
    InOrder:    6371402859
    PostOrder:  6734189520
    LevelOrder: 0123456789
    """
    node9 = TreeNode(9)
    node8 = TreeNode(8)
    node7 = TreeNode(7)
    node6 = TreeNode(6)
    node5 = TreeNode(5, node8, node9)
    node4 = TreeNode(4)

    node3 = TreeNode(3, node6, node7)
    node2 = TreeNode(2, None, node5)

    node1 = TreeNode(1, node3, node4)
    node0 = TreeNode(0, node1, node2)

    assert node0.val == 0
    assert node0.left.val == 1
    assert node0.right.val == 2


    assert node1.val == 1
    assert node1.left.val == 3
    assert node1.right.val == 4

    assert node2.val == 2
    assert node2.left is None
    assert node2.right.val == 5


    visit(node0, order=Order.INORDER)


Order = Enum('Order','PREORDER INORDER POSTORDER LEVELORDER')

def visit(node: TreeNode, order: Order = Order.PREORDER ):
    if node is None:
        return

    if order is Order.PREORDER:
        print(f'val: {node}')

    visit(node.left, order)

    if order is Order.INORDER:
        print(f'val: {node}')

    visit(node.right, order)

    if order is Order.POSTORDER:
        print(f'val: {node}')

