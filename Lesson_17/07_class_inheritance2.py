# extend
class Parent:
    def bye(self):
        print('Bye')


class Child_01(Parent):
    def hello(self):
        print('Hello!')


# overriding

class Parent2:
    def hello(self):
        print('Hello from Parent2!')

class Parent3:
    def hello(self):
        print('Hello from Parent3!')


class Child_02(Parent2, Parent3):
    # def hello(self):
    #     print('Hello!')
    pass


p2 = Parent2()
ch2 = Child_02()
ch2.hello()


# super()

class Parent3:
    def __init__(self, x):
        self.x = x
        self._obj = 78

    def print_obj(self):
        print(self._obj)


class Child_03_1(Parent3):
    # def __init__(self, x):
    #     self.x = x
    pass


class Child_03_2(Parent3):
    def __init__(self, x, y):
        # self.x = x

        # Parent3.__init__(self, x)
        # super(Child_03_2, self).__init__(x)
        super().__init__(x)
        self.y = y


ch = Child_03_2(10, 20)
print(ch.__dict__)
