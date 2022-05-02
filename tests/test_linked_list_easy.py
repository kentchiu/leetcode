from leetcode.linked_list_easy import reverse_list, create_linked_list_from_list, merge_two_lists_by_list, \
    merge_two_lists_by_loop, merge_two_lists_by_recursive, print_linked_list, delete_node, remove_nth_from_end, \
    is_palindrome, middle_node, has_cycle


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


def test_delete_note():
    head = create_linked_list_from_list([4, 5, 1, 9])
    assert print_linked_list(head) == '4 -> 5 -> 1 -> 9'
    delete_node(head.next)
    assert print_linked_list(head) == '4 -> 1 -> 9'


def test_remove_nth_from_end():
    head = create_linked_list_from_list([1, 2, 3, 4, 5])
    assert print_linked_list(remove_nth_from_end(head, 2), format='list') == '[1, 2, 3, 5]'

    head2 = create_linked_list_from_list([1])
    assert print_linked_list(remove_nth_from_end(head2, 1), format='list') == '[]'

    head3 = create_linked_list_from_list([1, 2])
    assert print_linked_list(remove_nth_from_end(head3, 1), format='list') == '[1]'

    head4 = create_linked_list_from_list([1, 2])
    assert print_linked_list(remove_nth_from_end(head4, 2), format='list') == '[2]'

    head5 = create_linked_list_from_list([1, 2, 3])
    assert print_linked_list(remove_nth_from_end(head5, 3), format='list') == '[2, 3]'


def test_is_palindrome():
    assert is_palindrome(create_linked_list_from_list([1, 2, 2, 1])) == True
    assert is_palindrome(create_linked_list_from_list([1, 2, 3, 2, 1])) == True
    assert is_palindrome(create_linked_list_from_list([1, 2, 3, 2])) == False
    assert is_palindrome(create_linked_list_from_list([1, 2])) == False
    assert is_palindrome(create_linked_list_from_list([0, 0])) == True
    assert is_palindrome(create_linked_list_from_list([1])) == True
    assert is_palindrome(None) == False


def test_middle_node():
    assert middle_node(create_linked_list_from_list([1, 2, 3, 4, 5])).val == 3
    assert middle_node(create_linked_list_from_list([1, 2, 3, 4, 5, 6])).val == 4
    assert middle_node(create_linked_list_from_list([1, 2])) is None
    assert middle_node(create_linked_list_from_list([1])) is None
    assert middle_node(None) is None


def test_has_cycle():
    l1 = create_linked_list_from_list([1])
    assert has_cycle(l1) == False

    l2 = create_linked_list_from_list([1, 2])
    assert has_cycle(l2) == False
    l2.next.next = l2
    assert has_cycle(l2) == True

    l3 = create_linked_list_from_list([3, 2, 0, -4])
    l3.next.next.next.next = l3.next
    assert has_cycle(l3) == True


##########################
# Test Until Methods
##########################
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
