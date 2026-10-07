N = int(input("Enter N: "))
board = [0] * (N + 1)

def is_safe(row, col):
    for i in range(1, row):
        if board[i] == col:
            return False
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def nqueen(row):
    if row > N:
        for i in range(1, N + 1):
            print(" ".join(str(board[i]) if j == board[i] else "0" for j in range(1, N + 1)))
        print()
        return

    for col in range(1, N + 1):
        if is_safe(row, col):
            board[row] = col
            nqueen(row + 1)
            board[row] = 0

nqueen(1)
