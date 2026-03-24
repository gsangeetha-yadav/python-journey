# simple calculator program 
#This program takes two numbers and an operator from the user
# and performs basic airthmetic operations

n1 = float(input("enter a first number:"))
n2 = float(input("enter a second number:"))
operator = input("enter operator (+,-,*,/):")
if operator == "+":
    print("result", n1+n2)
elif operator == "-":
    print("result",n1-n2)
elif operator == "*":
    print("result", n1*n2)
elif operator == "/":
    if n2 !=0:
        print("result", n1/n2)
    else:
        print("division by zero is not possible")
else:
    print("invalid operator")