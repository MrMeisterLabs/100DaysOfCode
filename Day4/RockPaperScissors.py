# Import the random module

import random

# Create multiline string representations of rock, paper, and scissors (copied from course notes)
# Link to graphics: https://replit.com/@appbrewery/rock-paper-scissors-start#main.py

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

options = [rock, paper, scissors]

players_selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n\n"))
print(f"\nPlayer chose: {options[players_selection]}")

computers_selection = random.randint(0, 2)
print(f"Computer chose: {options[computers_selection]}")

if players_selection >= 3 or players_selection < 0:
    print("Invalid number. Play the game again, LOSER!")
elif players_selection == 0 and computers_selection == 2:
    print("You defeated me!")
elif computers_selection == 0 and players_selection == 2:
    print("Haha! I beat you!")
elif computers_selection > players_selection:
    print("You just love losing, don't you? Try again?")
elif players_selection > computers_selection:
    print("You defeated me. Darn it!")
elif computers_selection == players_selection:
    print("It's a draw. Let's play again!")


# # Create a list of the play options

# options = [rock, paper, scissors]

# # Create a variable to store the user's choice

# player_choice = int(input("What do you choose? Type 1 for Rock, 2 for Paper, or 3 for Scissors."))

# # Create a variable to store the computer's choice

# computer_choice = random.randint(1, 3)

# # Print the user's choice

# print(f"You chose: {player_choice}")