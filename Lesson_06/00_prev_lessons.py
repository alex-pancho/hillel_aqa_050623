# flake8 inside Pycharm
# https://habr.com/ru/companies/dataart/articles/318776/

l1 = [1, 2, 3, 4]
print(l1[::-1])

# https://docs.python.org/3/library/itertools.html
# dict slices
d1 = {'1': 1, '2': 2, '3': 3, '4': 4}
from itertools import islice

print(dict(islice(d1.items(), 1, 3)))

# set slices
s1 = {1, 2, 3, 4, 5, 6, 7}
print(set(islice(s1, None, None, 2)))

from collections import OrderedDict

od1 = OrderedDict({'1': 1, '2': 2, '3': 3, '4': 4})
print(od1)
print(type(od1))
print({**od1, **{'5': 5, '6': 6}})
od2 = OrderedDict({**od1, **{'5': 5, '6': 6}})
print(od2)
od2.move_to_end('1', last=True)
print(od2)
od2.move_to_end('3', last=False)
print(od2)
print(dict(od2))
