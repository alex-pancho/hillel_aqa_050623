name = 'Adam'
t1 = 'Hello, %s!' % name   # old style
# logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s')
t2 = 'Hello, {0:}!'.format(name)   # python 2-3
t3 = f'Hello, {name=}!'       # f-strings
print(t1)
print(t2)
print(t3)

TEMPLATE = "Happy new {} YEAR!"
year = 2024
print(TEMPLATE.format(year))


e1 = """Example1"""
e2 = "Example2"
e3 = "Example3 can't be simple\n000000"
print(e1)
print(e2)
print(e3)


t4 = 'c:\windows\temp'
print(t4)

t5 = R'c:\windows\temp'
print(t5)
print(repr(t4))
print(t5)

