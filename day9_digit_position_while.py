# program to find the nth digit from the right of a number using while loop


num = 987654
pos = 3
i = 1
while i < pos:
      num//=10
      i+=1
print(num%10)