# program to check anagram 
# description : this program checks whether two input strings are
# anagram

string = input("enter the  string ").lower()
string1 = input("enter the string ").lower()
word = sorted(string)
words = sorted(string1)
if len(string)!= len(string1):
    print("not anagram")
elif word ==words:
    print("anagram")
else:
    print("not anagram")
    
    
