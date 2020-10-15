from tabulate import tabulate


def print_map():
    """Function for printing grid map of Campbell"""
    map = [['', 'English'],
           ['Math   ', 'Main Hall', 'History'],
           ['', 'French', ]]
    print(tabulate(map, tablefmt="grid"))


class Map:
    """Class for different classrooms teachers and dificulty"""
    def __init__(self, teacher, test_difficulty):
        self.teacher = teacher
        self.test_difficulty = test_difficulty

    def __str__(self):
        desc = (f"{self.teacher} is the teacher\nThe test difficulty is "                
                f"{self.test_difficulty}")
        return desc


# Defining the different classrooms
english_class = Map("Mrs.Repski", "moderate")
math_class = Map("Mr.Belle", "hard")
french_class = Map("Mr.Potvin", "easy")
history_class = Map("Mme.Therrien", "moderate")
