#python program to read name and age of a person & display
#whether a person is senior citizen or not

name = input("enter your name:")
yorb = int(input("enter your age:"))
from datetime import datetime
cyr = datetime.now().year
age = cyr - yorb
print(f"hello {name} your age is {age}")
if age >= 60:
    print("you are a senior citizen")
else:
    print("your not a senior citizen")