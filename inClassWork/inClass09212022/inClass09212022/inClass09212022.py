# Lilia Bodnar
# CMSC 140
# 09212022

# have the user decide how many times to execte the while loop
from ast import Num
from collections import Counter
from lib2to3.pgen2.token import NUMBER
import numbers

print("test exercise: ")
print("how many times do you want to run the while loop?")
repeatTime = input()
repeatTime = int(repeatTime)
timesThrough = 1
while(repeatTime + 1 > timesThrough):
    if(timesThrough == 1):
         print("hello, you have run this while loop " + str(timesThrough) + " time")
    else:
        print("hello, you have run this while loop " + str(timesThrough) + " times")
    timesThrough = timesThrough + 1
print("")

# new while loop
print("exercise 1: ")
print("how many times do you want to execute the loop?")
counter = 0
num = input()
num = int(num)

while (num > 1):
    num = num // 2 # divide in half and take the int version
    print("num is " + str(num))
    counter += 1
print("it took " + str(counter) + " times")
print("")

# exercise 2
print("exercise 2: ")
count = 0
while (count < 1001):
    print("counter = " + str(count))
    count += 2
print("")

# exercise 2.2
print("exercise 2.2: ")
printedNum = 0
for _ in range(501):
    print("counter = " + str(printedNum))
    printedNum += 2
print("")

# start homework 2
print("homework 2: ")

# cd folderYouWantToGoTo