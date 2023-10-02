# Given an integer x, return true if x is a palindrome , and false otherwise.
# Input: x = 121
# Output: true

x = 121  #
# true

# x = 1234
## false

z = str(x)[::-1]
assert str(x) == z, 'Not palindrome'
print('Palindrome')

# ternar if solution
val = True if str(x) == str(x)[::-1] else False
print(val)
