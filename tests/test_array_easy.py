from leetcode.array_easy import remove_duplicates


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




