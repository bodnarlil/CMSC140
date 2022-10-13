# Lilia Bodnar
# Lab 4
# 10062022
# not in attendance

# create a board
board = {
    "A": [".",".","."],
    "B": [".",".","."],
    "C": [".",".","."],
    }

# Credit: Prof. Acacia Ackles
def print_board(board):
    print("     A    B    C")
    for i in range(len(board.values())):
        print(str(i+1) + "    " + board["A"][i] + "    " +  board["B"][i] + "    " + board["C"][i])
    print("")
    # added the following two lines to print_board(board)
    print("---")
    print("")

# Function to get user input
def play_battleship(board):
    print("Welcome to Battleship!")
    print("")

    # take player 1 location for their ship, making sure it is in bounds
    print("Player 1, select a column for your battleship: ")
    column = input()
    column = column.upper()
    while((column != "A" and column != "B") and column != "C"):
        print("Invalid. Try another column: ")
        column = input()
        column = column.upper()
    print("Player 1, select a row for your battleship: ")
    row = input()
    while((row != "1" and row != "2") and row != "3"):
        print("Invalid. Try another row: ")
        row = input()

    # print current board
    print("")
    print("Current Board: ")
    print("")
    print_board(board)

    # take player 2's first guess, making sure it is in bounds
    print("Player 2, select a column to check: ")
    guessColumn = input()
    guessColumn = guessColumn.upper()
    while((guessColumn != "A" and guessColumn != "B") and guessColumn != "C"):
        print("Invalid. Try another column: ")
        guessColumn = input()
        guessColumn = guessColumn.upper()
    print("Player 2, select a row to check: ")
    guessRow = input()
    while((guessRow != "1" and guessRow != "2") and guessRow != "3"):
        print("Invalid. Try another row: ")
        guessRow = input()

    # set score to 1
    score = 1

    # keeps executing while if player two was wrong
    while(guessColumn != column or guessRow != row):
        board[guessColumn][int(guessRow) - 1] = "x"
        print("")
        print("Sorry, nothing there.")
        print("Current score: ", score)
        print("")
        print_board(board)
        score += 1

        print("Player 2, select another column to check: ")
        guessColumn = input()
        guessColumn = guessColumn.upper()
        while((guessColumn != "A" and guessColumn != "B") and guessColumn != "C"):
            print("Invalid. Try another column: ")
            guessColumn = input()
            guessColumn = guessColumn.upper()
        print("Player 2, select another row to check: ")
        guessRow = input()
        while((guessRow != "1" and guessRow != "2") and guessRow != "3"):
            print("Invalid. Try another row: ")
            guessRow = input()
        print("")

        if(board[guessColumn][int(guessRow) - 1] == "x"):
            print("You already guessed this coordinate!")
            score -= 1

    # the following three lines will execute when they choose the right coordinate
    board[column][int(row) - 1] = "!"
    print("You won!")
    print("Final Score: ", score)
    print_board(board)
    print("")

# play the game
play_battleship(board)