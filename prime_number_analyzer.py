# prime number Analyzer 
# this program checks and prints all prime numbers up to n 

prime_count = 0
n = int(input("enter any number:"))
for i in range(2,n+1):
    is_prime=True
    for j in range(2,i):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        print(i)
        prime_count+=1
print("total prime numbers are:",prime_count)    