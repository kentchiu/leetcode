from ast import For
from enum import Enum
from operator import le
from optparse import Option
from re import I
from time import perf_counter
from typing import List, Optional
from unittest import result

from leetcode.tree_easy import TreeNode


def max_depth(root: Optional[TreeNode]) -> int:
    def helper(root: Optional[TreeNode], depth=0):
        if root is None:
            return depth
        else:
            return max(helper(root.left, depth + 1), helper(root.right, depth + 1))

    return helper(root)


def is_valid_BST(root: Optional[TreeNode]) -> bool:
    """
    有效 二叉搜索樹定義如下：

    1. 節點的左子樹只包含 小於 當前節點的數。
    2. 節點的右子樹只包含 大於 當前節點的數。
    2. 所有左子樹和右子樹自身必須也是二叉搜索樹。 (特別注意)
    """
    upper = float("inf")
    lower = float("-inf")

    def helper(root: Optional[TreeNode], lower: int, upper: int) -> bool:
        if root is None:
            return True

        if lower < root.val < upper:
            # 檢查左子樹的值是否在負無限大 ~ 目前節點的值之間,     檢查右子樹的值是否在目前節點的值 ~ 無限大之間
            return helper(root.left, lower, root.val) and helper(
                root.right, root.val, upper
            )
        else:
            return False

    return helper(root, lower, upper)


def is_symmetric(root: Optional[TreeNode]) -> bool:
    """
    https://leetcode.cn/problems/symmetric-tree/
    """

    def helper(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        if left.val != right.val:
            return False

        # 重點: 把 tree 分成左右子樹, 在判斷左子樹的“左”邊,是否跟右子樹的“右”邊相等,以及左子樹的“右”邊,是否跟右子樹的“左”邊相等
        return helper(left.left, right.right) and helper(left.right, right.left)

    return helper(root.left, root.right)


def level_order(root: TreeNode) -> List[List[int]]:
    if root is None:
        return []

    results = []
    queue = [root]
    while queue:
        level = []
        for i in range(0, len(queue)):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        results.append(level)
    return results


def sorted_array_to_BST(nums: List[int]) -> Optional[TreeNode]:
    def helper(left, right):
        if left > right:
            return None

        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = helper(left, mid - 1)  # 左半部的右邊界要 -1 才會有 shrink 的效果
        root.right = helper(mid + 1, right)  # 右半部的左邊界要 +1 才會有 shrink 的效果
        return root

    return helper(0, len(nums) - 1)
