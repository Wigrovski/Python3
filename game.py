import random


class Warrior:
    def __init__(self, name, value2, value):
        self.health = value
        self.name = name
        self.ctd = value2  # chance to dodge

    def attack(self, enemy):
        enemy.health = enemy.health - 20


unit1 = Warrior("Рагнар", 6, 100)
unit2 = Warrior("Ульрик", 4, 100)

while unit1.health > 0 and unit2.health > 0:
    x = random.randint(0, 1)
    c = random.randint(1, 10)
    if x == 0:
        if unit2.ctd > c:
            print("{} увернулся от атаки {}a.".format(unit2.name, unit1.name))
        else:
            unit1.attack(unit2)
            print("{} атаковал {}. У {} осталось {} единиц здоровья.".format(unit1.name, unit2.name, unit2.name,
                                                                             unit2.health))
    else:
        if unit1.ctd > c:
            print("{} увернулся от атаки {}.".format(unit1.name, unit2.name))
        else:
            unit2.attack(unit1)
            print("{} атаковал {}. У {} осталось {} единиц здоровья.".format(unit2.name, unit1.name, unit1.name,
                                                                             unit1.health))

if unit1.health == 0:
    print(unit2.name, " победил!")
else:
    print(unit1.name, " победил!")