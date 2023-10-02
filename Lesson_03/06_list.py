# l0 = [1, 2, 34, 'tyerwe', tuple(range(10))]
# print(l0)
# l0[0] = 3
# print(l0[1])
# print(l0)
#
# # O(n)
#
# l1 = [1, 2, 3]
# pass
# # None
# my_var = l1.append(4)  # l1[len(l1):] = [4]
#
#
# size = 20
# my_list1 = [None] * size
# my_list2 = list(range(size))
# my_list3 = list('ABCDEFGHIJKLMNOP')
#
# from string import ascii_lowercase
#
# my_list4 = list(enumerate(ascii_lowercase, start=1))
#
# print(my_list1)
# print(my_list2)
# print(my_list3)
# print(my_list4)

#
# first, second, *rest, last = [1, 2, 3, 4, 5, 6, 7, 8]
# print(first)
# print(second)
# print(rest)
# print(last)
# print(type(rest))
def some_func(x):
    return x[1]
# #                01234
# print(some_func('banana'))

str_list = ["apple", "banana", "cherry", "dog", "shadow", "birthday", "coffee", "dolphin", "elephant", "fireplace",
            "guitar", "history", "internet", "jacket", "kangaroo", "lighthouse", "mountain", "napkin", "ocean", "piano"]

#str_list.sort()
#str_list.sort(key=some_func)
#str_list.sort(key=lambda x: x[1])
# str_list.sort(key=lambda x: len(x))
new_sorted_list = sorted(str_list, key=lambda x: x[1], reverse=False)
#print(str_list)
print(new_sorted_list)

three_column_list = [
    ("blue", "green", "yellow"),
    ("apple", "banana", "orange"),
    ("apple", "zigzag", "fall"),
    ("dog", "cat", "hamster"),
    ("apple", "winter", "fall"),
    ("book", "pen", "paper"),
    ("car", "bus", "bike"),
    ("sunny", "cloudy", "rainy"),
    ("happy", "sad", "angry"),
    ("mountain", "beach", "lake"),
    ("football", "basketball", "volleyball"),
    ("coffee", "tea", "milk"),
    ("lemon", "lime", "grapefruit"),
    ("jacket", "coat", "sweater"),
    ("movie", "music", "book"),
    ("work", "play", "rest"),
    ("pizza", "burger", "hotdog"),
    ("pencil", "eraser", "sharpener"),
    ("ocean", "river", "stream"),
    ("phone", "laptop", "tablet"),
    ("shirt", "pants", "shoes")
]

three_column_list.sort(key=lambda x: x[0][0] + x[1][0])
print(three_column_list)

from operator import itemgetter, attrgetter, methodcaller

three_column_list.sort(key=itemgetter(0, 1, 2))

print(three_column_list)

# flat list
import itertools

data = [[1, 2, 3], [4, 5, 6]]
print(list(itertools.chain.from_iterable(data)))


l1 = [[1, 2, 3], [4, 5], [6], [7, 8, 9, 0]]
print(sum(l1, []))
