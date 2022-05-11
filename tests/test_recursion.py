
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
    # Base Conditon
    if input == '':
        return ""

     # Shrink th problem space
    shrink = input[1:]
    s = reverse_string(shrink)

    # Smallest unit of work to contribute
    head = input[0]
    return s + head


def test_reverse_string():
    assert reverse_string('hello') == 'olleh'


def is_palindrome(input: str) -> bool:
    # Base Conditon
    if len(input) < 2:
        return True

    head = input[0]
    tail = input[-1]

    if head == tail:  # Smallest unit of work to contribute
        # Shrink th problem space
        shrink = input[1: -1]
        return is_palindrome(shrink)
    else:
        return False


def test_is_palindrome():
    assert is_palindrome('kayak') == True
    assert is_palindrome('abc') == False
    assert is_palindrome('abcba') == True
    assert is_palindrome('racecar') == True


def decimal_to_binary(decimal: int) -> str:
    # Base Condition
    if decimal < 2:
        return str(decimal)

    # Shrink the problem space
    shrink = decimal // 2
    # Smallest unit of work to contribute
    rem = str(decimal % 2)

    s = decimal_to_binary(shrink)
    return s + rem


def test_decimal_to_binary():
    assert decimal_to_binary(1) == '1'
    assert decimal_to_binary(0) == '0'
    assert decimal_to_binary(15) == '1111'
    assert decimal_to_binary(8) == '1000'
    assert decimal_to_binary(233) == '11101001'
