
import sys

student_name = str(input("Enter student name: "))
maths_marks = int(input("Enter Maths marks: "))
science_marks = int(input("Enter Science marks: "))
english_marks = int(input("Enter English marks: "))

if(maths_marks < 0 or maths_marks > 100):
    print("Invalid marks entered")
    sys.exit(1)
elif(science_marks < 0 or science_marks > 100):
    print("Invalid marks entered")
    sys.exit(1)
elif(english_marks < 0 or english_marks > 100):
    print("Invalid marks entered")
    sys.exit(1)


total_marks = english_marks + science_marks + maths_marks
avg_percentage = (total_marks / 3)

status="PASS"
if(maths_marks < 40 or science_marks < 40 or english_marks < 40):
    status="FAIL"

print(f"Student Name: {student_name}")
print(f"Total Marks: {total_marks}")
print(f"Percentage: {avg_percentage}")
print(f"Status: {status}")

grade=""
if status == "PASS":
    if(avg_percentage >= 75):
        grade = "A"
    elif(avg_percentage >= 60):
        grade = "B"
    elif(avg_percentage >= 40):
        grade = "C"

    print(f"Grade: {grade}")



