# strings creation str()

# print(str(b'\x89\x20\x31\x32\x33', encoding='utf-8', errors='ignore'))
# print(str(b'\x89\x20123', encoding='utf-8', errors='ignore'))
# #
# print(str(range(10)))
# print(str(1))

# print('\u00a9')
# print('\u1f98')
# print('Some line or info')
# name = 'Adam'
# print('<' + f'{name}' + '>')
# # print('==' * 10)


# methods
# print(*dir(str()), sep='\n')
# https://docs.python.org/3/library/stdtypes.html#str

# print(help('str.capitalize'))
# # print(help('str.center'))
#
# s1x2 = 1
# variable_name = 's1x2'
# print(variable_name.isidentifier())


import string


print(string.ascii_lowercase)
print(string.ascii_letters)
print(string.digits)
print(string.hexdigits)
print(string.punctuation)
print(string.capwords('hello world'))

str1 = '   Value    '
print(str1.lstrip())
print("What's wrong with ASCII?!?!?*".rstrip(string.punctuation))
#
#

# s1 = '123'
# print(*s1, sep='\n')
# print('#' * 20)
#
# string_iterator = iter(s1)  # s1.__iter__()
# print(next(string_iterator))
# print(next(string_iterator))
