
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
    # Base Condition
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
    # Base Condition
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


def sum_of_nums(num: int) -> int:
    if num <= 0:
        return 0

    shrink = num - 1
    s = sum_of_nums(shrink)
    return s + num


def test_sum_of_nums():
    assert sum_of_nums(10) == 55
    assert sum_of_nums(9) == 45
    assert sum_of_nums(0) == 0
    assert sum_of_nums(1) == 1
    assert sum_of_nums(-10) == 0


def binary_search(input: list[int], target: int) -> int:
    def helper(input: list[int], target: int, left: int, right: int) -> int:
        # Base Condition
        if left > right:
            return -1

        # mid 每次會縮小一半, 但是這邊沒有達到完全 shrink 的效果, 如果 right - left = 1, mid 會是 0,
        # 再次 right - left 的結果都是 1, 形成 infinity loop
        mid = left + (right-left) // 2

        print(f'L:{left}, R: {right}, m: {mid}, mv: {input[mid]}')

        if input[mid] == target:
            return mid

        if input[mid] < target:
            # 注意, 新的 left 必須是 mid + 1 而不是 mid, 這樣才有 shrink problem space 的效果
            # 或許可以這樣想,  mid 所在的值已經在  input[mid] < target 比對過了,
            # 而 helper method 要完全捨棄掉 左半部或是右半部, 所以, 要包含 mid 本身一起捨棄掉
            # 也就是需要對 mid 做 +1 (捨棄 left part) 或 mid 做 -1(捨棄 right part)
            return helper(input, target, mid + 1, right)
        else:
            # 注意, 新的 right 必須是 mid - 1 而不是 mid, 這樣才有 shrink problem space 的效果
            return helper(input, target, left, mid - 1)

    return helper(input, target, 0, len(input) - 1)


def test_binary_search():
    assert binary_search([-1, 0, 1, 2, 3, 4, 7, 9, 10, 20], 10) == 8
    assert binary_search([-1, 0, 1, 2, 3, 4, 7, 9, 10, 20], 8) == -1
    assert binary_search([-1, 0, 1, 2, 3, 4, 7, 9, 10, 20], -1) == -0
    assert binary_search([1, 2, 3, 4, 5], 5) == 4


def fibonacci(n: int) -> list[int]:
    """
    要從最滿足第一個 recursive call, 讓 n 有初始值 , 才有辦法做 n -1 , n-2 的 recrustions
    """
    # Base Condition
    if n == 0 or n == 1:
        return n
    else:
        # Shrink the problem space  n - 1, n - 2
        # Smallest unit of work to contribute F(n-1) + F(n-2)
        fn_1 = fibonacci(n - 1)
        fn_2 = fibonacci(n - 2)
        # 這邊故意拆成 fn_1, fn_2 寫, 來呈現出 fn_1 評估完成, 才會進行到fn_2
        return fn_1 + fn_2


def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
