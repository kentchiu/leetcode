## Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

```code
  3
 / \
9  20
   / \
  15  7
```

```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

## Fail Case:

date: (2022/05/09)
source: SELF

```code
  3          level 0
 / \
9  20        level 1
   / \
  15  7      level 2
```

直覺上, 這個用可以層序來處理, 困難的點在: 無法知道那些 nodes 是在同一個 level

利用 **PERFACT** binary tree 的特性, children nodes 數量為 parent node 的兩倍的特性, 可以換算出 level = len(nodes) / 2

```code
      3          level 0
   /    \
  9     20       level 1
 / \    / \
0   0  15  7     level 2
```

```python
    result: List[List[int]] = []
    # level 0
    level = 0
    nodes_count_of_level = 2 ** level
    node3 = root
    result.append([node3.val])

    # level 1
    level = 1
    nodes_count_of_level = 2 ** level
    node9: TreeNode = node3.left
    node20: TreeNode = node3.right
    result.append([node9.val, node20.val])

    # level 2
    level = 2
    nodes_count_of_level = 2 ** level
    node0: TreeNode = node9.left
    node0:  TreeNode = node9.right
    node15: TreeNode = node20.left
    node7: TreeNode = node20.right
    result.append([node0.val, node0.val,node15.val, node7.val])
```

### 檢討

不可行,因為 traversal 的方式是 call node.left, node.right, 上面的方式無法取得 parent node, 就算 parent node 記錄起來, 如果遇到 parent node 是 None 是, node.left , node.right 還是得要做計數, 而且, 變成了 special case, 整個 code 的可讀性會不好.

## Solution:

date: (2022/05/09)
source: 官方解法

讓每個 node 記住直接的 level, root node level=0 , root.left, root.right 的 level 為 root.level + 1, 最後再把所有的 node 依 level 用 dictionary 分類, 取出 values, 做成 2 dimensions array

### 檢討

1. dictionary 那邊的處理, 目前寫成 function, 應該有更好的寫法
2. 應該可以用 list 來取帶 dictionary , 透過 level 的 previous value 跟 cuurent value 相同是, 放在同一個 list; 不同時, 建立一個新的 list 來存放新的 level
3. 要找出規律, 然後, 專著在處理一組 (root, root.left, root.right) , 其他的放心交給 recursion
