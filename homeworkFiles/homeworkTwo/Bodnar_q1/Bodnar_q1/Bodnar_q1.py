# use the while loop to loop through 1000 times and print a number each time
print("Count to 1000 with while loop")
count = 1
total = 0;

while (count < 1001):
    total += count
    count += 1
print("total: " + str(total))
print("")

# use a for loop to loop through 1000 times and print out a number each time
print("Count to 1000 with for loop")
printedNum = 1
secondTotal = 0
for _ in range(1000):
    secondTotal += printedNum
    printedNum += 1
print("secondTotal: " + str(secondTotal))