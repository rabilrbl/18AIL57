size = 8

Board = [[0] * size for _ in range(size)]


def is_valid(row, col):
    # Check if a queen can be placed on board[row][col].
    # A queen can be placed on board[row][col] if no queen is placed in the same row,
    # same column and same diagonal
    for x in range(row):
        if Board[x][col] == 1 or abs(x - row) == abs(Board[x].index(1) - col):
            return False
    return True


def n_queens(row):
    # If we have placed all queens in the board, return True
    if row == size:
        return True

    for col in range(size):
        # Check if it is safe to place a queen in board[row][col]
        if is_valid(row, col):
            Board[row][col] = 1
            # Place this queen in board[row][col] and recursively check for other queens
            if n_queens(row + 1):
                return True
            # If placing queen in board[row][col] doesn't lead to a solution, remove queen from board[row][col]
            Board[row][col] = 0

    return False


n_queens(0)

for row in Board:
    print(row)
