class Student:
    school_name = "Springfield Elementary"

    def __init__(self, name, student_id=1):
        self.name = name
        self.student_id = student_id

    def __str__(self):
        return f"Student {self.name}"

    def set_name(self, name):
        self.name = name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name



