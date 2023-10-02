# Given function that accepts positional arguments
# write decorator that will accept params strings_allowed=True/False, numbers_allowed=True/False
# and raise Assert Error in case unfulfilled condition

def deco_params(strings_allowed=True, numbers_allowed=True):
    def deco(func):
        def wrapper(*args, **kwargs):
            # params logic
            # todo [23-07-20] refactor later -> simplify
            assert_err_flag = False
            if not strings_allowed:  # False
                if any(type(el) == str for el in args):
                    assert_err_flag = True
            if not numbers_allowed:  # False
                if any(type(el) == int for el in args):
                    assert_err_flag = True
            if assert_err_flag:
                raise ValueError('Condition not passed')

            print(f'Deco args: {args=}')
            print(f'Deco params: {strings_allowed=} ; {numbers_allowed=}')
            result = func(*args)
            print('-' * 30)
            return result

        return wrapper

    return deco


@deco_params(strings_allowed=True, numbers_allowed=True)
def func(*args):
    print(f"Working OK with {args=}")


# func(1, 2, 3, 5)
# func('a', 'b', 'c')
# func(1, 2, 3, 5)
func(1, 2, 4, 's', 8, 0)
