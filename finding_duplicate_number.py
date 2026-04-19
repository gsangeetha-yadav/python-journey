# find duplicate numbers in a list

n = input("enter the numbers:").split()
seen = []
duplicate = []
for num in n:
    if num in seen:
        if num  not in duplicate:
            duplicate.append(num)
    else:
        seen.append(num)
print("duplicate numbers are:",duplicate)
        
        
            