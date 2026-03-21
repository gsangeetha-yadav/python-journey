# program to take two numbers from the user and perform division
#using exception handling (try-except) to avoid errors like
# invalid input and division by zero

try:
    a = int(input("enter a first number:"))
    b = int(input("enter a second number:"))
    result = a/b
    print("Result",result)
except ValueError:
    print("please enter valid number!")
except ZeroDivisionError:
    print("division by zero is not possible")
finally:
    print("program finished")