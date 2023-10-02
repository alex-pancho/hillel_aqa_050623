num = 5
#    1  2
# 1  1  2
# 2  2  4

# caption
caption = [str(el) for el in range(1, num + 1)]
print(' '.join(caption))
print('-' * 10)

# O(n^2)
multiplication_table = []
for i in range(1, num + 1):
    curr_row_el = []
    for j in range(1, num + 1):
        curr_row_el.append(i * j)
        # print(f'{val:^4} ', end='')
    multiplication_table.append(curr_row_el)

# print(multiplication_table)

# alternative solution
for i in range(1, num + 1):
    print(" ".join('{:3}'.format(x) for x in range(i, i * num + 1, i)))
