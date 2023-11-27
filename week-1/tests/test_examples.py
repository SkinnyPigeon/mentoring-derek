from examples import (
    count_words,
    reverse_string,
    is_palindrome,
    is_anagram,
    find_missing_numbers,
    find_missing_numbers_2,
    Stack,
    max_subarray_sum,
    max_subarray_values,
    ListNode,
    reverse_linked_list,
    longest_common_prefix,
    is_valid_parentheses,
)


def test_count_words():
    input = "I love coding in Python"
    assert count_words(input) == 5


def test_reverse_string():
    input = "Hello, World!"
    expected = "!dlroW ,olleH"
    assert expected == reverse_string(input)


def test_is_palindrome():
    is_true = "racecar"
    is_false = "motorcar"
    assert is_palindrome(is_true) is True
    assert is_palindrome(is_false) is False


def test_is_anagram():
    assert is_anagram("listen", "silent") is True
    assert is_anagram("listen", "noise") is False


def test_find_missing_numbers():
    input = [1, 2, 4, 6, 3, 7, 8]
    expected = 5
    assert expected == find_missing_numbers(input)
    assert expected == find_missing_numbers_2(input)


def test_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.peek() == 2
    stack.pop()
    stack.pop()
    assert stack.pop() is None
    assert stack.peek() is None


def test_max_subarray_sum():
    input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert max_subarray_sum(input) == 6


def test_max_subarray_values():
    input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert max_subarray_values(input) == [4, -1, 2, 1]


def test_reverse_linked_list():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    reversed_head = reverse_linked_list(head)
    reversed_list = []
    while reversed_head:
        reversed_list.append(reversed_head.val)
        reversed_head = reversed_head.next


def test_longest_common_prefix():
    input = ["flower", "flow", "flight"]
    assert longest_common_prefix([]) == ""
    assert longest_common_prefix(input) == "fl"


def test_is_valid_parentheses():
    assert is_valid_parentheses("((()))") is True
    assert is_valid_parentheses("(((()))") is False
    assert is_valid_parentheses("([)]") is False
