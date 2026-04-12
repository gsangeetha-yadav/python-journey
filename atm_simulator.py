# Day 47: ATM Simulator
# This program simulates basic ATM operations
# Concepts: functions, loops, conditions

balance = 1000

def check_balance():
    print("Balance:", balance)

def deposit():
    global balance
    amount = int(input("Enter amount to deposit: "))
    balance += amount
    print("Amount deposited successfully!")

def withdraw():
    global balance
    amount = int(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print("Amount withdrawn successfully!")

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        check_balance()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
