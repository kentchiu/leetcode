from ast import For
from enum import Enum
from operator import le
from time import perf_counter
from typing import List, Optional

Order = Enum("Order", "PREORDER INORDER POSTORDER LEVELORDER")


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        val = str(self.val)
        left, right = "", ""
        if self.left:
            left = f"({self.left.val})"
        if self.right:
            right = f"({self.right.val})"
        return f"{val}, L:{left}, R:{right}"

    def __repr__(self) -> str:
        return str(self.val)


def max_depth(root: Optional[TreeNode]) -> int:
    def visit(node: Optional[TreeNode], depth: int):
        if not node:
            return depth
        l = visit(node.left, depth + 1)
        r = visit(node.right, depth + 1)
        return max(l, r)

    return visit(root, 0)


def max_depth_2(root: Optional[TreeNode]) -> int:
    def max_depth(node: Optional[TreeNode]):
        # Base Condition
        if node is None:
            return 0

        # Hypothesis
        left = max_depth(node.left)
        right = max_depth(node.right)

        print(f"node:{node.val},L-depth:{left},R-depth:{right}")

        # Induction
        return max(left, right) + 1

    return max_depth(root)


def is_valid_BST(root: Optional[TreeNode]) -> bool:
    # Use maximal system integer to represent infinity
    import sys

    INF = sys.maxsize

    def visit(node: Optional[TreeNode], lower, upper) -> bool:
        if not node:
            return True

        if lower < node.val < upper:
            # check if all tree nodes follow BST rule
            return visit(node.left, lower, node.val) and visit(
                node.right, node.val, upper
            )
        else:
            return False

    return visit(node=root, lower=-INF, upper=INF)


def is_symmetric(root: Optional[TreeNode]) -> bool:
    """

    1.???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
    2.??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????

    ?????????????????????????????????????????????????????????????????????A??????????????????????????????A?????????????????????A????????????????????????

    ???????????????????????????????????????????????????????????? ????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
    ??????????????????????????????????????????????????????????????????????????????A????????????????????????????????????????????????

    def ??????A???????????????????????? ???????????????????????????????????? ??? ??????A??????????????????????????????????????????????????????A?????????????????????????????????????????????????????? ????????????

    """

    def is_mirror(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        #  no child
        if node1 is None and node2 is None:
            return True

        #  ??????????????????
        if node1 is None or node2 is None:
            return False

        # ???????????????
        return (
            node1.val == node2.val
            and is_mirror(node1.left, node2.right)
            and is_mirror(node1.right, node2.left)
        )

    if root is None:
        return True

    return is_mirror(root.left, root.right)


def level_order(root: TreeNode) -> List[List[int]]:
    """
    ref: [BFS ?????????????????????????????????????????????????????????](https://leetcode.cn/problems/binary-tree-level-order-traversal/solution/bfs-de-shi-yong-chang-jing-zong-jie-ceng-xu-bian-l/)

    Args:
        root (TreeNode): _description_

    Returns:
        List[List[int]]: _description_
    """

    def monkey_dump(self):
        return f"{self.val}@{self.level}"

    TreeNode.__repr__ = monkey_dump

    def add_to_level_dict(level_dict: dict, node: TreeNode):
        level = level_dict.get(node.level) if level_dict.get(node.level) else []
        level.append(node.val)
        level_dict.update({node.level: level})

    if root is None:
        return []

    root.level = 0
    nodes = []
    q = [root]
    level_dict: dict[int, int] = {}
    while len(q) != 0:
        print(f"q: {q}")
        node = q[0]
        nodes.append(node)
        add_to_level_dict(level_dict, node)
        q.pop(0)
        if node.left:
            node.left.level = node.level + 1
            q.append(node.left)
        if node.right:
            node.right.level = node.level + 1
            q.append(node.right)

    return list(level_dict.values())


def sorted_array_to_BST(nums: List[int]) -> Optional[TreeNode]:
    # 1. input array ???????????????, ?????? root
    # 2. input array ??????????????????????????? left
    # 3. input array ??????????????????????????? right
    # 4. ??????????????????????????????, ?????????????????????, ??????????????????, ???????????????
    # 5. ??? left, ??? root, ??? right ??? root

    def helper(nums, left, right) -> Optional[TreeNode]:
        if left > right:
            return None

        mid = (left + right) // 2

        root = TreeNode(nums[mid])
        root.left = helper(nums, left, mid - 1)
        root.right = helper(nums, mid + 1, right)

        return root

    return helper(nums, 0, len(nums) - 1)


#####################
# Util Methods
#####################
def create_tree_from_list(list: list) -> Optional[TreeNode]:
    node_list = [TreeNode(item) for item in list]

    if len(node_list) == 2:
        node_list[0].left = node_list[1]
        return node_list[0]

    if len(node_list) == 0:
        return None

    for idx in range(0, len(list) // 2):
        v = node_list[idx]
        l = node_list[2 * idx + 1]
        r = node_list[2 * idx + 2]
        if v:
            v.left = l if l.val else None
            v.right = r if r.val else None

    # visit(, callback=lambda n : print(f'n: {n}'))
    return node_list[0]


Order = Enum("Order", "PREORDER INORDER POSTORDER LEVELORDER")


def visit(node: TreeNode, order: Order = Order.PREORDER, callback=None):
    r"""
    https://web.ntnu.edu.tw/~algo/BinaryTree5.png
    PreOrder:   0125742598
    InOrder:    6371402859
    PostOrder:  6734189520
    LevelOrder: 0123456789
    """
    if order is Order.LEVELORDER:
        # ?????????????????????, ????????????left, right ?????? queue, queue?????????, ??????????????? level ??? left, right, left, right, ...
        queue = [node]
        while len(queue) != 0:
            curr = queue[0]
            queue = queue[1:]
            callback(curr)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
    else:
        if node is None:
            return
        if order is Order.PREORDER:
            callback(node)

        visit(node.left, order)

        if order is Order.INORDER:
            callback(node)

        visit(node.right, order)

        if order is Order.POSTORDER:
            callback(node)


def prettyPrintTree(node, prefix="", isLeft=True):
    if not node:
        print("Empty Tree")
        return

    if node.right:
        prettyPrintTree(node.right, prefix + ("???   " if isLeft else "    "), False)

    print(prefix + ("????????? " if isLeft else "????????? ") + str(node.val))

    if node.left:
        prettyPrintTree(node.left, prefix + ("    " if isLeft else "???   "), True)


def stringToIntegerList(input):
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr
