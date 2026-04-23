# Program to find the first non-repeating character in a string

string = input("Enter a string: ")

for ch in string:
    if string.count(ch) == 1:
        print("First non-repeating character is:", ch)
        break
else:
    print("No non-repeating character found")
