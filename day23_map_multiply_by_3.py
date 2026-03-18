# program to take comma-separated input convert to integers,
# and multiply each number by 5 using map() and lambda

numbers = [5,10,15]
print(list(map(lambda x : x+5,numbers)))


num = (input("enter a comma separeated number:"))
nums = num.split(",")
print(list(map(lambda x: int(x)*3, nums)))