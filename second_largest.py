#program to find second largest number from user input

n = (input("enter the numbers"))
n = n.split(",")
numbers = []
for num in n:
    numbers.append(int(num))
largest = numbers[0]
second = numbers[0]
for num in numbers:
    if num>largest:
        second = largest
        largest = num
    elif num>second and num!=largest:
        second = num
print("second largest:", second)
        
        
