#progarm to perform set operations(union and inetrsection)
# takes input from user as comma-separated numbers
# convert input into sets and displays union and intersection

numbers = [1,1,2,3,4,5,6,7,8,9,8,3]
num = set(numbers)
print("unique_numbers=", num)
print("Total_unique = ", len(num))

num1 = (input("enter the numbers:"))
num2 = (input("enter the numbers:"))
list1 = num1.split(",")
list2 = num2.split(",")

set1=set(map(int, list1))
set2=set(map(int, list2))

print("union",set1 | set2)
print("intersection",set1 & set2)