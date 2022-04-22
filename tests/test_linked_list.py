from leetcode.linked_list import reverse_list, create_linked_list_from_list, merge_two_lists, merge_two_lists_by_list, \
    merge_two_lists_by_loop, merge_two_lists_by_recursive


def test_reverse_list():
    head = create_linked_list_from_list([1, 2, 3, 4, 5])
    result = reverse_list(head)

    assert result.val == 5
    assert result.next.val == 4
    assert result.next.next.val == 3
    assert result.next.next.next.val == 2
    assert result.next.next.next.next.val == 1
    assert result.next.next.next.next.next is None
    assert repr(result) == '[5, 4, 3, 2, 1]'

def test_merge_two_list_by_loop():
    list1 = create_linked_list_from_list([1, 2, 4])
    list2 = create_linked_list_from_list([1, 3, 4])

    assert repr(merge_two_lists_by_loop(list1, list2)) == '[1, 1, 2, 3, 4, 4]'

def test_merge_two_list_by_recursive():
    list1 = create_linked_list_from_list([1, 2, 4])
    list2 = create_linked_list_from_list([1, 3, 4])

    assert repr(merge_two_lists_by_recursive(list1, list2)) == '[1, 1, 2, 3, 4, 4]'

def test_merge_two_list_by_list():
    list1 = create_linked_list_from_list([1, 2, 4])
    list2 = create_linked_list_from_list([1, 3, 4])

    assert repr(merge_two_lists_by_list(list1, list2)) == '[1, 1, 2, 3, 4, 4]'


def test_create_linked_list_from_list():
    result = create_linked_list_from_list([1, 2, 3, 4, 5])
    assert result.val == 1
    assert result.next.val == 2
    assert result.next.next.val == 3
    assert result.next.next.next.val == 4
    assert result.next.next.next.next.val == 5
    assert result.next.next.next.next.next is None

    assert str(result) == '1 -> 2 -> 3 -> 4 -> 5 -> None'
    assert repr(result) == '[1, 2, 3, 4, 5]'


def test_create_linked_list_from_list_2():
    result = create_linked_list_from_list([4, 3, 2])
    assert result.val == 4
    assert result.next.val == 3
    assert result.next.next.val == 2
    assert result.next.next.next is None

    assert str(result) == '4 -> 3 -> 2 -> None'
    assert repr(result) == '[4, 3, 2]'
