

from leetcode.sort_and_searching_easy import merge


def test_merge():
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    merge(nums1=nums1, m=m, nums2=nums2, n=n)
    assert nums1 == [1]

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    merge(nums1=nums1, m=m, nums2=nums2, n=n)
    assert nums1 == [1]

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1=nums1, m=m, nums2=nums2, n=n)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1
    merge(nums1=nums1, m=m, nums2=nums2, n=n)
    assert nums1 == [1, 2]
