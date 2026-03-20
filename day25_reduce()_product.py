# program to take comma-separated numbers and find product using reduce() function

from functools import reduce
num = list(map(int, input("enter a comma separated numbers:").split(",")))
result = reduce(lambda x,y: x*y , num)
print(result)


# program to take comma separated numbers,convert them to integers and calculate  the product using reduce() with operator.mul 
from functools import reduce
from operator import mul
nums = [10,3,4,5]
print(reduce(mul,nums))
