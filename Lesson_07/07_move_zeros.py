# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
l1 = [0, 1, 0, -3, 12]

# lc = [str(itm) for itm in l1 if itm > 2]

l2 = [itm for itm in l1 if itm != 0]
num_zeros = l1.count(0)
print(num_zeros)
# l2.extend([0]*num_zeros)
l3 = l2 + [0]*num_zeros
print(l3)
