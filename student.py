students = []


class Student:

    school_name = "Washington Elementary"

    # Using self is the way we refer to our class from our class
    def __init__(self, name, student_id=332):
        """
        :param name: string - student name
        :param student_id: int - optional student id
        """
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalized(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name