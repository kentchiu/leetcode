import re
import math
#  Reverse String, First Unique Character in a String, String to Integer (atoi) and Implement strStr().

"""
cost: 180 minutes, 63%
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
"""
def my_atoi(s: str) -> int:
    regex = r"^\s*(?P<num>[+|-]?\d+\.?\d*)"
    match = re.search(regex, s, re.DOTALL | re.MULTILINE)
    if match is None:
        return 0

    num_val = match.group()
    try:
        int_value = int(float(num_val))
    except:
        return 0

    max_int = int(math.pow(2, 31) - 1)
    min_int = int(math.pow(-2, 31) )
    if int_value > max_int:
        return max_int
    if int_value < min_int:
        return min_int
    return int_value


"""
cost: 90 minutes, 97%
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""


def first_uniq_char(s: str) -> int:
    ## shortcircuit for single character
    if len(s) == 1:
        return 0

    duplicates = set()
    for idx, c in enumerate(s):
        if idx > len(s) - 1:
            return -1

        #  bypass duplicated characters
        if c not in duplicates:
            find = s.find(c, idx + 1)
            if find != -1:
                duplicates.add(c)
            else:
                return idx
    return -1


"""
cost: 45 minutes, 78%
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
"""


def reverse_string(s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    s.insert(0, ' ')
    tail = len(s) - 1
    head = 0
    for k in range(0, len(s) // 2):
        s[head] = s[tail]
        s[tail] = s[head + 1]
        head += 1
        tail -= 1
    s.pop(head)
