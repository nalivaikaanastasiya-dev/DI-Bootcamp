# Daily challenge GOLD: Caesar Cypher
# In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

# For example, with a left shift of 3 –> D would be replaced by A,
# –> E would become B, and so on.

# The method is named after Julius Caesar, who used it in his private correspondence.

# Create a python program that encrypts and decrypts messages with ceasar cypher.
# The user enters the program, and then the program asks him if he wants to encrypt or decrypt, and then execute encryption/decryption on a given message and a given shift.

# Hint:

# for letter in text:
#     cypher_text += chr(ord(letter) + 3)

def encrypt_caesar(text, shift):
    """Encrypts a message using the Caesar cipher, handling alphabet wrap-around."""
    result = ""
    # Normalize the shift value to be within 0 and 25
    shift = shift % 26

    for char in text:
        if 'a' <= char <= 'z':
            # Handle lowercase letters
            start = ord('a')
            # Calculate new position: (current position + shift) % 26 + ASCII base
            shifted_ord = start + (ord(char) - start + shift) % 26
            result += chr(shifted_ord)
        elif 'A' <= char <= 'Z':
            # Handle uppercase letters
            start = ord('A')
            shifted_ord = start + (ord(char) - start + shift) % 26
            result += chr(shifted_ord)
        else:
            # Keep other characters (spaces, punctuation) as they are
            result += char
    return result

# --- Interactive Program Start ---

print("Caesar Cipher Encryption Program")
print("---------------------------------------")

# 1. Prompt for the message
message = input("Enter the message to encrypt: ")

# 2. Prompt for the shift value
while True:
    try:
        shift_value = int(input("Enter the numerical shift (e.g., 3): "))
        break
    except ValueError:
        print("Error. Please enter a whole number.")

# 3. Encrypt and display the result
encrypted_message = encrypt_caesar(message, shift_value)

print("\n--- Result ---")
print(f"Original Message: {message}")
print(f"Shift Used: {shift_value}")
print(f"Encrypted Message: **{encrypted_message}**")
print("--------------\n")
