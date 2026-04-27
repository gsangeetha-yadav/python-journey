# Program to check if two strings are isomorphic

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# Step 1: length check
if len(s1) != len(s2):
    print("Not Isomorphic")
else:
    map1 = {}
    map2 = {}
    is_isomorphic = True

    # Step 2: check mapping
    for ch1, ch2 in zip(s1, s2):
        if ch1 in map1:
            if map1[ch1] != ch2:
                is_isomorphic = False
                break
        else:
            if ch2 in map2:
                is_isomorphic = False
                break
            map1[ch1] = ch2
            map2[ch2] = ch1

    # Step 3: result
    if is_isomorphic:
        print("Isomorphic")
    else:
        print("Not Isomorphic")
