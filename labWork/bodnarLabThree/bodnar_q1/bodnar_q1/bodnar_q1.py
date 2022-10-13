# create the function
def sumFunction(numOne, numTwo):
    total = 0
    for i in range(numOne, numTwo + 1):
        total += i
    return total

# ask user for input
print("Enter two numbers to find the sum of all the numbers together: ")
numTwo = input()
numOne = input()

# print out results
print("the sum is " + str(sumFunction(10,15)))