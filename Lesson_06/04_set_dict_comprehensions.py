# simple set comprehension
s1 = {1, 2, 3, 4}
sc = {itm for itm in s1}
print(sc)

s2 = [1, 2, 3, 4, 2, 3, 1]
sc2 = {itm for itm in s2}
print(sc2)

# simple dict comprehension
d1 = {'1': 1, '2': 2, '3': 3}
dc = {f'{key}-1': value*2 for key, value in d1.items()}
print(dc)
