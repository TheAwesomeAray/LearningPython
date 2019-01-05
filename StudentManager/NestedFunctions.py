
def get_students():
    def get_students_titlecase():
        students_titlecase = []
        for student in students:
            students_titlecase = f"{student['name']}  {student['student_id']}"
        return students_titlecase
    students_titlecase_names = get_students_titlecase()
    print(students_titlecase_names)
