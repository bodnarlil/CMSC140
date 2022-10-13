# create the function for the countdown
def countdownFunction(startingNum, countdownNum):
    print("")
    print(startingNum)
    while(startingNum - countdownNum >= 0):
        startingNum -= countdownNum
        print(startingNum)
    return startingNum

# ask user for input
print("This is a countdown function!")
print("Enter starting number: ")
numOne = input()
numOne = int(numOne)
print("Enter a number to count down by: ")
numTwo = input()
numTwo = int(numTwo)
    
# print out the results
print("Your countdown has reached " + str(countdownFunction(numOne, numTwo)))
print("")