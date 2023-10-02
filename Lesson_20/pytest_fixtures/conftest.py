import pytest
import time


@pytest.fixture(scope='function', autouse=True)
def some_code():
    # setup
    print('Sleeping 1 sec...')
    time.sleep(1)
    yield 'SomeString'

    # teardown
    print('Teardown...')
