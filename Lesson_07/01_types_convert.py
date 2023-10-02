s1 = '123'
# str -int
s1.isdecimal()
int(s1)

# str - list
list(s1)
lc = [itm for itm in s1]
# TypeError: 'int' object is not iterable


# str - set
set(s1)
# set comprehension

# str - dict
dc = {k: None for k in s1}
dict.fromkeys(s1)

# list -> str
# 1 list of strings
l1 = [1, 2, 3, 4]
[str(i) for i in l1]

# join all elements
''.join([str(i) for i in l1])

# list -> set
set(l1)

# list -> dict
d5 = {(1, 2, 3): 1, None: True, (1, 2): '12'}
print(d5)

l2 = [4, 6, 7, 8]
dict.fromkeys(l2)
dc2 = {k: None for k in l2}

# dict - str  'a1b2c3'  'abc123'
from itertools import chain

l_tmp = [('a', 1), ('b', 2), ('c', 3)]
''.join([str(el) for el in list(chain(*l_tmp))])

d1 = {'a': 1, 'b': 2, 'c': 3}
result = ''
for key, val in d1.items():
    result += str(key)
    result += str(val)


target_string = ''.join([f'{key}{val}' for key, val in d1.items()])
print(target_string)

# dict - list
list(d1.keys())
list(d1.values())
list(d1.items())


# dict - set
set(d1.keys())
set(d1.values())
set(d1.items())
