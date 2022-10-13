# Lilia Bodnar
# 09152022
# Lab 1

# imports

# problem 1
print("Problem 1:")
cur_year = 2022
end_of_year_age = 20
birthYear = cur_year - end_of_year_age

print("You were born in the year " + str(birthYear))
print(" ")

# problem 2
print("Problem 2:")

print("Enter your name")
name = input()
print("Nice name, " + str(name) + "!")

print("What's your favourite number?")
num = input()
num = int(num)
cubeRtNum = num ** (1/3)

print("The cube root is " + str(cubeRtNum))
print("Bye!")
print(" ")

# problem 3
print("Problem 2:")
print("How old are you?")
age = input()

print("Has your birthday already occured this year? If it has, enter Y. If it hasn't, enter N")
birthdayStatus = input()

if(birthdayStatus == "Y"):
  guessedBirthYear = int(cur_year) - int(age)

if(birthdayStatus == "N"):
    guessedBirthYear = int(cur_year) - int(age) - 1

print("You were born in " + str(guessedBirthYear) + "!")