# Program to sort words in a sentence alphabetically

sentence = input("Enter a sentence: ")

words = sentence.split()

words.sort()

result = " ".join(words)

print("Sorted sentence:", result)
