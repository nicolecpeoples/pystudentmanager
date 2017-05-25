class HighSchoolStudent(Student):

    school_name = "Lincoln High"

    def get_school_name(self):
        return "This is a high school student"

    def get_name_capitalized(self):
        original_value = super().get_name_capitalized()
        return original_value + "-HS"