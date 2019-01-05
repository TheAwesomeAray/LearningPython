from student import *

class HighSchoolStudent(Student):
    school_name = "Highschool"

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return f"{original_value} HS"

    #methods starting with _ are meant to not be inherited. All methods in python are public
