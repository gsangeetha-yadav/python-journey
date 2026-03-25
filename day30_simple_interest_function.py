# program to calculate simple interest using a function
#takes principal amount,time,and rate as input from user
#returns and prints the calculated simpke interest

def simple_interest(p,t,r):
    si = (p*t*r)/100
    return si 
p = float(input("enter a principle amount:"))
t = float(input("enter time in years:"))
r = float(input("enter rate of interest:"))
result=simple_interest(p,t,r)
print("simple interest is :",result)
