import math
from leetcode.strings_easy import reverse_string, first_uniq_char, my_atoi


def test_my_atoi():
    assert my_atoi("42") == 42
    assert my_atoi("    -42") == -42
    assert my_atoi("4193 with word") == 4193
    assert my_atoi("123456789012345678901234567890") == math.pow(2, 31) - 1
    assert my_atoi("-123456789012345678901234567890") == math.pow(-2, 31)
    assert my_atoi("words and 987") == 0
    assert my_atoi("3.14159") == 3
    assert my_atoi(" ") == 0
    assert my_atoi("") == 0
    assert my_atoi("  -0012a42") == -12

def test_first_uniq_char():
    assert first_uniq_char("dddccdbba") == 8
    assert first_uniq_char("leetcode") == 0
    assert first_uniq_char("loveleetcode") == 2
    assert first_uniq_char("aabb") == -1
    assert first_uniq_char("z") == 0


def test_rotate():
    s = ["h", "e", "l", "l", "o"]
    reverse_string(s)
    assert s == ["o", "l", "l", "e", "h"]

    s = ["H", "a", "n", "n", "a", "h"]
    reverse_string(s)
    assert s == ["h", "a", "n", "n", "a", "H"]
