#simple calculator program using float inputs and arthimetic #operators
n1 = float(input("Enter a first number:"))
n2 = float(input("Enter a second number:"))
Add= n1+n2
Sub = n1-n2
Mul = n1*n2
Div = n1/n2

#printing results
print(f"Addition is {Add}")
print(f"Subtraction is {Sub}")
print(f"MUltiplication is {Mul}")
print(f"Division is {Div}")

#printing data types
print(f"type of Addition is {type(Add)}")
print(f"type of Sutraction is {type(Sub)}")
print(f"type of Multiplication is {type(Mul)}")
print(f"type of Division is {type(Div)}")