# functions
# name is smth aka reference to function object
print
val = print
val()  # <- operator of function call
val('123')


# print = '123'
# print()
#
###################################   Purpose
# DRY  - Don't Repeat Yourself
#
#
# simple_func(5)
def simple_func(x):
    print(x)


simple_func(5)


#
#
# return
def func_with_return(x):
    result = x ** 2
    if result <= 100:
        return result
        # END OF FUNCTION EXECUTION  #######################
    return result * 2
    # return x


print(func_with_return(10))


def func_with_return2(x):
    result = False
    if x ** 2 <= 100:
        result = True
    return result


print('-' * 40)


# return as ternar
def get_max_two(a, b):
    return a if a >= b else b


x, y = 12, 5
print(get_max_two(x, y))


# # execution order
# x, y, z = 12, 5, 14
# print(get_max_two(x, get_max_two(y, z)))


def get_max_three(a, b, c):
    return get_max_two(a, get_max_two(b, c))


print(get_max_three(12, 5, 14))

print('=' * 40)


def even(x):
    return x % 3 == 0  # x%3  -> bool(2) -> True   bool(0) ->False


print([itm for itm in range(0, 21) if even(itm)])


# functions as objects inside other structures
def func1():
    print(1)


def func2():
    print(2)


def default():
    print('default')
    return  # return None

functions = {0: func1, 1: func2}

# def choice_func(choice=0):
#     return functions.get(choice, default)
#
#
# val = choice_func(0)  # <function func1>
# val2 = choice_func(1)  # <function default>


def choice_func2(choice=0):
    return functions.get(choice, default)()


choice_func2(0)
choice_func2(1)
choice_func2(100)
