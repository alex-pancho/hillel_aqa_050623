################  ITERATORS ############################

# https://docs.python.org/3/glossary.html
# iterator - An object representing a stream of data.
# iterable - An object capable of returning its members one at a time


s1 = '12345'
# it1 = s1.__iter__()
it1 = iter(s1)
print(next(it1))
print(next(it1))
print(next(it1))
for ch in it1:
    print(ch)
#
for ch in it1:
    print(ch)

# for ch in s1:
#     print(ch)
#
# for ch in s1:
#     print(ch)


# while True:
#     pass
#    break


print('-' * 30)
# infinite values
it2 = iter(int, 1)
# print(int())
print(next(it2))
print(next(it2))
print(next(it2))

print('-' * 30)
from itertools import count

it3 = count(start=1, step=1)
while val := next(it3):
    if val > 5:
        break
    print(val)

# ################  GENERATORS ############################
print('=' * 20)
my_generator = (x for x in range(3))
my_dict = {my_generator: 'literal generator'}
print(my_dict)
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))
print(f'Next: {next(my_generator)}')  # -> 0
for i in my_generator:
    print(i)
print('=' * 20)
# print(next(my_generator))
for i in my_generator:
    print(i)
print('End of second attempt')


def num_generator():
    for i in range(3):
        yield i


for i in num_generator():
    print(f'#1:{i}')

for i in num_generator():
    print(f'#2:{i}')

my_dict = {num_generator: 'generator function'}
print(my_dict)


############

def generator_with_return():
    for i in range(3):
        yield i
    return 'Important Message'   # StopIteration Message

g4 = generator_with_return()
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))
