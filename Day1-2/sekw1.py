a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(a[::2])
print(a[::-2])
print(a[2::2])
print(a[-2::-2])
print(a[-2:2:-2])
print(a[2:2:-2])

y = a[::2]
z = y[1:-1]
print(y)
print(z)




# print('Dwa środkowe:', a[3:5])
# print('Wszystkie poza skrajnymi:', a[1:7])
# assert a[:5] == a[0:5]
# assert a[5:] == a[5:(len(a))]
# # print(a[:])
# # print(a[:-1])
# # print(a[2:-1])
# # print(a[-3:-1])
#
# b = a[3:]
# print('Przed:     ', b)
# b[1] = 99
# print('Po:        ', b)
# print('Bez zmian:     ', a)
#
# c = ['czerwony', 'pomarańczowy', 'żółty', 'zielony', 'niebieski', 'fioletowy']
#
# odds = c[::2]
# evens = c[1::2]
# print(odds)
# print(evens)
#
# x = 'Tomek'
# y = x[::-1]
# print(y)
#
# w = '寿司'
# w.encode('utf-8')
# z = w[::-1]
# # z1 = z.decode('utf-8')
# print(z)
