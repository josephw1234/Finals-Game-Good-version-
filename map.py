from tabulate import tabulate
import second_day as second


# Note: map for first day is located in first_day.py to avoid circular import


def print_map():
    """Function for printing grid map of Campbell"""
    # vairables for classrooms
    english = "English"
    math = "Math"
    french = "French"
    history = "History"
    # classroom updates if player has been there
    if "english" in second.classes_done:
        english = "English(done)"
    if "math" in second.classes_done:
        math = "Math(done)"
    if "history" in second.classes_done:
        history = "History(done)"
    if "french" in second.classes_done:
        french = "French(done)"
    # print the map
    map = [['', english],
           [math, 'Main Hall', history],
           ['', french, ]]
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
