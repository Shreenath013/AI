def is_safe(board, row, col, n):
    # Check vertical column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(board, row, n, solutions):
    if row == n:
        # Deep copy the board to store the current solution
        solutions.append([r[:] for r in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, row + 1, n, solutions)
            board[row][col] = 0  # Backtrack

def display_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))
    print()

def main():
    n = int(input("Enter number of Queens: "))
    board = [[0] * n for _ in range(n)]
    solutions = []

    solve_n_queens(board, 0, n, solutions)

    print(f"\n1. Number of possible solutions: {len(solutions)}")
    k = int(input("2. Enter number of solutions you want to see: "))

    for index, sol in enumerate(solutions[:k], start=1):
        print(f"\nSolution {index}:")
        display_board(sol)

if __name__ == "__main__":
    main()
