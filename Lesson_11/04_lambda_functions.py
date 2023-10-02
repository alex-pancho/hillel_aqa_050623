l1 = [1, 2, 3, 4, 4, 5]

l2 = sorted(l1, key=lambda x: x < 3)

print(l2)

# function without name
fn = lambda a, b: a + b
print(fn(7, 8))

l2 = [0, 1, 2, lambda: 3, 4, 5]
print(l2[3])
print(l2[3]())

l3 = [1, 4, -9, 12, 18, 23]


def get_filter(l, filter_func=None):
    if filter is None:
        return l
    else:
        return [itm for itm in l if filter_func(itm)]


result = get_filter(l3, lambda x: x % 2 != 0)
print(result)
