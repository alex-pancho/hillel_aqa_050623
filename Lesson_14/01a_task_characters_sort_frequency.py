# Input:
# "tree"
#
# Output:
# "eert" "eetr"
#
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. There fore "eetr" is also a valid answer.
# Example 2:
#
# Input:
# "cccaaa"
#
# Output:
# "cccaaa"
#
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:

s1 = 'aarteeee'
# "eert" "eetr"

s2 = sorted(s1, key=s1.count, reverse=True)  # str.sort
print(s2)
