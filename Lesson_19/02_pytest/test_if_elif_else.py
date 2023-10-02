import pytest
from il_elif_else import min_from_four

data_set_min_1 = ((1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (0, 0, 0, 0))
data_set_min_2 = ((2, 1, 3, 4), (2, 1, 4, 3), (3, 1, 2, 4), (3, 1, 4, 2), (4, 1, 2, 3), (4, 1, 3, 2))
data_set_min_3 = ((2, 3, 1, 4), (2, 4, 1, 3), (3, 2, 1, 4), (3, 4, 1, 2), (4, 2, 1, 3), (4, 3, 1, 2))
data_set_min_4 = ((2, 3, 4, 1), (2, 4, 3, 1), (3, 2, 4, 1), (3, 4, 2, 1), (4, 2, 3, 1), (4, 3, 2, 1))


data = [
    ((2, 3, 4, 1), True),
    ((2, 4, 3, 1), True),
    ((3, 2, 4, 1), True),
    ((3, 4, 2, 1), True),
    ((4, 2, 3, 1), True),
    ((4, 3, 2, 1), True),
    ((0, 0, 0, 0), False),
]

def test_min_1():
    for itm in data_set_min_1:
        assert min_from_four(*itm) == 'w', f'Not passed value for {itm}'


def test_min_2():
    for itm in data_set_min_2:
        assert min_from_four(*itm) == 'x', f'Not passed value for {itm}'


def test_min_3():
    for itm in data_set_min_3:
        assert min_from_four(*itm) == 'y', f'Not passed value for {itm}'


def test_min_4():
    for itm in data_set_min_4:
        assert min_from_four(*itm) == 'z', f'Not passed value for {itm}'


@pytest.mark.parametrize("data_set, expected_result", data)
def test_min_4_parametrized(data_set, expected_result):
    result = min_from_four(*data_set) == 'z'
    assert result == expected_result

# from itertools import permutations
#
# four_combinations = list(permutations(range(1, 5), 4))
#
# data_min1 = sorted(four_combinations, key=lambda x: x[0])[:6]
# data_min2 = sorted(four_combinations, key=lambda x: x[1])[:6]
# data_min3 = sorted(four_combinations, key=lambda x: x[2])[:6]
# data_min4 = sorted(four_combinations, key=lambda x: x[3])[:6]
