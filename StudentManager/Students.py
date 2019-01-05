students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = f"{student['name']}  {student['student_id']}"
    return students_titlecase

def print_students_titlecase():
    print(get_students_titlecase())

def add_student(name, student_id = 0):
    student = { "name": name, "student_id": student_id }
    students.append(student)

student_name = input("Please enter the student's name: ")
student_id = input("Please enter the student's id: ")

add_student(student_name, student_id)

print_students_titlecase()