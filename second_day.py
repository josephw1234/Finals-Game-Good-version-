from first_day import cheats, knowledge
import random as random
import time as t
import characters as c
import map as m

# List of classes that are done
classes_done = []


# Functions for endings
def good_ending():
    """80% plus grade ending"""
    print("Congratulations!!\n")
    t.sleep(1)
    print("That is an excelent grade...\n")
    t.sleep(1)
    print("Not only has your application to U of R been accepted, "
          "the've also decided to give you a \nfull-ride scholarship "
          "because of your good work!")
    t.sleep(2)
    print("\n\nThank you very much for playing, but this is only one of "
          " multiple endings...")
    print("\nPlay again to discover what they are")


def decent_ending():
    """50-79% ending"""
    print("\nCongrats, you made it through finals!")
    t.sleep(1)
    print("\nThough your grade wont be winning any sholarships, "
          "it was enough for your application to be accepted "
          " at the U of R")
    t.sleep(2)
    print("\n\nThank you very much for playing, but this is only one of "
          " multiple endings...")
    print("\nPlay again to discover what they are")


def bad_ending():
    """Bellow 50% ending"""
    print("\nOuch!")
    t.sleep(1)
    print("\nYour grade was less thn 50%, you know what that means...")
    t.sleep(1.5)
    print("\nYou failed!!!")
    t.sleep(1)
    print("\nYour application to the U of R has been declined,")
    print("but hey at least theres still summer school")
    t.sleep(2)
    print("\n\nThank you very much for playing, but this is only one of "
          " multiple endings...")
    print("Play again to discover what they are, and maybe you'll "
          "do better next time")


def caught_ending():
    """Ending for if you get caught cheating"""
    print('"HEY!!!!!!"')
    t.sleep(0.3)
    print(".")
    t.sleep(0.3)
    print(".")
    t.sleep(0.3)
    print(".")
    t.sleep(0.5)
    print('"I saw what you did there!"')
    t.sleep(1)
    print('"We take cheating very seriously, you\'re '
          'coming with me to the principal\'s office"')
    t.sleep(1)
    print("\nUh oh. this doesn't look good....")
    t.sleep(2)
    print("\nAt the principal's office you immediately get expelled "
          "for cheating")
    t.sleep(1)
    print("Your cheating history is now known to all universities "
          "you apply to, including the U of R which turns down your "
          "application immediately")
    t.sleep(1)
    print("\nMaybe cheating wasn't your best option...")
    t.sleep(3)
    print("\n\nThank you very much for playing, but this is only one of "
          " multiple endings...")
    print("\nPlay again to discover what they are, and maybe you'll "
          "do better next time")


def sus_ending():
    """Too good to be true 100% cheat ending"""
    print("\nWow!")
    t.sleep(1)
    print("\nYour grade is incredible!")
    t.sleep(0.5)
    print(".")
    t.sleep(0.5)
    print(".")
    t.sleep(0.5)
    print(".")
    t.sleep(0.5)
    print("A little too incredible....")
    t.sleep(1)
    print("\nUh oh....")
    t.sleep(1)
    print("\nYou're starting to look a little suspicious...")
    t.sleep(1)
    print("\nIt's almost impossible to get that good of a grade...")
    t.sleep(2)
    print("\nUnless.....")
    print(".")
    t.sleep(0.5)
    print(".")
    t.sleep(0.5)
    print(".")
    t.sleep(.5)
    print("YOU CHEATED!!!!")
    t.sleep(2)
    print("\nYour cheating history is now known to all universities "
          "you apply to, including the U of R which turns down your "
          "application immediately")
    t.sleep(1)
    print("\nMaybe cheating wasn't your best option...")
    t.sleep(3)
    print("\n\nThank you very much for playing, but this is only one of "
          " multiple endings...")
    print("\nPlay again to discover what they are, and maybe you'll "
          "do better next time")


def second_day(grade):
    """ Main function for second day"""
    message_1 = ("\nYou are in the main hall.\n"
                 "Which class do you go to?\n>")
    for action in message_1:
        # ending
        if "english" in classes_done and "history" in classes_done \
           and "french" in classes_done and "math" in classes_done:
            print("You've been to all your classes!")
            t.sleep(1)
            print("\nLet's see how good you did...")
            t.sleep(1)
            print(f"\nYour final grade is {grade}%")
            if grade == 100:
                sus_ending()
                break
            if grade < 80 and grade >= 50:
                decent_ending()
                break
            if grade < 50:
                bad_ending()
                break
            if grade < 80:
                good_ending()
            break
        # map print
        t.sleep(1)
        m.print_map()
        action = input(message_1)
        # English path
        if action.lower() == "english" and "english" not in classes_done:
            print("\nYou go to English class...\n")
            print(c.english_teacher)
            print("\nYour finals assignment for this class is to write "
                  "an essay about Shakespeare's Hamlet, I hopeyou've studied")
            print(f"\nThe test diffculty is {m.english_class.test_difficulty}")
            t.sleep(1)
            message = ("\nHow are you going to tackle this assignment?\n"
                       "Use your study knowledge, cheat, or try your best?\n"
                       "('k', 'c' or 't')\n>")
            for action in message:
                action = input(message)
                # knowledge path
                if action == "k" and 'englsih' not in knowledge:
                    print("\nYou didn't study for english")
                    continue
                    g = random.randint(18, 22)
                    grade += g
                if action == "k" and 'english' in knowledge:
                    print("\nBecasue you re-read Hamlet last night, you feel"
                          " confident in your ability to write this essay...")
                    t.sleep(1)
                    print("\nThe essay isn't perfect, but it's pretty good")
                    print(f"\nGrade + {g}\nYour grade is now {grade}")
                    classes_done.append("english")
                    break
                # cheat path
                if action == "c" and "english" not in cheats:
                    print("\nYou have nothing to cheat with")
                    continue
                if action == "c" and "english" in cheats:
                    n = random.randint(0, 30)
                    if n >= 15:
                        print("\nYou look under your mask to see the notes you"
                              " wrote yesterday which helps you "
                              "write your essay...")
                        t.sleep(1)
                        g = 25
                        grade += g
                        print("\nYour grade is good\nSuspiciously good.....")
                        print(f"\nGrade + {g}\nYour grade is now {grade}%")
                        classes_done.append("english")
                        break
                    if n < 15:
                        t.sleep(2)
                        print()
                        caught_ending()
                        break
                # try your best path
                if action == "t":
                    g = random.randint(8, 12)
                    grade += g
                    print("\nYou try your best to write the essay but as "
                          "you neither studied for or cheated for this "
                          "\nclass, your grade doesn't look good...")
                    t.sleep(1)
                    print (f"\nGrade + {g}\nYour grade is now {grade}%")
                    classes_done.append("english")
                    break
                # unkown input
                else:
                    print("\nI don't know what you mean")
                    continue
            continue
        # French path
        if action.lower() == "french" and "french" not in classes_done:
            print("\nYou go to French class...\n")
            print(c.french_teacher)
            print("\nYour finals assignment for this class is to conjugate er"
                  ", ir and re verbs")
            print(f"\nThe test diffculty is {m.french_class.test_difficulty}")
            t.sleep(1)
            message = ("\nHow are you going to tackle this assignment?\n"
                       "Use your study knowledge, cheat, or try your best?\n"
                       "('k', 'c' or 't')\n>")
            for action in message:
                action = input(message)
                # knowledge path
                if action == "k":
                    print("\nBecause you studied your verbs, "
                          "you know exactly what to do...")
                    t.sleep(1)
                    print("\nYou're not quite fluent yet, "
                          "but your grade is still pretty good")
                    g = random.randint(22, 25)
                    grade += g
                    print(f"\nGrade + {g}\nYour grade is now {grade}%")
                    classes_done.append("french")
                    break
                # cheat path
                if action == "c" and "french" not in cheats:
                    print("\nYou don't have anything to cheat with")
                    continue
                if action == "c" and "french" in cheats:
                    n = random.randint(0, 30)
                    if n >= 10:
                        print("\nYou look under your mask to see a "
                              "whole Bescherelle stuffed under your mask."
                              " I don't know how you got it to"
                              " fit under there but it sure is useful")
                        t.sleep(1)
                        g = 25
                        grade += g
                        print("\nYour grade is good\n Suspiciously good.....")
                        print(f"\nGrade + {g}\nYour grade is now {grade}%")
                        classes_done.append("french")
                        break
                    if n < 10:
                        t.sleep(2)
                        print()
                        caught_ending()
                        break
                # try your best path
                if action == "t":
                    g = random.randint(10, 13)
                    grade += g
                    print("\nYou try your best to conjugate the verbs, "
                          "but because you didn't study your grade "
                          "doesn't look good...")
                    t.sleep(1)
                    print (f"\nGrade + {g}\nYour grade is now {grade}%")
                    classes_done.append("french")
                    break
                # unkown input
                else:
                    print("\nI dont know what you mean")
                    continue
            continue
        # History path
        if action.lower() == "history" and "history" not in classes_done:
            print("\nYou go to history class...\n")
            print(c.history_teacher)
            print("\nYour finals assignment for this class is to write "
                  "about the Battle of the Somme in WW1")
            print(f"\nThe test diffculty is {m.history_class.test_difficulty}")
            t.sleep(1)
            message = ("\nHow are you going to tackle this assignment?\n"
                       "Use your study knowledge, cheat, or try your best?\n"
                       "('k', 'c' or 't')\n>")
            for action in message:
                action = input(message)
                # knowledge path
                if action == "k" and 'history' not in knowledge:
                    print("\nYou didn't study for history")
                    continue
                if action == "k" and 'history' in knowledge:
                    g = random.randint(18, 22)
                    grade += g
                    print("\nBecasue you grinded WW1 documentaries last night "
                          "you feel confident about the test...")
                    t.sleep(1)
                    print("\nYour test isn't perfect, but it's pretty good")
                    print(f"\nGrade + {g}\nYour grade is now {grade}")
                    classes_done.append("history")
                    break
                # cheat path
                if action == "c" and "history" not in cheats:
                    print("\nYou have nothing to cheat with")
                    continue
                if action == "c" and "history" in cheats:
                    n = random.randint(0, 30)
                    if n >= 15:
                        print("\nYou look under your mask to see the notes you"
                              " wrote yesterday about WW1,\n"
                              "this should be easy...")
                        t.sleep(1)
                        g = 25
                        grade += g
                        print("\nYour grade is good\nSuspiciously good.....")
                        print(f"\nGrade + {g}\nYour grade is now {grade}%")
                        classes_done.append("history")
                        break
                    if n < 10:
                        t.sleep(2)
                        print()
                        caught_ending()
                        break
                # try your best path
                if action == "t":
                    g = random.randint(8, 12)
                    grade += g
                    print("\nYou try your best to write the essay "
                          "but as you neither studied for or cheated for "
                          "this class, your grade doesn't look good...")
                    print (f"\nGrade + {g}\nYour grade is now {grade}%")
                    classes_done.append("history")
                    break
                # unkown input
                else:
                    print("\nI don't know what you mean")
                    continue
            continue
        # Math path
        if action.lower() == "math" and "math" not in classes_done:
            print("\nYou go to Math class...\n")
            print(c.math_teacher)
            print(f"\nThe test diffculty is {m.math_class.test_difficulty}")
            print("\nThe finals assignment for this class is on trigonometry"
                  " and the quadratic formula, I hope \nyou've studied")
            t.sleep(1)
            message = ("\nHow are you going to tackle this assignment?\n"
                       "Use your study knowledge, cheat, or try your best?\n"
                       "('k', 'c' or 't')\n>")
            for action in message:
                action = input(message)
                # knowledge path
                if action == "k" and 'math' not in knowledge:
                    print("\nYou didn't study for math")
                    continue
                if action == "k" and 'math' in knowledge:
                    g = random.randint(17, 20)
                    grade += g
                    print("\nBecause you studied your trig skills, "
                          "you feel confident about this test...")
                    t.sleep(1)
                    print("\nYour work isn't perfect, but its pretty good")
                    print(f"\nGrade + {g}\nYour grade is now {grade}")
                    classes_done.append("math")
                    break
                # cheat path
                if action == "c" and "math" not in cheats:
                    print("\nYou have nothing to cheat with")
                    continue
                if action == "c" and "math" in cheats:
                    n = random.randint(0, 30)
                    if n >= 10:
                        print("\nYou look under your mask to find the "
                              "quadratic formula written there."
                              "\nJust what you needed...")
                        t.sleep(1)
                        g = 25
                        grade += g
                        print("\nYour grade is good\nSuspiciously good.....")
                        print(f"\nGrade + {g}\nYour grade is now{grade}%")
                        classes_done.append("math")
                        break
                    if n < 10:
                        print("Oh no!\nYou got caught cheating!")
                        break
                # try your best path
                if action == "t":
                    g = random.randint(7, 9)
                    grade += g
                    print("\nYou try your best to write the test "
                          "but as you neither studied or cheated "
                          "for this class, your grade doesn't look " "good...")
                    t.sleep(1)
                    print (f"\nGrade + {g}\nYour grade is now {grade}%")
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
            print("\nYou've already been to english")
            continue
        if action.lower() == "math" and "math" in classes_done:
            print("\nYou've already been to math")
            continue
        if action.lower() == "history" and "history" in classes_done:
            print("\nYou've already been to history")
            continue
        if action.lower() == "french" and "french" in classes_done:
            print("\nYou've already been to french")
            continue
        # unkown input
        else:
            print("\nI don't know what you mean")
