# def recursive(val):
#     print(val)
#     recursive(val + 1)
#
#
# recursive(1) # RecursionError: maximum recursion depth exceeded while calling a Python object

# # maximum recursion depth
# # functions stack . Order of function calls. Stackoverflow

def recursive(val):
    print(val)  # 1
    if val < 3:
        recursive(val + 1)  #
    print(val)

    # def recursive(val):  # second
    #     print(val)  # 1
    #     if val < 3:
    #         recursive(val + 1)  #
    #     print(val)
    #
    #     def recursive(val):   # third
    #         print(val)  # 1
    #         if val < 3:
    #             recursive(val + 1)  #
    #         print(val)


recursive(1)

#
#
# # call 1 -> call 2 -> call 3 ( val =3) -> return back  Call3 -> call2 -> call1
#
# ##################################################### factorial
# n! = 1*2*3*4     n! = (n-1)!*n

n = 2  # -> 1*2    4! -> 3! * 4  n! = (n-1)!*n


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


num = 4
result = factorial(num)
print(f"The factorial of {num} is {result}")
