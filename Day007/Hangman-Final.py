from hangman_art import stages, logo, welcome
from hangman_words import word_list
import random
from replit import clear

# Print welcome
print(logo)
# Print hangman
print(welcome)

end_of_game = False
words_list = word_list
chosen_word = random.choice(words_list)
word_length = len(chosen_word)

# print(f'\nPssst, the solution is {chosen_word}.')

# Create a variable called 'lives' to keep track of the number of lives left. 
# Set 'lives' to equal 6.

lives = 6

# Testing code

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess_list = []
    guess = input("Guess a letter: ").lower()
    guess_list.append(guess)
    print(guess_list)
    clear()

    if guess not in guess_list:
      continue

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter
            print(f"Good guess! {lives} attempts left, still. Keep going.")


    if guess not in chosen_word:
        lives -= 1
        print(f"\nTry again! {lives} guesses remaining.\n")

        if lives == 0:
            end_of_game = True
            print("You lose.")
            break

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}\n")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])

print(f"The word is: {chosen_word}")