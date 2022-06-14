from typing import List, Optional


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    p1 = m - 1
    p2 = n - 1
    tail = m + n - 1
    while p1 >= 0 or p2 >= 0:
        if p1 == -1:
            # 把nums 2 剩下的部分處理完成
            nums1[tail] = nums2[p2]
            p2 -= 1
        elif p2 == -1:
            # 把 num 1 剩下的部分處理完成
            nums1[tail] = nums1[p1]
            p1 -= 1
        elif nums1[p1] > nums2[p2]:
            nums1[tail] = nums1[p1]
            p1 -= 1
        else:
            nums1[tail] = nums2[p2]
            p2 -= 1
        tail -= 1


# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return version >= 2


def first_bad_version(n: int) -> int:
    if n == 1:
        return 1

    def helper(left: int, right) -> int:
        if left >= right:
            return left

        mid = left + (right - left) // 2 + 1
        if isBadVersion(mid) and not isBadVersion(mid - 1):
            return mid
        if not isBadVersion(mid):
            return helper(mid + 1, right)
        else:
            return helper(left, mid - 1)

    return helper(1, n)
