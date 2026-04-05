# progran to count vowels in a string it checks each character 
# and counts vowels

def count_vowel(text):
    text = text.lower()
    count=0
    for index, char in enumerate(text):
        if char in "aeiou":
            print(f"vowel '{char}' found at position {index}")
            count+=1
    return count
result = count_vowel("sangeetha")
print ("number of vowels in a text is ", result)
        