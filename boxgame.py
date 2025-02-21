board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")

def handle_move(board, symbol, move):
    row = move // 3
    col = move % 3
    if board[row][col] == "-":
        board[row][col] = symbol
        return True
    else:
        return False

def check_win(board, symbol):
    # Check rows
    for row in board:
        if row.count(symbol) == 3:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == symbol and board[1][col] == symbol and board[2][col] == symbol:
            return True

    # Check diagonals
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True
    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True

    return False

def play_game(board):
    current_player = "X"
    while True:
        print_board(board)
        move = int(input("Player " + current_player + ", enter your move (1-9): ")) - 1
        if handle_move(board, current_player, move):
            if check_win(board, current_player):
                print_board(board)
                print("Player " + current_player + " wins!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move, try again.")

play_game(board)