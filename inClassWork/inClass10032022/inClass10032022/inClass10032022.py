# Lilia Bodnar
# CMSC 140
# Week 4, Day 1
# Notes; Lists

# the main difference from other programming languages is that List in Python can hold other lists 
# and they also do not need to be of the same type (e.g. strings can be in the same list as ints)

print("Hey Adam! I hope your test went well! Here are the notes from class on Monday.")
print("Let me know if you need anything else! :)")
print("")

print("# IMPORT STATEMENTS")
import random as rand # shorten call name when you use random. Use rand instead now
import math

rand.seed(2) # normally chooses num by your time; by changing seed you get the same num
def randIntGenerator():
    a = rand.randint(0,5) # generate random num in [0, 1, 2, 3, 4, 5]
    print("random number: ")
for i in (0, 5):
    print(randIntGenerator())
print("")

b = math.ceil(2) # finds smallest int larger than input
print("ceiling of 1 and 2: " + str(b))
print("")

pi = math.pi
print("pi: " + str(pi))
print("")

print(".............................................................................")
print("")

print("# LISTS")
print("create a list with nothing in it: ")
firstList = []
print(firstList)
print("")

print("create a list with two ints, 1 and 2: ")
myList = [1, 2]
print(myList)
print("")

print("add a String 'Hello' to myList: ")
myList += ["Hello"]
print(myList)
print("")

print("add the word import letter by letter: ")
myList += "import"
print(myList)
print("")

print("the first index is 0. To find the first item, go to index 0")
print("myList index 0 should output 1")
print(myList[0])
print("")

print("you can use negative numbers and use them to iterate from the end.")
print("myList at intex -1 should be output 't'")
print(myList[-1])
print("")

print("you can splinch lists, too")
myList = myList[1:4]
print("myList splinched at 1, 4. It includes the stuff at indexes 1, 2, and 3 but NOT 4")
print(myList)
print("")

print("# you can add Lists together")
listOne = "hi", "list", True
print("create a list a: ")
print(listOne)

listTwo = "red", 3, 22.22
print("create a list b: ")
print(listTwo)
print("")

print("# add the lists together")
finalList = listOne + listTwo
print(finalList)
print("")

print("# print every item in the list")
for item in finalList:
    print(item)
print("")

print("# loop through and do stuff to each item in the list")
nums = [1, 2, 3, 4, 5]
for i in nums:
    print("square of ", i,  " is ", i**2)
print("")

print("# in class #3")
# create a list to hold the first set of ints
listOfInts = []

# fill the first list with 20 random ints
for i in range (20):
    listOfInts += [rand.randint(0, 101)]
print(listOfInts)

# create a new list
newList = []

# go through every int in teh first list and find the square root and add it to the new list
for i in range (len(listOfInts)):
    newList += [math.sqrt(listOfInts[i])]
print(newList)