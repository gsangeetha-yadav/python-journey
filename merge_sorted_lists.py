# Program to merge two sorted lists

list1 = list(map(int, input("Enter first sorted list: ").split()))
list2 = list(map(int, input("Enter second sorted list: ").split()))

i = 0
j = 0
result = []

while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        result.append(list1[i])
        i += 1
    else:
        result.append(list2[j])
        j += 1

# Add remaining elements
result.extend(list1[i:])
result.extend(list2[j:])

print("Merged list:", *result)
