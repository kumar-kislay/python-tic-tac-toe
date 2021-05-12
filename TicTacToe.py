from os import system, name
from time import sleep


playing_board = list()
playing_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
play_counter = 0

def board_reset():
    global playing_board
    playing_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def clear_output():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def display_board(board):
    clear_output()
    print(board[7]+"|"+board[8]+"|"+board[9])
    print(board[4]+"|"+board[5]+"|"+board[6])
    print(board[1]+"|"+board[2]+"|"+board[3])

    

def win_check(mark):
    l = list()
    l = playing_board
    win = l[1]==l[2]==l[3]==mark or \
    l[4]==l[5]==l[6]==mark or \
    l[7]==l[8]==l[9]==mark or \
    l[1]==l[4]==l[7]==mark or \
    l[2]==l[5]==l[8]==mark or \
    l[3]==l[6]==l[9]==mark or \
    l[1]==l[5]==l[9]==mark or \
    l[3]==l[5]==l[7]==mark
    
    return win
        

def play_board(marker,position):
    global play_counter
    if playing_board[int(position)]!=" ":
        print("The position is not available. Choose another...")
    else:
        playing_board.pop(int(position))
        playing_board.insert(int(position),marker)
        
        play_counter = play_counter + 1
        display_board(playing_board)
        
    return win_check(marker)


def player_input():
    print("Welcome to Tic Tac Toe! ")
    player1_marker = ""
    player2_marker = ""
    position = 0
    play_input = ""
    global play_counter

    
    while player1_marker.upper() not in ["X","O"]:
        player1_marker = input("Player 1: Do you want to be X or O? ")
    
    if player1_marker.upper() == "X":
        player2_marker = "O"
        player1_marker = "X"
    else:
        player2_marker = "X"
        player1_marker = "O"

        
    print("Player 1 is " + player1_marker + " Player 2 is " + player2_marker + " ")
    print("Player 1 will go first ")
    
    
    while play_input.upper() != "NO":
        position = input("Choose your next position: (1-9) ")
        
        if play_counter%2 == 0:
            player_marker = player1_marker
        else:
            player_marker = player2_marker
        
        if play_board(player_marker,position)==True:
            print("Congratulations, Player " + player_marker + " is the Winner ")
            play_input = input("Are you ready to play ? Enter yes or No. ")
            if play_input.upper() == "YES":
                print("Welcome back..! ")
                board_reset()

    print("Good Bye, see you soon...!")
        
player_input()


        