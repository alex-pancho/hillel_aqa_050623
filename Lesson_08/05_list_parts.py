#      0       1       2         3       4
l1 = ["az", "toto", "picaro", "zone", "kiwi"]

# [("az", "toto picaro zone kiwi"), ("az toto", "picaro zone kiwi"), ("az toto picaro", "zone kiwi")...

# 1
i = 1
print(l1[i + 1:])
# 2
print(' '.join(l1[i + 1:]))
# 3
print(' '.join(l1[:i + 1]))

lc = [(' '.join(l1[:i + 1]), ' '.join(l1[i + 1:])) for i in range(len(l1)-1)]
# print(lc)
print(*lc, sep='\n')
