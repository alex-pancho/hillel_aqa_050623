# class Write:
#     def prn():
#         print('Hello World')
#         return 10
#
#
# print(Write.prn())
# # Write.prn()
#
# w1 = Write()
# print(w1.prn)
#
#
# # w1.prn()
#
# ##### self
# class Write2:
#     def prn(self):
#         print(self)
#         print('Hello World2')
#
#
# w2 = Write2()
# # print(w2.prn)
# w2.prn()
# # print(hex(id(w2)))
# #
# print(Write2.prn(w2))
#
# Write2.prn()
# Write2.prn(w2)  # == w2.prn()


# self usage as access to local variables ability to create them

class Vehicle:

    def beep(self):
        if not hasattr(self, 'beep_count'):
            self.beep_count = 0
        self.beep_count += 1


v1 = Vehicle()
v1.beep()
v1.beep()
v2 = Vehicle()
v2.beep()
v2.beep()
v2.beep()
v2.beep()
v2.beep()
print(v1.beep_count)
print(v2.beep_count)
print(v1.__dict__)
print(v2.__dict__)
print(Vehicle.__dict__)
func = getattr(v1, 'beep')
#func = v1.beep
print(func)
func()
print(v1.beep_count)
