# Program to find pairs with target sum

numbers = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target sum: "))

seen = set()

for num in numbers:
    complement = target - num

    if complement in seen:
        print((complement, num))

    seen.add(num)
