import math
from dataclasses import dataclass
from functools import reduce, partial
from itertools import count


def circle(radius):
    return math.pi * radius ** 2


circle_area = lambda radius: math.pi * radius ** 2

print(circle(42))
print(circle_area(42))

@dataclass
class Person:
    age: int
    weight: int
    name: str

people = Person()

sorted(people, key=lambda person: weight.age)

print(f"Wynik map: {list(map(lambda x: x ** 2, range(10)))}")
print(f"Wynik map 2: {list(map(print, range(5), range(4), range(5)))}")
# print(f"Wynik map: {(map(lambda x: x**2, range(10)))}")
evens = filter(lambda number: number % 2 == 0, range(10))
odds = filter(lambda number: number % 2 == 1, range(10))
print(list(evens))
print(list(odds))
persons = ["tomek", "jakub", "tadeusz"]
s = filter(lambda person: person.startswith('t'), persons)
print(list(s))

print(reduce(lambda a, b: a + b, [2, 2]))
print(reduce(lambda a, b: a + b, range(100)))

for i in count():
    print(i)

n = 4
print(list(map(lambda x: x ** 2, range(n))))
sek = map(lambda x: x ** 2, count())
print(next(sek))
print(next(sek))
print(next(sek))
print("Tu robię coś innego...")
print(next(sek))

powers_of_2 = partial(pow, 2)
print(powers_of_2(2))
print(powers_of_2(5))
print(powers_of_2(10))

