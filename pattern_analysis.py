# pattern and number analysis program 
#concepts: loops, nested loops, conditions


n=int(input("enter any number:"))
for i in range(n):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
even_count=0
odd_count=0
for i in range(1,n+1):
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print("even numbers are:",even_count)
print("odd numbers are:",odd_count)
    