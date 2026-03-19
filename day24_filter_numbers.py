# program to take comma-separated numbers and filter numbers greater than 50 using filter() function

num = list(map(int, input("enter comma separated numbers:").split(",")))
result = list(filter(lambda x: x > 50 , num))
print(result)