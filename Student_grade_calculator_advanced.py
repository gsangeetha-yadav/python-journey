# Program to calculate total, average and grade using list and loop

marks = []

# Taking input using loop
for i in range(1, 6):
    m = int(input(f"Enter marks of subject {i}: "))
    marks.append(m)

# Calculating total and average
total = sum(marks)
average = total / len(marks)

# Assigning grade
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"

# Displaying results
print("Marks:", marks)
print("Total =", total)
print("Average =", average)
print("Grade =", grade)
