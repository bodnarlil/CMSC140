# Lilia Bodnar
# Professor Ackles
# Final Project: WORDLE Game
# CMSC 140

# tasks:
# print out instructions
# function that runs the wordle game itself
#   select the random word
#   write the loop that asks for guesses
#   print out/determine results
# function that asks if they want to play again
#   call the wordle game function if they enter yes to play again, else terminate




from random import random


def wordleGame():
    numGuesses = 0
    guessesLeft = 0
    guessLevel = 0
    randomWord = ""
    userGuess = ""
    guessResults = ""

    print("Welcome to our Wordle game! Try and find the five letter word before running out of guesses.")
    print("")
    print("Levels: ")
    print("1: Easy (8 guesses)")
    print("2: Medium (6 guesses)")
    print("3: Hard (4 guesses)")
    print("")
    print("Enter the number corresponding with the number of guesses you would like: ")
    guessLevel = input()
    while(int(guessLevel) != 1 and int(guessLevel) != 2 and int(guessLevel) != 3):
        print("That was not a valid level. Please try again: ")
        guessLevel = input()
    if(int(guessLevel) == 1):
        numGuesses = 8
        guessesLeft = 8
    elif(int(guessLevel) == 2):
        numGuesses = 6
        guessesLeft = 6
    else:
        numGuesses = 4
        guessesLeft = 4

    # import doc from Prof G and generate a random word from there
    # learned how to import a file from https://datagy.io/python-read-text-file/ and https://www.geeksforgeeks.org/reading-writing-text-files-python/
    # Permission was acquired from Professor Gregg on 10092022 via email
    wordleFile = open("wordle.txt","r")
    print(wordleFile)
        #wordleList = wordleFile.readlines()
        #wordleList = [item.rstrip() for item in wordleList]
        #randomWord = wordleList[randint(0,len(wordleList))]
    #randomWord = randomWord.upper()
    #print("DELETE AFTER TEST CASES; random word is ", randomWord)

    # use for testing
    randomWord = "PLANK"

    for i in (0, numGuesses-1):
        print("You have ", guessesLeft, " guesses left.")
        print("Enter your guess: ")
        userGuess = input()
        userGuess = userGuess.upper()
        for i in (0, len(userGuess)-1):
            if(userGuess[i-1] == randomWord[i-1]):
                guessResults[i-1] = userGuess[i-1]
            else:
                guessResults[i-1] = "-"
        print("Your guess results: ", guessResults)
        guessesLeft -= 1
    
wordleGame()