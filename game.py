'''
Adventure Game
Version: 1.0
Author: Christopher Coon
Description:
This is a text-based adventure game where the player makes choices 
to navigate through a mysterious forest.
'''


# Welcome message and introduction
print("Welcome to the Adventure Game!")  
print("Your journey begins here...")

# Ask for the Player's name
player_name = input ('What is your name, adventurer?')

# Concatenate strings to create a personalized message.
print("Welcome, " + player_name + "! Your journey begins here.")

# Use an f-string to display the message in a more readable way.
print(f"Welcome, {player_name}! Your journey begins here.")

# Describe the starting area
starting_area = """
You find yourself in a dark forest.
The sound of rustling leaves fills the air.
A faint path lies ahead, leading deeper into the unknown...
"""
print(starting_area)

# Ask the player to make their first descision
decision = input("Do you wish to take the path? (Yes or No) ") .lower()

# Response based on the player's decision
if decision == "yes":
    print(f"Brave choice, {player_name}! You step onto the path and vetnture onward!")

elif decision == "no":
    print(f"{player_name}, you decide to wait. Perhaps courage will find you later.")

else:
    print("Confused, you stand still, unsure what to do.")
