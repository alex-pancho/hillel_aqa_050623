# Given an integer num, repeatedly add all its digits until
# the result has only one digit, and return it.
# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2
# Since 2 has only one digit, return it.

num = 9999
# num -> list of integers
l1 = [int(el) for el in str(num)]
print(l1)

# sum
print(sum(l1))

# while
result = num
while result > 9:
    result = sum([int(el) for el in str(result)])

print(result)
