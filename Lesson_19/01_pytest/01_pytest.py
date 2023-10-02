# https://docs.pytest.org
# https://pypi.org/project/pytest/
# pip install pytest
import pytest

print(pytest.__version__)
print(pytest.version_tuple)

import sys

if (3,8,0 ) > (3,7,2):
    print('OK')

if sys.version_info > (3, 7, 2):
    print('Expected python version')

# pytest -v  # detailed info
# pytest -s  # print to stdout
# pytest -m "not slow"
# pytest -m "slow"
# https://docs.pytest.org/en/stable/how-to/mark.html
# https://docs.pytest.org/en/6.2.x/usage.html


