import time

print('== Привет, это записная книжка ==')
# Занесение данных и отображение всех записей
agree = input("Заносим данные y/n ?: ")
while agree == 'y':
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    phone = input('Введите номер телефона: ')
    user = (name, surname, phone)
    file = open("phone.txt", 'a+')
    s = 'Имя: {} , Фамилия: {} , Телефон: {} '.format(name, surname, phone)
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
file.close()
# Система поиска по файлу
