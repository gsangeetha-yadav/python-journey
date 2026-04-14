# character frequency counter 
# this program counts frequency of each character
# concepts : dictionary,loops,string


sentence = input("enter the string:").lower()

freq = {}
for ch in sentence:
    if ch!=" ":
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
for ch in freq:
    print(ch,":",freq[ch])