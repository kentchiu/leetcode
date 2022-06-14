import math
import re


def str_str(haystack: str, needle: str) -> int:
    """
    cost: 120 minutes, 94%
    Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
    A.K.A: indexOf
    """
    if len(needle) == 0 or len(haystack) == 0:
        return 0
    if len(needle) > len(haystack):
        return -1

    i = 0
    j = 0
    while i < len(haystack):
        if haystack[i] == needle[j]:
            while j < len(needle):
                if i + j >= len(haystack):
                    return -1
                if haystack[i + j] != needle[j]:
                    j = 0
                    break
                j += 1
                if j == len(needle):
                    return i
        i += 1

    return -1


def my_atoi(s: str) -> int:
    """
    cost: 180 minutes, 63%
    Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
    """
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
    min_int = int(math.pow(-2, 31))
    if int_value > max_int:
        return max_int
    if int_value < min_int:
        return min_int
    return int_value


def first_uniq_char(s: str) -> int:
    """
    cost: 90 minutes, 97%
    Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
    """
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


def reverse_string(s: list[str]) -> None:
    """
    cost: 45 minutes, 78%
    Write a function that reverses a string. The input string is given as an array of characters s.
    You must do this by modifying the input array in-place with O(1) extra memory.
    Do not return anything, modify s in-place instead.
    """
    s.insert(0, " ")
    tail = len(s) - 1
    head = 0
    for k in range(0, len(s) // 2):
        s[head] = s[tail]
        s[tail] = s[head + 1]
        head += 1
        tail -= 1
    s.pop(head)
