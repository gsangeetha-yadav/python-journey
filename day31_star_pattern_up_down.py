# program to print a star pattern (increasing and then 
# decreasing) using nested loops
#increasing part
for i in range(1,5):
    for j in range(1,i+1):
        print("*", end=" ")
    print()
#decreasing part
for i in range(3,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()