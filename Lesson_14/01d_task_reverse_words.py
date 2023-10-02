# Given an input string, reverse the string word by word.
#
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".

s1 = "the sky is blue"
s2 = ' '.join(s1.split(' ')[::-1])

# l1 = s1.split(' ')
# l2 = l1[::-1]
# s2 = ' '.join(l2)

print(s2)
