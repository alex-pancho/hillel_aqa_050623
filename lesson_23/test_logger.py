import pytest
from logger import logger

def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        1/0
    logger.info("devide error is ok")

def test_sum():
    a = 1
    b = 2
    logger.debug(f"a={a}, b={b}")
    logger.error("Wrong count")
    assert a + b == 2, "Wrong count"