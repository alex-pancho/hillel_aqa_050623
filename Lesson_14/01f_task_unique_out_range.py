#
# Given an array containing values from some range and one value that has distance
# For example,
# Input: [0, 2, 11, 3, 1]
# Output: 11

# Input: [7, 0, 2, 4, 1, 3, 5]
# Output: 7

# 0 1 2 3   8
# 0 1 2    11
# 0 1      33

l1 = [7, 0, 2, 4, 1, 3, 5]
# l1 = [0, 2, 11, 3, 1]

result = sorted(l1)[-1]
print(result)
