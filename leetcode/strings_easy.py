#  Reverse String, First Unique Character in a String, String to Integer (atoi) and Implement strStr().

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
    tail = len(s) -1
    head = 0
    for k in range(0 , len(s) // 2):
        s[head] = s[tail]
        s[tail] = s[head +1]
        head += 1
        tail -= 1
    s.pop(head)