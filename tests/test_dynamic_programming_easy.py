#
#  Climbing Stairs
#  Best Time to Buy and Sell Stock
#  Maximum Subarray
#  House Robber


from typing import List


def climb_stairs(n: int) -> int:
    def dfs(i: int, memo: dict) -> int:
        # 使用 dict.get() 在 key 不存在時, 才不會報錯
        if memo.get(i):
            return memo[i]

        result = dfs(i - 1, memo) + dfs(i - 2, memo)
        memo[i] = result
        return result

    memo: dict = {1: 1, 2: 2}
    return dfs(n, memo)


def test_climb_stairs():
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(4) == 5
    assert climb_stairs(5) == 8


def max_profit(prices: List[int]) -> int:
    # 沒有到 DP
    # out of time
    max = 0
    for i, p1 in enumerate(prices):
        for j, p2 in enumerate(prices[i:]):
            print(f'i:{i}->{p1}, j:{j}->{p2}')
            profit = p2 - p1
            if profit > max:
                max = profit
    return max


def test_max_profit():
    assert max_profit([7, 1, 5, 3, 6, 3]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
