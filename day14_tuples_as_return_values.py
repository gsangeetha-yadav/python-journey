#program to perform tuple as return values
#Returning multiple values

import math
def circle_stats(r):
    """Return (circumference,area) of a circle of radius """
    circumference=2*math.pi*r
    area = math.pi*r*r
    return(circumference,area)
result = circle_stats(5)
print(result)