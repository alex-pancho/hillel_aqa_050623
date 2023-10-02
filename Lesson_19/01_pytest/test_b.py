import pytest

t1 = (True, 1, 5*2 == 10, True)
some_val = 80


def test_b_001():
    assert all(t1), 'Not all elements are True'

@pytest.mark.skip('Reason')
def test_b_002():
    if some_val < 100:
        pytest.fail('Very small value')


def test_b_003():
    with pytest.raises(ZeroDivisionError):
        val = 1 / 0
        print(val)
        #raise ValueError()

    print('Exception was handled')
