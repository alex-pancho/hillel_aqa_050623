# | Mutable Object | Description |
# | --- | --- |
# | `list` | An ordered collection of items that can be added, removed, or modified. |
# | `dict` | A collection of key-value pairs that can be added, removed, or modified. |
# | `set` | An unordered collection of unique items that can be added, removed, or modified. |
# | `bytearray` | A mutable sequence of bytes. |
# | `deque` | A double-ended queue that supports adding and removing elements from both ends efficiently. |
# | `User-defined classes` | Classes defined by the user that can have attributes modified. |
# | `array` | A module that provides an array object that can be used to store a collection of items of the same type. |


# | Object | Description |
# |--------|-------------|
# | int    | Integer values |
# | float  | Floating-point values |
# | bool   | True or False values |
# | complex | Complex numbers |
# | str    | String of characters |
# | bytes  | Sequence of bytes |
# | frozenset | Immutable version of set |
# | tuple | Ordered sequence of elements |
# | range | Sequence of integers |
# | bytes | Immutable version of byte arrays |
# | frozenset | Immutable version of set |
# | None | Represents absence of value |


import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='')
_log = logging.getLogger(__name__)


# var1 = 1
# var2 = 2
# list1 = [var1, var2]
# var1 += 5
#
# print(list1)
# print(var1)
# print(list1)
#
# el1 = [1]
# el2 = [2]
# list2 = [el1, el2]
# el1.append(5)
#
# _log.info(list1)
# _log.info(list2)


def some_func(val, obj=[]):
    obj.append(val)
    return obj


_log.info(some_func(2, [1]))
_log.info(some_func(3))
_log.info(some_func(4))

def some_func(val, obj=()):
   pass

# dict keys
correct_dict = {b'23': (1, 2, 3, 4), object: 23, str: 67, frozenset(('a', 'b')): {'a': 1, 'b': 2}, None: True}
_log.info(correct_dict)
incorrect_dict = {(1, 2, 3, 4): 12, [1, 2, 3, 4]: 23}
_log.info(incorrect_dict)
