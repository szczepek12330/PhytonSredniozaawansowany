def printfile(file):
    try:
        contents = file.read()
        print(file)
    finally:
        file.close()


# print(7 * 6)
# print(3.14 * 2)
# print(["a", "b"] * 3)
# print("ala " * 2)


class Matrix:
    def __init__(self, rows):
        if len(set(len(row) for row in rows)) > 1:
            raise ValueError("Wszystkie wiersze macierzy muszą być tej samej długości")
        self.rows = rows

def __add__(self, other):
    if(
        len(self.rows) != len(other.rows) or
        len(self.rows[0]) != len(other.rows[0])
    ):
        raise ValueError("Macierze mają niezgodne wymiary")
    return Matrix([
        [a + b for a,b in zip(a_row, b_row)]
        for a_row, b_row in zip(self.rows, other.rows)
    ])
def __sub__(self, other):
    if(
            len(self.rows) != len(other.rows) or
            len(self.rows[0]) != len(other.rows[0])
    ):
        raise ValueError("Macierze mają niezgodne wymiary")
    return Matrix([
        [a - b for a,b in zip(a_row, b_row)]
        for a_row, b_row in zip(self.rows, other.rows)
    ])
