def print_board(board):
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_board_full(board):
    return all(space != ' ' for space in board)

def main():
    board = [' '] * 9
    current_player = 'X'

    while True:
        print_board(board)
        
        # Get valid move from the current player
        while True:
            try:
                move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
                if board[move] == ' ' and 0 <= move <= 8:
                    board[move] = current_player
                    break
                else:
                    print("Invalid move. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter a number between 1 and 9.")

        # Check for a winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for a tie
        if is_board_full(board):
            print_board(board)
            print("The game is a tie!")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
