# file Name : save_and_read_names.py
#description: this program takes three names as input from the 
#user
# stores them in a file (names.txt) and then reads and displays 
# the saved names.

name1 = input("enter first name:")
name2 = input("enter second name:")
name3 = input("enter third name:")
with open("names.txt","w") as file:
    file.write(name1 + "\n")
    file.write(name2 + "\n")
    file.write(name3 + "\n")
print("\nsaved Names:")
with open("names.txt", "r") as file:
    print(file.read())