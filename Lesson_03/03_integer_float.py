import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='')
_log = logging.getLogger(__name__)

# int
# -----------------------------------------
int1 = 2342134213421341234213421342134123423142314234213412342134213421342134123423142134
int2 = int('2')
int3 = 10_000_000
#_log.info(f'{int1 + int2 + int3:_}')



# float
# -----------------------------------------
fl1 = 1.1
fl_exp = 0.0000000000000000000000005
_log.info(fl_exp)  # 5*(10**-25)
_log.info(f'{5 * (10 ** -25):.25f}')

fl1 = float(1.1)
fl2 = float(2.2)
_log.info(fl1 + fl2)

fl3 = float(1.0)
fl4 = float(7.0)
_log.info(fl3 / fl4)

# decimal
# -----------------------------------------
from decimal import getcontext, Decimal

getcontext().prec = 17
_log.info(Decimal(1) / Decimal(7))
getcontext().prec = 30
_log.info(Decimal(1) / Decimal(7))
