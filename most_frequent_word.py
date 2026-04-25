# Program to find the most frequent word in a sentence

sentence = input("Enter a sentence: ")
words = sentence.split()

freq = {}

# Count frequency
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

# Find most frequent word
max_word = None
max_count = 0

for word in freq:
    if freq[word] > max_count:
        max_count = freq[word]
        max_word = word

print(max_word, "→", max_count)
