# program to find the first non-repeating character in a given
# string using loop and built-in count() function


string = input("enter the words")
for ch in string:
    if string.count(ch)==1:
        
        print(ch)
        break
        