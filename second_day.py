from first_day import cheats, knowledge
import random as random
import time as t
import characters as c
import map as m

# List of classes that are done
classes_done = []


def second_day(grade):
    """ Main function for second day"""
    message_1 = ("You are in the main hall.\n"
                 "Which class do you go to?\n>")
    for action in message_1:
        # ending
        if "english" in classes_done and "history" in classes_done \
           and "french" in classes_done and "math" in classes_done:
            print("You've been to all classes")
            print(f"Your final grade is {grade}%")
            break
        action = input(message_1)
        # map print
        m.print_map()
        # English path
        if action.lower() == "english" and "english" not in classes_done:
            print("You go to English class...")
            print(c.english_teacher)
            print("Your finals assignment for this class is to write "
                  "an essay about Shakespeare's Hamlet, I hopeyou've studied")
            print(f"The test diffculty is {m.english_class.test_difficulty}")
            message = ("How are you going to tackle this assignment?\n"
                       "Use your study knowledge, cheat, or try your best?\n"
                       "('k', 'c' or 't')\n>")
            for action in message:
                action = input(message)
                # knowledge path
                if action == "k" and 'englsih' not in knowledge:
                    print("You didn't study for english")
                    continue
                    g = random.randint(18, 22)
                    grade += g
                if action == "k" and 'english' in knowledge:
                    print("Becasue you re-read Hamlet last night, you feel"
                          " confident in your ability to write this essay...")
                    print("The essay isn't perfect, but it's pretty good")
                    print(f"Grade + {g}\nYour grade is now {grade}")
                    classes_done.append("english")
                    break
                # cheat path
                if action == "c" and "englsih" not in cheats:
                    print("You have nothing to cheat with")
                    continue
                if action == "c" and "english" in cheats:
                    n = random.randint(0, 30)
                    if n >= 15:
                        print("You look under your mask to see the notes you "
                              "wrote yesterday which helps you "
                              "write your essay...")
                        g = random.randint(21, 24)
                        grade += g
                        print("Your grade is good\nSuspiciously good.....")
                        print(f"Grade + {g}\nYour grade is now {grade}%")
                        classes_done.append("english")
                        break
                    if n < 15:
                        print("Oh no!\nYou got caught cheating!")
                        break
                # try your best path
                if action == "t":
                    g = random.randint(8, 12)
                    grade += g
                    print("You try your best to write the essay but as "
                          "you neither studied for or cheated for this class,"
                          " your grade doesn't look good...")
                    t.sleep(1)
                    print (f"Grade + {g}\nYour grade is now {grade}%")
                    classes_done.append("english")
                    break
                # unkown input
                else:
                    print("I don't know what you mean")
                    continue
            continue
        # French path
        if action.lower() == "french" and "french" not in classes_done:
            print("You go to French class...")
            print(c.french_teacher)
            print("Your finals assignment for this class is to conjugate er"
                  "ir and re verbs")
            print(f"The test diffculty is {m.french_class.test_difficulty}")
            message = ("How are you going to tackle this assignment?\n"
                       "Use your study knowledge, cheat, or try your best?\n"
                       "('k', 'c' or 't')\n>")
            for action in message:
                action = input(message)
                # knowledge path
                if action == "k":
                    print("Because you studied your verbs, "
                          "you know exactly what to do...")
                    print("You're not quite fluent yet, "
                          "but your grade is still pretty good")
                    g = random.randint(22, 25)
                    grade += g
                    print(f"Grade + {g}\nYour grade is now {grade}%")
                    classes_done.append("french")
                    break
                # cheat path
                if action == "c" and "french" not in cheats:
                    print("You don't have anything to cheat with")
                    continue
                if action == "c" and "french" in cheats:
                    n = random.randint(0, 30)
                    if n >= 10:
                        print("You look under your mask to see a "
                              "whole Bescherelle stuffed under your mask."
                              " I don't know how you got it to"
                              " fit under there but it sure is useful")
                        g = random.randint(23, 25)
                        grade += g
                        print("Your grade is good\n Suspiciously good.....")
                        print(f"Grade + {g}\nYour grade is now {grade}%")
                        classes_done.append("french")
                        break
                    if n < 10:
                        print("Oh no!\nYou got caught cheating!")
                        break
                # try your best path
                if action == "t":
                    g = random.randint(10, 13)
                    grade += g
                    print("You try your best to conjugate the verbs, "
                          "but because you didn't study your grade "
                          "doesn't look good...")
                    print (f"Grade + {g}\nYour grade is now {grade}%")
                    classes_done.append("french")
                    break
                # unkown input
                else:
                    print("I dont know what you mean")
                    continue
            continue
        # History path
        if action.lower() == "history" and "history" not in classes_done:
            print("You go to history class...")
            print(c.history_teacher)
            print("Your finals assignment for this class is to write "
                  "about the Battle of the Somme in WW1")
            print(f"The test diffculty is {m.history_class.test_difficulty}")
            message = ("How are you going to tackle this assignment?\n"
                       "Use your study knowledge, cheat, or try your best?\n"
                       "('k', 'c' or 't')\n>")
            for action in message:
                action = input(message)
                # knowledge path
                if action == "k" and 'history' not in knowledge:
                    print("You didn't study for history")
                    continue
                if action == "k" and 'history' in knowledge:
                    g = random.randint(18, 22)
                    grade += g
                    print("Becasue you grinded WW1 documentaries last night "
                          "you feel confident about the test...")
                    print("Your test isn't perfect, but it's pretty good")
                    print(f"Grade + {g}\nYour grade is now {grade}")
                    classes_done.append("history")
                    break
                # cheat path
                if action == "c" and "history" not in cheats:
                    print("You have nothing to cheat with")
                    continue
                if action == "c" and "history" in cheats:
                    n = random.randint(0, 30)
                    if n >= 15:
                        print("You look under your mask to see the notes you "
                              "wrote yesterday about WW1, "
                              "this should be easy...")
                        g = random.randint(21, 24)
                        grade += g
                        print("Your grade is good\nSuspiciously good.....")
                        print(f"Grade + {g}\nYour grade is now {grade}%")
                        classes_done.append("history")
                        break
                    if n < 10:
                        print("Oh no!\nYou got caught cheating!")
                        break
                # try your best path
                if action == "t":
                    g = random.randint(8, 12)
                    grade += g
                    print("You try your best to write the essay "
                          "but as you neither studied for or cheated for "
                          "this class, your grade doesn't look good...")
                    print (f"Grade + {g}\nYour grade is now {grade}%")
                    classes_done.append("history")
                    break
                # unkown input
                else:
                    print("I don't know what you mean")
                    continue
            continue
        # Math path
        if action.lower() == "math" and "math" not in classes_done:
            print("You go to Math class...")
            print(c.math_teacher)
            print(f"The test diffculty is {m.math_class.test_difficulty}")
            print("Your finals assignment for this class is on trigonometry"
                  " and the quadratic formula, I hope you've studied")
            message = ("How are you going to tackle this assignment?\n"
                       "Use your study knowledge, cheat, or try your best?\n"
                       "('k', 'c' or 't')\n>")
            for action in message:
                action = input(message)
                # knowledge path
                if action == "k" and 'math' not in knowledge:
                    print("You didn't study for math")
                    continue
                if action == "k" and 'math' in knowledge:
                    g = random.randint(17, 20)
                    grade += g
                    print("Because you studied your trig skills, "
                          "you feel confident about this test...")
                    print("Your work isn't perfect, but its pretty good")
                    print(f"Grade + {g}\nYour grade is now {grade}")
                    classes_done.append("math")
                    break
                # cheat path
                if action == "c" and "math" not in cheats:
                    print("You have nothing to cheat with")
                    continue
                if action == "c" and "math" in cheats:
                    n = random.randint(0, 30)
                    if n >= 10:
                        print("You look under your mask to find the "
                              "quadratic formula written there."
                              " Just what you needed...")
                        g = random.randint(20, 23)
                        grade += g
                        print("Your grade is good\nSuspiciously good.....")
                        print(f"Grade + {g}\nYour grade is now{grade}%")
                        classes_done.append("math")
                        break
                    if n < 10:
                        print("Oh no!\nYou got caught cheating!")
                        break
                # try your best path
                if action == "t":
                    g = random.randint(7, 9)
                    grade += g
                    print("You try your best to write the test "
                          "but as you neither studied or cheated "
                          "for this class, your grade doesn't look " "good...")
                    print (f"Grade + {g}\nYour grade is now {grade}%")
                    classes_done.append("math")
                    break
                # unkown input
                else:
                    print("I don't know what you mean")
                    continue
            continue
        # done path
        if action.lower() == "done":
            break
        # classes already done
        if action.lower() == "english" and "english" in classes_done:
            print("You've already been to english")
            continue
        if action.lower() == "math" and "math" in classes_done:
            print("You've already been to math")
            continue
        if action.lower() == "history" and "history" in classes_done:
            print("You've already been to history")
            continue
        if action.lower() == "french" and "french" in classes_done:
            print("You've already been to french")
            continue
        # unkown input
        else:
            print("I don't know what you mean")
