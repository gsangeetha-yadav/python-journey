# program to find and print all even numbers from a given list
# using a function

def even_numbers(numbers):
    even_list =[]
    for num in numbers:
        if num%2==0:
            even_list.append(num)
    return even_list
numbers = [10,25,30,56,78,90,80]
result = even_numbers(numbers)
print("Even numbers in the list are:",result)