
# get list of available built-in functions
# -----------------------------------------
import builtins

print(dir(builtins))

# get list of available modules
# -----------------------------------------
help('modules')
#
# list keywords
# -----------------------------------------
from keyword import kwlist
print('\n'.join(kwlist))
