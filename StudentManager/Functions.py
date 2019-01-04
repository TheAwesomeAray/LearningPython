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

add_student("Andrew", 1)
add_student("Candice")
print_students_titlecase()

def var_args(name, **kwargs):
    print(name)
    print(kwargs["description"])


var_args("Test", description="Loves Python", other_variable="Other")


