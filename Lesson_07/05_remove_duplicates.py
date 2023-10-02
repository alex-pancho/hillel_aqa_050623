# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.
# Then return the number of unique elements in nums.
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

# 1 set
# 2 len(set)
# 3 len(l1) - len(set)   -> * '-'

l1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
s1 = set(l1)
print(s1)
print(len(s1))
l_with_underscores = ['_'] * (len(l1) - len(s1))
l2 = list(s1) + l_with_underscores
print(l2)
