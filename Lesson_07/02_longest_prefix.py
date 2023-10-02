# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string ""
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# understand how many characters


# for
# startwith

l1 = ['flower', 'flow', 'flight']


# lesson solution
iter_obj = min(l1, key=lambda x: len(x))
prefix = ''
for ch in iter_obj:
    prefix += ch
    if not all([el.startswith(prefix) for el in l1]):
        prefix = prefix[:-1]
        break
print(f'{prefix=}')

# alternative solution #2
iter_obj = min(l1, key=lambda x: len(x))
prefix2 = ''
for i in range(len(iter_obj) + 1):
    if all([el.startswith(iter_obj[:i]) for el in l1]):
        prefix2 = iter_obj[:i]
print(f'{prefix2=}')
