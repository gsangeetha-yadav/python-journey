# program to find missing number in an list of integers 

def find_missing_number(arr,n):
    total = n*(n+1)//2
    arr_sum = sum(arr)
    return total - arr_sum

#example
arr = [1,2,4,5,6]
n=6
print("missing number is :",find_missing_number(arr,n))