def alt_case(inputString):
    newString = ""
    upDown = 0 # used to determine if the character should be uppercase or lowercase
    for i in range (0,len(inputString)): # loop through all of the characters in the string
        if (inputString[i].isalpha() == False): # check to see if it is not a letter
            newString += inputString[i]
        elif(upDown%2 == 1):
            newString += inputString[i].lower()
            upDown+=1
        else:
            newString += inputString[i].upper()
            upDown+=1
    print(newString)

alt_case("Hello class!!")