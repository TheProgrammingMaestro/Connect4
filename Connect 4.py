#player = 0 = empty,  1 = player1, 2 = player2
#Row and column = player input
def getInput(player, board):
    valid = False 
    while not valid:
        column = int(input("Enter a column #   (eg. 4):  "))
        column -= 1
        valid = True
        if column not in range(0, len(board[0])):
            valid = False
        elif board[0][column] != 0:
            print("Pick a different column")
            valid = False
    return column

def row_finder(column, board):
    row = 4
    for i in range(0,5):
        if board[row][column] == 0:
            return row
        else:
            row -= 1
    
def checker(player, row1, column1, board, connect_four):
    row = row1
    column = column1
    #row
    counter = 0
    for i in range(0, len(board)):
        if board[row][i] == player:
            counter += 1
        else:
            counter = 0
        if counter == 4:
            return True
            
    
    #column
    counter = 0
    for i in range(0, len(board)):
        if board[i][column] == player:
            counter += 1
        else:
            counter = 0
        if counter == 4:
            return True
    #back diagonal
    counter = 0
    while len(board[row]) >= 0 and column >= 0:
        row -= 1
        column -= 1
    row += 1
    column += 1
 
    while row < len(board) and column < len(board[0]):
        if board[row][column] == player:
            counter += 1
        else:
            counter = 0
        if counter == 4:
            return True
        row += 1
        column += 1
        
    #forward diagonal
    row = row1
    column = column1
    counter = 0
    while row >= 0 and column < len(board[row]):
        row -= 1
        column += 1
    row += 1
    column -= 1
 
    while row < len(board) and column >= 0:
        if board[row][column] == player:
            counter += 1
        else:
            counter = 0
        if counter == 4:
            return True
        row += 1
        column -= 1
        
    return False

def boardChange(column, current_player, board):
    row = 4
    while board[row][column] != 0:
        row -= 1
    board[row][column] = current_player
    return row
#Make table
def display(board):
    
    row1 = """+---+---+---+---+---+---+---+----------+---
    | {}  | {}  | {}  | {}  | {}  | {}  | {}  |
+--------------------------------------+---"""
    for i in range(0,5):
        print(row1.format(*board[i]))

board = [
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0]
]
player1 = "O"
player2 = "X"
connect_four1 = "OOOO"
connect_four2 = "XXXX"
current_player = player1
current_four = connect_four1
checker2 = False
while not checker2:
    #Display
    display(board)
    #Get input
    column = getInput(current_player, board)

    #Change table
    row = boardChange(column, current_player, board)

    #Check if four in a row
    checker2 = checker(current_player, row, column, board, current_four)
    # If four in a row show who won
    if checker2:
        if current_player == player1:
            print("Player 1 wins!")
            
        else:
            print("Player 2 wins!")
        display(board)
    #Change player
    if current_player == player1:
        current_player = player2
        current_four = connect_four2
    else:
        current_player = player1
