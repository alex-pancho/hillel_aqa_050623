# class Coordinates:
#     MIN_X = 0
#     MIN_Y = 0
#     MAX_X = 1920
#     MAX_y = 1280
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     @classmethod
#     def set_max_x(cls, x):
#         cls.MAX_X = x
#
#
# pt1 = Coordinates(100, 200)
# pt2 = Coordinates(300, 250)
# print(pt1.MAX_X)
# pt1.set_max_x(2000)
# print(pt1.__dict__)
# print(Coordinates.__dict__)
class Geom:
    doc = 'Hello'


class Coordinates:
    MIN_X = 0
    MIN_Y = 0
    MAX_X = 1920
    MAX_y = 1280

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_max_x(self, x):
        self.MAX_X = x

    def __getattribute__(self, attr):
        print('we were looking for some attribute')
        if attr == 'x':
            print('Yes we were looking for X')
        else:
            #raise ValueError('Other attributes are not allowed')
            return super().__getattribute__(attr)

    def __setattr__(self, key, value):
        # print('=' * 30)
        # print('we set some values to attributes')
        # print('=' * 30)
        # self.x = value*2 # recursion error
        self.__dict__['y'] = value*2
        super().__setattr__(key, value)

    def __getattr__(self, item):
        print('Call to non existing attributes')

    def __delattr__(self, item):
        print('Attribute deleted only within this info')


pt1 = Coordinates(100, 200)
#x_attr = pt1.x
#y_attr = pt1.y
#print(x_attr)
# attr3 = pt1.z
pt1.x = 500
print(pt1.y)
print(pt1.x)
del pt1.x
