v1 = object
# # return an alphabetized list of names comprising (some of) the attributes
# # of the given object, and of attributes reachable from it
# print(help(dir))
# print(*dir(v1), sep='\n')
# print(repr(v1))
# print(v1)
# # -----------------------------------------------------------
# all types are childs of python object
# s1 = 'Some Text'
# print(*dir(s1), sep='\n')
# print(help(str))
# print(s1.__class__.__bases__)
#
# multiple variables in one line
# x = 1
# x, y, z = 's1', 's2', 's3'
#
# print(x,y,z)
#
# a = 5
# b = 10
# a, b = b, a
# print(a, b)
#
# immutable type
var1 = 'Sample Text'
print(id(var1))
var2 = 'Another Text'
list1 = [var1, var2]
var1 += '!!!'
el = '!!!'
var1 = f'{el} {var1} {el}'
var1 = '{0} {1} {0} {0}'.format(el, var1)
print(id(var1))
print(var1)
print(list1)
#
# # from hometask multiline string definition < 79
# var1 = 12
# str2 = (f'{var1}-------------------------------------------------------------------------'
#         f'{var1}adfdfsssssssssssssssssssssssssssssssssssssssssssf')
# print(str2)
