from pathlib import Path

a_list = [3, 1, 2]
b_list = [4, 5, 6 ]#[7, 8]

a_list.extend(b_list)
#a_list.append(b_list)
print(a_list)
#a_list.sort()
a = sorted(a_list)
print(a)
b = a.pop(0)
print(b)
print(a)

some_dict = {"a": "b"}
some_dict["b"] = "c"
some_dict.update({"d":"f"})
print(some_dict)
x = some_dict.pop("a")
print(x)
del some_dict["b"]
for k, v in some_dict.items():
    print(k, v)

c_list = [2, 3, 4, 2, 3, 5, 1, 6, 2, 3, 4, 4, 2, 33, 4, 2, ]
set_c = set(c_list)
print(set_c)
unic_c = list(set_c)
set_d = {4, 5, 6, 9, 10}
print(unic_c)
print("1" in "123")
print(set_d ^ set_c)

tuple1 = (1, 2, 3)
tuple2 = ("apple", "banana", "cherry")
tuple3 = tuple1 + tuple2
print(tuple3)


filename = Path("text.txt")

with open(filename, 'w') as f:
    f.write("ta ta ta")
print("end record")


class ItsGirl():

    def __str__(self) -> str:
        return "its Anna"

    def __int__(self) -> int:
        return 2


abc = ItsGirl()
print(bool(abc))
