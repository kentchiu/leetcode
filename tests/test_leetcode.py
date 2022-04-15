def test_remove_duplicates_from_sorted_array_1():
    nums = [1, 1, 2]
    expected_nums = [1, 2]
    k = remove_duplicates(nums)

    assert k == len(expected_nums)

    for i, expected in enumerate(expected_nums):
        assert nums[i] == expected;


def test_remove_duplicates_from_sorted_array_2():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expected_nums = [0, 1, 2, 3, 4]
    k = remove_duplicates(nums)

    assert k == len(expected_nums)

    for i, expected in enumerate(expected_nums):
        assert nums[i] == expected;


def remove_duplicates(nums: list[int]) -> int:
    p1 = 0
    p2 = 1
    while p2 <= len(nums) - 1:
        prev_num = nums[p1]
        current_num = nums[p2]
        if current_num != prev_num:
            p1 += 1
            p2 += 1
        else:
            nums.pop(p2)
    return len(nums)


