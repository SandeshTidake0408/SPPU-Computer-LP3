def print_board(board):
    for row in board:
        print("  ".join("Q" if col else "_" for col in row))
    print()


def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueen(board, row, n):
    if row >= n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if (solve_nqueen(board, row+1, n)):
                return True

            board[row][col] = 0

    return False


if __name__ == "__main__":
    n = 8
    board = [[0 for _ in range(n)] for _ in range(n)]

    board[0][0] = 1  # placed first queen

    if solve_nqueen(board, 1, n):
        print("8 - Queens Solution : ")
        print_board(board)
    else:
        print("No Solution Exists :( ")
