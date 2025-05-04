import heapq


board = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]


def printboard():
    for i in board:
        print(i)
    print("\n\n")


def isBoardfull():
    for i in board:
        for j in i:
            if j == '_':
                return False
    return True


def heuristic_score(symbol):
    opponent = 'O' if symbol == 'X' else 'X'


    def line_score(line):
        if line.count(symbol) == 3:
            return 100
        elif line.count(symbol) == 2 and line.count('_') == 1:
            return 10  
        elif line.count(opponent) == 2 and line.count('_') == 1:
            return -10  
        return 0


    score = 0


    for row in board:
        score += line_score(row)


    for col in range(3):
        column = [board[row][col] for row in range(3)]
        score += line_score(column)


    main_diag = [board[i][i] for i in range(3)]
    anti_diag = [board[i][2 - i] for i in range(3)]
    score += line_score(main_diag)
    score += line_score(anti_diag)


    return score


def get_available_moves():
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == '_']


def Computer_turn():
    if isBoardfull():
        print("Match Draw....")
        return


    def calculate_f_score(move, depth):
        i, j = move
        board[i][j] = 'X'
        g = depth  
        h = heuristic_score('X')  
        board[i][j] = '_'  
        return g + h


    priority_queue = []
    depth = 0


    for move in get_available_moves():
        f_score = calculate_f_score(move, depth)
        heapq.heappush(priority_queue, (-f_score, move))  


    _, best_move = heapq.heappop(priority_queue)
    i, j = best_move
    board[i][j] = 'X'


    if win_by_symbol('X'):
        print("Computer Won.......!!!")
        printboard()
        exit(0)


    printboard()


def Your_turn():
    if isBoardfull():
        print("Match Draw....")
        return


    print("\nYour turn Now:- ")
    i = int(input("Enter i (0-2): "))
    j = int(input("Enter j (0-2): "))


    if board[i][j] == '_':
        board[i][j] = 'O'
        if win_by_symbol('O'):
            print("You Won.......!!!")
            printboard()
            exit(0)
    else:
        print("Invalid move. Try again.")
        Your_turn()
        return

    printboard()


def win_by_symbol(symbol):
    for i in range(3):
        if win_by_row(symbol, i) or win_by_col(symbol, i):
            return True
    return win_by_diagonal(symbol)


def win_by_diagonal(symbol):
    return all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3))


def win_by_row(symbol, i):
    return all(board[i][j] == symbol for j in range(3))


def win_by_col(symbol, j):
    return all(board[i][j] == symbol for i in range(3))


while not isBoardfull():
    Your_turn()
    Computer_turn()
