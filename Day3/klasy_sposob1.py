from collections import defaultdict, namedtuple


class Gradebook:
    def __init__(self):
        self._students = defaultdict(Subject)

    def student(self, name):
        return self._students[name]


Grade = namedtuple('Grade', ('score', 'weight'))


class Subject:
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight



class Student:
    def __init__(self):
        self._subjects = defaultdict(Subject)

    def get_subject(self, name):
        return self._subjects[name]
    

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count

book = Gradebook()
tomek = book.student('Tomasz Kaniecki')
tomek.report_grade(80, 0.10)
tomek.report_grade(60, 0.60)
tomek.report_grade(70, 0.15)


# book = Gradebook()
# book.add_student('Tomasz Kaniecki')
# book.report_grade('Tomasz Kaniecki', 'informatyka', 90, 0.05)
# book.report_grade('Tomasz Kaniecki', 'WF', 95, 0.15)
# book.report_grade('Tomasz Kaniecki', 'Angielski', 75, 0.65)
#
# print(book.average_grade('Tomasz Kaniecki'))


# grades = []
# grades.append((95, 0.45, "Great job"))
# grades.append((85, 0.55, "Bedzie lepiej..."))
# total = sum(score * weight for score, weight in grades)
# total_weight = sum(weight for _, weight in grades)
# average_grade = total / total_weight
# print(average_grade)
# 
# Grade = namedtuple('Grade', ('score', 'weight'))
