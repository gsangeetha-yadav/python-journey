#Take account balance from user
balance = int(input("Enter your account balance:"))
#Take withdrawal amount from user
withdrawal = int(input("Enter withdrawal amount:"))
#check if withdrawal amount is invalid (zero or negative)
if withdrawal<=0:
    print("Invalid amount:")
#check if withdrawal amount is greater than available balance
elif withdrawal>balance:
    print("Insufficient balance:")
#if all conditions are valid, perform withdrawal
else: 
    #subtract withdrawal amount from balance
    balance = balance-withdrawal
    print("withdrawal successful:")
    print("Remaining balance:",balance)