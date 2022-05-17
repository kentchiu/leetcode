#
#  Climbing Stairs
#  Best Time to Buy and Sell Stock
#  Maximum Subarray
#  House Robber

def climb_stairs(n: int) -> int:
    # fn = f(n-1) + f(n-2)
    if n == 1:
        return 1
    if n == 2:
        return 2

    return climb_stairs(n - 1) + climb_stairs(n - 2)


def test_climb_stairs():
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(4) == 5
    assert climb_stairs(5) == 8
