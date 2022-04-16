
"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.
"""
def max_profit(prices: list[int] ) -> int:
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

"""
Remove Duplicates from Sorted Array
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""
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


