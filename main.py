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
print("Type 'done' to skip the rest of your turns "
      "and go straight to Campbell")
print("Type 'inventory' to check your inventory")
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
