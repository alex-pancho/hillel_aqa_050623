# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#    1
#   1 1
#  1 2 1
# 1 3 3 1
# 1 4 6 4 1

num_rows = 7

# single iteration
# #           0  1  2  3  4
# prev_row = [1, 3, 3, 1]
# print(len(prev_row) - 1)

# curr_row ...
# curr_row = [1, 4, 6, 4, 1]

pascal_triangle = []
prev_row = [1]
for row_idx in range(1, num_rows+1):
    # single iteration
    curr_row = []
    for i in range(len(prev_row) + 1):
        if i == 0 or i == len(prev_row):
            curr_row.append(1)
        else:
            curr_row.append(prev_row[i] + prev_row[i - 1])
    pascal_triangle.append(prev_row)
    prev_row = curr_row[:]

print(pascal_triangle)

for row in pascal_triangle:
    print(f'{" ".join([str(el) for el in row]):^{num_rows*4}}')

