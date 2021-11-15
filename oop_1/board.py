from collections import defaultdict
from itertools import chain


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
        self.__size = size
        self.__free_steps = set((i, j) for i in range(self.__size) for j in range(self.__size))
        self._done_steps = defaultdict(set)
        self.board = [[0 for _ in range(self.__size)] for _ in range(self.__size)]

    def print_board(self):
        print(self)

    def add_step(self, step: tuple[int, int], user: str):
        if step in self.__free_steps:
            self._done_steps[user].add(step)
            self.__free_steps.remove(step)
            self.board[step[0]][step[1]] = user
        else:
            raise ValueError("Ячейка не существует или занята")

    def board_match(self) -> bool:
        def chek_line(line):
            line_set = set(line)
            if 0 not in line_set and len(line_set) == 1:
                raise ValueError("CHECK_LINE")
            return False

        board_len = len(self.board)
        diagonal = map(lambda idx: self.board[idx][idx], range(0, board_len))
        diagonal_invert = map(lambda idx: self.board[idx][board_len - idx - 1], range(board_len - 1, -1, -1))
        try:
            _ = any(map(chek_line, (diagonal, diagonal_invert)))
            for row, column in zip(self.board, zip(*self.board)):
                _ = any(map(chek_line, (row, column)))
        except ValueError as exc:
            if 'CHECK_LINE' in exc.args:
                return True
            else:
                raise exc
        return False

    def get_free_cells(self) -> set:
        return self.__free_steps
        # all_steps = set((i, j) for i in range(self.__size) for j in range(self.__size))
        # return all_steps.difference({itm for itm in chain(self._done_steps.values())})

    def __str__(self):
        separator = '#' * self.__size * 2 + '##'
        title_row = f'  {" ".join(map(str, list(range(self.__size))))}'
        rows = ""
        for idx, row in enumerate(self.board):
            rows += f'{idx} {"|".join(f"{i}" for i in row)}\n'

        return f"{separator}\n{title_row}\n{rows}{separator}"


if __name__ == "__main__":
    board = Board(3)

    board.add_step((0, 1), "X")
    board.add_step((0, 0), "X")
    board.add_step((2, 2), "X")
    # print(board.board_match())
    print(board)
    board.print_board()

    print(board.get_free_cells())
