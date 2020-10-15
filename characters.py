class Teacher:
    """Parent class for strict/not strict teachers"""
    def __init__(self, name, location):
        self.name = name
        self.location = location


class StrictTeacher(Teacher):
    """Class for strict teachers"""
    def __init__(self, name, location):
        super().__init__(name, location)

    def __str__(self):
        desc = (f"{self.name} is your {self.location} teacher\n"
                f"{self.name} is very strict, cheating is gonna be riskier...")
        return desc


class NotStrictTeacher(Teacher):
    """Class for not strict teachers"""
    def __init__(self, name, location):
        super().__init__(name, location)

    def __str__(self):
        desc = (f"{self.name} is the {self.location} teacher\n"
                f"{self.name} is not very strict, you might "
                "be able to get away with something...")
        return desc


# Defining the different teachers
english_teacher = StrictTeacher("Mrs.Repski", "english")
math_teacher = NotStrictTeacher("Mr.Belle", "math")
history_teacher = StrictTeacher("Mme.Therien", "history")
french_teacher = NotStrictTeacher("Mr.Potvin", "french")
