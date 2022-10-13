import re

# ask birth year
print("Hi! What year were you born in?")
birthYear = input()

print("")

# ask if they have already had a birthday this year
print("Has your birthday already occured this year?")
yesNoResponse = input()
yesResponseRegex = re.compile(r'(y|Y)("es")?$')
noResponseRegex = re.compile(r'(n|N)("o")?')

print("")

# determine age and print out the response
if re.search(yesResponseRegex, yesNoResponse) and not re.search(noResponseRegex, yesNoResponse):
    age = 2022 - int(birthYear)
    print("You are " + str(age) + " years old")
elif re.search(noResponseRegex, yesNoResponse) and not re.search(yesResponseRegex, yesNoResponse):
    age = 2022 - int(birthYear) - 1
    print("You are " + str(age) + " years old")
else:
    print("unknown error")