# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
# task from target list of int create list of doubled values
l1 = [2, 4, 6, 8, 10]
new_l = []
for itm in l1:
    new_l.append(itm * 2)
print(new_l)

# simple comprehension list
#    [statement  <for> current_element <in> object for iterations ]
lc = [itm * 2 for itm in l1]
lc2 = [itm for itm in l1]
print(lc2)
print(id(l1))
print(id(lc))
print(lc)
#
# # syntax
# # temporary variables inside list comprehensions
s1 = 'abcceeedffff'
lc2 = [s1.count(ch) for ch in s1]
print(lc2)

from itertools import groupby

# ( 'A', '<iter_object>')
lc2_grouped = [s1.count(key) for key, _ in groupby(s1)]
print(lc2_grouped)

# conditions, ternar if inside
#    [statement                            <for> current_element <in> object for iterations ]
print(list(range(10)))
lc3 = ['even' if x % 2 == 0 else 'odd' for x in range(0, 10)]
print(lc3)

# 1.1  1.2  1.3  1.4 .. 2.0
lc1 = [itm / 10 for itm in range(11, 21)]
print(lc1)

# https://docs.python.org/3/library/itertools.html#itertools.groupby
from itertools import groupby

lc2 = [list(group) for _, group in groupby('AAAABBBCCDEEFFFFFFF')]
print(*lc2, sep='\n')


#  RARE!!
# double for
phrase = 'Some phrase'
# phrase = [[1, 2, 3], [4, 5, 6]]
l1 = [character for word in phrase for character in word]
print(l1)

list_of_lists = [[1, 2, 3], [4, 5, 6]]
flat_list = [number for internal_list in list_of_lists for number in internal_list]
print(flat_list)
