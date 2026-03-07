#program to find the smallest number in a list using loop

numbers = [100,25,50,51,20,5]
smallest = numbers[0]
for i in numbers:
   if i<smallest:
       smallest=i
print("smallest number is" , smallest)