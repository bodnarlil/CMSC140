# function compares each item at i and adds the index to a list if it is not equal
def takeTwo(listOne, listTwo): # assuming the lengths of the lists are equal
    diffList = []
    for i in range (0, len(a)):
        if(listOne[i] != listTwo[i]):
            diffList += [i]
    return diffList

# create the two lists from the instructions
a = [0, 1, 2, 3, 4, 5, 6, 7, 7, 9, 10, 11, 12, 13, 14, 16, 15, 17, 18, 18]
b = list(range(20))

differences = takeTwo(a, b)
print("the differences are at " + str(differences))
print("")