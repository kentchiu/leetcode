
def print_1_to_n(n: int):
    if n == 0:
        return  # Base Condition
    print_1_to_n(n - 1)  # Hypothesis
    print(n)  # Induction


def test_print_1_to_n():
    print_1_to_n(7)


def print_n_to_1(n: int):
    if n == 0:
        return  # Base Condition
    print(n)  # Induction
    print_n_to_1(n - 1)  # Hypothesis


def test_print_n_to_1():
    print_n_to_1(7)


def reverse_string(input: str):
    if input == '':
        return ""

    # Hypothesis
    s = reverse_string(input[1:])

    # Induction
    return s + input[0]


def test_reverse_string():
    assert reverse_string('hello') == 'olleh'


def is_palindrome(input: str) -> bool:
    if len(input) < 2:
        return True
    head = input[0]
    tail = input[-1]

    if head == tail:
        return is_palindrome(input[1: -1])
    else:
        return False


def test_is_palindrome():
    assert is_palindrome('kayak') == True
    assert is_palindrome('abc') == False
    assert is_palindrome('abcba') == True
    assert is_palindrome('racecar') == True
