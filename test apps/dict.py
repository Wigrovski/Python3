class Person():
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.full = name + " " + surname + " " + age
        # print(self.full)

    def __str__(self):
        return '{} {} {}'.format(self.name, self.surname, self.age)


agree = input("Заносим данные y/n ?: ")
while agree == 'y':
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    age = input('Введите возраст: ')
    user = Person(name, surname, age)
    text = str(user)
    with open(r"file.txt", 'a') as file:
        for line in text:
            file.writelines(text + '\n')
    continue
    agree = input("Заносим данные y/n ?: ")
    if agree == 'n':
        break


