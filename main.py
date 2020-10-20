# Joseph Woodward
# CS 30 Q1 AM
# Oct 13 2020
# Finals Game (For map assignment)

# Imports
import first_day as first
import second_day as second
import time as t
import characters as c
import map as m

# Intro message
print("Hello there!\n")
t.sleep(1)
print("You currently have 4 hours to prepare for your finals"
      " tomorrow at Campbell Colleigate\n")
t.sleep(1)
print("You can chose how to prepare either by studying like a"
      " good student or trying to sneak some  extra notes into"
      " your class....\nBut watch out! If you get caught cheating"
      " it's gonna cost you big time.\n")
t.sleep(1)
print("Here's a general idea of what your room looks like:")
m.print_map1()
t.sleep(1)
print("\nIf you look hard enough, you might be able to find something "
      " useful around here...")
print("Type 'map' to check back in on this anytime")
t.sleep(1)
print("\nGood luck!")
t.sleep(1)
print("\nType 'done' to skip the rest of your turns "
      "and go straight to Campbell")
print("Type 'inventory' to check your inventory")
t.sleep(.5)
print()

# First day
turns_left = 4
first.first_day(turns_left, True, True)

# Transition
print("It's getting late....")
t.sleep(1)
print("\n\n\n....You decide to go to bed for the night....\n\n\n")
print("You enter Campbell Colleigate ready to do your finals...")
t.sleep(1)

# Second day
print("Type 'map' to see your map and available classes")
grade = 0
second.second_day(grade)
