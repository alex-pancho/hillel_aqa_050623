# # def deco(func):
# #     def wrapper(a, b):
# #         print('-' * 30)
# #         v = func(a, b) * 2
# #         print('_' * 30)
# #         return v
# #
# #     return wrapper
# #
# # @deco
# # def target_func(v1, v2):
# #     print('Creating tuple:')
# #     return (v1, v2)
# #
# # #
# # val = target_func(1, 2)
# # print(val)
# # #
# # ## internal_function = deco(target_func)
# # ## val2 = internal_function(1, 2)
# # ## print(val2)
# #
# #
# # #
# # # target_func = deco(target_func)
# # # val = target_func(4, 5)
# # # print(val)
# # # # args kwargs inside wrapper
#
# measure time
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.monotonic()
        v = func(*args, **kwargs)
        end = time.monotonic()
        print(f'Time:{end - start:.5f} sec')
        return v

    return wrapper

@measure_time
def create_list(range_num):
    return list(range(range_num))


create_list(80_000_000)


# decorators with parameters
def deco_print(func):
    def wrapper(x, *args, **kwargs):
        print('-' * 5)
        print(x, *args, **kwargs)
        print('-' * 5)
        return

    return wrapper


@deco_print
def _x(x):
    return x


_x('Hi')

from functools import wraps


def deco_params(ch, print_len):
    def deco_prn(func):
        @wraps(func)
        def wrapper(x, *args, **kwargs):
            print(ch * print_len)
            print(x, *args, **kwargs)
            print(ch * print_len)

        # wrapper.__name__ = '_x1'
        # wrapper.__doc__ = 'Some doc.'

        return wrapper

    return deco_prn


@deco_params(ch='*', print_len=30)
def _x1(x):
    """Some doc1."""
    return x


# _x1 = deco_params(ch='*', print_len=10)(_x1)
_x1('Hi!')
print(_x1.__name__)
print(_x1.__doc__)
# # wrapper.__name__ = func.__name__
# # wrapper.__doc__ = func.__doc__
#
# # from functools import wraps
# # wrapper should use decorator @wraps(func)
