# ===============================================================
# public
# full access
class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels


v1 = Vehicle(wheels=4)
print(v1.wheels)


# ===============================================================
# protected
# access in current class and child classes

class Vehicle2:
    def __init__(self, wheels):
        self._wheels = wheels


print('-' * 30)
v1 = Vehicle2(wheels=5)
v1._wheels = 7
print(v1._wheels)  # only warning


# ===============================================================
# private  ( setters/getters)
# access only form current class
class Secret3:
    def __init__(self, password):
        self.__password = password


class Vehicle3:
    def __init__(self, wheels):
        self.__wheels = wheels
        #self.__year = year

    def get_wheels_num(self):
        return self.__wheels

    def set_wheels_num(self, wheels):
        self.__wheels = wheels

    def __prn(self, smth):
        print(smth)


v1 = Vehicle3(wheels=5)
# print(v1.__wheels)
# print(v1.__prn('Smth'))
# print(v1._Vehicle3__prn('Smth'))


print(v1.get_wheels_num())
v1.set_wheels_num(wheels=6)
print(v1.get_wheels_num())


# incapsulation
# print(v1.__dict__)
# print(v1._Vehicle3__wheels)

# v1.__prn()
# v1._Vehicle3__prn('Text')

# # from accessify import protected, private


# setters and getters via @property
class Vehicle4:
    def __init__(self, wheels):
        self.__wheels = wheels

    @property  # doc
    def wheels(self):

        return self.__wheels

    @wheels.setter
    def wheels(self, wheels):
        # additional checks
        self.__wheels = wheels


print('=' * 10)
v4 = Vehicle4(wheels=10)
v4.wheels = 5  # setter
print(v4.wheels)  # getter
