# Daily challenge Gold: Solve the Matrix

# Goal: Decrypt a hidden message from a matrix string by processing it column-wise and filtering characters.

# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# Python Basics
# Conditionals
# Loops
# Functions
# Lists (2D lists/matrices)
# String Manipulation

# Key Python Topics:

# Strings
# Lists (2D lists)
# Loops (for loops)
# Conditional statements (if, else)
# String methods (.isalpha(), etc.)
# String concatenation.

# Instructions:

# You are given a “Matrix” string:

# MATRIX_STR = '''
# 7ir
# Tsi
# h%x
# i ?
# sM# 
# $a 
# #t%'''       

# This represents a grid of characters, and your task is to decode the hidden message within.

# Understanding the Matrix:

# Imagine this string arranged in rows and columns, forming a grid.
# To work with it in Python, you’ll need to transform this string into a 2D list (a list of lists), where each inner list represents a row.

# Step 1: Transforming the String into a 2D List

# Step 2: Processing Columns

# Neo reads the matrix column by column, from top to bottom, starting from the leftmost column.
# You’ll need to write code that iterates through the columns of your 2D list.
# Think about how you can access the elements of a 2D list by column.

# Step 3: Filtering Alpha Characters

# only select alpha characters (letters).
# For each character in a column, check if it’s an alpha character.
# If it is, add it to a temporary string.
# Think about how you can check if a character is an alphabet letter.

# Step 4: Replacing Symbols with Spaces

# Replace every group of symbols (non-alpha characters) between two alpha characters with a space.
# After you have gathered the alpha characters, you will need to iterate through them, and where there are non alpha characters between them, you will insert a space.
# Think about how you can keep track of when you encounter an alphabet character, and when you encounter a non alphabet character.

# Step 5: Constructing the Secret Message

# Combine the filtered and processed characters to form the decoded message.
# Print the decoded message.

# Example:

# MATRIX_STR = '''
# 7ii
# Tsx
# h%?
# i #
# sM 
# $a 
# #t%''' 

# # Step 1: Convert matrix_string to a 2D list (matrix)
# matrix = []
# # ... code to create matrix ...

# # Step 2: Iterate through columns
# # ... code to iterate through columns ...

# # Step 3: Filter alpha characters
# # ... code to filter alpha characters ...

# # Step 4: Replace symbols with spaces
# decoded_message = ""
# # ... code to replace symbols with spaces ...

# # Step 5: Print the decoded message
# print(decoded_message)

MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''

def decode_matrix(matrix_string):
    """
    Decodes a message from a multi-line string by reading it column-by-column,
    filtering for alphabetic characters, and replacing sequences of non-letters
    between two letters with a single space.
    """
    # Step 1: Convert the multi-line string into a 2D list (matrix)
    
    # 1. Clean up and split the input string into rows
    rows = matrix_string.strip().split('\n')
    
    # 2. Determine the maximum width to handle misaligned rows
    if not rows:
        return "Error: Empty matrix provided."
        
    max_cols = max(len(row) for row in rows)
    
    # 3. Pad shorter rows with spaces and convert to list of lists (the matrix)
    matrix = [list(line.ljust(max_cols)) for line in rows]
    num_rows = len(matrix)

    # Step 2: Build the raw stream of characters (column by column)
    raw_stream = ""
    for col in range(max_cols):
        for row in range(num_rows):
            # This is the sequence of characters as Neo reads the matrix
            raw_stream += matrix[row][col]

    # Step 3 & 4: Filter alpha characters and replace symbol sequences with spaces
    decoded_message = ""
    # Flag to track if we are currently inside a non-alphabetic sequence.
    # This prevents multiple spaces from being inserted for multiple consecutive symbols.
    in_symbol_sequence = False 

    for char in raw_stream:
        if char.isalpha():
            # If the character is a letter, append it directly
            decoded_message += char
            in_symbol_sequence = False # Reset the flag
        else: # The character is a symbol, number, or space (non-alpha)
            # We insert a space ONLY IF:
            # 1. The decoded message is not empty (i.e., not leading symbols)
            # 2. The *last* character we appended was a letter (decoded_message[-1].isalpha())
            # 3. We are NOT already inside a symbol sequence (in_symbol_sequence is False)
            if decoded_message and decoded_message[-1].isalpha() and not in_symbol_sequence:
                decoded_message += ' '
                in_symbol_sequence = True
                
            # If in_symbol_sequence is True, we simply skip the current symbol 
            # (it's already represented by the single space we previously added).
            
    # Step 5: Compose and print the secret message
    # Use .strip() to remove any trailing space that might have been added 
    # if the stream ended on a symbol.
    return decoded_message.strip()

# --- Execution ---

secret_message = decode_matrix(MATRIX_STR)

print(f"Original Matrix:\n{MATRIX_STR}")
print("-" * 30)
print(f"Decoded Message: {secret_message}")

# Example of a fully decoded message would be 'This is a matrix' 
# if the symbols were perfectly aligned to separate the words.