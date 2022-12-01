# def fibo():
#     a, b = 0, 1
#     while True:
#         yield b
#         a, b = b, a + b
from functools import wraps


# fib = fibo()
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
#
# for i in fibo():
#     print(i)
#     if i > 10:
#         break


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r})'
              f'->{result!r}')
        return result

    return wrapper


@trace
def fibo(n):
    '''Watość zwrotna to nta liczba ciągu Fibo'''
    if n in (0, 1):
        return n
    return (fibo(n - 2) + fibo(n - 1))

fibo(4)
print(fibo)
print(help(fibo))