from collections import UserDict
from typing import Any, List


class CaseInsesitiveDict(UserDict):
    def __setitem__(self, key: str, value: Any):
        return super().__setitem__(key.lower(), value)

    def __getitem__(self, key: str) -> Any:
        return super().__getitem__(key.lower())

    def __delitem__(self, key: str) -> None:
        return super().__delitem__(key.lower())


# headers = CaseInsesitiveDict({
#     "Content-Length": 30,
#     "Content-Type": "json",
# })
#
# print(headers["CONTENT-LENGTH"])
# print(headers["Content-Length"])
# print(headers["content-length"])

# class CommonBase:
#     pass
#
# class Base1(CommonBase):
#     pass
#
# class Base2(CommonBase):
#     def method(self):
#         print("Wywołanie Base2")
#
# class MyClass(Base1,Base2):
#     pass
#
# k1 = MyClass()
# k1.method()
#
# print(MyClass.__mro__)

class Point:
    x = 0
    y = 0

    def __init__(self, x, y):  # stinky code - nie do końca poprawnie pisany kod
        self.x = x
        self.y = y


# class Aggregator:
#
#     def __init__(self):
#         self.all_aggregated = []
#         self.last_aggregated = None
#
#     def aggregate(self, value):
#         self.last_aggregated = value
#         self.all_aggregated.append(value)

class Aggregator:
    all_aggregated = List[Any]
    last_aggregated = Any
    def __init__(self):
        self.all_aggregated = []
        self.last_aggregated = None

    def aggregate(self, value):
        self.last_aggregated = value
        self.all_aggregated.append(value)
a1 = Aggregator()
a2 = Aggregator()
a1.aggregate("a1-1")
a1.aggregate("a1-2")
a2.aggregate("a2-1")

print(a1.all_aggregated)
print(a2.all_aggregated)
print(a1.last_aggregated)
print(a2.last_aggregated)
# print(Aggregator.all_aggregated)
# print(Aggregator.last_aggregated)


class MyClass:
    def __init__(self):
        self.__secret_value = 1


class MyClass2(MyClass):
    pass

# isinstance_of = MyClass
# print(isinstance_of.__secret_value)
