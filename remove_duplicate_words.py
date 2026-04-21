# program to remove duplicate words from a sentence
# convert words to lowercase and keeps only unique words

string = input("enter the sentence:")
string1 = string.split()
my_list = []
for word in string1:
    words = word.lower()
    if words not in my_list:
        my_list.append(words)
result=" ".join(my_list)
print(result)
