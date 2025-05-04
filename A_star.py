import heapq

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-----")

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def possible_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def heuristic_score(board, symbol):
    opponent = 'X' if symbol == 'O' else 'O'
    lines = board + \
            [[board[i][j] for i in range(3)] for j in range(3)] + \
            [[board[i][i] for i in range(3)], [board[i][2 - i] for i in range(3)]]
    score = 0
    for line in lines:
        if line.count(symbol) == 3:
            score += 100
        elif line.count(symbol) == 2 and line.count(" ") == 1:
            score += 10
        elif line.count(opponent) == 2 and line.count(" ") == 1:
            score -= 10
    return score

def a_star(board, symbol):
    frontier = [(0, board, 0, None)]
    visited = set()

    while frontier:
        f_score, current, steps, last_move = heapq.heappop(frontier)
        if check_winner(current, symbol):
            return last_move
        for i, j in possible_moves(current):
            new_board = [row[:] for row in current]
            new_board[i][j] = symbol
            board_key = tuple(map(tuple, new_board))
            if board_key in visited:
                continue
            visited.add(board_key)
            g_cost = steps + 1
            h = heuristic_score(new_board, symbol)
            f_score = g_cost + h
            heapq.heappush(frontier, (f_score, new_board, g_cost, (i, j)))
    return None

def main():
    board = [[" "] * 3 for _ in range(3)]
    while True:
        print_board(board)
        row, col = map(int, input("Your turn (Enter row col): ").split())
        if board[row][col] != " ":
            print("Invalid move! Try again.")
            continue
        board[row][col] = "X"
        if check_winner(board, "X"):
            print_board(board)
            print("You win!")
            break
        if is_full(board): 
            print_board(board)
            print("Draw!")
            break
        ai_move = a_star(board, "O")
        if ai_move:
            ai_row, ai_col = ai_move
            board[ai_row][ai_col] = "O"
            if check_winner(board, "O"):
                print_board(board)
            print("AI wins!")
            break
            if is_full(board): print_board(board)
            print("Draw!")
            break

if __name__ == "__main__":
    main()
