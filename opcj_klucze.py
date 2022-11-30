import json
from datetime import datetime
from time import sleep


def reminder(number, divisor):
    return number % divisor


assert reminder(20, 7) == 6

my_kwargs = {
    'number': 20,

}

other_kwarg = {
    'divisor': 7,
}

assert reminder(**my_kwargs, **other_kwarg) == 6


def print_param(**kwargs):
    for k, v in kwargs.items():
        print(f'{k}={v}')
    print(param)



# print_param(11, alpha=1, beta=0.8, gamma=2.6)

def log(message, when=None):
    '''Wyświetlenie komunikatu wraz ze znacznikiem czasu'''
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')

log('Witaj!')
sleep(0.1)
log('Witaj ponownie')


def decode(data, default=None):
    try:
        return json.loads(data)
    except ValueError:
        if default is None:
            default = {}
        return default

f = decode('dane nieprawidłowe')
f['dane'] = 54
b = decode('też niedobrze')
b['dane2'] = 1
print("f:", f)
print("b:", b)