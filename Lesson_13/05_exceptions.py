a = [1, 2, 3]
try:
    print("Second element = %d" % (a[1]))

    # Throws error since there are only 3 elements in array
    #print("Fourth element = %d" % (a[3]))
    raise ZeroDivisionError()
except (IndexError, ValueError) as custom_err:
    print("Index error")
except Exception as g_exc:
    print("Global error occurred:")
    print(g_exc)



# print("Fourth element = %d" % (a[3]))

print(a)


# several exceptions

def fun(a):
    if a < 4:
        # throws ZeroDivisionError for a = 3
        b = a / (a - 3)

    # throws NameError if a >= 4
    print("Value of b = ", b)


try:
    # fun(3)
    fun(5)

# note that braces () are necessary here for
# multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")



# else statement
def AbyB(a, b):
    try:
        c = ((a + b) / (a - b))
    except ZeroDivisionError:
        print("a/b result in 0")
    # else:
    #     print(c)
    finally:
        print(a)
        print(b)


# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

# finally
# Program to depict Raising Exception



from colorama import init, Fore

init(autoreset=True)


def exception_hook(exc_type, exc_value, tb):
    local_vars = {}
    while tb:
        filename = tb.tb_frame.f_code.co_filename
        name = tb.tb_frame.f_code.co_name
        line_no = tb.tb_lineno
        print(f"{Fore.RED}File {filename} line {line_no}, in {name}")
        local_vars = tb.tb_frame.f_locals
        tb = tb.tb_next
    print(f"{Fore.GREEN}Local variables in top frame: {local_vars}")

import sys
sys.excepthook = exception_hook


try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print("An exception")
    raise # To determine whether the exception was raised or not
# raise ValueError('hi!')
