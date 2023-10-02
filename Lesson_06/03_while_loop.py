# https://docs.python.org/3/reference/compound_stmts.html#while

counter = 0
#        True
while counter < 10:
    counter += 1
    if counter == 5:
        continue
        # break
        # print('Five')
    print(counter)
else:
    print('Done')

# iterate over numbers 11.0 11.3 11.6 ..   until 20.0

# https://docs.python.org/3/library/itertools.html#itertools.count
from itertools import count

i1 = iter(count(start=11, step=0.3))
# print(next(i1))
# print(next(i1))

# curr_val = next(i1)
while (curr_val := next(i1)) < 20:
    # print(curr_val)
    print(float(round(curr_val, 1)))
