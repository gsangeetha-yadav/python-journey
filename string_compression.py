# Program for Run-Length Encoding (String Compression)

string = input("Enter a string: ")

result = ""
count = 1

for i in range(1, len(string)):
    if string[i] == string[i - 1]:
        count += 1
    else:
        result += string[i - 1] + str(count)
        count = 1

# Add last character
result += string[-1] + str(count)

print("Compressed string:", result)
