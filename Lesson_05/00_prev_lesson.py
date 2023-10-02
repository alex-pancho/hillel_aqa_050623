# Copy Paste?

# Certain Hometask - > only task related files
# How copy file from branch to main
# git checkout main
# git checkout <your branch> <target file>

# alternative solutions please attach as separate file. Please do not mix all in one file


# python debugger variable scope


# list copy
l1 = [1,2,3]
l2 = l1
l2 += [4]

l3 = l1[:] # real copy


# ==================================================
t1 = (1, 2, 3)
t2 = 4, 5, 6
t3 = (7,)
print(type(t2))
print(t1 + t2)

set1 = {1, 4, 5}
set2 = {5, 6, 7, 5}
print(set1 | set2)

a0, *a, a1 = 1, 2, 3, 4, 5
print(a)
print(type(a))

b = [1, 2, 3]
print((b,))
print((*b,))
#
custom_range = -1, 11
print(list(range(*custom_range)))
print([*range(*custom_range)])

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'d': 4, 'e': 5, 'f': 6}
# print(*d1)
# print(*d1.values())
print({**d1})
d3 = {**d1, **d2}

ch = 'w'
var1 = 18
if 1 <= var1 <= 100:
    pass
if 'a' <= ch <= 'd':
    print(ch)
else:
    print('Nothing')

# ===========
year = 2023
is_summer = True
country = 'Ukraine'
if all((year == 2023, is_summer, country.startswith('U'))):
    print('Target condition correct')

val = 100
if val > 200:
    print('>200')
elif val > 500:
    print('>500')
else:
    print('Other')
