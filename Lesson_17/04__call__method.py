# make class object callable ( behave as function)
class SomeCounter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, *args, **kwargs):
        print('Here was call')
        start = kwargs.get('start', 1)
        self.__counter += start
        return self.__counter


c = SomeCounter()
c()
# c()
# print(c())
# print(c())
c2 = SomeCounter()
c2(start=21)
c2()
print(c2())

# class decoractors
import math


class SinX:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, *args, **kwargs):
        return math.sin(self.__fn(x))


@SinX
def simple(x):
    return x


# simple = SinX(simple)
print(simple(math.pi / 2))


# call usage for frequently used methods as alias


class SomeCounter2:
    def __init__(self):
        self.__counter = 0

    def hello_world(self):
        print('Hello World!')

    def __call__(self, *args, **kwargs):
        return self.hello_world()


c2 = SomeCounter2()
c2.hello_world()
c2()
