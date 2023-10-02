# common usage
class Vehicle:

    def beep(self):
        if not hasattr(self, 'beep_count'):
            self.beep_count = 0
        self.beep_count += 1
        print(self.beep_count)


v1 = Vehicle()
v1.beep()  # Vehicle.beep(v1)
Vehicle.beep(v1)


# classmethod
class Vehicle2:
    MIN_TEMP = -20
    MAX_TEMP = 50

    def engine_start(self, temparature):
        print(f'Attempt to start engine with {temparature=}')
        if self.validate_temperature(temparature):
            print('Engine started')
        else:
            print('Engine start not allowed')

    @classmethod
    def validate_temperature(cls, temp):
        # print(cls.__name__)
        # return Vehicle2.MIN_TEMP <= temp <= Vehicle2.MAX_TEMP
        return cls.MIN_TEMP <= temp <= cls.MAX_TEMP


v2 = Vehicle2()
v2.engine_start(temparature=50)
print(v2.validate_temperature(temp=40))
print(Vehicle2.validate_temperature(temp=40))

# cls as class name -> best practices
# self as instance name -> best practices


# staticmethod
class Vehicle4:

    def __init__(self, distance):
        self.__distance = distance

    @staticmethod
    def _km_to_miles(km_distance):
        KM_IN_MILE = 1.609
        return km_distance / KM_IN_MILE

    def odometer(self, miles=False):
        distance = f'{self._km_to_miles(self.__distance):.3f} miles' if miles else f'{self.__distance} km'
        return distance

    def ride(self, curr_distance):
        self.__distance += curr_distance


v4 = Vehicle4(distance=105)
v4.ride(100)
print(v4.odometer(miles=True))
