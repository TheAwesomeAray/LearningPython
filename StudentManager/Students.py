students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"])
    return students_titlecase

def print_students_titlecase():
    print(get_students_titlecase())

def add_student(name, student_id = 0):
    student = { "name": name, "student_id": student_id }
    students.append(student)

def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception as error:
        print("Failed to save student")
        print(error)

def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")

read_file()
student_name = input("Please enter the student's name: ")
add_student(student_name)

save_file(student_name)
print_students_titlecase()