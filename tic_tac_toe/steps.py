import random
from itertools import count


def get_step() -> list[int, int]:
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
            print("Ошибка ввода, повторите")
            continue
        return result


def chek_step(board: list[list], step: list[int, int]) -> bool:
    if step[0] < 1 or step[1] < 1:
        return False
    try:
        cell = board[step[0] - 1][step[1] - 1]
        if not cell:
            return True
    except IndexError:
        print("Неверные координаты")
    return False


def user_step(user: dict, board: list[list]):
    while True:
        step = get_step()
        if chek_step(board, step):
            board[step[0] - 1][step[1] - 1] = user["symbol"]
            break
        else:
            print("Ячейка не существует или занята")
            continue


def computer_step(user: dict, board: list[list]):
    board_size = len(board)
    possible_steps = set((i, j) for i in range(board_size) for j in range(board_size))
    comp_step = random.choice(tuple(possible_steps.difference(user["all_steps"])))
    board[comp_step[0]][comp_step[1]] = user["symbol"]


def make_step(user: dict, board: list[list]):
    if user['mode'] == 'COMP':
        computer_step(user, board)
    else:
        user_step(user, board)


def ask_new_game() -> bool:
    variants = ('Y', 'N')

    while True:
        user_answer = input(f"Желаете начать новую игру? {'/'.join(variants)}").upper()
        if user_answer in variants:
            return user_answer == variants[0]
        print("Ошибка ввода, введите верное значение")

