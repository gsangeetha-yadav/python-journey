# program to demonstrate dictionary creation , updatr values, adding a new key , and displaying dictionary items

student = {
    "name" : "sangeetha",
    "age" : "18",
    "marks" : "90"
}
print(student)
new_marks = {"marks" : "95"}
student.update(new_marks)
print(student)

student["city"] = "siruguppa"
print(student)
print(student.items())