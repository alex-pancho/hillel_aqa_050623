#
# Given an array containing n distinct numbers taken from
# 0, 1, 2, ..., n, find the one that is missing from the array.
#
# For example,
# Given nums = [0, 1, 3] return 2.

def check_num(target_list):
    # 0 1 2 3 4
    _l1 = sorted(target_list)
    for i in range(len(target_list)):
        if i == _l1[i]:
            continue
        else:
            return i
    else:
        return None
    # return None


l1 = [0, 1, 4, 3, 2, 8, 5]
print(check_num(l1))
