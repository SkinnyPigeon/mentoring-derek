from typing import List, Any

# Challenge 1: Count Words in a Sentence
# Description: Write a function that takes a sentence as input and returns the count of words in the sentence.
# Example: Input: "I love coding in Python" Output: 5


def count_words(sentence: str) -> int:
    """Count the number of words in a sentence.

    Parameters:
        sentence (str): The sentence to count the words in.

    Returns:
        word_count(int): The number of words in the sentence."""
    words = sentence.split()
    return len(words)


# Challenge 2: Reverse a String
# Description: Write a function that takes a string as input and returns the string in reverse order.
# Example: Input: "Hello, World!" Output: "!dlroW ,olleH"


def reverse_string(s: str) -> str:
    """Reverse a string.

    Parameters:
        s (str): The string to reverse.

    Returns:
        reversed_string (str): The reversed string."""
    return s[::-1]


# Challenge 3: Check for Palindrome
# Description: Write a function that checks if a given string is a palindrome (reads the same forwards and backwards).
# Example: Input: "racecar" Output: True


def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome.

    Parameters:
        s (str): The string to check.

    Returns:
        is_palindrome (bool): True if the string is a palindrome, False otherwise."""
    return s == s[::-1]


# Challenge 4: Check for Anagrams
# Description: Write a function that checks if two strings are anagrams (contain the same characters in a different order).
# Example: Input: "listen", "silent" Output: True


def is_anagram(s1: str, s2: str) -> bool:
    """Check if two strings are anagrams.

    Parameters:
        s1 (str): The first string to check.
        s2 (str): The second string to check.

    Returns:
        is_anagram (bool): True if the strings are anagrams, False otherwise."""
    return sorted(s1) == sorted(s2)


# Challenge 5: Find the Missing Number
# Description: Given an array of integers from 1 to n, one number is missing. Write a function to find the missing number.
# Example: Input: [1, 2, 4, 6, 3, 7, 8] Output: 5


def find_missing_numbers(nums: List[int]) -> int:
    """Find the missing number in a list of integers.

    Parameters:
        nums (List[int]): The list of integers to check.

    Returns:
        missing_number (int): The missing number in the list."""
    sorted_nums = sorted(nums)
    for i in range(len(sorted_nums[:-1])):
        if sorted_nums[i] + 1 != sorted_nums[i + 1]:
            return sorted_nums[i] + 1


def find_missing_numbers_2(nums: List[int]) -> int:
    """Find the missing number in a list of integers.

    Parameters:
        nums (List[int]): The list of integers to check.

    Returns:
        missing_number (int): The missing number in the list."""
    n = len(nums) + 1
    total_sum = (n * (n + 1)) // 2
    actual_sum = sum(nums)
    return total_sum - actual_sum


# Challenge 6: Implement a Stack
# Description: Implement a stack data structure with push, pop, is_full, is_empty, and peek.
# Example: Input: push(1), push(2), push(3), pop() Output: 2


class Stack:
    """A stack data structure.

    Attributes:
        stack (List): The stack."""

    def __init__(self, size: int = 10):
        self.stack = []
        self.size = size

    def push(self, item):
        """Push an item onto the stack.

        Parameters:
            item (Any): The item to push onto the stack."""
        if not self.is_full():
            self.stack.append(item)

    def pop(self) -> Any:
        """Pop an item off the stack.

        Returns:
            item (Any): The item popped off the stack."""
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self) -> Any:
        """Peek at the top item on the stack.

        Returns:
            item (Any): The item at the top of the stack."""
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self) -> bool:
        """Check if the stack is empty.

        Returns:
            is_empty (bool): True if the stack is empty, False otherwise."""
        return len(self.stack) == 0

    def is_full(self) -> bool:
        """Check if the stack is full.

        Returns:
            is_full (bool): True if the stack is full, False otherwise."""
        return len(self.stack) == self.size


# Challenge 7: Find the Maximum Subarray Sum
# Description: Given an array of integers, find the contiguous subarray with the largest sum and return the sum.
# Example: Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4] Output: 6


def max_subarray_sum(nums: List[int]) -> int:
    """Find the maximum subarray sum.

    Parameters:
        nums (List[int]): The list of integers to check.

    Returns:
        max_sum (int): The maximum subarray sum."""
    max_sum = float("-inf")
    current_sum = 0
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum


# Challenge 7.1: Find the values that make up the Maximum Subarray Sum
# Description: Given an array of integers, find the contiguous subarray with the largest sum and return the sum.
# Example: Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4] Output: [4, -1, 2, 1]


def max_subarray_values(nums: List[int]) -> List[int]:
    """Find the values that make up the maximum subarray sum.

    Parameters:
        nums (List[int]): The list of integers to check.

    Returns:
        max_sum (List[int]): The values that make up the maximum subarray sum."""
    max_sum = float("-inf")
    current_sum = 0
    start = 0
    end = 0
    for i, num in enumerate(nums):
        if current_sum <= 0:
            start = i
            current_sum = num
        else:
            current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
            end = i

    return nums[start : end + 1]


# Challenge 8: Reverse a Linked List
# Description: Given a singly linked list, reverse the order of the nodes.
# Example: Input: 1 -> 2 -> 3 -> 4 -> 5 Output: 5 -> 4 -> 3 -> 2 -> 1


class ListNode:
    """A node in a linked list.

    Attributes:
        val (int): The value of the node.
        next (ListNode): The next node in the linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head):
    """Reverse a linked list.

    Parameters:
        head (ListNode): The head of the linked list.

    Returns:
        prev (ListNode): The head of the reversed linked list."""
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


# Challenge 9: Find the Longest Common Prefix
# Description: Write a function that finds the longest common prefix among an array of strings.
# Example: Input: ["flower", "flow", "flight"] Output: "fl"


def longest_common_prefix(strs: List[str]) -> str:
    """Find the longest common prefix among an array of strings.

    Parameters:
        strs (List[str]): The list of strings to check.

    Returns:
        prefix (str): The longest common prefix among the strings."""
    if not strs:
        return ""
    min_length = min(len(s) for s in strs)
    prefix = ""
    for i in range(min_length):
        char = strs[0][i]
        if all(s[i] == char for s in strs):
            prefix += char
        else:
            break
    return prefix


# Challenge 10: Validate Parentheses
# Description: Write a function that checks if a given string of parentheses is valid (open and close parentheses are balanced).
# Example: Input: "((()))" Output: True


def is_valid_parentheses(s: str) -> bool:
    """Check if a string of parentheses is valid.

    Parameters:
        s (str): The string of parentheses to check.

    Returns:
        is_valid (bool): True if the string of parentheses is valid, False otherwise."""
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    return len(stack) == 0
