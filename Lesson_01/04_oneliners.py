# -c option
# python -c "import secrets; print(secrets.token_hex(8))"
# python -c "import json; d1={'name': 'Tom', 'age': 25, 'city': 'New York'};print(json.dumps(d1, indent=4, sort_keys=True))


# -m option
# python -m http.server 8000  # http server
# python -m calendar 2001     # certain year calendar
# python -m timeit -s "a='text'; f'{a}'"  # timimg profiler
# python -m dis <python_file> # bytecode dissasembler
# python -OO -m py_compile <python_file> # pyc file creation 2 stage of optimization
# python -m zipapp zip_app -c  # creation of zip files containing Python code (pyz)

import calendar
import http.server