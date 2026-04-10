# strong number checker
# this program checks whether a number is a strong number
# concepts : loops, factorial,conditions


n=int(input("enter the number:"))
original=n
sum_factorial =0
while n > 0:
    digit = n%10
    fact = 1
    for i in range(1,digit+1):
        fact*=i
    sum_factorial+=fact
    n = n//10
if sum_factorial == original:
    print("strong number")
else:
    print("not a strong number")