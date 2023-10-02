t1 = (1, 2, 3, 4)


def test_a_001():
    print('Test start')
    assert 2 * 6 == 10, 'Something went wrong'


def test_a_002():
    print('*'* 40)
    print('Debug log')
    assert type(t1) == tuple

#
#
# try:
#     test_a_001()
#     test_a_002()
# except AssertionError:
#     print('Handled assertion')



