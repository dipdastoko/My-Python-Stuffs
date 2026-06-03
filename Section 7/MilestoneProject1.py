from IPython.display import clear_output
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

def place_maker(board,marker,position):
    