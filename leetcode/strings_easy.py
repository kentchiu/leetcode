#  Reverse String, First Unique Character in a String, String to Integer (atoi) and Implement strStr().


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
