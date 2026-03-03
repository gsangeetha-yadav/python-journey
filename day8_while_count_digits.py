#program to count number of digits in a number using while loop


num = 54879
count = 0
while num >0:
    num//=10
    count+=1
print("Number of digit:" , count)
