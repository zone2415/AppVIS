def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], "|", end=" ")
        print()
        print("-------------")

def check_win(board, player):
    for i in range(3):
        if (board[i][0] == player and board[i][1] == player and board[i][2] == player) or \
           (board[0][i] == player and board[1][i] == player and board[2][i] == player):
            return True
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
       (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return True
    return False

def tic_tac_toe():
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    players = ["X", "O"]
    current_player = players[0]
    while True:
        print_board(board)
        row = int(input("Введите строку (1-3) для " + current_player + ": ")) - 1
        col = int(input("Введите столбец (1-3) для " + current_player + ": ")) - 1
        if board[row][col] != " ":
            print("Это место уже занято!")
            continue
        board[row][col] = current_player
        if check_win(board, current_player):
            print_board(board)
            print(current_player + " побеждает!")
            break
        if all([cell != " " for row in board for cell in row]):
            print_board(board)
            print("Это ничья!")
            break
        current_player = players[(players.index(current_player) + 1) % 2]

tic_tac_toe()

