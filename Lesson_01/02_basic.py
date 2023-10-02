# PEP Python Enhancement Proposal
# https://peps.python.org/pep-0000/
# https://peps.python.org/pep-0008/
# https://peps.python.org/pep-0020/

import this

import sys

print('Error', 'Value', sep=' * ', end='\n\n', file=sys.stderr)

x = None
y = None

print(x.__sizeof__())

print(x is y)
print(id(x))
print(id(y))

s1 = 'some text'    # memory object + value  obj1
s2 = s1             # s2 -> s1 -> obj1
print(s2)
print(id(s1))
print(id(s2))
print(s1 is s2)  # the same memory object
del s1  # variable name removing  # s2 -> obj1

s3 = s2
print(s3)
print(id(s3))

del s2
del s3      # obj1  will be deleted from memory by garbage collector

# # values
# # variables
# # memory object
