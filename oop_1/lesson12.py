import random


class Human:
    __population = []

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
        Human.__population.append(self)

    def say(self):
        print("hello, my name is", self.name)

    def reproduction(self, other: "Human") -> "Human":
        name = "Some_new_name"
        sex = random.choice((self.sex, other.sex))
        skin = random.choice((self.skin, other.skin))
        # return Human(name, sex, skin)
        return self.__class__(name, sex, skin)

    def population_count(self) -> int:
        return len(self.__population)


class Board:
    # size - размер доски
    # содержимое таблица доски (матрица)
    # выбывшие ячейки в виде кортежей
    # Отображение доски
    # Принять ход
    # Проверка на матчинг

    # TODO: Создать класс реализующий доску для игры в крестики нолики
    # TODO: Метод установки шага на доску
    # TODO: Метод проверки что есть победитель
    # TODO: Метод печати доски на экран

    def __init__(self, size):
        self.size = size
        self.all_steps = set((n, m) for n in range(self.size) for m in range(self.size))
        self.done_steps = set()

    def print_board(self):
        pass

    def add_step(self, step: tuple[int, int]):
        pass

    def check(self) -> bool:
        pass


class Animal:
    def __init__(self, color: str):
        self.color = color

    def some(self):
        print("hello")


class Dog(Animal):
    def __init__(self, breed, height, color: str):
        self.breed = breed
        self.height = height
        super().__init__(color)

    def say(self):
        print("Gaf-gaf")


dog = Dog(123, "ter", "ginger")
dog.some()
