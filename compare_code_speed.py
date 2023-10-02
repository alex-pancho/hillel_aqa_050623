import timeit

def func_a(l1):
    new_l = []
    for itm in l1:
        new_l.append(itm * 2)
    return new_l


def func_b(l1):
    return [itm * 2 for itm in l1]


init_list = list(range(1, 100, 2))
t_a = timeit.Timer(lambda: func_a(init_list))
t_b = timeit.Timer(lambda: func_b(init_list))

print(f'a: {t_a.timeit(10000):.6f}')
print(f'b: {t_b.timeit(10000):.6f}')
print(f'gain: {t_a.timeit(10000)/t_b.timeit(10000):.6f}')
