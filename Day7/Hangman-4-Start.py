#Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print('''
 /$$      /$$           /$$                                            
| $$  /$ | $$          | $$                                            
| $$ /$$$| $$  /$$$$$$ | $$  /$$$$$$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$ 
| $$/$$ $$ $$ /$$__  $$| $$ /$$_____/ /$$__  $$| $$_  $$_  $$ /$$__  $$
| $$$$_  $$$$| $$$$$$$$| $$| $$      | $$  \ $$| $$ \ $$ \ $$| $$$$$$$$
| $$$/ \  $$$| $$_____/| $$| $$      | $$  | $$| $$ | $$ | $$| $$_____/
| $$/   \  $$|  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$ | $$ | $$|  $$$$$$$
|__/     \__/ \_______/|__/ \_______/ \______/ |__/ |__/ |__/ \_______/
''')

end_of_game = False
word_list = ["aardvark", "camel", "chewbaca", "dinosaur", "elephant", "falcon", "giraffe", "hippopotamus", "iguana", "jaguar", "kangaroo", "lemur", "manatee", "narwhal", "octopus", "panda", "quail", "rhinoceros", "salamander", "tiger", "unicorn", "vulture", "wombat", "xenops", "yak", "zebra"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

lives = 6

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            print(f"Good guess! {lives} attempts left, still. Keep going.")


    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        print(f"\nTry again! {lives} guesses remaining.\n")

        if lives == 0:
            end_of_game = True
            print("You lose.")
            break
        # else:
        #     print(stages[lives])
        #     break

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}\n")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])