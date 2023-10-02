# we have two lists with equal or different size
# ex. l1=[1,3,5,7]  l2=[1,4,5]
# task:
# create list that will store such values list_target = [(1,1), (3,4), (5,5), (7,0)]
# zero (0) is our default value that we set if no such element by index was found in certain list.
# code should work and vise versa
# ex. l1=[1,4,5] l2=[1,3,5,7] input data should produce list_target = [(1,1), (4,3), (5,5), (0,7)]

# l1 = [1, 4, 5]
# l2 = [1, 3, 5, 7]
l2 = [1, 4, 5]
l1 = [1, 3, 5, 7]

from itertools import zip_longest

l3 = list(zip_longest(l1, l2, fillvalue=0))
print(l3)
