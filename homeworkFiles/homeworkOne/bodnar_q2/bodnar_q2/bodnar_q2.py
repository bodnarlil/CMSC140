# Lilia Bodnar
# 09142022
# Homework 1

# import statements
import random;

print("This is a random number guesser!");
print("Please enter a number between 1 and 10");

# get a number from the user and cast it as a string
userGuess = input();
userGuess = str(userGuess);

# generate a random number and cast it as a string
generatedNum = random.randint(1,10);
generatedNum = str(generatedNum);

# reply to the user
print("Your number was " + userGuess + " and my number was " + generatedNum + ". Did you guess it?");