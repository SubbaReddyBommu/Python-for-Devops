import sys

type = sys.argv[1]

if type == "basic":
    print("this will charge 2$")
elif type == "medium":
    print("this will charge 4$")
elif type == "large":
    print("this will charge 10$")
else:
    print("please enter a valid instance type")
