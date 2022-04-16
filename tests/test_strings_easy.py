from leetcode.strings_easy import reverse_string, first_uniq_char


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
