import time as t
import random as r
from tabulate import tabulate

# Lsits and dicts
knowledge = []
cheats = []
items = {}
map_updates = []

# Message for look path
message_1 = ("You look around your room and see your desk and bookshelf\n"
             "Look in one of these or leave? \n>")

# Message for bookshelf path
message_2 = ("You see a French English dictionary and a History textbook,\n"
             "these might help you, take them?\n>")

# Message for desk path
message_3 = ("You see a calculator and a pencil, take them?\n>")

# Message for cheat/study path
subject_message = ("What sublect? (English, french, Math, history)\n>")


# Functions for adding items
def add_pencil():
    items['Pencil'] = {"description": "A pencil usefull for writing essays",
                       "helps with": "English"
                       }


def add_calculator():
    items['Calculator'] = {"description": "A scientific calculator for"
                                          " all you math needs",
                           "helps with": "Math"
                           }


def add_dictionary():
    items['Dictionary'] = {"description": "Paperback Google Translate",
                           "helps with": "English"
                           }


def add_textbook():
    items['Textbook'] = {"description": "A history textbook",
                         "helps with": "History"
                         }


def print_map1():
    """Map function for first day"""
    # varaibles for desk/bookshelf
    desk = "Desk"
    bookshelf = "Bookshelf"
    # updates for if desk/bookshelf is empty
    if "bookshelf" in map_updates:
        bookshelf = "Bookshelf(empty)"
    if "desk" in map_updates:
        desk = "Desk(empty)"
    # print map
    map = [['', 'Studying Table'],
           [' ', 'Looking around'],
           [desk, '', bookshelf]]
    print(tabulate(map, tablefmt="grid"))


# Main function
# Turns left is how many study/cheat actions the player can take
# desk and bookshlef should be set to True
def first_day(turns_left, bookshelf, desk):
    while turns_left > 0:
        message = (f"Cheat, study or look around?\n"
                   f"(You have {turns_left} hours left)\n>")
        for keypress in message:
            keypress = input(message)
            # map
            if keypress.lower() == "map":
                print_map1()
                break
            # Study path
            if keypress.lower() == "study":
                subject = input(subject_message)
                # already done
                if subject.lower() in knowledge:
                    print(f"You've already studied for {subject}")
                    continue
                # items paths
                if subject.lower() == "english" and "Pencil" in items:
                    n = r.randint(1, 3)
                    if n == 1:
                        print("Oh no!\nYou were writing so hard that "
                              "you broke your pencil")
                        print("You can still study, "
                              "but it's gonna take some time")
                        turns_left -= 1
                        knowledge.append(subject)
                        print(f"You studied for {subject}")
                        break
                    if n >= 2:
                        print("With your pencil, studying for english"
                              " barely takes any time at all...")
                        knowledge.append(subject)
                        print(f"You studied for {subject}")
                        break
                if subject.lower() == "math" and "Calculator" in items:
                    n = r.randint(1, 3)
                    if n == 1:
                        print("Oh no!\nYour calculator ran out of battery")
                        print("You can still study, but it's "
                              "gonna take some time")
                        turns_left -= 1
                        knowledge.append(subject)
                        print(f"You studied for {subject}")
                        break
                    if n >= 2:
                        print("With your calculator, studying for math"
                              " barely takes any time at all...")
                        knowledge.append(subject)
                        print(f"You studied for {subject}")
                        break
                if subject.lower() == "history" and "Textbook" in items:
                    n = r.randint(1, 3)
                    if n == 1:
                        print("Oh no!\nThe textbook was so boring you "
                              "fell asleep while reading")
                        print("You can still study, but you wasted some time")
                        turns_left -= 1
                        knowledge.append(subject)
                        print(f"You studied for {subject}")
                        break
                    if n >= 2:
                        print("With your textbook, studying for history"
                              " barely takes any time at all...")
                        knowledge.append(subject)
                        print(f"You studied for {subject}")
                        break
                if subject.lower() == "french" and "Dictionary" in items:
                    n = r.randint(1, 3)
                    if n == 1:
                        print("Oh no!\nYour cat got a little hungry and "
                              "decided to rip apart your dictionary")
                        print("You can still study, but it's gonna "
                              "take some time")
                        turns_left -= 1
                        knowledge.append(subject)
                        print(f"You studied for {subject}")
                        break
                    if n >= 2:
                        print("With your dictionary, studying for french"
                              " barely takes any time at all...")
                        knowledge.append(subject)
                        print(f"You studied for {subject}")
                        break
                # no items paths
                if subject.lower() == "english" and "Pencil" not in items:
                    turns_left -= 1
                    knowledge.append(subject)
                    print(f"You studied for {subject}")
                    break
                if subject.lower() == "math" and "Calculator" not in items:
                    turns_left -= 1
                    knowledge.append(subject)
                    print(f"You studied for {subject}")
                    break
                if subject.lower() == "history" and "Textbook" not in items:
                    turns_left -= 1
                    knowledge.append(subject)
                    print(f"You studied for {subject}")
                    break
                if subject.lower() == "french" and "Dictionary" not in items:
                    turns_left -= 1
                    knowledge.append(subject)
                    print(f"You studied for {subject}")
                    break
                # unknown input
                else:
                    print("That isn't a subject")
                    continue
            # Cheat path
            if keypress.lower() == "cheat":
                subject = input(subject_message)
                if subject.lower() in cheats:
                    print(f"You've already cheated on {subject}")
                    break
                if subject.lower() == "english" or \
                   subject.lower() == "french"\
                   or subject.lower() == "history" or \
                   subject.lower() == "math":
                        cheats.append(subject)
                        turns_left -= 1
                        print(f"You cheated for {subject}")
                        break
                else:
                    print("That isn't a subject")
                    continue
            # Look path
            if keypress.lower() == "look":
                active = True
                while active == True:
                    action = input(message_1)
                    if action == "look":
                        choice = input("Desk or bookshelf\n>")
                        # Bookshelf path
                        if choice.lower() == "bookshelf" and \
                           bookshelf == True:
                            item = input(message_2)
                            if item.lower() == "yes":
                                add_dictionary()
                                add_textbook()
                                bookshelf = False
                                map_updates.append("bookshelf")
                                continue
                            if item.lower() == "no":
                                continue
                        if choice.lower() == "bookshelf" and \
                           bookshelf == False:
                            print("You've already looked in there")
                            continue
                        # Desk path
                        if choice.lower() == "desk" and \
                           desk == True:
                            item = input(message_3)
                            if item.lower() == "yes":
                                add_pencil()
                                add_calculator()
                                desk = False
                                map_updates.append("desk")
                                continue
                            if item.lower() == "no":
                                continue
                        if choice.lower() == "desk" and \
                           desk == False:
                            print("You've already looked there")
                    # Leave path
                    if action.lower() == "leave":
                        turns_left -= 1
                        active = False
                        break
                break
            # Inventory check path
            if keypress.lower() == "inventory":
                if items == {}:
                    print("Your inventory is empty")
                for item, desc in items.items():
                    print(f"Item: {item}")
                    print(f"\tDescription: {desc['description']}")
                    print(f"\tHelps with: {desc['helps with']}")
                    print()
                continue
            # Done path
            if keypress.lower() == "done":
                turns_left = 0
                break
            # Unknown input
            else:
                print("I don't know what you mean")
                continue
