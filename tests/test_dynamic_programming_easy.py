#
#  Climbing Stairs
#  Best Time to Buy and Sell Stock
#  Maximum Subarray
#  House Robber


from typing import List

from leetcode.dynamic_programming_easy import climb_stairs, max_profit


def test_climb_stairs():
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(4) == 5
    assert climb_stairs(5) == 8


def test_max_profit():
    assert max_profit([7, 1, 5, 3, 6, 3]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
