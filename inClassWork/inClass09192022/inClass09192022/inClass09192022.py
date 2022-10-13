# problem number one
numberOne = 18 < 81
print("1: " + str(numberOne))

numberTwo = 0 != 3 | 9 != 2
print("2: " + str(numberTwo))

numberThree = 21 >= 21 and 21 == 23
print("3: " + str(numberThree))
print("")
print("")

# problem number two
print("enter your name")
userInputName = input()
myName = "Lilia"
userInputNameStr = str(userInputName)

# change them to lowercase so they will evaluate properly
userInputNameStr = str.lower(userInputNameStr)
myName = str.lower(myName)

print("my name: " + myName)
print("your name: " + userInputNameStr)
print("")

# compare the names
if(userInputNameStr == myName):
    print("we have the same name!")
elif(myName[:1] == userInputNameStr[:1]):
    print("our names start with the same letter")
elif(myName[:1] < userInputNameStr[:1]):
    print("your name comes after mine in the alphabet")
# elif(userInputNameStr[:1] == "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9"):
#     print("your name starts with a number?!")
elif(myName[:1] > userInputNameStr[:1]):
    print("your name comes before mine in the alphabet")
else:
    print("error")
print("")