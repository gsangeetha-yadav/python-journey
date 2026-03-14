# program to demonstrate python string methods

sentence = input("enter a sentence:")
word = input("enter a word to find:")
find=(sentence.find(word))
print(find)

words = sentence.split()
print(words)

final_result="The word {} is found at position {}".format(word, find)
print(final_result)

total_sentence="total words in sentence are {}".format(len(words))
print(total_sentence)