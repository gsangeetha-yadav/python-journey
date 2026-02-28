#program to check exam eligibility and scholarship based on attendence and marks using nested if

marks = int(input("Enter your marks: "))
attendence = int(input("Enter your attendence percentage: "))
if attendence<75:
    print("not eligible for exam")
else:
    print("eligible for exam")
    
    if marks >= 90:
        print("scholarship awarded")
    elif 75 <= marks <90:
        print("No scholarship")
    elif 50 <= marks < 75:
        print("needs improvment")
    else:
        print("failed")