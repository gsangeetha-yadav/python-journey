# this program demonstrate the use of functions as arguments in
# python 
# it implements basic arithmetic operations (add, subtract,
#multiply) and uses a higher-order function 'calculate ' to 
# execute them

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def calculate(func, a, b):
    result = func(a,b)
    print(result)
calculate(add, 3, 4)
calculate(sub, 5, 8)
calculate(mul, 8, 9)
