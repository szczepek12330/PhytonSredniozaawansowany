from datetime import datetime
from functools import singledispatch, singledispatchmethod
from numbers import Real


# class Example:
#     @singledispatchmethod
#     def method(self, argument):
#         pass
#
#     @method.register
#     def _(self, argument: float):
#         pass


@singledispatch
def report(value):
    return f'Bez określania typu: {value}'


@report.register
def _(value: datetime):
    return f'Obiekt datetime: {value.isoformat()}'
#
#
# @report.register
# def _(value: complex):
#     return f'Liczba zespolona: {value.real}{value.imag:+}j'

#
# @report.register
# def _(value: Real):
#     return f'Liczba zespolona: {value:f}'


print(report(datetime.now()))
# print(report(100.0-30.0j))
# print(report("Tomek"))

# for k, v in report.registry.items():
#     print(f"{k} -> {v}")


