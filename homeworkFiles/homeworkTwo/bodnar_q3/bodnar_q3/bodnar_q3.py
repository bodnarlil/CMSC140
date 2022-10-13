# ask birth year
print("Hi! What year were you born in?")
birthYear = input()

print("")

# ask if they have already had a birthday this year
print("Has your birthday already occured this year?")
yesNoResponse = input()

print("")

# determine age and print out the response
if(yesNoResponse == "y" or yesNoResponse == "yes" or yesNoResponse == "Y" or yesNoResponse == "Yes"):
    age = 2022 - int(birthYear)
    print("You are " + str(age) + " years old")
elif(yesNoResponse == "n" or yesNoResponse == "no" or yesNoResponse == "N" or yesNoResponse == "No"):
    age = 2022 - int(birthYear) - 1
    print("You are " + str(age) + " years old")
else:
    print("input invalid")