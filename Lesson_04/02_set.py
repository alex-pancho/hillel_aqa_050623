# s0 = {1, 2, 3}
# print(s0)
# s1 = set('Hi')
# print(s1)
import string

list_with_duplicates = list(string.ascii_lowercase) * 2
print(list_with_duplicates)
s2 = set(list_with_duplicates)
print(s2)
print(len(s2))

# a = {'🍎', '🍏', '🍓', '🍐'}
# b = {'🍌', '🍓', '🍇', '🍎'}
# # 1. Union (`|` or `union()` method): Returns a set containing all elements from both sets.
# # 2. Intersection (`&` or `intersection()` method): Returns a set containing only elements that are in both sets.
# # 3. Difference (`-` or `difference()` method): Returns a set containing elements that are in the first set but not in the second set.
# # 4. Symmetric Difference (`^` or `symmetric_difference()` method): Returns a set containing elements that are in either of the sets, but not both.
# # 5. Subset (`<=` or `issubset()` method): Returns `True` if all elements of the first set are in the second set.
# # 6. Superset (`>=` or `issuperset()` method): Returns `True` if all elements of the second set are in the first set.
# # 7. Disjoint (`isdisjoint()` method): Returns `True` if there are no common elements between the two sets.
# print(f'{"a =":<15}: {a}')
# print(f'{"b =":<15}: {b}')
# print(f'{"Union":<15}: {a | b}')
# print(f'{"Intersection":<15}: {a & b}')
# print(f'{"Difference":<15}: {a - b}')
# print(f'{"Symm Difference":<15}: {a ^ b}')
# print('=' * 30)

# exclude duplications
fruit_set = {'🍎', '🍓', '🍐', '🍎', '🍎', '🍓'}
print(fruit_set)
fs_fruit_set = frozenset(fruit_set)
print(frozenset(fruit_set))
print(fruit_set.__sizeof__())
print(fs_fruit_set.__sizeof__())

fs = frozenset((1, 2, 3))
print(fs)
#
# ordered set ?
# remove duplicates from list
my_list = ['a', 'b', 'c', 'b', 'a', 'd', 'e', 'f']

no_dupl1 = list(set(my_list))
print(no_dupl1)
no_dupl2 = list(dict.fromkeys(my_list))
print(set(no_dupl2))
print(no_dupl2)
