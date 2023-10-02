# class Example:
#     def __new__(cls, *args, **kwargs):
#         print('We are in NEW')
#         return super().__new__(cls)
#
#     def __init__(self):
#         print('We are in init')
#
#
# ex1 = Example()
# ex2 = Example()
# print(id(ex1))
# print(id(ex2))


class SomeConnection:
    __instance = None
    __ip = None
    __port = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        print('Cleanup')

    def __init__(self, ip, port):
        self.__ip = ip if self.__ip is None else self.__ip
        self.__port = port if self.__port is None else self.__port

    def connect(self):
        print(f'Trying to connect to {self.__ip}:{self.__port}')

    def disconnect(self):
        print('Closing connection')
        SomeConnection.__instance = None
        self.__ip = None
        self.__port = None

    def send_data(self, data):
        print(f'Sending {data=}')


import sys

print(sys.getrefcount(SomeConnection))
conn1 = SomeConnection('8.8.8.8', 53)
print(sys.getrefcount(SomeConnection))
print(id(conn1))
conn2 = SomeConnection('1.2.3.4', 80)
print(id(conn2))

conn1.connect()
conn1.disconnect()

conn3 = SomeConnection('1.1.1.1', 80)
conn3.connect()
