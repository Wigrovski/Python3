import datetime

a = input('Введите первую дату гггг-мм-дд: ')
b = input('Введите вторую дату гггг-мм-дд: ')
a = a.split('-')
b = b.split('-')
aa = datetime.date(int(a[0]), int(a[1]), int(a[2]))
bb = datetime.date(int(b[0]), int(b[1]), int(b[2]))
delta = aa - bb
delta = abs(delta)
print(str(delta))
