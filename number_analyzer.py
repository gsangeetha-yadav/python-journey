# number analyzer program 
#features : sum of digits,reverse,palindrome check,even/odd
#digit count
n=int(input("enter any digits"))
original = n
sum_digit= 0
reverse = 0
even_count = 0
odd_count = 0
while n>0:
    digit = n%10
    #sum of digits
    sum_digit+=digit
    
    #reverse  number
    reverse = reverse*10+digit
    
    if digit % 2 ==0:
        even_count+=1
    else:
        odd_count+=1
    n = n//10
# palindrome check
if original == reverse:
    palindrome = "yes"
else:
    palindrome ="no"
print("sum of digits:",sum_digit)
print("Reverse:",reverse)
print("palindrome:", palindrome)
print("Even digits :",even_count)
print("odd digits:",odd_count)











