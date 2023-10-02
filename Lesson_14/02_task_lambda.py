# Given: list of integers/floats with lambda function as one of the element inside list
# Write function that will produce new list by applying lambda to all integers and floats
# Input: [lambda a: a + 2, 9, 3, 1, 0]
# Output: [11, 5, 3, 2]

# Input: [9, 2, 3, lambda a: a / 2.0, 1, 0]
# Output: [4.5, 1, 1.5, 0.5, 0.0]

def no_name(a):
    return a + 2


no_name(11)


def lambda_func(target_list):
    _l1 = [itm for itm in target_list if type(itm) not in (int, float)]
    if len(_l1) == 1:
        return [_l1[0](el) for el in target_list if type(el) in (int, float)]
    else:
        raise ValueError('Only one lambda function expected')


l1 = [lambda a: a + 2, 9, 3, 1, 0]
# l1 = [9, 2, 3, lambda a: a / 2.0, 1, 0]
result = lambda_func(l1)
print(result)

###########  alternative solution ####################

from types import LambdaType


def find_lambda(target_list):
    _lambda_items = [itm for itm in target_list if type(itm) == LambdaType]
    if len(_lambda_items) == 1:
        return [_lambda_items[0](num) for num in target_list if type(num) in (int, float)]
    else:
        raise ValueError('Should be only one lambda element inside')


print(find_lambda([lambda a: a + 2, 9, 3, 1, 0]))
print(find_lambda([9, 2, 3, lambda a: a / 2.0, 1, 0]))
