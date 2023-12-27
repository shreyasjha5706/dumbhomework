# Task 14: Check the grade of a student
marks = float(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A+")
elif 80 <= marks < 90:
    print("Grade: A")
elif 70 <= marks < 80:
    print("Grade: B")
elif 60 <= marks < 70:
    print("Grade: C")
else:
    print("Grade: F")
