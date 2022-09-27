from ascii import caesar_cipher

print(caesar_cipher)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input(f"Type 'encode' to encrypt, type 'decode' to decrypt:\n\n")
print("")
text = input(f"Type your message:\n\n").lower()
print("")
shift = int(input(f"Type the shift number:\n\n"))

# Encrypt' function takes the 'text' and 'shift' as inputs.

def encrypt(user_text, shift_index):

    encrypted_text = ""

    for i in user_text:
        
        current_index = alphabet.index(i)
        new_index = current_index + shift_index

        # What if the current index is 26, and the we run out of indexed alphabets?
        if new_index > 25:
            new_index = current_index + shift_index - 26

            # Use multiple of 26 to deal with values greater than 26

        # Get new alphabet with the new index from the alphabet list    
        new_alphabet = alphabet[new_index]

        # Join the letters together
        encrypted_text += new_alphabet

    safety = input(f"Are you somewhere safe, with no-one behind or next to you? Type 'yes' or 'no':\n\n").lower()
    if safety == "yes":    
        print(f"The encrypted message is: {encrypted_text}. Clear the session before you leave.")
    else:
        print("Please go to a safe place before you run the program again.")


def decrypt(user_text, shift_index):

    decrypted_text = ""

    for i in user_text:
        
        current_index = alphabet.index(i)
        new_index = current_index - shift_index

        # Get new alphabet with the new index from the alphabet list    
        new_alphabet = alphabet[new_index]

        # Join the letters together
        decrypted_text += new_alphabet

    safety = input(f"Are you somewhere safe, with no-one behind or next to you? Type 'yes' or 'no':\n").lower()
    if safety == "yes":    
        print(f"The encrypted message is: {decrypted_text}. Clear the session before you leave.")
    else:
        print("Please go to a safe place before you run the program again.")

# Call the encrypt function and pass in the user inputs.

if direction == "encode":
    encrypt(user_text=text, shift_index=shift)
else:
    decrypt(user_text=text, shift_index=shift)