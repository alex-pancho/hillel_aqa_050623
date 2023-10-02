# Given an integer array nums, return true if present integer that has no second duplicate

# Example 1:
# Input: nums = [1,2,2,1,3]
# Output: true

# Example 2:
# Input: nums = [1,2,3,1,2,3]
# Output: false

# count for each number
l1 = [1, 2, 3, 1, 2, 3]
# lc = [l1.count(itm) for itm in set(l1)]
result = any([l1.count(itm) % 2 for itm in set(l1)])
print(result)


# alternative solution
# | A | B | XOR Output |
# |---|---|------------|
# | 0 | 0 |     0      |
# | 0 | 1 |     1      |
# | 1 | 0 |     1      |
# | 1 | 1 |     0      |

l2 = [1, 2, 2, 1]
result2 = 0
for el in l2:
    result2 ^= el
print(bool(result2))

a = 17
b = 17
print(a ^ b)  # 0
