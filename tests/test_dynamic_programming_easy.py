#
#  Climbing Stairs
#  Best Time to Buy and Sell Stock
#  Maximum Subarray
#  House Robber

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
