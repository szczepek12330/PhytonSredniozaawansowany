from collections import defaultdict

import result as result


def log_missing():
    print('klucz został dodany')
    return 0


current = {'zielony': 12, 'niebieski': 3}
increments = [
    ('czerwony', 5),
    ('niebieski', 17),
    ('pomarańczowy', 9),
]


print('Przed:', dict(
for key, amount in increments:
    result[key] += amount
result, count =
class CountMissing:
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0


counter = CountMissing()
result = defaultdict(counter.missing, current)
for key, amount in increments:
    result[key] += amount
assert counter.added == 2
