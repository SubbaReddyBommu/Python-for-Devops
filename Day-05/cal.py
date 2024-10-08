# import sys for command line arguments
import sys  

def add(num1, num2):
    result= num1 + num2
    return result

def sub(num1, num2):
    result= num1 - num2
    return result

def mul(num1, num2):
    result= num1 * num2
    return result

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "add":
    output = add(num1, num2)
    print(output)
    
elif operation == "sub":
    output = sub(num1, num2)
    print(output)
elif operation == "mul":
    output= mul(num1, num2)
    print(output)
else:
    print("enter a valid operation")

