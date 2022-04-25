from leetcode.linked_list import reverse_list, create_linked_list_from_list, merge_two_lists_by_list, \
    merge_two_lists_by_loop, merge_two_lists_by_recursive, print_linked_list


def test_reverse_list():
    head = create_linked_list_from_list([1, 2, 3, 4, 5])
    result = reverse_list(head)

    assert result.val == 5
    assert result.next.val == 4
    assert result.next.next.val == 3
    assert result.next.next.next.val == 2
    assert result.next.next.next.next.val == 1
    assert result.next.next.next.next.next is None
    assert print_linked_list(result, format='list') == '[5, 4, 3, 2, 1]'


def test_merge_two_list_by_loop():
    list1 = create_linked_list_from_list([1, 2, 4])
    list2 = create_linked_list_from_list([1, 3, 4])

    assert print_linked_list(merge_two_lists_by_loop(list1, list2), format='list') == '[1, 1, 2, 3, 4, 4]'


def test_merge_two_list_by_recursive():
    list1 = create_linked_list_from_list([1, 2, 4])
    list2 = create_linked_list_from_list([1, 3, 4])

    assert print_linked_list(merge_two_lists_by_recursive(list1, list2), format='list') == '[1, 1, 2, 3, 4, 4]'


def test_merge_two_list_by_list():
    list1 = create_linked_list_from_list([1, 2, 4])
    list2 = create_linked_list_from_list([1, 3, 4])

    assert print_linked_list(merge_two_lists_by_list(list1, list2), format='list') == '[1, 1, 2, 3, 4, 4]'


def test_create_linked_list_from_list():
    result = create_linked_list_from_list([1, 2, 3, 4, 5])
    assert result.val == 1
    assert result.next.val == 2
    assert result.next.next.val == 3
    assert result.next.next.next.val == 4
    assert result.next.next.next.next.val == 5
    assert result.next.next.next.next.next is None

    assert print_linked_list(result) == '1 -> 2 -> 3 -> 4 -> 5'
    assert print_linked_list(result, format='list') == '[1, 2, 3, 4, 5]'


def test_create_linked_list_from_list_2():
    result = create_linked_list_from_list([4, 3, 2])
    assert result.val == 4
    assert result.next.val == 3
    assert result.next.next.val == 2
    assert result.next.next.next is None

    assert print_linked_list(result) == '4 -> 3 -> 2'
    assert print_linked_list(result, format='list') == '[4, 3, 2]'


def test_print_linked_list():
    l1 = create_linked_list_from_list([1, 2, 3])
    assert str(print_linked_list(l1)) == '1 -> 2 -> 3'
    assert str(print_linked_list(l1, format='arrow')) == '1 -> 2 -> 3'
    assert str(print_linked_list(l1, format='list')) == '[1, 2, 3]'

    l2 = create_linked_list_from_list([5, 4, 3, 2, 1])
    assert str(print_linked_list(l2)) == '5 -> 4 -> 3 -> 2 -> 1'

    l3 = create_linked_list_from_list([0])
    assert str(print_linked_list(l3)) == '0'

    l4 = create_linked_list_from_list([])
    assert str(print_linked_list(l4)) == ''
