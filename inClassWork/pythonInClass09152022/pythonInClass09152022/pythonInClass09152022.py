#Lilia Bodnar
# 09152022
# In class work

# imports
import math

# test stuff
integer = 1;
float = 3.2;
string = "lawrence";

print("this is a string: " + string);
print("this is a float: " + str(float));
print("this is an int: " + str(integer));

# pythag. theory -> a^2 + b^2 = c^2
print("Welcome to the Pythagorean Theorem Solver!");
print("Please enter the numbers of the two legs and the hypotinuse in the problem you are trying to solve.");
print("For the missing number, just enter 0.");

# get the user's numbers
print("Leg one: ");
legOne = input();

print("Leg two: ");
legTwo = input();

print("Hypotinuse: ");
hypot = input();

# execute this if you are solving for the hypotinuse
if(hypot == 0):
    hypot = math.sqrt((legOne*legOne) + (legTwo*legTwo))
    print("The hypotinuse is " + str(hypot))

# execute this if you are solving for legOne
if (legOne == 0):
    legOne = math.sqrt((hypot*hypot) - (legTwo*legTwo))
    print("The missing leg is: " + str(legOne)

# execute this if you are solving for legTwo
if (legTwo == 0):
    legTwo = math.sqrt((hypot*hypot) - (legOne*legOne))
    print("The missing leg is: " + str(legTwo)

# execture this if you are not missing any numbers
if(legTwo != 0 && legOne != 0 && hypot != 0):
    print("You have all three numbers already! Your numbers were: " + str(legOne) + " " + str(legTwo) + " " + str(hypot))
