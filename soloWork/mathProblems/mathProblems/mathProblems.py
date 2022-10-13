import math

def pythTheorem():
    leg = 0; legTwo = 0; hyp = 0

    print("First, enter 'leg' if you are missing a  leg and 'hyp' if you are missing the hypotinuse")
    legOrHyp = input()
    while(str(legOrHyp) != "leg" and str(legOrHyp != "hyp")):
          print("Please enter 'leg' or 'hyp': ")
          legOrHyp = input()
    print("Now, enter the first leg that you know: ")
    leg = input()

    print("now, enter the second number, either the leg or the hypotinuse, that you do know")
    if(str(legOrHyp) == leg): legTwo = input()
    else: hyp = input()
    
    if(int(legTwo) == 0):
        legTwo = math.sqrt(int(hyp)*int(hyp) - int(leg)*int(leg))
        print("your missing leg is ", legTwo)
    else:
        hyp = sqrt(int(leg)*int(leg) + int(legTwo)*int(legTwo))
        print("your missing hypotinuse is ", hyp)

def pacePerLap():
    print("enter you distance in meters: "); distance = input()

    print("enter your goal time in seconds: "); goalTime = input()

    laps = distance / 400
    secondsPerLap = goalTime/laps
    print("You should run each lap in ", secondsPerLap, " to get a goal time of ", goalTime, " for ", distance, " meters. You got this!")

def randNumGen():
    print("This is a random number generator.")

def sqrtFinder():
    print("This finds the square root of your number")

def getCompliment():
    print("This gives you a compliment")

def easyMath():
    print("This does easy math")

def phoneNumGen():
    print("This generates a random phone number")

def licenseGen():
    print("this generated a random license plate number")

def listSaver():
    print("This creates a list and adds and removes stuff as needed")

def numPicker():
    print("this picked a number for you based on your needs")
    print("Enter yes or no to all of the following questions: ")
    print("do you need an even number?")
    print("Does your number need to be a perfect square?")
print("1. Pythagorean Theorem Solver")
print("2. Seconds Per Track Lap Calculator")
print("3. Random Number Generator")
print("4. Square Root Finder")
print("5. Get a compliment!")
print("6. Simple 4 way calculator")
print("7. Random phone number generator")
print("8. License Plate Generater")
print("9. List Saver")
print("10. Number Picker")
print("")
print("Enter the number corresponding with your choice:")
choice = int(input())

if(choice == 1):
    pythTheorem()
elif(choice == 2):
    pacePerLap()
elif(choice == 3):
    randNumGen()
elif(choice == 4):
    sqrtFinder()
elif(choice == 5):
    getCompliment()
elif(choice == 6):
    easyMath()
elif(choice == 7):
    phoneNumGen()
elif(choice == 8):
    licenseGen()
elif(choice == 9):
    listSaver()
elif(choice == 10):
    numPicker()
else:
    print("You did not enter a valid choice.")