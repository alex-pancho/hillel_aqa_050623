# hardcodes
filter_num = 5
num = 10
while num > filter_num:
    num -= 1
    print(num)

l1 = [1, 3, 4, 5, 8, 9, 0]
l2 = sorted(l1)[:4]
print(l2)




# strange naming
np = 108
npl = 17
result = np * npl

d1 = {'black': 'white', 'right': 'top'}




# do not invent simple things


l4 = [-1, 0, 1, -12]
from itertools import combinations

l_comb = list(combinations(l4, 3))
print(l_comb)
