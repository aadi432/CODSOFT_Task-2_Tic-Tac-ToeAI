import math
import random

WIN_PATTERNS = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

board = [' '] * 9
turnO = True 

def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def reset_game():
    global board, turnO
    board = [' '] * 9
    turnO = True

def is_winner(symbol):
    for pattern in WIN_PATTERNS:
        if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] == symbol:
            return True
    return False

def check_winner():
    if is_winner('O'):
        print("Congratulations, Winner is O!")
        return True
    elif is_winner('X'):
        print("Congratulations, Winner is X!")
        return True
    elif ' ' not in board:
        print("It's a draw!")
        return True
    return False

def evaluate_board():
    if is_winner('O'):
        return 10
    elif is_winner('X'):
        return -10
    else:
        return 0

def minimax(depth, is_maximizing):
    score = evaluate_board()
    
    if score == 10:
        return score

    if score == -10:
        return score

    if ' ' not in board:
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = max(best, minimax(depth + 1, not is_maximizing))
                board[i] = ' '
        return best

    else:
        best = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = min(best, minimax(depth + 1, not is_maximizing))
                board[i] = ' '
        return best

def find_best_move():
    best_val = -math.inf
    best_move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            move_val = minimax(0, False)
            board[i] = ' '
            if move_val > best_val:
                best_move = i
                best_val = move_val
    return best_move

def get_human_move():
    while True:
        try:
            move = int(input("Enter a position (1-9): ")) - 1
            if 0 <= move < 9 and board[move] == ' ':
                return move
            else:
                print("Invalid move. Position either taken or out of range.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def play_game():
    global turnO
    while True:
        print_board()
        if turnO:
            print("Bot turn.")
            move = find_best_move()
        else:
            print("Player turn.")
            move = get_human_move()
        
        board[move] = 'O' if turnO else 'X'
        turnO = not turnO
        
        if check_winner():
            print_board()
            if input("Play again? (y/n): ").lower() != 'y':
                break
            reset_game()

if __name__ == "__main__":
    play_game()
