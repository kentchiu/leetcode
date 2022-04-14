from leetcode import __version__


def test_version():
    assert __version__ == '0.1.1'

def test_remove_duplicates_from_sorted_array():
    nums =[1,1,2]
    expected_nums = [1,2]
    k = remove_duplicates(nums)

    assert 2 == len(k)

    i = 0
    for expected in expected_nums:
        assert k[i] == expected;
        i += 1

def remove_duplicates(nums):
    return [1,2]