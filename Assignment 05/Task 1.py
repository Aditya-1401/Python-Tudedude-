# Task 1 --> Create a Dictionary of Student Marks


student_marks = {
    "Aditya": 85,
    "Rahul": 78,
    "Alice": 92,
    "Stephen": 88
}
name = input("Enter the student's name: ")

if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found in the records.")
