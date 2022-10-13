# this is how you create a comment
# commmmment
print("# commment")

# this is how you import statements
import math
from pickle import FALSE, TRUE
print("this is how you import something: import math")
print("this is how you import something else: from pickle import FALSE, TRUE")
print(" ")

# this is how you create variables
integer = 1
string = "string"
float = 1.2

print("integer = 1")
print("string = ''string''")
print("float = 1.2")
print("this is an integer: " + str(integer))
print("this is a string: " + string)
print("this is a float: " + str(float))
print(" ")

# reset integer back to an int
print("int(integer)")
int(integer)

# this is how you change variable types
print("str(integer)")
str(integer)
print("this is an int: " + str(integer))
print(" ")

# this is how you print
print("print(''print this out'')")
print("print this out")
wordToAdd = "added"
print("print(''this is how you print with something '' + wordToAdd + ''.'')")
print("this is how you print with something " + wordToAdd + ".")
print(" ")

# this is how you get info from the user
print("enter something random: ")
userInput = input()
print("this is how you get user input: userInput = input()")
print("this is what the user entered into the console: " + str(userInput))
print(" ")

# this is how you do some basic math
x = 1
y = 2
z = 0
print("these are the numbers x, y, and z before x + y = z: " + str(x) + ", " + str(y) + ", " + str(z))
z = x + y
print("these are the numbers x, y, and z after x + y = z: " + str(x) + ", " + str(y) + ", " + str(z))
print(" ")

x = 1
y = 2
z = 0
print("these are the numbers x, y, and z before x - y = z: " + str(x) + ", " + str(y) + ", " + str(z))
z = x - y
print("these are the numbers x, y, and z after  x - y = z: " + str(x) + ", " + str(y) + ", " + str(z))
print(" ")

x = 1
y = 2
z = 0
print("these are the numbers x, y, and z before x * y = z: " + str(x) + ", " + str(y) + ", " + str(z))
z = x * y
print("these are the numbers x, y, and z after x * y = z: " + str(x) + ", " + str(y) + ", " + str(z))
print(" ")

x = 1
y = 2
z = 0
print("these are the numbers x, y, and z before x / y = z: " + str(x) + ", " + str(y) + ", " + str(z))
z = x / y
print("these are the numbers x, y, and z after x / y = z: " + str(x) + ", " + str(y) + ", " + str(z))
print(" ")

# this is how you create a match case
# int = 1
# def int(int):
#    match int:
#        case 1:
#            return 10
#        case 2 | 3:
#            return 25
#        case 4:
#            return 4
#        case _:
#            return 0
# print(" ")


# this is how you create an if-else statement
int = 1
def int(int):
    if int == 1:
        return 10
    elif int == 2 | int == 3:
        return 25
    elif int == 4:
        return 40
    else:
        return 0
print(" ")


# this is how you write a for loop

# num = 3
# for num in num:
#    print(f'It is time to {num}!')
# print(" ")

# this is some random notes
print("integer or floating-point value will always be unequal to a string value.")
print(" ")

# this is how you write a while loop with a break and CREATE AN INFINITE WHILE LOOP
import random
isTrue = FALSE
myNumber = random.randrange(0,10)
print("random number: " + str(myNumber))
print("guess the number between 0 and 10!")

while isTrue == FALSE:
    print("enter another guess: ")
    number = input()
    if(str(number) == str(myNumber)):
        isTrue = TRUE
        break
print("you guessed the number!")
print("thanks for playing!")
print(" ")

# this is how you write boolean stuff
print("boolean stuff")
print("and")
print("T and T: ", True and True)
print("T and F: ", True and False)
print("F and T: ", False and True)
print("F and F", False and False)
print("")

print("or")
print("T or T: ", True or True)
print("T or F: ", True or False)
print("F or T: ", False or True)
print("F or F", False or False)
print("")

print("not")
print("not T: ", not True)
print("not F: ", not False)
print("")

# this is how you get a numebr from a string at position x (starts at 1, NOT 0)
myName = "Lilia"
firstLetter = myName[:1]
print("the first letter of Lilia is " + firstLetter)

# this is how you change to lowercase and uppercase
string = "raNdOMCaSe"
print(string)
print("stringOne = string.lower()")
stringOne = string.lower()
print(stringOne)

print(string)
print("stringTwo = string.upper()")
stringTwo = string.upper()
print(stringTwo)
print("")

# this is how you write a for loop // from textbook
stringTwo = string.upper()
print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')

# this is how you print out the total of 0-100 // from textbook
total = 0
for num in range(101):
    total = total + num
print(total)  