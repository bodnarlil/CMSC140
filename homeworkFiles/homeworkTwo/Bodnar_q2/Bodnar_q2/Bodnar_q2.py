# get the user's input
print("Enter a number to start at: ")
startingNum = input()
print("Enter a number to count down by: ")
endingNum = input()

# print out the starting number
print("")
print("Countdown: ")
print(str(startingNum))

# use the while loop to get as close to zero as possible without passing it
#while (int(startingNum) > 0):
#    startingNum = int(startingNum) - int(endingNum)
#    if(startingNum > 0):
#        print(str(startingNum))

for _ in range(int(startingNum), 0, -1*int(endingNum)):
    startingNum = int(startingNum) - int(endingNum)
    if(int(startingNum) < 0):
        break
    print(str(startingNum))