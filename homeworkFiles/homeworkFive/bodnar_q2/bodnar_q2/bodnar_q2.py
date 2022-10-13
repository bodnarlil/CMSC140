# create a function that takes in a list and pics out the BIOL courses and prints them
def findBioCourses(courses):
    bio_courses = []

    for course in courses:
        name, number = course.split() # will split along the " "
        number = int(number) # change to an integer
        if(name == "BIOL"):
            bio_courses += [number] # add to new list of bio courses
    print(bio_courses)

major_courses = [
    "BIOL 130", "BIOL 150", "BIOL 280", "PHYS 141",
    "PHYS 151", "GEOL 110", "GEOS 210", "BIOL 650"]
findBioCourses(major_courses)