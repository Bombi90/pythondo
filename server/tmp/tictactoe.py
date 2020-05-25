#Define the table board

def display_board(board):
    print('       |       |       ')
    print('   '+board[1]+'   '+'|'+'   '+board[2]+'   '+'|'+'   '+board[3]+'   ')
    print('       |       |       ')
    print('-----------------------')
    print('       |       |       ')
    print('   '+board[4]+'   '+'|'+'   '+board[5]+'   '+'|'+'   '+board[6]+'   ')
    print('       |       |       ')
    print('-----------------------')
    print('       |       |       ')
    print('   '+board[7]+'   '+'|'+'   '+board[8]+'   '+'|'+'   '+board[9]+'   ')
    print('       |       |       ')
    

#Define the marker for each player

def player_input():
    
    marker = ''
    
    while marker != 'X' and marker != 'O':
        marker = input('Player1, choose X or O:').upper()
    
    if marker == 'X':
        return ('X', 'O')
        
    else:
        return ('O', 'X')

    
#Assigne the marker to a position

def place_marker(board,marker,position):
    
    board[position] = marker
    

#Check if someone wins

def win_check(board,mark):
    
    return(
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[1] == mark and board[4] == mark and board[7] == mark) or
    (board[2] == mark and board[5] == mark and board[8] == mark) or
    (board[3] == mark and board[6] == mark and board[9] == mark) or
    (board[1] == mark and board[5] == mark and board[9] == mark) or
    (board[3] == mark and board[5] == mark and board[7] == mark)
    )


#Random choose initial player

import random

def choose_first():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    

#Check if the cell is empty

def space_check(board,position):
    
    return board[position] == ' '


#Check if the board is full

def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    # the board is full
    return True


#Select the position

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9)'))
        
    return position


#Replay function

def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')



#COMPLETE CICLE FOR PLAYING

print('Welcome to the Tic Tac Toe')

while True:
    #play the game
    #setting everytinh up (board, whos start, marker)
    
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    
    turn = choose_first()
    print(turn+' will go first')
    
    play_game = input('Ready to play? (Y/N)')
    if play_game.lower() == 'y':
        game_on = True
    else:
        game_on = False

    #Play the game
    
    while game_on:
        
        if turn == 'Player 1':
            
            #PLAYER 1 TURN
            
            #show the board
            display_board(the_board)
            
            #choose a position
            position = player_choice(the_board)
            
            #place a marker in the position
            place_marker(the_board,player1_marker, position)
            
            #check if they whon
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 has won')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('There is a Tie')
                    game_on = False
                else:
                    turn = 'Player 2'
        
        else:
            
            #PLAYER 2 TURN
            
            #show the board
            display_board(the_board)
            
            #choose a position
            position = player_choice(the_board)
            
            #place a marker in the position
            place_marker(the_board,player2_marker, position)
            
            #check if they whon
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 has won')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('There is a Tie')
                    game_on = False
                else:
                    turn = 'Player 1'



    if not replay():
        break
    # break out the while on the replay function
