# import statements
import random

print("This is a random number guesser!");

# get a number from the user and cast it as a string
print("Please enter a number between 1 and 100");
userGuess = input()
print("")

# generate a random number
generatedNum = random.randint(1,100)

while(userGuess != generatedNum):
    if(int(userGuess) > int(generatedNum)):
        print("Your guess is too high")
        print("")
    elif(int(userGuess) < int(generatedNum)):
        print("your guess is too low")
        print("")
    else:
        break
    userGuess = input();

print("Good job! You guessed the number! ")
print("Your number was " + str(userGuess) + " and my number was " + str(generatedNum))