import copy


def get_board(board_size):
    board = [0] * board_size
    for i in range(board_size):
        board[i] = [0] * board_size
    return board


def print_board(boards, board_size):
    for i in boards:
        for j in i:
            print(j)
        print()


def check_promising(board, row, col, board_size):
    # 같은 행
    for i in range(col):
        if board[row][i] == 1:
            return False

    # \ 방향 대각선
    x, y = row, col

    while x >= 0 and y >= 0:
        if board[x][y] == 1:
            return False
        x -= 1
        y -= 1

    # / 방향 대각선
    x2, y2 = row, col

    while x2 < board_size and y2 >= 0:
        if board[x2][y2] == 1:
            return False
        x2 += 1
        y2 -= 1

    return True


def n_queen(board, col, board_size):
    # 열이 N을 초과하면 return
    if col >= board_size:
        return

    for i in range(board_size):
        if check_promising(board, i, col, board_size):
            board[i][col] = 1
            if col == board_size - 1:
                add_board(board)
                board[i][col] = 0
                return
            n_queen(board, col + 1, board_size)
            board[i][col] = 0


def add_board(board):
    global boards
    saved_board = copy.deepcopy(board)
    boards.append(saved_board)


board_size = int(input('N = '))
print()
board = get_board(board_size)
boards = []
n_queen(board, 0, board_size)
print_board(boards, board_size)