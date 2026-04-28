# Program to find length of longest substring without repeating characters

string = input("Enter a string: ")

char_set = set()
start = 0
max_length = 0

for end in range(len(string)):
    
    # If duplicate found, shrink window
    while string[end] in char_set:
        char_set.remove(string[start])
        start += 1
    
    # Add current character
    char_set.add(string[end])
    
    # Update max length
    current_length = end - start + 1
    if current_length > max_length:
        max_length = current_length

print("Length of longest substring:", max_length)
