#program to print subjects with numbering using enumerate()

subjects = ["maths" , "Science" , "english" , "social"]

for index, subject in enumerate(subjects, start=1):
    print(f"{index} . {subject}")
    
#program to combine student names with marks using zip()


students = ["john" , "Maxi" , "Mick", "Jack"]
marks = [90, 85, 75, 95]
for student,mark in zip(students,marks):
    print(f"{student} : {mark}")
    
    
    
