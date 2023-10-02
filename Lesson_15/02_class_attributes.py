class Point:
    pass


d1 = {Point: 1}
print(d1)

# attributes
# variables visibility area
# class Point:
#     x = 5
#     y = 10


# Point.x = 3
# print(Point.x)
# print(Point.__dict__)
# print(Point.__class__.__bases__)

# class instance
class Point:
    x = 5
    y = 10

p1 = Point()
p2 = Point()
# p1()
print(id(p1))
print(id(p2))
print(type(p1))

print(p1.__dict__)
print(p2.__dict__)
#print(p1.x)
#print(p1.z)
#
# # own visibility area   (outer/inner functions analog)
# p1.x = 11
# print(Point.x)
# print(p1.x)
# print(p1.__dict__)
# #
# # attributes operations
# Point.z = 100
# print(Point.z)
# # Point.color = 'red'
# setattr(Point, 'color', 'red')
# print(Point.color)
#
# # possible Attribute error
# #print(Point.non_existing)
#
# # d1 = {'a':1}
# # #'b'
# # b = d1.get('b', 1000000)
# # print(b)
# print(getattr(Point, 'non_existing', 5000))
# #print(Point.non_existing)
# print(Point.__dict__)
# del Point.color
# print('-'*50)
# print(Point.__dict__)
#
# if hasattr(Point, 'color'):
#     delattr(Point, 'color')
# else:
#     print("attr not exists")
#
# print(hasattr(Point, 'non_existing'))
# print(hasattr(p1,'y'))
#
