def print_board(board):
    """Function to print the Tic-Tac-Toe board"""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Function to check if there is a winner"""
    # Check rows, columns and diagonals for a win
    for i in range(3):
        if all([spot == player for spot in board[i]]):  # Check row
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check column
            return True
    if all([board[i][i] == player for i in range(3)]):  # Check diagonal
        return True
    if all([board[i][2-i] == player for i in range(3)]):  # Check anti-diagonal
            return True
    return False

def is_full(board):
    """Function to check if the board is full"""
    return all([spot != ' ' for row in board for spot in row])

def main():
    """Main function to run the Tic-Tac-Toe game"""
    board = [[' ' for _ in range(3)] for _ in range(3)]  # Initialize a 3x3 board
    players = ['X', 'O']
    current_player = 0

    while True:
        print_board(board)
        try:
            row = int(input(f"Player {players[current_player]}, enter the row (0, 1, 2): "))
            col = int(input(f"Player {players[current_player]}, enter the column (0, 1, 2): "))
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input. Please enter 0, 1, or 2.")
                continue
        except ValueError:
            print("Invalid input. Please enter numbers 0, 1, or 2.")
            continue

        if board[row][col] == ' ':
            board[row][col] = players[current_player]
            if check_winner(board, players[current_player]):
                print_board(board)
                print(f"Player {players[current_player]} wins!")
                break
            elif is_full(board):
                print_board(board)
                print("The game is a draw!")
                break
            current_player = 1 - current_player
        else:
            print("This spot is already taken. Please choose another one.")
    
if __name__ == "__main__":
    main()
