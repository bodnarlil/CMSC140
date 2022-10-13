emails = ['erik.j.justen@lawrence.edu',
         'jason.vandenberg@lawrence.edu',
         'brianna.bernard@lawrence.edu',
         'rebkb@lawr.edu',
         'lilia.z.bodnar@lawrence.edu',
         'elizabelth.k.sattler@lawrenc.edu']

# test case 1 (split)
for email in emails:
    e = email.split('@')
    print(e)
    if(e[1] == 'lawrence.edu'):
        print(email, " is valid")
print("")

# test case 2 (if in)
for email in emails:
    if '@lawrence.edu' in email:
        print(email, " is valid")
print("")

# test case 3 (endswith)
for email in emails:
    if email.endswith('@lawrence.edu'):
        print(email, " is valid")
print("")

# in class 1
def isValidFile(file):
    if(file.endswith('.py') or file.endswith('.pdf')):
        return True
    else:
        return False

print(isValidFile("q1.py"))
print(isValidFile("hwk.pdf"))
print(isValidFile("py.pdf"))
print(isValidFile("q1.cpp"))
print(isValidFile("hwk.pdf.txt"))
print(isValidFile("py.txt"))
print("")

# conditions

def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

def isEven(num):
    return not num % 2

def newFunction(condition):
    return not condition

# regular expressions
import re

# letters only . letters only . letters only

emailRegex = re.compile(r'[a-z]+\.([a-z].)[a-z]+@lawrence.edu$')
for email in emails:
    if re.search(emailRegex, email):
        print(f"{email} is a valid address.")

print("")

# in class 2
def isValidFileRegex(file):
    regex = re.compile(r'[A-Za-z0-9]+\.(py|pdf)')
    return re.search(regex, file)