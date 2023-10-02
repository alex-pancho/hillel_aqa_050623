# class Parent:
#     name = 'Parent'
#
#
# p = Parent()
# print(dir(p))
# print(p.__class__.__bases__)
#
#
# class Child(Parent):
#     ch_name = 'Child'
#
#
# ch = Child()
# print(ch.__class__.__bases__)

import random


class CustomList(list):
    def __str__(self):
        return ' -> '.join([str(itm) for itm in self])

    def shuffle(self):
        target_list = self.copy()
        random.shuffle(target_list)
        return target_list


l1 = [1, 2, 3, 4]
print(f'String: {l1}')

l2 = CustomList(l1)
l2.append(40)
print(l2)

print(l2.shuffle())
print(l2.shuffle())
print(l2.shuffle())

