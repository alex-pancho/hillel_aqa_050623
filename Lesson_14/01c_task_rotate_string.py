# We are given two strings, A and B.
#
# A shift on A consists of taking string A and moving the leftmost character to the rightmost position.
# For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True
# if and only if A can become B after some number of shifts on A.
#
# Example 1:
# Input: A = 'abcde'-> , B = 'cdeab'
# Output: true
#
# Example 2:
# Input: A = 'abcde', B = 'abced'
# Output: false
#
# Note:
# - A and B will have length at most 100.

from collections import deque


def string_comparison(target_str, compare_str):
    d1 = deque(target_str)
    for i in range(1, len(target_str) + 1):
        d1.rotate(i)
        print(''.join(d1))
        if ''.join(d1) == compare_str:
            return True
    return False


def string_comparison2(target_str, compare_str):
    try:
        idx = target_str.index(compare_str[0])
        s3 = target_str[idx:] + target_str[:idx]
        return True if s3 == compare_str else False
    except ValueError:
        return False


s1 = 'abcde'
# s2 = 'cdeab'
# s2 = 'abced'
s2 = 'ftyuo'
result = string_comparison2(s1, s2)
print(result)
