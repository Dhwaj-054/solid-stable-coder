#Tic Tac Toe game for 1v1 and 1vComputer

#Tic Tac Toe game code in python for 2 players input based

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    return any(all(cell == player for cell in row) for row in board) or \
           any(all(board[r][c] == player for r in range(3)) for c in range(3)) or \
           all(board[i][i] == player for i in range(3)) or \
           all(board[i][2 - i] == player for i in range(3))

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        print(f"Player {players[turn]}'s turn.")
        try:
            row, col = map(int, input("Enter row and column (0-2) separated by a space: ").split())
            if board[row][col] != " ":
                print("Cell already taken. Try again!")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Enter row and column as two numbers (0-2).")
            continue

        board[row][col] = players[turn]
        print_board(board)

        if check_winner(board, players[turn]):
            print(f"Player {players[turn]} wins!")
            break
        elif all(cell != " " for row in board for cell in row):
            print("It's a tie!")
            break

        turn = 1 - turn  # Switch player

if __name__ == "__main__":
    tic_tac_toe()


Output:
Welcome to Tic Tac Toe!
  |   |  
-----
  |   |  
-----
  |   |  
-----
Player X's turn.
Enter row and column (0-2) separated by a space: 1 1
  |   |  
-----
  | X |  
-----
  |   |  
-----
Player O's turn.
Enter row and column (0-2) separated by a space: 1 0
  |   |  
-----
O | X |  
-----
  |   |  
-----
Player X's turn.
Enter row and column (0-2) separated by a space: 0 0 
X |   |  
-----
O | X |  
-----
  |   |  
-----
Player O's turn.
Enter row and column (0-2) separated by a space: 2 0
X |   |  
-----
O | X |  
-----
O |   |  
-----
Player X's turn.
Enter row and column (0-2) separated by a space: 2 2
X |   |  
-----
O | X |  
-----
O |   | X
-----
Player X wins!




TicTacToe 1 player input based against computer
import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    return any(all(cell == player for cell in row) for row in board) or \
           any(all(board[r][c] == player for r in range(3)) for c in range(3)) or \
           all(board[i][i] == player for i in range(3)) or \
           all(board[i][2 - i] == player for i in range(3))

def get_empty_cells(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def computer_move(board):
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells)  # Randomly choose an empty cell

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    computer = "O"
    
    print("Welcome to Tic Tac Toe! You are X, and the computer is O.")
    print_board(board)

    while True:
        # Player's turn
        print("Your turn!")
        try:
            row, col = map(int, input("Enter row and column (0-2) separated by a space: ").split())
            if board[row][col] != " ":
                print("Cell already taken. Try again!")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Enter row and column as two numbers (0-2).")
            continue

        board[row][col] = player
        print_board(board)

        if check_winner(board, player):
            print("Congratulations! You win!")
            break
        elif not get_empty_cells(board):
            print("It's a tie!")
            break

        # Computer's turn
        print("Computer's turn...")
        row, col = computer_move(board)
        board[row][col] = computer
        print_board(board)

        if check_winner(board, computer):
            print("Computer wins! Better luck next time.")
            break
        elif not get_empty_cells(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    tic_tac_toe()


"""
Output:
Welcome to Tic Tac Toe! You are X, and the computer is O.
  |   |  
-----
  |   |  
-----
  |   |  
-----
Your turn!
Enter row and column (0-2) separated by a space: 1 1
  |   |  
-----
  | X |  
-----
  |   |  
-----
Computer's turn...
  |   |  
-----
  | X |  
-----
  |   | O
-----
Your turn!
Enter row and column (0-2) separated by a space: 0 1
  | X |  
-----
  | X |  
-----
  |   | O
-----
Computer's turn...
  | X |  
-----
  | X |  
-----
  | O | O
-----
Your turn!
Enter row and column (0-2) separated by a space: 2 0
  | X |  
-----
  | X |  
-----
X | O | O
-----
Computer's turn...
  | X |  
-----
O | X |  
-----
X | O | O
-----
Your turn!
Enter row and column (0-2) separated by a space: 0 2
  | X | X
-----
O | X |  
-----
X | O | O
-----
Congratulations! You win!
"""
