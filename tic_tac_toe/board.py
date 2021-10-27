def get_board(size):
    result = []
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(0)
        result.append(row)
    return result


def board_match(board):
    def chek_line(line):
        line_set = set(line)
        if (0 not in line_set and len(line_set) == 1):
            raise ValueError("CHECK_LINE")
        return False

    board_len = len(board)
    diagonal = map(lambda idx: board[idx][idx], range(0, board_len))
    diagonal_invert = map(lambda idx: board[idx][board_len - idx - 1], range(board_len - 1, -1, -1))
    try:
        _ = any(map(chek_line, (diagonal, diagonal_invert)))
        for row, column in zip(board, zip(*board)):
            _ = any(map(chek_line, (row, column)))
    except ValueError as exc:
        if 'CHECK_LINE' in exc.args:
            return True
        else:
            raise exc
    return False


def is_draw(board):
    board_len = len(board)

    def check_line(line):
        filtered_line = list(filter(None, line))
        return len(filtered_line) == board_len and len(set(filtered_line)) == board_len - 1

    diagonal = map(lambda idx: board[idx][idx], range(0, board_len))
    diagonal_invert = map(lambda idx: board[idx][board_len - idx - 1], range(board_len - 1, -1, -1))

    result = [all(map(check_line, (diagonal, diagonal_invert)))]

    for row, column in zip(board, zip(*board)):
        result.append(all(map(check_line, (row, column))))

    return result[0] and result[1]


def display_board(board):
    board = [[symbol or '-' for symbol in row] for row in board]
    counter = 1

    print('#' * 8)
    print("1 2 3".rjust(7, " "))
    for raw in board:
        print(f'{counter} {raw[0]}|{raw[1]}|{raw[2]}')
        counter += 1
    print('#' * 8)
