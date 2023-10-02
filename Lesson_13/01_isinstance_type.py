a = 3

print(isinstance(a, int))

b = True
print(isinstance(b, bool))
print(isinstance(b, int))    # INT -> bool

print(type(b) == bool)
print(type(b) == int)   # strict verification

c = None
print(type(b) is None)

# filter

data = (4.7, 8.1, 'Book', True, 8, 11, -1, ['EL1', None])
s = 0
for x in data:
    if isinstance(x, (float, int)):
        s += x
print(s)

s = sum((itm for itm in data if isinstance(itm, (float, int))))
s1 = sum(filter(lambda x: isinstance(x, (float, int)), data))
print(s1)

s2 = sum((itm for itm in data if type(itm) in (float, int)))
print(s2)
