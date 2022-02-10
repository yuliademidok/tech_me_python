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


# pawns = {"b4", "d4", "f4", "c3", "e3", "g5", "d2"}
#
# pawns_indexes = list()
# for i in pawns:
#     row = int(i[1]) - 1
#     col = ord(i[0]) - 97
#     pawns_indexes.append([row, col])


class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.max_health = health
        self.attack = attack

    @property
    def is_alive(self) -> bool:
        return self.health > 0

    def hit(self, other: list, healer=None):
        other[0].health_loss(self.attack)
        if healer:
            healer.heal(self)

    def health_loss(self, enemy_attack_weight):
        self.health -= enemy_attack_weight
        return enemy_attack_weight


class Knight(Warrior):
    def __init__(self):
        super().__init__(attack=7)


class Defender(Warrior):
    def __init__(self):
        super().__init__(health=60, attack=3)
        self.defense = 2

    def health_loss(self, enemy_attack_weight):
        loss = max(0, enemy_attack_weight - self.defense)
        self.health -= loss
        return loss


class Vampire(Warrior):
    def __init__(self):
        super().__init__(health=40, attack=4)
        self.vampirism = 50

    def hit(self, other: list, healer=None):
        damage = other[0].health_loss(self.attack)
        self.health += damage * (self.vampirism / 100)
        if healer:
            healer.heal(self)


class Lancer(Warrior):
    def __init__(self):
        super().__init__(attack=6)
        self.next_attach = 0.5

    def hit(self, other: list, healer=None):
        other[0].health_loss(self.attack)
        if len(other) > 1:
            other[1].health_loss(self.attack * self.next_attach)
        if healer:
            healer.heal(self)


class Healer(Warrior):
    def __init__(self):
        super().__init__(health=60, attack=0)
        self.heal_power = 2

    def heal(self, other):
        other.health = min(other.health + self.heal_power, other.max_health)

    def hit(self, other: list, healer=None):
        pass


class Army:
    def __init__(self):
        self.soldiers = []

    def add_units(self, obj, qty):
        self.soldiers.extend(obj() for _ in range(qty))

    @property
    def alive_soldiers(self):
        return list(filter(lambda x: x.is_alive, self.soldiers))

    @property
    def healer(self):
        if len(self.alive_soldiers) > 1 and isinstance(self.alive_soldiers[1], Healer):
            return self.alive_soldiers[1]
        else:
            return None

    @property
    def is_alive(self):
        return len(self.alive_soldiers) > 0


def fight(unit_1, unit_2):
    while unit_1.is_alive:
        unit_1.hit([unit_2])
        if not unit_2.is_alive:
            return True
        unit_2.hit([unit_1])
    return unit_1.is_alive


class Battle:

    @staticmethod
    def fight(arm_1, arm_2):
        while arm_1.is_alive and arm_2.is_alive:
            arm_1_soldier = arm_1.alive_soldiers[0]
            arm_2_soldier = arm_2.alive_soldiers[0]

            if arm_1_soldier.is_alive:
                arm_1_soldier.hit(arm_2.alive_soldiers, arm_1.healer)
            if arm_2_soldier.is_alive:
                arm_2_soldier.hit(arm_1.alive_soldiers, arm_2.healer)
        return arm_1.is_alive

    @staticmethod
    def straight_fight(arm_1, arm_2):
        while arm_1.is_alive and arm_2.is_alive:
            counter = min(len(arm_1.alive_soldiers), len(arm_2.alive_soldiers))
            arm_1_soldiers = arm_1.alive_soldiers
            arm_2_soldiers = arm_2.alive_soldiers

            while counter:
                arm_1_soldiers[counter - 1].hit([arm_2_soldiers[counter - 1]])
                if arm_2_soldiers[counter - 1].is_alive:
                    arm_2_soldiers[counter - 1].hit([arm_1_soldiers[counter - 1]])
                counter -= 1
        return arm_1.is_alive
