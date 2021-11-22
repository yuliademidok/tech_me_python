# import re
#
# text = "Hello.World"
# text = "Hello world"
# text = " a word "
# text = "... and so on ..."
#
# result = re.split(r'[`\-=~!@#$%^&*()_+\[\]{};\\\:"|<,./<>? ]', text)
# result = list(filter(None, result))
# print(result)
import itertools
from datetime import datetime

from datetime import date, timedelta

# f = date(2014, 12, 31) # 31 december 2014
# s = date(2011, 1, 1) # 1 january 2011
# f - s == datetime.timedelta(1460)


# def days_diff(a, b):
#     a = date(*a)
#     b = date(*b)
#     # a = datetime.strptime(", ".join(map(str, a)), "%Y, %m, %d")
#     # b = datetime.strptime(", ".join(map(str, b)), "%Y, %m, %d")
#     c = b - a
#     return c.days
#
#
# print(days_diff([1982,4,19], [1982,4,22]))

from itertools import cycle


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self) -> bool:
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Army:
    def __init__(self):
        self.soldiers = []

    def add_units(self, obj, qty):
        while qty:
            soldier = obj()
            self.soldiers.append(soldier)
            qty -= 1
        return self.soldiers

    def __getitem__(self, item):
        return self.soldiers

    def __self__(self):
        return self.soldiers


class Battle:

    # @staticmethod
    # def alive_soldier(army):
    #     return list(filter(lambda x: x.is_alive, army.soldiers))

    @staticmethod
    def fight(arm_1, arm_2):
        # if len(arm_1.soldiers) in (10, 20):
        #     return True

        attack_weight = 0
        for i in cycle((arm_1, arm_2)):
            if len(arm_1.soldiers) == 0 or len(arm_2.soldiers) == 0:
                break
            i.soldiers[0].health -= attack_weight
            attack_weight = i.soldiers[0].attack
            i.soldiers = list(filter(lambda x: x.is_alive, i.soldiers))

        return not len(arm_1.soldiers) == 0


def fight(unit_1, unit_2):
    attack_weight = 0
    for i in cycle((unit_1, unit_2)):
        i.health -= attack_weight
        attack_weight = i.attack
        if not (unit_1.is_alive and unit_2.is_alive):
            return unit_1.health > 0


army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 20)
army_2.add_units(Warrior, 21)
battle = Battle()
print(battle.fight(army_1, army_2))
print(army_2.soldiers[0].health)


# my_army = Army()
# my_army.add_units(Knight, 1)
# enemy_army = Army()
# enemy_army.add_units(Warrior, 3)
#
# # s1 = enemy_army.soldiers[0]
# # s2 = enemy_army.soldiers[1]
# # s2.health = 0
# # s3 = enemy_army.soldiers[2]
# # print(list(filter(lambda x: x.is_alive, enemy_army.soldiers)))
#
# battle = Battle()
# # result = battle.fight(my_army, enemy_army)
# result = battle.fight(enemy_army, my_army)
# print(result)
#
