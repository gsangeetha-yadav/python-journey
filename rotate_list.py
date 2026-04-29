# Program to rotate a list by K positions

numbers = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter K: "))

n = len(numbers)

# Handle K greater than length
k = k % n

# Rotate list
rotated = numbers[-k:] + numbers[:-k]

print("Rotated list:", *rotated)
