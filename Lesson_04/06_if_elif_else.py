# # https://docs.python.org/3/reference/compound_stmts.html#if

x1 = -101
if x1 < 0:
    x1 = -x1
    if x1 == 100:
        print('Bingo!')
print(x1)

# double comparison
x2 = 15
if 10 > x2 > 2:  # x2<10 and x2>2
    print('X between 2 and 10')

# and or not
x3 = 12
if x3 % 3 == 0 and x3 % 4 == 0 and 60 // x3 == 5:
    print('All fine')

if (x3 % 3 == 1) or ((x3 % 4 == 0) and (60 // x3 == 5)):
    print('All fine, but...')
#
# in operator  ( related to iterators)
if ('a' in 'Map'):
    print('a found')
# if 5 in 4435345345:
#     print('5 found')

# boolean types
empty_tuple = ()
print(type(empty_tuple))
empty_dict = {}
print(type(empty_dict))
print(f'Empty tuple = {bool(())}')
print(f'Empty string = {bool("")}')
print(f'Empty list = {bool([])}')
print(f'Empty set = {bool(set())}')
print(f'Empty dict = {bool({})}')

d1 = {'a':1}
print(bool(d1))
if d1:
    print('Not empty')

l1 = [100, 200]
l1.pop()
if l1:
    print('Not empty')

val1 = None # is None
print(None == False)
print(bool(None) == False)
print(bool(val1))
if not val1: # not False == True
    print('We should do smth with this')

# max for three numbers
x, y, z = 100, 200, 350
if x > y:
    if x > z:
        print('X')
    else:
        print('Z')
else:
    if y > z:
        print('Y')
    else:
        print('Z')

# ternar if
a = 5
b = 11
#print('Yes') if (a < b) and (b % 10 == 0) else print('No')
print(f'b is {("round" if (b % 10 == 0) else "not round")} number')
#
# ternar max from three numbers but not the best practice
x, y, z = 100, 200, 350
max_num = (x if x > z else z) if x > y else (y if y > z else z)
print(max_num)

# value   -> if statement - > else - > value2