from itertools import cycle, count
import random

"""
Игра крестики-нолики.
"""

interface_string = {
    "rules": "",
    "hello": "Здравсвуй, игрок",
    "game_type": "С кем желаешь играть {variants}",
    "enter_name": "Игрок #{user_number}: Введите свое имя",
    "ask_step": "Ход #{step_number} игрока {name}",
    "win": "Победил игрок {name} на ходу #{step_number}",
    "draw": "Ничья, победителей нет",
    "new_game": "Желаете начать новую игру? {variants}",
    "invalid_step": "Этот шаг не доступен, попробуй еще раз",
    "bye": "До встречи",
}

template_variants = {
    "enter_name": lambda template, **kwargs: template.format(**kwargs),
    "game_type": lambda template, **kwargs: template.format(variants=("C", "U")),
    "ask_step": lambda template, **kwargs: template.format(**kwargs),
    "win": lambda template, **kwargs: template.format(**kwargs),
    "new_game": lambda template, **kwargs: template.format(variants=("Y", "N")),
}


def user_interface(template_name, **template_vars):
    if template_name in template_variants:
        ask_str = template_variants[template_name](interface_string[template_name], **template_vars)
        user_input = input(ask_str.format(variants=template_variants[template_name])) + '\n'
        return user_input
    else:
        print(interface_string[template_name])


def matrix_match(board):
    def check_line(line):
        line_set = set(line)
        if 0 not in line_set and len(line_set) == 1:
            raise ValueError("CHECK_LINE")
        return False

    board_len = len(board)

    diagonal = set(map(lambda idx: board[idx][idx], range(0, board_len)))
    diagonal_invert = set(map(lambda idx: board[idx][board_len - idx - 1], range(board_len - 1, -1, -1)))

    try:
        _ = any(map(check_line, (diagonal, diagonal_invert)))

        for row, column in zip(board, zip(*board)):
            _ = any(map(check_line, (row, column)))
    except ValueError as exc:
        if "CHECK_LINE" in exc.args:
            return True
        else:
            raise exc

    return False


def is_draw(board):
    for row in board:
        if 0 in row:
            return False
    return True


def step_available(user_step: list, board):
    try:
        user_step = [int(i) for i in user_step]
    except ValueError:
        return False

    board_len = len(board)
    return len(user_step) == 2 and user_step[0] <= board_len and user_step[1] <= board_len\
        and board[user_step[0] - 1][user_step[1] - 1] == 0


def do_user_step(step_number, name, board):
    user_step = user_interface("ask_step", step_number=step_number, name=name).strip()

    user_step = user_step.split(' ')
    if step_available(user_step, board):
        user_step = [int(i) for i in user_step]
        board[user_step[0] - 1][user_step[1] - 1] = name
        print(board)
    else:
        user_interface("invalid_step")
        return do_user_step(step_number, name, board)


def do_computer_step(board):
    possible_steps = []
    for row in board:
        possible_steps.extend([(board.index(row), i) for i, j in zip(count(), row) if j == 0])

    comp_step = random.choice(possible_steps)
    board[comp_step[0]][comp_step[1]] = "C"

    print(board)


# game_type = {
#     "U": lambda x: "",
#     "C": lambda x: "",
# }

user_type = {
    "user_1": "U",
    "user_2": ""
}


def game():
    board = (
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    )

    user_type["user_2"] = user_interface("game_type").strip()
    users_list = [user_interface("enter_name", user_number=1).strip()]

    step_number = 0

    if user_type["user_2"].upper() == "C":
        users_list.append('computer')
    else:
        users_list.append(user_interface("enter_name", user_number=2).strip())

    user_name = cycle(users_list)

    while not matrix_match(board) and not is_draw(board):
        user = next(user_name)

        if users_list.index(user) == 0:
            step_number += 1

        if user_type["user_2"].upper() == "C" and users_list.index(user) == 1:
            do_computer_step(board)
        else:
            do_user_step(step_number=step_number, name=user, board=board)

    if matrix_match(board):
        next(user_name)
        user_interface("win", name=next(user_name), step_number=step_number)
    elif is_draw(board):
        user_interface("draw")

    return None


def main():
    user_interface("hello")
    game()

    if user_interface("new_game").strip().lower() == 'y':
        return game()
    else:
        return user_interface("bye")


main()
