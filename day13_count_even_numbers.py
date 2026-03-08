# program to count even numbers in a list using function and loop

numbers = [2,5,4,3,6,7,8]
def even_numbers(numbers):
    count = 0
    for i in numbers:
        if i%2==0:
            count+=1
    return(count)
result = even_numbers(numbers)
print("even numbers are:",result)
