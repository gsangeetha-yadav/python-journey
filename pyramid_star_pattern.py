# program to print a pyramid star pattern using nested for loop
# it prints spaces first and then stars in each row

for i in range(1,5):
    # spaces
    for j in range(4-i):
        print(" ", end="")
    # stars
    for j in range(i):
        print("*", end=" ")
    print()