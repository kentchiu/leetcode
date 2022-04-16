from leetcode.array_easy import remove_duplicates, max_profit, rotate


def test_rotate():
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 1
    rotate(nums, k)
    assert nums == [7, 1, 2, 3, 4, 5, 6]

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 2
    rotate(nums, k)
    assert nums == [6, 7, 1, 2, 3, 4, 5]

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    rotate(nums, k)
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    nums = [-1,-100,3,99]
    k = 1
    rotate(nums, k)
    assert nums ==  [99,-1,-100,3]

    nums = [-1,-100,3,99]
    k = 2
    rotate(nums, k)
    assert nums == [3,99,-1,-100]


def test_max_profit():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 7
    assert max_profit([1, 2, 3, 4, 5]) == 4
    assert max_profit([7, 6, 4, 3, 1]) == 0


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
