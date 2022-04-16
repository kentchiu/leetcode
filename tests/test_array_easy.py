from leetcode.array_easy import remove_duplicates, max_profit


def test_max_profit():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 7
    assert max_profit([1,2,3,4,5]) == 4
    assert max_profit([7,6,4,3,1]) == 0


def test_remove_duplicates_1():
    nums = [1, 1, 2]
    expected_nums = [1, 2]
    k = remove_duplicates(nums)

    assert k == len(expected_nums)

    for i, expected in enumerate(expected_nums):
        assert nums[i] == expected;


def test_remove_duplicates_2():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expected_nums = [0, 1, 2, 3, 4]
    k = remove_duplicates(nums)

    assert k == len(expected_nums)

    for i, expected in enumerate(expected_nums):
        assert nums[i] == expected;




