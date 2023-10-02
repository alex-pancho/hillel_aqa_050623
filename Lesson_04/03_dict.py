# d1 = {}
# # print(type(d1))
# # d2 = dict()
# # d3 = {(1, 2, 3): None, frozenset((1,)): 56, 'some_string': 45, 5.0: 2.8,
# #       True: False}
# #
# # # d3 = {[1, 2, 3]: None, frozenset((1,)): 56, 'some_string': 45, 5.0: 2.8,
# # #       True: False}
# # # print(d3)
# d4 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6:6}  # 2/3
# # #
# # # # O(1)
# # O (n)
# # #
# print(d1.__sizeof__())
# # # print(d2.__sizeof__())
# # # print(d3.__sizeof__())
# print(d4.__sizeof__())
# print(d4)
# del d4[1]
# del d4[2]
# print(d4)
# print(d4.__sizeof__())
# #
# # # dictionary changed size during iteration
# # d_new = {'a': 1, 'b': 2}
# # for itm in d_new:
# #     d_new.pop(itm)
#
# # dictionary changed size during iteration
# d_new = {'a': 1, 'b': 2}
# for itm in list(d_new.keys()):
#     d_new.pop(itm)
d_new = {'a': 1, 'b': 2}
for itm in d_new.values():
    print(type(itm))
    print(itm)

