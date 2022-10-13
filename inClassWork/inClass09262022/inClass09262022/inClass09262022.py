# functions to reuse code over and over again

def sayHello(name):
    print("hey," + name)
sayHello("stranger")
sayHello("person")
sayHello("you")

print("")

namelength = len("Lilia")
print(namelength)
print(len("Lilia"))

print("")

counter = 1
for i in range(1, 11):
    print("hello " + str(counter))
    counter += 1

print("")

def ourFirstFunction():
    print("this is a function")
    a = 7 + 2
    print("a: " + str(a))
ourFirstFunction()
ourFirstFunction()
ourFirstFunction()

print("")

def excitedPrint(myString):
    return myString + "!!!"
print("enter something")
something = "red" #optional so you can delete the next lime
# something = input()
this = excitedPrint(something)
print(this)

print("")
def powers(numOne, numTwo):
    return int(int(numOne) ** int(numTwo))
print("enter a number")
first = input()
print("enter another number")
second = input()
print(str(first) + " raised to the power of " + str(second) + " is " + str(powers(first, second)))

print("")

def untilOne(number):
    counter = 0
    while(int(number) > 1):
        counter += 1
        number = int(int(number) / 2)
    return counter

print("enter a number: ")
num = input()
print("It took " + str(untilOne(num)) + " steps to get to 1 from " + str(num))