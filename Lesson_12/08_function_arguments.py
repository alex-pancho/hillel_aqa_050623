# named arguments
# positional arguments
def func1(x):
    return x


def swimming_pool_volume(length, width, height=3):
    print(f'L:{length}, W:{width}, H:{height}')
    return length * height * width


print(swimming_pool_volume(5, 2, 1))
print(swimming_pool_volume(1, height=4, width=5))


# multiple values for argument restricted

# #################################
# def add_list(val, l1=[]):
#     l1.append(val)
#     return l1
#
#
# # def add_list(val, l1=None):
# #     l1  = [] if l1 is None else l1
# #     l1.append(val)
# #     return l1
#
#
# l1 = add_list(1)
# print(l1)
# l2 = add_list(2)
# print(l2)
#
#
# #
# #
# ##############################
#
# def max_value(a, b, *args):
#     print(a)
#     print(b)
#     print(args)
#     return max(a, b, *args)
#
#
# print(max_value(1, 4, 17, 3, 18))


def kwargs_example(a, *args, **kwargs):
    print(a)
    print(args)
    # print(lenght)
    print(kwargs)
    return {**kwargs, 'custom': True}


print(kwargs_example(5, 1, 2, 3, lenght=10, color='red', width=5))
# #print(kwargs_example(5, 1, 2, 3))

def some_example(*, a, **kwargs):
    print(a)

some_example(a=1)
# *
def func(a, *, b, c):
    print(a, b, c)
    # a - positional
    # b, c -named


func(1, c=2, b=3)

# **
