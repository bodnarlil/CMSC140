from collections import ChainMap
from concurrent.futures.process import _chain_from_iterable_of_lists

print("collatz program 2.0")
print("")


def longest_collatz(startingNum, finishingNum):
    
    # create variables to hold the chain info and starting numbers
    chain = 0
    longestChain = 0
    currentNum = startingNum
    longestNumChain = 0
    chainLengths = []

    # create a nested while loop that does the appropriate addition, multiplication, or division and 
    # check for the longest number and incriment startingNum as needed
    while (int(startingNum) < int(finishingNum) + 1): # loop through all the numbers whithin the starting and finishing number including both end points
        currentNum = startingNum # use currentNum instead of startingNum
        while(currentNum != 1):
            if(int(currentNum) % 2 == 0):
                chain += 1
                currentNum = int(int(currentNum) / 2)
            else:
                chain += 1
                currentNum = int((int(currentNum) * 3) + 1)

            if(int(longestChain) < chain):
                longestChain = chain
                longestNumChain = startingNum

        # reset the currentChain and move startingNum to the next number between startingNum and finishingNum
        chainLengths.append(chain)
        chain = 0
        startingNum = int(startingNum) + 1

    # print when you are all done and have found the longest chain and the number it was found in
    print("the starting number was " + str(originalStart) + ". finishing number was " + str(originalFinish))
    print("the largest number in our chain was " + str(longestChain))
    print("this is the list of the chain lengths: " + str(chainLengths))
    print("end of the function")
    print("")
    return str(longestNumChain)

# get input from the user and create variables to hold the original start and finish
print("enter the starting number: ")
start = input()
originalStart = start
print("enter the finishing number: ")
stop = input()
originalFinish = stop

print("the longest chain was from the number " + str(longest_collatz(start, stop)))
print("")