# pull request
# check your solutions


# full syntax with condition
l1 = [1, 2, 3, 4]
# [statement  <for> current_element <in> object for iterations if <condition>   ]
lc = [str(itm) for itm in l1 if itm > 2]
print(lc)

# Task
# print all numbers in range 0-30 that has no digit 3 inside
numbers = [itm for itm in range(0, 31) if '3' not in str(itm)]
print(numbers)

# double for within comprehension

# code speed compare example


# zip
l1 = [1, 11, 111]
l2 = [2, 22, 222, 555,888]

l3 = list(zip(l1, l2))
print(l3)

# =============================================================
# string copy
s1 = '1234'
s2 = s1  # because immutable
print(s2)
print(type(s2))

# list copy
l1 = [1, 2, 3, 4]
from copy import copy

l2 = copy(l1)
l3 = l1[:]

# dict copy
d1 = {'1': 1, '2': 2, '3': 3}
d2 = {k: v for k, v in d1.items()}
d3 = {**d1}
print(d2)
print(d3)
