# program to find squares of numbers whose square is greater than 59 using list comprehension

squares = [i*i for i in range(1,21) if i*i>50]
print(squares)