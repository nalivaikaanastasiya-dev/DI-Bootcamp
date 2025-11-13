# Goal: Decode a hidden message from a matrix string by reading column-by-column,
# filtering for letters, and replacing non-letter sequences with a single space.

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
