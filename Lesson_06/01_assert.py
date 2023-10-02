# https://docs.python.org/3/reference/simple_stmts.html#assert

print(__name__)
print(__debug__)  # -O option

l_new = []
for itm in range(0, 9):
    l_new.append(2)

assert len(l_new) == 10, f'Current len={len(l_new)}'
assert sum(l_new) == 22, f'Incorrect sum={sum(l_new)}'


