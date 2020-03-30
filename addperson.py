import time

agree = input("Заносим данные y/n ?: ")
while agree == 'y':
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    age = input('Введите возраст: ')
    user = (name, surname, age)
    file = open("file.txt", 'a+')
    s = '{} , {} , {} лет'.format(name, surname, age)
    file.write('\n' + s)
    file.close
    agree = input("Заносим  еще данные y/n ?: ")
    if agree == 'n':
        continue
print('== Смотрим заполненный журнал ==')
time.sleep(1)
file = open("file.txt", 'r')
f = file.read()
print(f)
file.close()
