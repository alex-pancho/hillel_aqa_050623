import time
import pytest


@pytest.mark.any_other_name
@pytest.mark.slow
def test_c_001():
    print('Just waiting...')
    time.sleep(1)
