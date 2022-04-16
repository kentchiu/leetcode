from leetcode.strings_easy import reverse_string


def test_rotate():
    s = ["h", "e", "l", "l", "o"]
    reverse_string(s)
    assert s == ["o", "l", "l", "e", "h"]

    s = ["H", "a", "n", "n", "a", "h"]
    reverse_string(s)
    assert s == ["h", "a", "n", "n", "a", "H"]

    s = ["1", "2", "3", "4", "5", "6", "7","8","9"]
    reverse_string(s)
    print(f'---->{s}')
