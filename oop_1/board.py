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
        self._possible_steps = set((n, m) for n in range(self.__size) for m in range(self.__size))
        self._done_steps = set()
        self.board = [[0 for _ in range(self.__size)] for _ in range(self.__size)]

    def print_board(self):
        separator = '#' * self.__size * 2 + '##'

        print(separator)
        print(" ", " ".join(map(str, list(range(self.__size)))))
        for idx, row in enumerate(self.board):
            print(f'{idx} {"|".join(f"{i}" for i in row)}')
        print(separator)

    def add_step(self, step: tuple[int, int], symbol: str):
        if step in self._possible_steps:
            self._done_steps.add(step)
            self._possible_steps.remove(step)
            self.board[step[0]][step[1]] = symbol
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


if __name__ == "__main__":
    board = Board(3)

    board.add_step((0, 1), "X")
    board.print_board()

    print(board.board_match())

    board.add_step((0, 0), "X")
    board.add_step((0, 2), "X")
    print(board.board_match())

