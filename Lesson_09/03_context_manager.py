# https://peps.python.org/pep-0343/

# fh = open('some_file_new.txt')
# fh.write('Hello')
# fh.close()
#
with open('../../Lesson_09/some_cm.txt', 'w') as fh:
    fh.write('Hello')
# --------->  fh.close()
# print()


# __enter__ ()  runs when object created

# __exit__() runs when we exit or when exception raised

# VAR = EXPR
# VAR.__enter__()
# try:
#     BLOCK
# finally:
#     VAR.__exit__()

class CM:
    def __init__(self, x):
        self.x = x

    def __enter__(self):
        print('Enter Context Manager')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exit Context manager')
        if exc_type is None:
            print(f'No errors and we print our value= {self.x * 2}')
        else:
            print('There were some errors')


with CM(2) as my_cm:
    print('In the middle')
    #val = 1/0


