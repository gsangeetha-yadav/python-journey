# program to demonstrate collatz 3n+1 sequence

n = int(input("enter any value for n"))
steps = 0
while n!=1:
    print(n,end = ",")
    if n%2==0:
        n=n//2
    else:
        n=3*n+1
    steps+=1
print(n)
print("Total steps taken:",steps)