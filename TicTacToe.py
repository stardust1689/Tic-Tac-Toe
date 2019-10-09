# Code by Christopher Peters
# Started August 20th, 2019
# Last edited August 20th, 2019
import sys
import random as rand

print('Welcome to Tic-Tac-Toe for two players!')
print(' ')
print('Before you start, make sure the NUM-PAD on your keyboard is activated.')
print(' ')

# b is a list that represents the board, so it starts empty.
b = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# "winner" and "tie" are booleans that can change depending on the current board.
# If three identical marks are found in a row on the board, the "winner" 
# boolean becomes True.
winner = False
tie = False  
# count represnts the number of marks on the board. If count = 9, the "tie"
# boolean becomes True.
count = 0

# Function used to display the rules
def rules():
    print('To play, the two players select a single-key mark. They then take turns')
    print('placing their mark on an empty square on this board:')
    print(' ')
    print('     |     |     ')
    print('     |     |     ')
    print('_____|_____|_____')
    print('     |     |     ')
    print('     |     |     ')
    print('_____|_____|_____')
    print('     |     |     ')
    print('     |     |     ')
    print('     |     |     ')
    print(' ')
    print('To place a mark, press the NUM-PAD key that corresponds to the square')
    print('which you want your mark placed.')
    print(' ')
    print('When you do, your oppenent will be prompted to do the same.')
    print('The first player to place three identical marks in a row will be the')
    print('winner!')

# Function for Player 1 to place a mark
def X():
    select = ' '
    while select == ' ':
        select = input('Player 1 - Enter the number for the square to place your mark, or press "r" to review the rules: ')
        invalid = False
        try:
            int(select)
        except ValueError:
            invalid = True
        # The player can input the key 'r' to review the rules. 
        if select == 'r':
            rules()
            select = ' '
        elif invalid == True:
            print('Invalid selection. Try again.')
            select = ' '
            invalid = False
        elif int(select) in range(1,10):
            if b[int(select)-1] == ' ':
                b[int(select)-1] = mark1
                print('     |     |     ')
                print('  {}  |  {}  |  {}  '.format(b[6],b[7],b[8]))
                print('_____|_____|_____')
                print('     |     |     ')
                print('  {}  |  {}  |  {}  '.format(b[3],b[4],b[5]))
                print('_____|_____|_____')
                print('     |     |     ')
                print('  {}  |  {}  |  {}  '.format(b[0],b[1],b[2]))
                print('     |     |     ')
                check(b)
                global count
                count += 1
                if count == 9:
                    print('Tie game!')
                    playagain()
            else:
                print('Square is taken. Try again.')
                select = ' '
        else:
            select = ' '     

# Function for Player 2 to place a mark            
def O():
    select = ' '
    while select == ' ':
        select = input('Player 2: Enter the number for the square to place your mark, or press "r" to review the rules: ')
        invalid = False
        try:
            int(select)
        except ValueError:
            invalid = True
        if select == 'r':
            rules()
            select = ' '
        elif invalid == True:
            print('Invalid selection. Try again.')
            select = ' '
            invalid = False
        elif int(select) in range(1,10):
            if b[int(select)-1] == ' ':
                b[int(select)-1] = mark2
                print('     |     |     ')
                print('  {}  |  {}  |  {}  '.format(b[6],b[7],b[8]))
                print('_____|_____|_____')
                print('     |     |     ')
                print('  {}  |  {}  |  {}  '.format(b[3],b[4],b[5]))
                print('_____|_____|_____')
                print('     |     |     ')
                print('  {}  |  {}  |  {}  '.format(b[0],b[1],b[2]))
                print('     |     |     ')
                check(b)
                global count
                count += 1
                if count == 9:
                    print('Tie game!')
                    global tie
                    tie = True
                    playagain()
            else:
                print('Square is taken. Try again.')
                select = ' '
        else:
            select = ' '       

# Function to check whether a player has obtained three in a row; can affect the "winner" boolean
def check(b):
    if (b[0] == b[1] == b[2] == mark1) or (b[3] == b[4] == b[5] == mark1) or (b[6] == b[7] == b[8] == mark1):
        print('Player 1 wins!')
        global winner
        winner = True
    elif (b[0] == b[1] == b[2] == mark2) or (b[3] == b[4] == b[5] == mark2) or (b[6] == b[7] == b[8] == mark2):
        print('Player 2 wins!')
        winner = True
    elif (b[0] == b[3] == b[6] == mark1) or (b[1] == b[4] == b[7] == mark1) or (b[2] == b[5] == b[8] == mark1):
        print('Player 1 wins!')
        winner = True
    elif (b[0] == b[3] == b[6] == mark2) or (b[1] == b[4] == b[7] == mark2) or (b[2] == b[5] == b[8] == mark2):
        print('Player 2 wins!')
        winner = True
    elif (b[0] == b[4] == b[8] == mark1) or (b[6] == b[4] == b[2] == mark1):
        print('Player 1 wins!')
        winner = True
    elif (b[0] == b[4] == b[8] == mark2) or (b[6] == b[4] == b[2] == mark2):
        print('Player 2 wins!')
        winner = True

# Function that executes after the game has concluded ("winner" or "tie"
# becomes True) which asks the players if they wnat to play again. If players
# say yes, then a new round ensues, and game asks who goes first. If players 
# say no, the program exits.        
def playagain():
    again = None
    while again != 'y':
        again = input('Play again? y/n ')
        if again == 'y':
            global b
            b = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            global count
            count = 0
            global winner
            winner = False
            first = None
            while first == None:
                first = input('Who will go first ({} or {})? Or should the game decide for you (g)? '.format(mark1, mark2))
                if first == '{}'.format(mark1):
                    XFirst()
                elif first == '{}'.format(mark2):
                    OFirst()
                else:
                    first = None
        elif again == 'n':
            print('Okay, bye.')
            sys.exit()
        else:
            again = None   

# Function for Player 1 going first            
def XFirst():
    while winner == False:
        X()
        if tie == True or winner == True:
            break
        O()
        if tie == True or winner == True:
            break     
    if tie == True or winner == True:
        playagain()        

# Function for Player 2 going first            
def OFirst():  
    while winner == False:
        O()
        if tie == True or winner == True:
            break     
        X()
        if tie == True or winner == True:
            break
    if tie == True or winner == True:
        playagain()       

# Game is optimally played with the NUM-PAD on, so game first prompts players
# to activate it.
pad = None
while pad == None:
    pad = input('Is the NUM-PAD activated? y/n ')
    if pad == 'y':
        print('Good!')
        print(' ')
    else:
        pad == None

# Game then displays the rules...        
rules()

# ...then asks the players if they are ready.
ready = None
while ready == None:
    ready = input('Are both players ready? y/n ')
    if ready == 'y':
        print('Good fortunes!')
    else:
        ready = None

# The two players then decide and input their marks. Game allows only a single
# key for a mark, but otherwise it can be any mark; not just the traditional X or O.        
mark1 = None
while mark1 == None:
    mark1 = input('Player 1, choose your mark (single key please!): ')
    if len(mark1) != 1:
        mark1 = None
        print('Single key please!')
    elif mark1 == ' ':
        mark1 = None
        print('Err...space-bar is not a key.')
    else:
        print("Player 1's mark will be {}.".format(mark1))
        
mark2 = None
while mark2 == None:
    mark2 = input('Player 2, choose your mark (single key please!): ')
    if len(mark2) != 1:
        mark2 = None
        print('Single key please!')
    elif mark2 == ' ':
        mark2 = None
        print('Err...space-bar is not a key.')
    elif mark2 == mark1:
        mark2 = None
        print("That's Player 1's mark silly.")
    else:
        print("Player 2's mark will be {}.".format(mark2))



# Game asks which player will go first, or if it should be randomly decided. 
# The outcome decides whether the XFirst() or OFisrt function executes.
first = None
while first == None:
    first = input('Who will go first ({} or {})? Or should the game decide for you (press the space-bar)? '.format(mark1, mark2))
    if first == '{}'.format(mark1):
        XFirst()
    elif first == '{}'.format(mark2):
        OFirst()
    elif first == ' ':
        first = rand.randint(1,2)
        if first == 1:
            print('Player 1 ({}) was chosen at random to go first.'.format(mark1))
            XFirst()
        elif first == 2:
            print('Player 2 ({}) was chosen at random to go first.'.format(mark2))
            OFirst()
    else:
        first = None