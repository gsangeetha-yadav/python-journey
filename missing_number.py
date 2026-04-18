# Find Missing number from 1 to n

n = int(input("enter n numbers"))
n1 = list(map(int, input("enter numbers:").split()))
expected_total = n*(n+1)//2
actual_total =sum(n1)
missing_number = expected_total-actual_total
print("Missing number is:",missing_number)