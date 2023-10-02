# yield from

def gen1(num):
    for i in range(num):
        yield i

g1 = gen1(6)
for el in g1:
    print(el)


def gen2(num):
    yield from range(num)

    # equal
    # for i in range(num):
    #     yield i

print('-' * 30)
g2 = gen2(6)
for el in g2:
    print(el)


