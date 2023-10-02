class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self, increment):
        self.speed += increment

    def brake(self, decrement):
        self.speed -= decrement

    def display_speed(self):
        print(f"The car's current speed is {self.speed} mph.")

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


# A Python program (script) typically begins execution at the first line, which is the program's indentation level 0.
# A __name__ variable is generated prior to the execution of a Python program, though.

# without this first line is entry point


if __name__ == '__main__':
    print('Something will be printed during import')

    print(__name__)

    print('Script was called directly')
    # Instantiate a Car object
    my_car = Car("Tesla", "Model 3", 2021)

    # Access and modify attributes
    print(f"Make: {my_car.make}")
    print(f"Model: {my_car.model}")
    print(f"Year: {my_car.year}")

    my_car.accelerate(30)
    my_car.display_speed()

    my_car.brake(10)
    my_car.display_speed()

    # Call another method
    my_car.display_info()
