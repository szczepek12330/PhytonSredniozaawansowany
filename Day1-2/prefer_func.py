# def divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         return None
# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return False, None
def divide(a: float, b: float):
    '''dzieli wartość a przez b
    zgłasza wyjątek jesli nie można przeprowadzić operacji
    '''
    try:
        wynik = a / b
    except Exception as e:
        print("nieprawidłowe dane", e.args)
    else:
        print('wynik operacji to %.1f' % wynik)
        return wynik

# x, y = 1, 0
# result = divide(x, y)
# if result is None:
#     print('Nieprawidłowe dane')

# x, y = 0, 5
# _, result = divide(x, y)
# if not result:
#     print('Nieprawidłowe dane')

x, y = 4, 0
result = divide(x, y)
print(result)