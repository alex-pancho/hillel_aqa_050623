#     0  1  2  3  4   5   6   7   8   9
l1 = [1, 2, 5, 8, 10, 17, 24, 25, 78, 101]
# print(id(l1))
#
# print(l1[0])
# print(l1[1])
# print(l1[1:4])
# ls1 = l1[1:12:2]
# print(ls1)
# print(id(ls1))
#
# s1 = 'Hello world!'
# print(s1[::-1])
# l2 = l1[:]
# print(id(l2))

# ls1 = l1[1:12:2][::-1]
print(id(l1))
print(l1)
del l1[1:3]
print(l1)

s1 = 'Some String with Greetings!'
s2 = 'Some Text with Spam!'
target_slice = slice(4, None)
print(s1[target_slice])
print(s2[target_slice])

# l2 = list.copy(l1)  # l2 = l1[:]
# print(f'{l2=}')
# del l2[:]
# print(f'{l2=}')
#
# l3 = l1[::-1]
# print(l3)


l2 = [[1, 2, 5, 8, 10, 17, 24, 25, 78, 101],
      [1, 2, 5, 200, 200, 200, 200, 25, 78, 101],
      [1, 2, 5, 200, 200, 200, 200, 25, 78, 101],
      [1, 2, 5, 8, 10, 17, 24, 25, 78, 101]]

import numpy as np

np_arr = np.array(l2)
np_sl = np_arr[1:3, 3:-3]
print(np_sl)
print(np_sl.tolist())
