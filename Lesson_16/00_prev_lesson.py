# https://habr.com/ru/articles/475120/
# https://docs.python.org/3.8/c-api/typeobj.html
from weakref import WeakValueDictionary


class SomeConnection:
    __instance = WeakValueDictionary()
    __ip = None
    __port = None

    def __new__(cls, *args, **kwargs):
        if len(cls.__instance) == 0:
            instance = super().__new__(cls)
            cls.__instance['key'] = instance
        return cls.__instance['key']

    def __del__(self):
        print('Cleanup')
        SomeConnection.__instance = WeakValueDictionary()
        self.__ip = None
        self.__port = None

    def __init__(self, ip, port):
        self.__ip = ip if self.__ip is None else self.__ip
        self.__port = port if self.__port is None else self.__port

    def connect(self):
        print(f'Trying to connect to {self.__ip}:{self.__port}')

    def disconnect(self):
        print('Closing connection')
        self.__instance = None
        self.__ip = None
        self.__port = None

    def send_data(self, data):
        print(f'Sending {data=}')


import sys

print(sys.getrefcount(SomeConnection))
conn1 = SomeConnection('8.8.8.8', 53)
print(sys.getrefcount(SomeConnection))
print(id(conn1))
conn1.connect()


conn1 = None
# import gc
# gc.disable()
# gc.collect()
# import time
# time.sleep(4)
#
# print('-' * 30)
# print(len(list([itm for itm in gc.get_objects() if 'SomeConnection' in str(itm)])))
# print(*[itm for itm in gc.get_objects() if 'SomeConnection' in str(itm)], sep='\n')

# conn1.disconnect()
conn2 = SomeConnection('1.2.3.4', 80)
print(id(conn2))
conn2.connect()

# #############################################################
