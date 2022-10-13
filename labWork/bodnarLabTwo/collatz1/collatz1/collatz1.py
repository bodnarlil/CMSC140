print("collatz program")
print("")

# create a variable to hold the length of the chain
def collatz(startingNum):
    chain = 0

    while(startingNum != 1):
        if(int(startingNum) % 2 == 0):
            chain += 1
            print("divide " + str(startingNum) + " by two: ")
            startingNum = int(int(startingNum) / 2)
            print("new number: " + str(startingNum))
            print("")
        else:
            chain += 1
            print("multiply " + str(startingNum) + " by 3 and add 1: ")
            startingNum = int((int(startingNum) * 3) + 1)
            print("")
    return "we got to 1 in " + str(chain) + " steps!"

# get input from the user
print("enter the starting number: ")
userNum = input()
print(collatz(userNum))