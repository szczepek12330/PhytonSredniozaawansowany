def log(seq, message, *values):
    if not values:
        print(f'{seq}= {message}')
    else:
        values_str = ",".join(str(x)for x in values)
        print(f'{seq} - {message}:{values_str}')


def gen():
    for i in range(10):
        yield i

def my_func(*args):
    print(args)
fav = [5, 66, 889]
log('Moje liczby to', 1, 2)
log(1, "Hello!")
log("Moje ulubione cyfry", fav)
log("Moje ulubione cyfry", *fav)