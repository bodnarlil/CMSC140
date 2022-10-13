#create dictionaries for each class
cs = {
    "class":"Intro to Python Programming",
    "prof":"Professor Ackles",
    "units":"6",
    "time":["M 950-1100", "W 950-1100", "R 1025-1210"]
    }
span = {
    "class":"Latin American Visual Arts",
    "prof":"Professor ",
    "units":"6",
    "time":["M 1350-1500", "W 1350-1500", "R 1350-1500"]
    }
math = {
    "class":"Multivariable Calculus",
    "prof":"Profesor Heaton",
    "units":"6",
    "time":["M 1510-1620", "W 1510-1620", "R 1510-1620"]
    }

# create a main map
schedule = {
    "CMSC 140": cs,
    "SPAN 425": span,
    "MATH 155": math
    }

# loop and print for each class
for item, schedule in schedule.items():
    print("Course Code: ", item)
    print(" Course Name: ", schedule["class"])
    print(" Professor: ", schedule["prof"])
    print(" Units: ", schedule["units"])
    print(" Meeting Times: ")
    print("", schedule["time"][0])
    print("", schedule["time"][1])
    print("", schedule["time"][2])

    print("")
    print("---")
    print("")