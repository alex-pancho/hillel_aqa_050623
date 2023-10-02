# what is pep8
# https://peps.python.org/pep-0008/

# what is dosctring
"""
HomeTask 03 List Operations.

Description...
"""

# how to convert list to string '1234'
l1 = [1, 2, 3, 4]
result = ''.join((str(i) for i in l1))

# how to check if string with spaces palindrom ? 'argentina manit negra' (Reading left->right == right->left)
s1 = 'argentina manit negra'
s2 = s1.replace(' ', '')
bool(s2 == s2[::-1])
