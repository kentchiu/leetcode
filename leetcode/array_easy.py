from typing import List


def rotate(nums: list[int], k: int) -> None:
    """
    cost 60 minutes, 15%
    Given an array, rotate the array to the right by k steps, where k is non-negative.
    Do not return anything, modify nums in-place instead.
    """
    for i in range(0, k):
        last = nums[len(nums) - 1]
        # TODO: insert and pop only once and use index switch to improve performance
        nums.insert(0, last)
        nums.pop(len(nums) - 1)


def max_profit(prices: list[int]) -> int:
    """
    cost: 120 minutes, 93%
    You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
    On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
    Find and return the maximum profit you can achieve.
    """
    profits: list[int] = []
    i = 1
    while i < len(prices):
        prev_price = prices[i - 1]
        curr_price = prices[i]
        profit = curr_price - prev_price
        if profit > 0:
            profits.append(profit)
        i += 1
    return sum(profits)


def remove_duplicates(nums: list[int]) -> int:
    """
    cost: 240 minutes, 33%
    Remove Duplicates from Sorted Array
    Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
    Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
    Return k after placing the final result in the first k slots of nums.
    Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
    """
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


def two_sum_slow(nums: List[int], target: int) -> List[int]:
    length = len(nums)

    for i in range(length):
        for j in range(i + 1, length):
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum(nums: List[int], target: int) -> List[int]:
    for idx, n in enumerate(nums):
        # python ??? try catch cost ??????, 3.11 ???, ????????? zero cost ??? exception handling
        try:
            # index ??????????????? idx + 1 ?????????, !!!python AWESOME!!!
            idx2 = nums.index(target - n, idx + 1)
            return [idx, idx2]
        except ValueError:
            pass
