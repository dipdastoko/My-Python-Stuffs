from IPython.display import clear_output
import random

test_board = ["#", " "," "," "," "," "," "," "," "," "]
def display_board(board):
    clear_output()
    print("   |   |   ")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("   |   |   ")
    print("----------")
    print("   |   |   ")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("   |   |   ")
    print("----------")
    print("   |   |   ")
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("   |   |   ")

def player_input():
    player1 = 'Wrong Choice'
    player2 = ""
    while player1 not in ["X","O"]:
        player1 = input("Player1 please choose your marker: X or O -- ")
        if player1 not in ["X","O"]:
            print("Please choose X or O")
        else:
            if player1=="X":
                player2="O"
            else:
                player2="X"
    print(f"Player1 marker is: {player1}")
    print(f"Player2 marker is: {player2}")
    return [player1,player2]

def place_marker(board,marker,position):
    board[position]=marker
    display_board(board)

test_board = ['#','X','O','X','O','X','O','X','O','X']
def win_check(board,mark):
    if board[7]==mark and board[8]==mark and board[9]==mark:
        return True
    elif board[4]==mark and board[5]==mark and board[6]==mark:
        return True
    elif board[1]==mark and board[2]==mark and board[3]==mark:
        return True
    elif board[7]==mark and board[4]==mark and board[1]==mark:
        return True
    elif board[8]==mark and board[5]==mark and board[2]==mark:
        return True
    elif board[9]==mark and board[6]==mark and board[3]==mark:
        return True
    elif board[7]==mark and board[5]==mark and board[3]==mark:
        return True
    elif board[1]==mark and board[5]==mark and board[9]==mark:
        return True
    else:
        return False

def choose_first():
    choice = random.randint(1,2)
    print(f"Player{choice} will choose first")
    return choice

def space_check(board,position):
    if board[position] != "":
        return True
    else:
        return False