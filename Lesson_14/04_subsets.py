# Given a set of distinct integers, S, return all possible subsets.
#
# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If S = [1,2,3], a solution is:
#
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

from itertools import combinations


def subsets(target_list):
    all_subsets = []
    for i in range(len(target_list) + 1):
        curr_result = [list(itm) for itm in combinations(target_list, i)]
        all_subsets.extend(curr_result)
    return all_subsets


l1 = [1, 2, 3]
result = subsets(l1)
print(result)

# ###########  alternative solution ####################
from itertools import combinations


def sublists(target_list):
    subsets = []
    for i in range(len(target_list) + 1):
        subsets.extend([list(itm) for itm in combinations(target_list, i)])
    return subsets


print(sublists([1, 2, 3]))
