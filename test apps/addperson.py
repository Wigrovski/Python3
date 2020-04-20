import time

print('== Привет, это записная книжка, что делаем? ==' + '\n' +
                '1: Запись || 2: Поиск'                )
# Занесение данных и отображение всех записей
agree = input("Заносим данные y/n ?: ")
while agree == 'y':
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    phone = input('Введите номер телефона: ')
    user = (name, surname, phone)
    file = open("phone.txt", 'a+')
    s = 'Имя: {},Фамилия: {},Телефон: {}'.format(name, surname, phone)
    file.write('\n' + s)
    file.close
    agree = input("Заносим  еще данные y/n ?: ")
    if agree == 'n':
        continue
print('== Смотрим записную книжку ==')
time.sleep(1)
file = open("phone.txt", 'r')
f = file.read()
print(f)

# Система поиска по файлу

print('==== Давай поищем: ======')
data = str(input('введите имя или фамилию: '))
file = open("phone.txt", 'r')
for line in file.readlines():
    sl = (dict(l.strip().split(':', 1) for l in line.split(', ')))
flag = True
for search in sl:
    if sl[search]['Имя'] == data:
        print(sl[search]['Телефон'])
        flag = False
file.close()





# for key, value in sl.items():
#         print(value)


# def poisk(value):
#     if value == data:
#         return sl.values[value]
# res = list(filter(poisk, sl.values()))
# print(res)


