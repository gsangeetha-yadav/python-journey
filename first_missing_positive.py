# Program to find the first missing positive number

numbers = list(map(int, input("Enter numbers: ").split()))

num_set = set(numbers)

i = 1

while True:
    if i not in num_set:
        print("First missing positive:", i)
        break
    i += 1
