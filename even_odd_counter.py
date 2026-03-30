# program to print numbers from 1 to n and counts even and
#odd numbers uses a for loop and basic conditions 
even_count = 0 
odd_count = 0
n = int(input("enter any number:"))
for num in range(1,n+1):
    print(num, end=" ")
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
print("\neven count is :", even_count)
print("odd count is :",odd_count)
   