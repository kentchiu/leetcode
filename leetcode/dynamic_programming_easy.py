#
#  Climbing Stairs
#  Best Time to Buy and Sell Stock
#  Maximum Subarray
#  House Robber


from typing import List


def climb_stairs(n: int) -> int:
    # 沒有用到 DP, DP通常會使用 iteration 而不是 recursion
    def dfs(i: int, memo: dict) -> int:
        # 使用 dict.get() 在 key 不存在時, 才不會報錯
        if memo.get(i):
            return memo[i]

        result = dfs(i - 1, memo) + dfs(i - 2, memo)
        memo[i] = result
        return result

    memo: dict = {1: 1, 2: 2}
    return dfs(n, memo)


def max_profit_timeout(prices: List[int]) -> int:
    # 沒有到 DP
    # out of time
    max = 0
    for i, p1 in enumerate(prices):
        for j, p2 in enumerate(prices[i:]):
            print(f"i:{i}->{p1}, j:{j}->{p2}")
            profit = p2 - p1
            if profit > max:
                max = profit
    return max


def max_profit(prices: List[int]) -> int:
    # 這個算是 two pointer 的解法, 也不太算是 DP
    min_price = float("inf")
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit
