# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
nums = [7, 7, 11, 11, 15]
target_sum = 14
# result = [0,1]
idx = -1
idx2 = -1

# sum - curr_el = value
# search for target  value inside list
for idx, el in enumerate(nums):
    value = target_sum - el
    if value in nums:
        idx2 = nums.index(value, idx + 1)
        break
print([idx, idx2])
