# Python Class 3080
# Lesson 12 Problem 1
# Author: MC42 (697130)

# This list labels the columns 
labels = [str(numLabel) for numLabel in range(1, 8)] 

# This is the list for the grid
gridList = [ [ '-' for space in range(7) ] for setupRow in range(6)] 

while True: # Repeat until broken:
    playerOneSymbol = \
    input('Hello player one, would you like to be x or o? ').upper()
    
    # Check if the user entered it properly
    if playerOneSymbol != 'X' and playerOneSymbol != 'O':
        print('Please enter x or o!')
    else:
        break

# Set player two's symbol to be the opposite of player one's
if playerOneSymbol == 'X':
    playerTwoSymbol = 'O'
else:
    playerTwoSymbol = 'X'

print('Player two, you are ' + playerTwoSymbol + '.')
    
# Keep track of how many tokens are left
playerOneCount = 21
playerTwoCount = 21

# Set the current player to player one
currentPlayer = 'Player one'
currentPlayerToken = playerOneSymbol

# Functions for the game:

# Determine if a cell is occupied
def is_occupied(cell):
    '''is_occupied(element) -> bool
    determines if a slot is taken.'''
    if cell != '-':
        return True
    else:
        return False

    
# Function for playing in a space
def player_move():
    '''player_move() -> str
    plays a token in the desired column'''
    filledSpaces = 0
  
    # Take the desired column number
    while True:
        column = input(currentPlayer + 
        ', what column would you like to play in? ')
      
        # Check if the user entered a number
        if column.isnumeric() == False:
            print('Enter a number from 1 to 7!')
        else:
            # Check if the user entered a wrong number:
            if int(column)-1 not in range(7):
                print('Enter a number from 1 to 7!')
            else:
                # If they entered it right, proceed
                column = int(column)-1
                break
          
    # Check if the bottom space is empty or not
    for height in range(5, -1, -1):
        # If it is empty, continue
        if is_occupied(gridList[height][column]) == False:
            break
        else:
            # If not, increase filledSPaces by one & repeat
            filledSpaces += 1
          
    # Check if the column is full
    while True:
        if filledSpaces == 6: # If it is full,
            print('This column is full!')
            return player_move() # Run the function again
        else: # If not,replace the empty slot with the token  
            gridList[height][column] = currentPlayerToken 
            break
            
    print_grid()
    

# Check if anyone has won horizontally
def is_winner_horizontal():
    '''is_winner_horizontal() -> bool
    determines if someone has won the game horizontally'''
    for winRow in range(6):
        for winColumn in range(4):
            if gridList[winRow][winColumn] == \
            gridList[winRow][winColumn+1] == \
            gridList[winRow][winColumn+2] == \
            gridList[winRow][winColumn+3] != '-':
                return True

# Check if anyone has won vertically
def is_winner_vertical():
    '''is_winner_vertical() -> bool
    determines if someone has won the game vertically'''              
    for winRow in range(3):
        for winColumn in range(6):
            if gridList[winRow][winColumn] == \
            gridList[winRow+1][winColumn] == \
            gridList[winRow+2][winColumn] == \
            gridList[winRow+3][winColumn] != '-':
                return True

# Check if anyone has won diagonally (right-facing)
def is_winner_diag_right():
    '''is_winner_vertical() -> bool
    determines if someone has won the game diagonally to the right''' 
    for winRow in range(3):
        for winColumn in range(4):
            if gridList[winRow][winColumn] == \
            gridList[winRow+1][winColumn+1] == \
            gridList[winRow+2][winColumn+2] == \
            gridList[winRow+3][winColumn+3] != '-':
                return True

# Check if anyone has won diagonally (left-facing)
def is_winner_diag_left():
    '''is_winner_vertical() -> bool
    determines if someone has won the game diagonally to the left'''
    for winRow in range(3):
        for winColumn in range(3, 7):
            if gridList[winRow][winColumn] == \
            gridList[winRow+1][winColumn-1] == \
            gridList[winRow+2][winColumn-2] == \
            gridList[winRow+3][winColumn-3] != '-':
                return True

# Check all the functions for any kind of winner
def find_winner():
  '''find_winner() -> bool
  Checks all possibilities to find a winner'''
  if is_winner_horizontal() == True or \
      is_winner_vertical() == True or \
      is_winner_diag_left() == True or \
      is_winner_diag_right() == True:
          return True

    
# Function for printing the grid
def print_grid():
    '''print_grid() -> str
    prints the board'''
    print("   ".join(labels))
    for rowList in gridList:
        print("   ".join(rowList))

                
# Print the grid
print_grid()

# Play the game
while True:    
    
    # Player one's move
    player_move()
    playerOneCount -= 1
    
    # Check if player one has won
    if find_winner() == True:
        print(currentPlayer + ', you are the winner!')
        break
        
    # Check if both players have run out of tokens
    if playerOneCount == 0 and playerTwoCount == 0:
        print("Both players have run out of tokens, it's a tie!")
        break

        
    # Set the current player to player two
    currentPlayer = 'Player two'
    currentPlayerToken = playerTwoSymbol

    # Repeat the process for player two
    player_move()
    playerTwoCount -= 1
    
    if find_winner() == True:
        print(currentPlayer + ', you are the winner!')
        break
        
    if playerOneCount == 0 and playerTwoCount == 0:
        print("Both players have run out of tokens, it's a tie!")
        break

    # Reset the current player for the next iteration
    currentPlayer = 'Player one'
    currentPlayerToken = playerOneSymbol
