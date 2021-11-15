import random

from oop_1.board import Board

COMP_NAMES = [
    "R2D2",
    "C3PO",
    "WALLE",
    "DALEK",
]


class Player:

    def __init__(self, symbol, name=None):
        self.name = self._get_name(name)
        self.symbol = symbol

    def _get_name(self, name):
        if name:
            return name
        return random.choice(COMP_NAMES)

    def get_step(self, board: Board):
        return random.choice(tuple(board.get_free_cells()))


class Gamer(Player):

    def _get_name(self, name):
        if name:
            return name
        user_input = input("Enter your name:")
        return user_input

    def get_step(self, board: Board):
        while True:
            result = []
            input_step = input("Введите координаты хода через пробел\n")
            steps = input_step.split(" ")
            try:
                if len(steps) != 2:
                    raise ValueError
                for itm in steps:
                    result.append(int(itm))
            except ValueError:
                print("Ячейка не существует или занята")
                continue
            return tuple(result)


if __name__ == "__main__":
    user = Gamer("X")
    board = Board(3)
    user.get_step(board)

