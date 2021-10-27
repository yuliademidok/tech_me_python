import random
from itertools import count

from tic_tac_toe.board import display_board, get_board


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
            display_board(board)
            break
        else:
            print("Ячейка не существует или занята")
            continue


def computer_step(user: dict, board: list[list]):
    possible_steps = []
    for row in board:
        possible_steps.extend([(board.index(row), i) for i, j in zip(count(), row) if j == 0])

    comp_step = random.choice(possible_steps)
    board[comp_step[0]][comp_step[1]] = user["symbol"]
    display_board(board)


def make_step(user: dict, board: list[list]):
    if user['mode'] == 'COMP':
        computer_step(user, board)
    else:
        user_step(user, board)


def want_new_game() -> bool:
    new_game_string = "Желаете начать новую игру?\ny/N>>>"
    while True:
        user_answer = input(new_game_string)
        if user_answer.lower() == 'y':
            return True
        if user_answer.lower() in ('', 'n'):
            return False
        else:
            print("Ошибка ввода, введите верное значение")
            continue
