# Program to check if parentheses are balanced

expression = input("Enter expression: ")

stack = []
pairs = {')': '(', '}': '{', ']': '['}

balanced = True

for ch in expression:
    if ch in "({[":
        stack.append(ch)
    elif ch in ")}]":
        if not stack:
            balanced = False
            break
        top = stack.pop()
        if pairs[ch] != top:
            balanced = False
            break

# Final check
if balanced and not stack:
    print("Balanced")
else:
    print("Not Balanced")
