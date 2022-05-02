"""
LinkedList 特性:

1. 一開始只能知道 head node
2. 只能透過 next 做移動, 無法直接用 index 對特定位置做 access
3. 無法知道前一個 node 的值
4. 最後一個 node 的 next 為 None

解題技巧:

non in place:  如果沒有要求用 in place 處理, 可轉換成 array 處理,簡單, 直覺

in place:

linked list 通常是要求用 in place 處理, 充分利用 linked list 特性, in place 的解法可以分成

1. 用 recursive 處理 -> 通常比較簡單
2. 用 while loop 處理 -> 難度較高

用 while loop 處理時, 可以使用以下幾個技巧:

1. pre_head: 建立一個 pre_head 做不可改變的錨點, 最終把整個 linked list 串接完成後, 傳回 pre_head.next (真正的 head node)
2. 用 next, curr, prev (都是 ListNode 的 instance) 指標 cache 住當下的 snapshot, 方便後續處理
3. 用 node = node.next 讓指標前進到下一個 node

"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list_deprecated(head: ListNode | None) -> ListNode | None:
    """
    NOTE: this solution is deprecated
    cost: 150 minutes, 66%,58%
    Given the head of a singly linked list, reverse the list, and return the reversed list.
    """
    nodes = []
    node = head
    while node:
        nodes.append(node)
        node = node.next

    for idx, n in enumerate(nodes, start=0):
        rev_idx = len(nodes) - idx - 1
        if rev_idx > 0:
            nodes[rev_idx].next = nodes[rev_idx - 1]
        else:
            nodes[rev_idx].next = None

    tail = nodes[len(nodes) - 1]
    return tail


def reverse_list(head: ListNode | None) -> ListNode | None:
    prev = None
    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


def merge_two_lists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    """
    cost: days
    You are given the heads of two sorted linked lists list1 and list2.
    Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
    Return the head of the merged linked list.
    """
    return merge_two_lists_by_loop(list1, list2)


def merge_two_lists_by_loop(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    """
    list 1: 1 -> 2 -> 4
    list 2: 1 -> 3 -> 4
    result: 1 -> 1 -> 2 -> 3 -> 4 -> 4

    init state:
        dummy (固定不動)
        prev(前一個node) = dump
            v
            1 -> 2 -> 4
            v
            1 -> 3 -> 4

    step 1:
        list1 < list2 -> yes
        prev.next = list1
        list1 = list1.next
        prev = prev.next

                prev  v
        dummy ->  1 -> 2 -> 4
                 v
                 1 -> 3 -> 4

    step 2:
        list1 < list2 -> no
        prev.next = list2
        list2 = list2.next
        prev = prev.next

                      v
        dummy ->  1 -> 2 -> 4
                prev  v
                 1 -> 3 -> 4

    step 3:
        list1 < list2 -> yes
        prev.next = list1
        list1 = list1.next
        prev = prev.next

                     prev  v
        dummy ->  1 -> 2 -> 4
                      v
                 1 -> 3 -> 4

    step N:
        while list1 is None and list2  is not None
            list1 < list2 -> yes
            prev.next = list1
            list1 = list1.next
        prev = prev.next

                          prev v
        dummy ->  1 -> 2 -> 4
                           v
                 1 -> 3 -> 4

    step last:
       prev.next = list1 if list is not None else list2

    """

    dummy = ListNode()
    prev = dummy

    while list1 and list2:
        if list1.val < list2.val:
            prev.next = list1
            list1 = list1.next
        else:
            prev.next = list2
            list2 = list2.next

        prev = prev.next

    if list1 is None:
        prev.next = list2
    else:
        prev.next = list1

    return dummy.next


def merge_two_lists_by_recursive(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.val < list2.val:
        list1.next = merge_two_lists_by_recursive(list1.next, list2)
        return list1
    else:
        list2.next = merge_two_lists_by_recursive(list1, list2.next)
        return list2


def merge_two_lists_by_list(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    """
    用 list 處理, non in place 的做法, 先轉換成 list , 做完串接及排序後, 在將 list 轉成 linked list
    """
    l1 = linked_list_to_list(list1)
    l2 = linked_list_to_list(list2)
    l1.extend(l2)
    l3 = sorted(l1)
    return list_to_lined_list(l3)


def delete_node(node: ListNode):
    """
    cost: 45 minutes
    Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.
    It is guaranteed that the node to be deleted is not a tail node in the list.

    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """

    while node.next:
        node.val = node.next.val
        if node.next.next:
            node = node.next
        else:
            node.next = None


def remove_nth_from_end(head: ListNode | None, n: int) -> ListNode | None:
    """
    Given the head of a linked list, remove the nth node from the end of the list and return its head.
    """

    if n == 0:
        return head

    temp = head
    length = 0

    while temp:
        length += 1
        temp = temp.next

    idx_remove = length - n

    if idx_remove == 0:
        head = head.next
        return head

    if length == 0:
        head = None
        return head

    if length == 2:
        if n == 1:
            head.next = None
        return head

    idx = 0
    curr = head
    while curr:
        # 前門還有有 head 可以串接的狀況
        if idx_remove > 0 and idx == idx_remove - 1:
            curr.next = curr.next.next
        else:
            curr = curr.next
        idx += 1

    return head


def is_palindrome(head: ListNode | None) -> bool:
    if head is None:
        return False

    if head is not None:
        # only one node
        if head.next is None:
            return True
        # only two nodes
        elif head.next.next is None:
            # two nodes is equals
            if head.val == head.next.val:
                return True

    fast = head
    slow = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    stack = []
    middle = slow.next
    while middle:
        stack.append(middle.val)
        middle = middle.next

    while head and len(stack) != 0:
        if head.val != stack.pop():
            return False
        head = head.next

    return True


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    r"""
    cost: 60 minutes
    Given the head of a singly linked list, return the middle node of the linked list.
    If there are two middle nodes, return the second middle node.

    Input: head = [1,2,3,4,5]
    Output: [3,4,5]
    Explanation: The middle node of the list is node 3.
    """
    fast = head
    slow = head

    if fast is None or fast.next is None or fast.next.next is None:
        return None

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    if fast.next:
        return slow.next
    else:
        return slow


def has_cycle(head: Optional[ListNode]) -> bool:
    r"""
    cost: 45 minutes
    Given head, the head of a linked list, determine if the linked list has a cycle in it.
    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
    Return true if there is a cycle in the linked list. Otherwise, return false.
    """
    if head is None:
        return False

    slow = fast = head
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


#######################################
# Util Methods
#######################################


def linked_list_to_list(node: ListNode) -> [int]:
    # linked list to list
    result: [int] = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def list_to_lined_list(vals: [int]) -> ListNode:
    nodes = [ListNode(val) for val in vals]
    for idx, node in enumerate(nodes):
        if idx < len(nodes) - 1:
            node.next = nodes[idx + 1]
    return nodes[0]


def create_linked_list_from_list(nums: list):
    """
    Util method which convert list to linked list
    """
    if len(nums) == 0:
        return None

    nodes = [ListNode(num) for num in nums]
    for idx, n in enumerate(nodes):
        if idx < len(nodes) - 1:
            nodes[idx].next = nodes[idx + 1]
        else:
            nodes[idx].next = None
    return nodes[0]


def print_linked_list(node: ListNode, format='arrow') -> str:
    """
    Util method for print linked list
    """
    result = ''
    while node:
        result += str(node.val)
        if node.next:
            if format == 'list':
                result += ', '
            else:
                result += ' -> '
        node = node.next

    if format == 'list':
        result = '[' + result + ']'

    return result
