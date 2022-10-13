# escape characters

#ex_string = 'this won't work
ex_string = "this wil' work"
ex_string_two = 'this will" work'
print(ex_string)
print(ex_string_two)

esc_double = "this is \"fine\" now" # use \" and \'
esc_single = "this is \\ ok as well" # print \
print(esc_double)
print(esc_single)

# raw string does not worry about ", ', \, etc.
rawstring = r'This prints \' exactly \" what I type.'
print(rawstring)

print("hello")
print("this is on a new line")

trip_quote = """string on multiple
lines"""
print(trip_quote)

new_line = "this is a string with \n a new line"
print(new_line)

print("")
""" comment that
is multiple
lines long
"""

print("Here's a string for you!\nThis \\n is a newline command\nthat didn't actually do anything.")

# string slicing and indexing (just like lists, using [])
print("")

name = "Lilia Z Bodnar"
print(name[0])
print(name[0:6])
print(name)
firstName = name[0:4]
print(firstName)
# cannot change just one character in a string or append stuff; you have to create a whole new character

print(firstName in name, " should be true because firstName is in name")
print("j" in firstName, " should be false because j is not in firstName")
# can use these in if statements

splitName = name.split()
print(splitName) # splits into a list on whitespace automatically
first, middle, last = name.split()

print(first)
print(middle)
print(last)

print(splitName[0]) # prints out whatever is stored at 0 in the splitName list
name.split('a') # will split on a and not include it

print("")

my_list = ["hello", "python", "class"]
noSpace = "".join(my_list)
space = " ".join(my_list)
print(space)
print(noSpace)

print("")
# exercise, goal: replace spaces with - and keep \
string = r"C:\MyDocuments\Classes\Intro to Python\Week 5"; splitString = string.split()
postString = "-".join(splitString)
print("postString: ", postString)

print("")

print(".".join("There are not spaces anymore".split()))

print("")

num = 3
fruit = "apples"

print("I have " + str(num) + " " + fruit + ".")
print("I have %s %s." % (num, fruit))
print("I have", num, fruit + ".")
print(f"I have {num} {fruit}.")

print("")

space_string = "      hweodnoc       "
left = space_string.lstrip()
right = space_string.rstrip()
both = space_string.strip()

print(space_string)
print(left)
print(right)
print(both)