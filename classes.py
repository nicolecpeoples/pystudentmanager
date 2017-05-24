students = []


class Student:

    school_name = "Washington Elementary"

    # Using self is the way we refer to our class from our class
    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalized(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


class HighSchoolStudent(Student):

    school_name = "Lincoln High"

    def get_school_name(self):
        return "This is a high school student"

    def get_name_capitalized(self):
        original_value = super().get_name_capitalized()
        return original_value + "-HS"

nicole = Student("nicole")
james = HighSchoolStudent("james")
print(nicole.get_name_capitalized())
print(james.get_name_capitalized())
