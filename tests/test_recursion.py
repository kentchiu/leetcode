
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
