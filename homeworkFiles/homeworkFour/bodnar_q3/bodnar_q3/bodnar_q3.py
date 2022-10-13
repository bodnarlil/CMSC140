# import statements
import random

# function to find average
def findAverage(totalGuessesList, guessesTakenInt):
    sum = 0
    average = 0
    for i in totalGuessesList:
        sum += int(i)
    average = sum/guessesTakenInt
    return average

# function random_number_guesser
def random_number_guesser(guesses):

    # generate a random number
    generatedNum = random.randint(1,100)

    # list to store guesses
    guessList = []
    sumOfGuesses = 0;
    average = 0
    guessesTaken = 0;

    # this loops through the number of times of guesses you have. Tells you if you
    # got the number right or whether your guess was too low or high
    for i in guesses:
        userGuess = -1

        while(int(guesses) != 0):
            print("You have " + str(guesses) + " guesses left.")
            print("Enter your guess: ");
            userGuess = input()
            guessList += [userGuess]
            guessesTaken += 1

            if(int(userGuess) > int(generatedNum)):
                print("Your guess is too high")
                print("")
            elif(int(userGuess) < int(generatedNum)):
                print("Your guess is too low")
                print("")
            elif(int(userGuess) == int(generatedNum)):
                print("")
                print("Good job! You guessed the number!")
                average = findAverage(guessList, guessesTaken)
                print(average, " was your average guess number")
                return ("Your number was " + str(userGuess) + " and my number was " + str(generatedNum))
            else:
                break

            guesses = int(guesses) - 1

        # only executes this if you ran out of guesses
        print("You did not guess the number.")
        average = findAverage(guessList, guessesTaken)
        print(average, " was your average guess number")
        return ("You ran out of guesses. The number was " + str(generatedNum))

# ask the user how many guesses they want
print("This is a random number guesser! Guess the number between 1 and 100");
print("")

# ask how many guesses the user would like to have
print("How many guesses do you want?")
numGuesses = input()
print("")

# run the random_number_guesser method with the user's input passed in as a parameter
print(random_number_guesser(numGuesses))
print("")