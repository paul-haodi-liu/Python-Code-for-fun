from IPython.display import clear_output

# Print out the current game board and make sure to remove the previously displayed board.
def printboard(b):
    
    clear_output()
    print(b[1],'|',b[2], '|',b[3])
    print('- - - - - ')
    print(b[4],'|',b[5], '|',b[6])
    print('- - - - - ')
    print(b[7],'|',b[8], '|',b[9])

# b is the list standing for the game board. First one #, the following 9 represent the 9 slots. ' ' represents unoccupied slot.
# Player p put chess at the location n (1-9)
def move(n,p,b):
    
    if b[n] == ' ':
        b[n] = p
    else:
        print('The spot has already been occupied!')

# Check if anyone has won in the current board
def check_win(b):
    return (b[1]==b[2]==b[3]=='X') or (b[1]==b[2]==b[3]=='O')or (b[4]==b[5]==b[6]=='X') or (b[4]==b[5]==b[6]=='O') \
    or (b[7]==b[8]==b[9]=='X') or (b[7]==b[8]==b[9]=='O') or (b[1]==b[4]==b[7]=='X') or (b[1]==b[4]==b[7]=='O') or (b[2]==b[5]==b[8]=='X') \
    or (b[2]==b[5]==b[8]=='O') or (b[3]==b[6]==b[9]=='X') or (b[3]==b[6]==b[9]=='O') or (b[1]==b[5]==b[9]=='X')\
    or (b[1]==b[5]==b[9]=='O') or (b[3]==b[5]==b[7]=='X') or (b[3]==b[5]==b[7]=='O')

def replay():

    while True:
        answer = input("Do you want to play again? Enter Yes or No ")
    
        if answer == 'Yes':
            return True
        elif answer == 'No':
            return False
        else:
            pass

# Check if the board is full.
def fullBoard(b):
    
    return ' ' not in b

# Let's start to play the game!
while True:
    print("Welcome to the Tic Tac Toe game!")
    # Set up the initial empty board
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    printboard(board)
    # Make sure each player has picked a marker
    setup = False
    while setup==False:
        player1 = input('Player 1: Do you want to be X or O ？')
        if player1 == 'X':
            player2 = 'O'
            setup = True

        elif player1 == 'O':
            player2 = 'X'
            setup = True

        else:
            continue
    # An indicator keeping track of whose turn it is. (True, then it is player1's turn. False, then it is player 2's turn)
    xianshou = True
    
    # Continue the subsequent turns of the game
    while True:
        
        # A player select a place to put its marker
        location = int(input("Please make a move (1-9)"))
        
        # Make sure to negate xianshou in order for the two players to play alternately
        if xianshou:
            move(location,player1,board)
            xianshou = not xianshou
        else:
            move(location,player2,board)
            xianshou = not xianshou
        
        # Print out the new board after each move
        printboard(board)
    
        # check if any player has won after each move
        if check_win(board):
            # Note that the xianshou has already been negated after the move. 
            if not xianshou:
                print("Congratulations! Player 1 has won!")
                break
                
            else:
                print("Congratulations! Player 2 has won!")
                break
        
        # If no one has won, check if the board is full. If it is, then there is a tie. The game is over if one player wins or there is 
        # a tie.(That is why we break!) Otherwise, we keep playing and go to the next round.
        else:
        
            if fullBoard(board):
                print("There is a tie!")
                break
            else:
                pass
    # Ask the user whether to restart the game
    if replay():
        continue
    
    else:
        break
    
    