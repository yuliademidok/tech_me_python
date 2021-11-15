import random

from oop_1.mixins import PainMixin


class Bio:
    def __init__(self):
        self.dnk = random.randint(10 ** 2, 10 ** 5)


class Bacteria(Bio):
    def __init__(self):
        self.eat = random.choice(("O", "C", "H"))
        super().__init__()


class Reptile(Bacteria):
    def __init__(self):
        self.brain = random.choice((True, False))
        super().__init__()

    def say(self):
        say_str = "HELLO" if self.brain else "bla-bla"
        print(say_str)


class UFO(Bio):
    name = None

    def say(self):
        print(f"My name is {self.name}")


class Human(UFO):
    def __init__(self):
        self.name = random.choice(("Bob", "Laura", "Clara"))
        super().__init__()


class Hybrid(Human, Reptile, PainMixin):

    def say(self):
        print("Who am I?")
        super().say()


hybrid = Hybrid()
hybrid.pain()
hybrid.say()
