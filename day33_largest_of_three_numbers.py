# program to find the largest of three numbers 
# it takes three inputs from the user and checks for the largest 
# number
# Also handles the case when all three numbers are equal


n1 = int(input("enter first number:"))
n2 = int(input("enter second number:"))
n3 = int(input("enter third number:"))
if n1==n2==n3:
    print("All numbers are equal")
elif n1>=n2 and n1>=n3:
    print(f"largest number is {n1}")
elif n2>=n1 and n2>=n3:
    print(f"largest number is {n2} ")
else:
    print(f"largest number is {n3}")