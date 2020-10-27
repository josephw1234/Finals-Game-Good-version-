import random as r
from tabulate import tabulate

# Lists of things you've cheated/studied
knowledge = []
cheats = []

# inventory
items = {}

# list for map updates
map_updates = []

# lists of what classes you can cheat/study for
knowledge_subjects = ["Math", "French", "History", "English"]
cheat_subjects = ["Math", "French", "History", "English"]

# Message for look path
message_1 = ("\nYou look around your room and see your desk and bookshelf\n"
             "Look in one of these or leave? \n>")

# Message for bookshelf path
message_2 = ("\nYou see a French English dictionary and a History textbook,\n"
             "these might help you, take them?\n>")

# Message for desk path
message_3 = ("\nYou see a calculator and a pencil, take them?\n>")


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


def first_day(turns_left, bookshelf, desk):
    """Main function for first day, urns left is how many
       study/cheat actions the player can take, desk and bookshelf
       should be set to True"""
    while turns_left > 0:
        message = (f"\nCheat, study or look around?\n"
                   f"(You have {turns_left} hours left)\n>")
        for keypress in message:
            keypress = input(message)
            # map
            if keypress.lower() == "map":
                print_map1()
                break
            # Study path
            if keypress.lower() == "study":
                subject = input(f"\nWhat sublect? "
                                f"({', '.join(knowledge_subjects)})\n>")
                # already done
                if subject.lower() in knowledge:
                    print(f"\nYou've already studied for {subject}")
                    continue
                # items paths
                if subject.lower() == "english" and "Pencil" in items:
                    n = r.randint(1, 3)
                    if n == 1:
                        print("\nOh no!\nYou were writing so hard that "
                              "you broke your pencil")
                        print("\nYou can still study, "
                              "but it's gonna take some time")
                        turns_left -= 1
                        knowledge.append(subject)
                        knowledge_subjects.remove(subject.title())
                        print(f"\nYou studied for {subject}")
                        break
                    if n >= 2:
                        print("\nWith your pencil, studying for english"
                              " barely takes any time at all...")
                        knowledge.append(subject)
                        knowledge_subjects.remove(subject.title())
                        print(f"\nYou studied for {subject}")
                        break
                if subject.lower() == "math" and "Calculator" in items:
                    n = r.randint(1, 3)
                    if n == 1:
                        print("\nOh no!\nYour calculator ran out of battery")
                        print("\nYou can still study, but it's "
                              "gonna take some time")
                        turns_left -= 1
                        knowledge.append(subject)
                        knowledge_subjects.remove(subject.title())
                        print(f"\nYou studied for {subject}")
                        break
                    if n >= 2:
                        print("\nWith your calculator, studying for math"
                              " barely takes any time at all...")
                        knowledge.append(subject)
                        knowledge_subjects.remove(subject.title())
                        print(f"\nYou studied for {subject}")
                        break
                if subject.lower() == "history" and "Textbook" in items:
                    n = r.randint(1, 3)
                    if n == 1:
                        print("\nOh no!\nThe textbook was so boring you "
                              "fell asleep while reading")
                        print("\nYou can still study, "
                              "but you wasted some time")
                        turns_left -= 1
                        knowledge.append(subject)
                        knowledge_subjects.remove(subject.title())
                        print(f"\nYou studied for {subject}")
                        break
                    if n >= 2:
                        print("\nWith your textbook, studying for history"
                              " barely takes any time at all...")
                        knowledge.append(subject)
                        knowledge_subjects.remove(subject.title())
                        print(f"\nYou studied for {subject}")
                        break
                if subject.lower() == "french" and "Dictionary" in items:
                    n = r.randint(1, 3)
                    if n == 1:
                        print("\nOh no!\nYour cat got a little hungry and "
                              "decided to rip apart your dictionary")
                        print("\nYou can still study, but it's gonna "
                              "take some time")
                        turns_left -= 1
                        knowledge.append(subject)
                        knowledge_subjects.remove(subject.title())
                        print(f"\nYou studied for {subject}")
                        break
                    if n >= 2:
                        print("\nWith your dictionary, studying for french"
                              " barely takes any time at all...")
                        knowledge.append(subject)
                        knowledge_subjects.remove(subject.title())
                        print(f"\nYou studied for {subject}")
                        break
                # no items paths
                if subject.lower() == "english" and "Pencil" not in items:
                    turns_left -= 1
                    knowledge.append(subject)
                    knowledge_subjects.remove(subject.title())
                    print(f"\nYou studied for {subject}")
                    break
                if subject.lower() == "math" and "Calculator" not in items:
                    knowledge_subjects.remove(subject.title())
                    turns_left -= 1
                    knowledge.append(subject)
                    print(f"\nYou studied for {subject}")
                    break
                if subject.lower() == "history" and "Textbook" not in items:
                    turns_left -= 1
                    knowledge.append(subject)
                    knowledge_subjects.remove(subject.title())
                    print(f"\nYou studied for {subject}")
                    break
                if subject.lower() == "french" and "Dictionary" not in items:
                    turns_left -= 1
                    knowledge.append(subject)
                    knowledge_subjects.remove(subject.title())
                    print(f"\nYou studied for {subject}")
                    break
                # unknown input
                else:
                    print("\nThat isn't a subject")
                    continue
            # Cheat path
            if keypress.lower() == "cheat":
                subject = input(f"\nWhat sublect? "
                                f"({', '.join(cheat_subjects)})\n>")
                if subject.lower() in cheats:
                    print(f"\nYou've already cheated on {subject}")
                    break
                if subject.lower() == "english" or \
                   subject.lower() == "french"\
                   or subject.lower() == "history" or \
                   subject.lower() == "math":
                        cheat_subjects.remove(subject.title())
                        cheats.append(subject)
                        turns_left -= 1
                        print(f"\nYou cheated for {subject}")
                        break
                else:
                    print("\nThat isn't a subject")
                    continue
            # Look path
            if keypress.lower() == "look":
                active = True
                while active == True:
                    action = input(message_1)
                    if action == "look":
                        choice = input("\nDesk or bookshelf\n>")
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
                            print("\nYou've already looked in there")
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
                            print("\nYou've already looked there")
                            continue
                    # Leave path
                    if action.lower() == "leave":
                        turns_left -= 1
                        active = False
                        break
                    else:
                        print("\nI don't know what you mean")
                break
            # Inventory check path
            if keypress.lower() == "inventory":
                if items == {}:
                    print("\nYour inventory is empty")
                for item, desc in items.items():
                    print()
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
                print("\nI don't know what you mean")
                continue
