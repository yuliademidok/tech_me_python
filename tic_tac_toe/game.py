from itertools import cycle

from tic_tac_toe.board import get_board, board_match, is_draw
from tic_tac_toe.steps import make_step, want_new_game
from tic_tac_toe.users import ask_mode, create_users


def game_init() -> dict:
    print("Добро пожаловать в Игру Крестики Нолики")
    return {
        "users": create_users(ask_mode()),
        "board": get_board(3),
    }


game_vars = game_init()


def game_end():
    if want_new_game():
        game_vars['board'] = get_board(3)
        game_cycle(**game_vars)
    else:
        print("До встречи")


def game_cycle(users: list[dict, ...], board: list[list]):
    # 1 должна циклично итерироваться по пользователям либо написать свой цикличный итератор либо найти его в itertools
    # Опрашивать пользователя на предмет хода
    # Проверяем возможность хода
    # Проверяем выйгрышный вариант
    # Либо поздравить с победой, либо обьявить Ничью
    for step_num, user in enumerate(cycle(users), 1):
        print(f"Ход {step_num} Игрока: {user['name']}")
        make_step(user, board)
        if board_match(board):
            print(f"Победил {user['name']} на ходе #{step_num}")
            break
        if is_draw(board):
            print("Ничья")
            break

    game_end()


game_cycle(**game_vars)

