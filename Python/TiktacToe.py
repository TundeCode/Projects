import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]
currentPlayer = "X"
winner = None
gameRunning = True

#print a game board
def printBoard(board):
    print(board[0] + " | " + board[1] + "  | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + "  | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + "  | " + board[8])  

#take player input
#asking a player to pick a number 1-9 that corresponding with section of game board
def pplinput(board):
    inp= int(input("Enter a number 1-9: "))
    #first two expressions make the inp a valid number, the third one checks if the position has a dash
    #meaning no player has gone there
    if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
        board[inp - 1] = currentPlayer
    else:
        print("Spot already been taken")

#check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != '-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return True
    
def checkRow(board):
    global winner 
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[2]
        return True
 
def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2]
        return True

def checkTie(board):
    if "-" not in board:
        printBoard(board)
        print("It's a TIE!!")
        global gameRunning
        gameRunning = False


def checkWin():
    if checkDiagonal(board) or checkHorizontal(board) or checkRow(board):
        #F-strings are a faster way to format strings instead of using concatenation
        print(f"The winner is {winner}")
    

#switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "0"
    else:
        currentPlayer = "X"

#computer
def computer(board):
    while currentPlayer == "0":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "0"
            switchPlayer()

#check for win or tie again

while gameRunning:
    printBoard(board)
    pplinput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)
