import logging

_log = logging.getLogger('Main')
log_formatter = logging.Formatter('%(asctime)s [%(levelname)s]  %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)
_log.addHandler(console_handler)
_log.setLevel(logging.DEBUG)

from conftest_plugin import Cfg
from code.recursion import complex_list_sum

MAX_TIMEOUT = Cfg.params.get('max_timeout')


class TestRestApi:
    def test_001(self):
        assert True

    def test_002(self):
        assert MAX_TIMEOUT >= 100, 'Incorrect max timeout'
        assert True

    def test_003(self):
        l1 = [[[[1, 4, 5], [[6, 9], [[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]
        assert complex_list_sum(l1) == 72, 'Incorrect sum'
