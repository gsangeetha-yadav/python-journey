#  Student Marks Analyzer
# This program analyzes student marks using lists
# Concepts: lists, loops, conditions

n = int(input("Enter number of students: "))

marks = []

# Taking input
for i in range(n):
    m = int(input(f"Enter marks of student {i+1}: "))
    marks.append(m)

# Calculations
total = sum(marks)
average = total / n
highest = max(marks)
lowest = min(marks)

# Count passed students
passed = 0
for m in marks:
    if m >= 40:
        passed += 1

# Output
print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Passed students:", passed)
