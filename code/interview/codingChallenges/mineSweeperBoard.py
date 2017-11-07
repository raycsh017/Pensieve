# /* Given width, height, and numMines, generate and print a Minesweeper board
#  *
#  * e.g.:
#  * > generateBoard(5, 5, 8)
#  
#   * 1 1 * *
#   1 1 1 3 *
#   0 0 0 1 1
#   1 2 2 3 2
#   * 2 * * *
#  
#  */

# // Create a 2D array for the board - initialize it with 0
# // Place the mines on the board - replace 0 with *
# // random function for mines
# // a variable to keep track of how many mines were placed
# // dictionary of mines' coordinates
# // Fill the rest of the board
# // Go through the dictionary of mines' coordinates, increment surrounding elements by 1, only if they are not *

import random

def generateBoard(numRows, numColumns, numMines):
    board = []
    
    for i in range(0, numRows):
        row = []
        for j in range(0, numColumns):
            row.append('0')
        board.append(row)

    mineCoordinates = []
    tempNumMines = numMines
    while tempNumMines > 0:
        randomRow = random.randint(0, numRows - 1)
        randomCol = random.randint(0, numColumns - 1)
        if (randomRow, randomCol) not in mineCoordinates:
            mineCoordinates.append((randomRow, randomCol))
            board[randomRow][randomCol] = '*'
            tempNumMines -= 1
        
    for coord in mineCoordinates:
        row = coord[0]
        col = coord[1]
        
        topLeft = (row - 1, col - 1)
        top = (row - 1, col)
        topRight = (row - 1, col + 1)
        left = (row, col - 1)
        right = (row, col + 1)
        botLeft = (row + 1, col - 1)
        bottom = (row + 1, col)
        botRight = (row + 1, col + 1)
        
        surroundingCoord = [topLeft, top, topRight, left, right, botLeft, bottom, botRight]
        
        for surCoord in surroundingCoord:
            if (surCoord[0] > -1 and surCoord[0] < numRows and surCoord[1] > -1 and surCoord[1] < numColumns) and board[surCoord[0]][surCoord[1]] != '*':
                board[surCoord[0]][surCoord[1]] = str(int(board[surCoord[0]][surCoord[1]]) + 1)
    
    for i in range(0, numRows):
        output = ''
        for j in range(0, numColumns):
            output += board[i][j]
        print(output)
        
# generateBoard(6, 5, 8)