# -*- coding: utf-8 -*-
"""futureintern_pd_03.ipynb"""

#Tic Tac Toe Game Manually 

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    win_conditions = [
        # Rows
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    return [player, player, player] in win_conditions

def is_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def tic_tac_toe():
    while True:
        board = [[' ' for _ in range(3)] for _ in range(3)]
        current_player = 'X'

        while True:
            print_board(board)
            try:
                row = int(input(f"Current Player is {current_player}, enter row (0, 1, 2): "))
                col = int(input(f"Current player is {current_player}, enter column (0, 1, 2): "))
                if board[row][col] != ' ':
                    print("Cell is already taken. Please try again.")
                    continue
            except (IndexError, ValueError):
                print("Invalid input. Please enter numbers between 0 and 2.")
                continue

            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"{current_player} Player wins the game!!!")
                break
            if is_draw(board):
                print_board(board)
                print("It's a draw!!!")
                break

            # Switch player
            current_player = 'O' if current_player == 'X' else 'X'

        # Ask if players want to play again
        restart = input("Do you want to play again? (yes/no): ").strip().lower()
        if restart != 'yes':
            print("Thankyou for playing! Come again as when your interested.")
            break

if __name__ == "__main__":
    tic_tac_toe()

