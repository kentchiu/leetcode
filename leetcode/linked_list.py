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


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(f'{self.val} -> {self.next}')

    def __repr__(self):
        # print('--------------------')
        nums = []
        node = self
        while node is not None:
            nums.append(node.val)
            # print(f'node.val: {node.val}')
            node = node.next

        return str(nums)



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
    You are given the heads of two sorted linked lists list1 and list2.
    Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
    Return the head of the merged linked list.
    """
    return merge_two_lists_by_loop(list1, list2)


def merge_two_lists_by_loop(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    pre_head = ListNode(None)
    tail = pre_head

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        print(f'pre_head: {repr(pre_head)},tail:{repr(tail)}, val: {tail.val}, next: {repr(tail.next)}')
        tail = tail.next

    if list1 is None:
        tail.next = list2
    elif list2 is None:
        tail.next = list1

    return pre_head.next

def merge_two_lists_by_recursive(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.val < list2.val:
        list1.next =  merge_two_lists_by_recursive(list1.next, list2)
        return list1
    else:
        list2.next =  merge_two_lists_by_recursive(list1, list2.next)
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
    return  nodes[0]


def create_linked_list_from_list(nums: list):
    """
    Util method which convert list to linked list
    """
    nodes = [ListNode(num) for num in nums]
    for idx, n in enumerate(nodes):
        if (idx < len(nodes) - 1):
            nodes[idx].next = nodes[idx + 1]
        else:
            nodes[idx].next = None
    return nodes[0]
