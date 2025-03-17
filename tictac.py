def print_board(board):

    for row in board:

        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):

    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):

        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):

        return True

    return False


def is_draw(board):

    return all(cell in ['X', 'O'] for row in board for cell in row)


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Tic Tac Toe")
    print_board(board)

    while True:
        print(f"Player {players[current_player]}'s turn.")
        
        try:

            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            
            if board[row][col] != " ":
                print("Spot taken")
                continue
        
        except (ValueError, IndexError):
            print("invalid input")
            continue

        board[row][col] = players[current_player]
        print_board(board)

        if check_winner(board, players[current_player]):
            print(f"Player {players[current_player]} wins!")
            break

        if is_draw(board):
            print("Draw")
            break

        current_player = 1 - current_player


if __name__ == "__main__":
    tic_tac_toe()