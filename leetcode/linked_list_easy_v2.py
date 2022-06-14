from typing import Optional
from leetcode.linked_list_easy import ListNode


def reverse_list(head: ListNode | None) -> ListNode | None:
    if head is None:
        return None

    if head.next is None:
        return head

    # 這邊比較特別, 通用的形式是 head.next = recursion()
    # 但是 reverse 後, tail 變 head , 所以要把 tail 記錄下來, 並且不要改變他
    tail = reverse_list(head.next)
    # 由後往前逐一處理每個節點
    head.next.next = head  # 下一個節點的 next 指向 current node (a.k.a head)
    head.next = None  # 原來 head 的 next 取消

    return tail


def merge_two_lists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    if list1 is None:
        return list2

    if list2 is None:
        return list1

    if list1.val < list2.val:
        list1.next = merge_two_lists(list1.next, list2)
        return list1
    else:
        list2.next = merge_two_lists(list1, list2.next)
        return list2


def delete_node(node: ListNode):
    # 把 next copy 過來目前的node , 在跳過 next
    node.val = node.next.val
    node.next = node.next.next


def remove_nth_from_end(head: ListNode | None, n: int) -> ListNode | None:

    count = 0

    def helper(node: ListNode | None, n: int) -> ListNode | None:
        if node is None:
            return None

        node.next = helper(node.next, n)
        # 在 reverse的過程加入一個 count 計數目前做了幾次"歸"的操作
        nonlocal count
        count += 1
        if count == n:
            return node.next  # nth 時, 返回下一個節點, 就會跳過目前節點, 達到刪除的效果
        return node

    return helper(head, n)


def is_palindrome(head: ListNode) -> bool:
    def helper(node: ListNode) -> bool:
        if node is None:
            return True

        if helper(node.next):  # recursion call
            nonlocal head
            if head.val != node.val:  # node 是reverse order 由後往前跑
                return False
            head = head.next  # head 由前往後跑
            return True
        else:
            return False

    return helper(head)


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    def solve(node: Optional[ListNode]) -> Optional[ListNode]:
        nonlocal n
        nonlocal len
        nonlocal mid

        if node is None:
            return

        n += 1

        if node.next is None:  # 最後一個節點時, 可以取得總長度
            len = n

        node.next = solve(node.next)

        if n == len // 2 + 1:
            mid = node

        n -= 1
        return node

    n = 0  # 計算目前節點數
    len = 0  # LinkedList 長度
    mid = None  # LinkedList 中間節點

    solve(head)
    return mid


def has_cycle(head: Optional[ListNode]) -> bool:
    """
    沒有找到使用 recursion 的解法
    """
    slow, fast = head, head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


def sum(head: ListNode) -> int:
    if head is None:
        return 0

    return head.val + sum(head.next)


def delete_duplicates(head: ListNode) -> ListNode:
    if head is None:
        return None

    if head.next is None:
        return head

    head.next = delete_duplicates(head.next)
    if head.val == head.next.val:
        head.next = head.next.next

    return head


def append_node(head: ListNode, val: int) -> ListNode:
    if head is None:
        return None

    head.next = append_node(head.next, val)

    if head.next is None:
        head.next = ListNode(val)
    return head


def insert_sorted(head: ListNode, val: int) -> ListNode:
    if head is None:
        return None

    head.next = insert_sorted(head.next, val)

    if head.next is None:
        head.next = ListNode(val)
    elif head.next.val > val:
        head.next.next = None
        head.next = ListNode(val, head.next)

    return head


def remove_first(head: ListNode, val: int) -> ListNode:
    if head is None:
        return None

    if head.val == val:
        head = head.next
    else:
        head.next = remove_first(head.next, val)

    return head


def remove_all(head: ListNode, val: int) -> ListNode:
    if head is None:
        return None

    # 跟 remove_first 解法類似, recursion call 的 result 是下一個節點的處理結果
    if head.val == val:
        head = remove_all(head.next, val)
    else:
        head.next = remove_all(head.next, val)
    return head
