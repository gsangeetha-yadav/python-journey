# program to count words , characters, and lines in a sentence

se = input("enter the sentence \n")
words = se.split()

freq ={}

for word in words:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
freq1 ={}
for ch in se:
    if ch!=" ":
        if ch in freq1:
            freq1[ch]+=1
        else:
            freq1[ch]=1

lines = se.split("\n")   
print("words",(freq))
print("characters" , (freq1))
print("lines",len(lines))

    