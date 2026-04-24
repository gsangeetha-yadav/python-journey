# Program to group words based on their length

sentence = input("Enter a sentence: ")
words = sentence.split()

result = {}

for word in words:
    length = len(word)
    
    if length in result:
        result[length].append(word)
    else:
        result[length] = [word]

print(result)
