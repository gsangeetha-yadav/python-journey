# program to count voels, consonants,digits and spaces in a 
# given sentence


sentence = input("enter the sentence:").lower()

consonant = 0
vowel = 0
digit = 0
space = 0
for ch in sentence:
    if ch in "aeiou":
        vowel+=1
    elif ch.isalpha():
        consonant+=1
    elif ch.isdigit():
        digit+=1
    elif ch==" ":
        space+=1

print("vowel are ", vowel)
print("consonants are", consonant)
print("digits are", digit)
print("empty spaces are", space)
    