class MyObject:
    def __init__(self):
        self.public_field = 5
        self.__private_field = 10

    def get_private_field(self):
        return self.__private_field


class MyOtherObject:
    def __init__(self):
        self.__private_field = 71

    # @classmethod
    # def get_private_field_of_instance(cls, instance):
    #     return instance.__private_field

class MyChildObject(MyOtherObject):
    def get_private_field(self):
        return self.__private_field


f3 = MyChildObject()
# f3.get_private_field()
f1 = MyObject()
assert f1.public_field == 5
assert f1.get_private_field() == 10
f2 = MyOtherObject()
# assert MyOtherObject.get_private_field_of_instance(f2) == 71
assert f3._MyOtherObject__private_field == 71
print(f3.__dict__)
