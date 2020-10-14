from first_day import cheats, knowledge
import random as random
import time as t
from map import print_map


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
            break
        action = input(message_1)
        # map
        if action.lower() == "map":
            print_map()
            continue
        # English path
        if action.lower() == "english" and "english" not in classes_done:
            print("You go to English in Mrs.Repski's class...")
            print("Your finals assignment for this class is to write "
                  "an essay about Shakespeare's Hamlet, I hope you've studied")
            message = ("How are you going to tackle this assignment?\n"
                       "Use your study knowledge, cheat, or try your best?\n"
                       "('k', 'c' or 't')\n>")
            for action in message:
                action = input(message)
                # knowledge path
                if action == "k" and 'englsih' not in knowledge:
                    print("You didn't study for english")
                    continue
                    grade += 20
                if action == "k" and 'english' in knowledge:
                    print("Becasue you re-read Hamlet last night, you feel"
                          " confident in your ability to write this essay...")
                    print("The essay isn't perfect, but it's pretty good")
                    print(f"Grade + 20\nYour grade is now {grade}")
                    classes_done.append("english")
                    break
                # cheat path
                if action == "c" and "englsih" not in cheats:
                    print("You have nothing to cheat with")
                    continue
                if action == "c" and "english" in cheats:
                    n = random.randint(0, 30)
                    if n >= 13:
                        print("You look under your mask to see the notes you "
                              "wrote yesterday which helps you "
                              "write your essay...")
                        grade += 25
                        print("Your grade is good\nSuspiciously good.....")
                        print(f"Grade + 25\nYour grade is now {grade}%")
                        classes_done.append("english")
                        break
                    if n < 13:
                        print("Oh no!\nYou got caught cheating!")
                        break
                # try your best path
                if action == "t":
                    grade += 10
                    print("You try your best to write the essay but as "
                          "you neither studied for or cheated for this class,"
                          " your grade doesn't look good...")
                    t.sleep(1)
                    print (f"Grade + 10\nYour grade is now {grade}%")
                    classes_done.append("english")
                    break
                # unkown input
                else:
                    print("I don't know what you mean")
                    continue
            continue
        # French path
        if action.lower() == "french" and "french" not in classes_done:
            print("You go to French in Mr.Potivin's class...")
            print("Your finals assignment for this class is to conjugate er"
                  "ir and re verbs")
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
                    grade += 20
                    print(f"Your grade is now {grade}%")
                    classes_done.append("french")
                    break
                # cheat path
                if action == "c" and "french" not in cheats:
                    print("You don't ahve anything to cheat with")
                    continue
                if action == "c" and "french" in cheats:
                    n = random.randint(0, 30)
                    if n >= 13:
                        print("You look under your mask to see a "
                              "whole Bescherelle stuffed under your mask."
                              " I don't know how you got it to"
                              " fit under there but it sure is useful")
                        grade += 25
                        print("Your grade is good\n Suspiciously good.....")
                        print(f"Grade + 25\nYour grade is now {grade}%")
                        classes_done.append("french")
                        break
                    if n < 13:
                        print("Oh no!\nYou got caught cheating!")
                        break
                # try your best path
                if action == "t":
                    grade += 10
                    print("You try your best to conjugate the verbs, "
                          "but because you didn't study your grade "
                          "doesn't look good...")
                    print (f"Grade + 10\nYour grade is now {grade}%")
                    classes_done.append("french")
                    break
                # unkown input
                else:
                    print("I dont know what you mean")
                    continue
            continue
        # History path
        if action.lower() == "history" and "history" not in classes_done:
            print("You go to history in Mme.Therien's class...")
            print("Your finals assignment for this class is to write "
                  "about the Battle of the Somme in WW1")
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
                    grade += 20
                    print("Becasue you grinded WW1 documentaries last night "
                          "you feel confident about the test...")
                    print("Your test isn't perfect, but it's pretty good")
                    print(f"Grade + 20\nYour grade is now {grade}")
                    classes_done.append("history")
                    break
                # cheat path
                if action == "c" and "history" not in cheats:
                    print("You have nothing to cheat with")
                    continue
                if action == "c" and "history" in cheats:
                    n = random.randint(0, 30)
                    if n >= 13:
                        print("You look under your mask to see the notes you "
                              "wrote yesterday about WW1, "
                              "this should be easy...")
                        grade += 25
                        print("Your grade is good\nSuspiciously good.....")
                        print(f"Grade + 25\nYour grade is now {grade}%")
                        classes_done.append("history")
                        break
                    if n < 13:
                        print("Oh no!\nYou got caught cheating!")
                        break
                # try your best path
                if action == "t":
                    grade += 10
                    print("You try your best to write the essay "
                          "but as you neither studied for or cheated for "
                          "this class, your grade doesn't look good...")
                    print (f"Grade + 10\nYour grade is now {grade}%")
                    classes_done.append("history")
                    break
                # unkown input
                else:
                    print("I don't know what you mean")
                    continue
            continue
        # Math path
        if action.lower() == "math" and "math" not in classes_done:
            print("You go to Math in Mr.Belle's class...")
            print("Your finals assignment for this class is on trigonometry"
                  "and the quadratic formula, I hope you've studied")
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
                    grade = grade + 20
                    print("Because you studied your trig skills, "
                          "you feel confident about this test...")
                    print("Your work isn't perfect, but its pretty good")
                    print(f"Grade + 20\nYour grade is now {grade}")
                    classes_done.append("math")
                    break
                # cheat path
                if action == "c" and "math" not in cheats:
                    print("You have nothing to cheat with")
                    continue
                if action == "c" and "math" in cheats:
                    n = random.randint(0, 30)
                    if n >= 13:
                        print("You look under your mask to find the "
                              "quadratic formula written there."
                              " Just what you needed...")
                        grade = grade + 25
                        print("Your grade is good\nSuspiciously good.....")
                        print(f"Grade + 25\nYour grade is now{grade}%")
                        classes_done.append("math")
                        break
                    if n < 13:
                        print("Oh no!\nYou got caught cheating!")
                        break
                # try your best path
                if action == "t":
                    grade = grade + 10
                    print("You try your best to write the test "
                          "but as you neither studied or cheated "
                          "for this class, your grade doesn't look " "good...")
                    print (f"Grade + 10\nYour grade is now {grade}%")
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
