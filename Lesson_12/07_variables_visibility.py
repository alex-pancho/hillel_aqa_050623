# def my_func():
#     x = 1
#     print(x)
#
#
# x = 10
# # print(x)
# # my_func()
# # print(x)
#
#
# #CONST = 15
# # def my_func2(x):
# #     CONST = 5
# #     print(CONST)
# #
# #
# # my_func2(10)
# # print(CONST)
#
#
# CONST = 15
# #CONST = 7
# def my_func3():
#     global CONST
#     CONST = 7
#     print(CONST)
#
#
# my_func3(10)
# print(CONST)


x = 0

def outer():
    # global x
    # nonlocal x
    x = 1

    def inner():
        # global x
        nonlocal x
        x = 2
        print(f'Inner: {x}')

    inner()
    print(f'Outer: {x}')


outer()
print(f'Global: {x}')

# nonlocal
# nonlocal in outer
