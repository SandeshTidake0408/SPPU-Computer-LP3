def isSafe(board, row, col, n):
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left side
    i, j = row, col
    while j >= 0 and i < n:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solveNQueens(board, col, n):
    # Base case: if all queens are placed
    if col >= n:
        return True

    for i in range(n):
        if isSafe(board, i, col, n):
            board[i][col] = 1

            if solveNQueens(board, col + 1, n):
                return True

            board[i][col] = 0  # Backtrack

    return False


def printSolution(board):
    for row in board:
        print(" ".join(str(x) for x in row))


# Driver code
n = 8
board = [[0 for _ in range(n)] for _ in range(n)]

if not solveNQueens(board, 0, n):
    print("Solution does not exist")
else:
    printSolution(board)
