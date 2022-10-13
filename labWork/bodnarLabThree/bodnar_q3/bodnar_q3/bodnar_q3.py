# create the function for the sum
def sumFunction(firstNum, secondNum):
    total = 0
    for i in range(firstNum, secondNum + 1):
        total += i
    return total

# create the function for the countdown
def countdownFunction(startingNum, countdownNum):
    print(startingNum)
    while(startingNum - countdownNum >= 0):
        startingNum -= countdownNum
        print(startingNum)
    return startingNum

# Ask user for their choice between sum or countdown
print("(1) Sum program")
print("(2) Countdown program")
print("Enter the number corresponding to your choice:")
userChoice = input();
userChoice = int(userChoice)
print("")

# determine which program to run based on input
if(userChoice == int(1)):
    print("Enter starting number: ")
    numOne = input()
    numOne = int(numOne)
    print("Enter ending number: ")
    numTwo = input()
    numTwo = int(numTwo)

    # print out results
    print("the sum is " + str(sumFunction(numOne,numTwo)))
    print("")
elif(userChoice == int(2)):
    # ask user for input
    print("Enter starting number: ")
    numOne = input()
    numOne = int(numOne)
    print("Enter a number to count down by: ")
    numTwo = input()
    numTwo = int(numTwo)
    
    # print out the results
    print("")
    print("Your countdown has reached " + str(countdownFunction(numOne, numTwo)))
    print("")
else:
    print("You didn't choose a valid option")
    print("")