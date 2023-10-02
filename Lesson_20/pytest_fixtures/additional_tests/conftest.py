import pytest
import time


@pytest.fixture(scope='function', autouse=True)
def some_code_2():
    # setup
    print('Sleeping 2 sec...')
    time.sleep(2)
    yield 'SomeString'

    # teardown
    print('Teardown...')
