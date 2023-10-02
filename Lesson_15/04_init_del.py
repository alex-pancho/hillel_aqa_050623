class Vehicle:
    wheels = 4
    year = 2023


v1 = Vehicle()
v1.wheels = 2
v1.year = 2021


###### init
class VehicleInit:
    def __init__(self, wheels=4, year=2023, eng_vol=2):
        print('WE are in INIT')
        self.wheels = wheels
        self.year = year
        self.eng_vol = eng_vol


v3 = VehicleInit(wheels=2, year=2021)
# print(VehicleInit.wheels)
print(v3.wheels)
v4 = VehicleInit()
print(v4.wheels)


# __del__

class VehicleDel:
    def __del__(self):
        print("We are in del")

vd1 = VehicleDel()
print('created')

vd1 = None

print('After reassign')
#
#
