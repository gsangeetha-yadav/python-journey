#  Word Frequency Counter
# This program counts how many times each word appears
# Concepts: dictionary, loops, strings

sentence = input("Enter the sentence: ").lower()

words = sentence.split()
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

# Print result
for word in freq:
    print(word, ":", freq[word])
