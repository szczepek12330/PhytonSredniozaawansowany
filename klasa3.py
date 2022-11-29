import random


import random


# class InitOnAccess:
#     def __init__(self, init_func, *args, **kwargs):
#         self.klass = init_func
#         self.args = args
#         self.kwargs = kwargs
#         self._initialized = None
#
#     def __get__(self, instance, owner):
#         if self._initialized is None:
#             print("Inicjalizacja!")
#             self._initialized = self.klass(*self.args, **self.kwargs)
#         else:
#             print("Z pamięci podręcznej!")
#         return self._initialized
#
#
# class WithSortedRandoms:
#     lazily_initialized = InitOnAccess(
#         sorted,
#         [random.random() for _ in range(5)]
#     )
#
# m = WithSortedRandoms()
# print(m.lazily_initialized)
# print(m.lazily_initialized)
class lazy_property():
    def __init__(self, function):
        self.fget = function

    def __get__(self, obj, cls):
        value = self.fget(obj)
        setattr(obj, self.fget.__name__, value)
        return value


class WithSortedRandoms2:
    @lazy_property
    def lazily_initialized(self):
        return sorted([random.random() for _ in range(5)])
