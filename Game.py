import os
import random

# Function to clear console (works on Windows + Mac/Linux)
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_console()

# Function to display the Tic Tac Toe board
def display_board(board):
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

# Function to show position guide
def show_positions():
    print('Position Guide:')
    print(' 7 | 8 | 9')
    print('-----------')
    print(' 4 | 5 | 6')
    print('-----------')
    print(' 1 | 2 | 3')

# Ask Player 1 to choose marker
def player_input():
    marker = ''
    while marker not in ['X', 'O']:
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# Place marker on board
def place_marker(board, marker, position):
    board[position] = marker

# Check winning condition
def win_check(board, mark):
    return (
        (board[7] == mark and board[8] == mark and board[9] == mark) or
        (board[4] == mark and board[5] == mark and board[6] == mark) or
        (board[1] == mark and board[2] == mark and board[3] == mark) or
        (board[7] == mark and board[4] == mark and board[1] == mark) or
        (board[8] == mark and board[5] == mark and board[2] == mark) or
        (board[9] == mark and board[6] == mark and board[3] == mark) or
        (board[7] == mark and board[5] == mark and board[3] == mark) or
        (board[9] == mark and board[5] == mark and board[1] == mark)
    )

# Randomly decide who goes first
def choose_first():
    return 'Player 1' if random.randint(0, 1) else 'Player 2'

# Check if space is empty
def space_check(board, position):
    return board[position] == ' '

# Check if board is full
def full_board_check(board):
    return all(board[i] != ' ' for i in range(1, 10))

# Take valid player input
def player_choice(board):
    while True:
        try:
            position = int(input('Choose your next position (1-9): '))
            if position in range(1, 10) and space_check(board, position):
                return position
            else:
                print("Invalid position! Try again.")
        except:
            print("Please enter a valid number!")

# Replay option
def replay():
    return input('Do you want to play again? (Yes/No): ').lower().startswith('y')


# ------------------ MAIN GAME ------------------

print('Welcome to Tic Tac Toe!')
show_positions()

# Score tracking
player1_score = 0
player2_score = 0

while True:
    # Reset board
    theBoard = [' '] * 10

    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(f"{turn} will go first.")

    play_game = input('Are you ready to play? (Yes/No): ').lower()
    game_on = True if play_game == 'yes' else False

    while game_on:

        # -------- Player 1 Turn --------
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print(f'{turn} wins the game!')
                player1_score += 1
                game_on = False

            elif full_board_check(theBoard):
                display_board(theBoard)
                print('The game is a draw!')
                break

            else:
                turn = 'Player 2'

        # -------- Player 2 Turn --------
        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print(f'{turn} wins the game!')
                player2_score += 1
                game_on = False

            elif full_board_check(theBoard):
                display_board(theBoard)
                print('The game is a draw!')
                break

            else:
                turn = 'Player 1'

    # Show score after each game
    print("=" * 30)
    print(f"Score -> Player 1: {player1_score} | Player 2: {player2_score}")
    print("=" * 30)

    # Ask replay
    if not replay():
        print("Thanks for playing!")
        break
