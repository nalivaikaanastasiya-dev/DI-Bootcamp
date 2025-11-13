# Exercise 1 : What’s your name ?
# Write a function called get_full_name() that takes three arguments: 1: first_name, 2: middle_name 3: last_name.
# middle_name should be optional, if it’s omitted by the user, the name returned should only contain the first and the last name.
# For example, get_full_name(first_name="john", middle_name="hooker", last_name="lee") will return John Hooker Lee.
# But get_full_name(first_name="bruce", last_name="lee") will return Bruce Lee.

def get_full_name(first_name, last_name, middle_name=None):
    
    # Format the first and last name
    formatted_first = first_name.title()
    formatted_last = last_name.title()

    if middle_name:
        # If a middle name is provided, include it
        formatted_middle = middle_name.title()
        full_name = f"{formatted_first} {formatted_middle} {formatted_last}"
    else:
        # If the middle name is omitted, use only first and last name
        full_name = f"{formatted_first} {formatted_last}"

    return full_name

# Example 1: Using all three arguments (positional)
name1 = get_full_name("john", "lee", "hooker")
print(f"1. With three names: {name1}")

# Example 2: Omitting the middle name
# Using keyword arguments for clarity
name2 = get_full_name(first_name="bruce", last_name="lee")
print(f"2. With two names: {name2}")

# Example 3: Using keyword arguments with a middle name
name3 = get_full_name(last_name="king", first_name="B.B.", middle_name="blues")
print(f"3. Using keyword arguments: {name3}")

# Exercise 2 : From English to Morse
# Instructions
# Write a function that converts English text to morse code and another one that does the opposite.
# Hint: Check the internet for a translation table, every letter is separated with a space and every word is separated with a slash /.

# Dictionary defining the standard International Morse Code
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '!': '-.-.--', 
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': ' ' # Space is needed for internal handling
}

# Create a reverse dictionary for fast translation from Morse to English
REVERSE_MORSE_CODE = {code: char for char, code in MORSE_CODE.items()}

def english_to_morse(text):
    """
    Converts English text to Morse code.
    Letters are separated by spaces, words by a slash (/).
    """
    # 1. Convert to uppercase to match the dictionary keys
    text = text.upper()
    
    # 2. Process word by word
    morse_words = []
    
    # Split the text by spaces to get individual words
    for word in text.split():
        morse_chars = []
        
        # Translate each character in the word
        for char in word:
            # Check if the character is supported
            if char in MORSE_CODE:
                morse_chars.append(MORSE_CODE[char])
            # Ignore unsupported characters (or add a placeholder)
            
        # Join characters with a single space (letter separation rule)
        morse_words.append(" ".join(morse_chars))

    # Join words with a slash (word separation rule) and return
    return " / ".join(morse_words)

def morse_to_english(morse_code):
    """
    Converts Morse code back to English text.
    Assumes letters are separated by spaces and words by a slash (/).
    """
    # 1. Process Morse code word by word (separated by /)
    english_words = []
    
    # Split the code by " / " to get individual morse words
    for morse_word in morse_code.split(" / "):
        english_chars = []
        
        # Split the morse word by " " to get individual morse characters (letters)
        for morse_char in morse_word.split(" "):
            # Check if the code is supported
            if morse_char in REVERSE_MORSE_CODE:
                english_chars.append(REVERSE_MORSE_CODE[morse_char])
            # Handle unknown or empty codes silently

        # Join the translated characters to form an English word
        english_words.append("".join(english_chars))
        
    # Join the English words with a single space and return
    return " ".join(english_words)

# --- Примеры использования ---

english_sentence = "Hello world! This is Python."
print(f"Original Text: {english_sentence}")

# 1. Преобразование из английского в код Морзе
morse_output = english_to_morse(english_sentence)
print(f"Morse Code:    {morse_output}")

# 2. Обратное преобразование из кода Морзе в английский
english_output = morse_to_english(morse_output)
print(f"English Result:  {english_output}")

# Exercise 3 : Box of stars
# Instructions
# Write a function named box_printer that takes any amount of strings (not in a list) and prints them, one per line, in a rectangular frame.
# For example calling box_printer("Hello", "World", "in", "reallylongword", "a", "frame") will result as:

# ******************
# * Hello          *
# * World          *
# * in             *
# * reallylongword *
# * a              *
# * frame          *
# ******************

def box_printer(*args):
    """
    Accepts any number of strings and prints them, one per line, 
    inside a rectangular frame of asterisks.
    """
    if not args:
        print("*******************")
        print("* No strings provided *")
        print("*******************")
        return

    # 1. Find the length of the longest string to set the frame width
    max_length = 0
    for s in args:
        if len(s) > max_length:
            max_length = len(s)

    # Total frame width: 2 spaces + 2 asterisks on each side (max_length + 4)
    frame_width = max_length + 4

    # 2. Print the top border
    print("*" * frame_width)

    # 3. Print each string inside the frame
    for s in args:
        # Use the .ljust() method for string alignment
        # s.ljust(max_length) pads the string with spaces on the right up to max_length
        print(f"* {s.ljust(max_length)} *")

    # 4. Print the bottom border
    print("*" * frame_width)

# --- Examples of Usage ---

# Example 1: The example from the assignment
print("--- Example 1 ---")
box_printer("Hello", "World", "in", "reallylongword", "a", "frame")

# Example 2: A different set of strings
print("\n--- Example 2 ---")
box_printer("Short", "Programming", "Example")

# Example 3: Just one line
print("\n--- Example 3 ---")
box_printer("Just one line")

# Exercise 4 : What is the purpose of this code?
# Analyse this code before executing it. What is the purpose of this code?

# def insertion_sort(alist):
#    for index in range(1,len(alist)):

#      currentvalue = alist[index]
#      position = index

#      while position>0 and alist[position-1]>currentvalue:
#          alist[position]=alist[position-1]
#          position = position-1

#      alist[position]=currentvalue

# alist = [54,26,93,17,77,31,44,55,20]
# insertion_sort(alist)
# print(alist)

This code implements the Insertion Sort algorithm.

Its sole purpose is to take an unsorted list of elements (alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]) and sort it in ascending order (from smallest to largest).

🔍 Detailed Code Analysis
The function insertion_sort(alist):

It takes one argument: alist (the list to be sorted).

The sorting happens in-place, meaning it modifies the original list rather than creating a new one.

The outer loop for index in range(1, len(alist)):

The loop starts at index 1, as the first element (alist[0]) is considered already sorted (a sorted sublist of one element).

In each iteration, it takes the element at alist[index] (the current value) and attempts to insert it into the correct position within the already sorted part of the list to its left.

Variables currentvalue and position:

currentvalue holds the element we are trying to insert.

position is the index used to track where the shift operation starts.

The inner loop while position > 0 and alist[position-1] > currentvalue::

This is the core shifting logic of Insertion Sort.

It continues as long as:

We haven't reached the start of the list (position > 0).

The element immediately to the left (alist[position-1]) is greater than the value we are trying to insert (currentvalue).

Shift action: alist[position] = alist[position-1]—the larger element is shifted one position to the right.

Position move: position = position - 1—the index where the insertion will happen moves one step to the left.

The insertion alist[position] = currentvalue:

When the while loop finishes, we have found the correct spot (either the start of the list or the element to the left is smaller).

The original currentvalue is placed into this final, correct position.

🎯 Expected Output
The code starts with the list:

[54, 26, 93, 17, 77, 31, 44, 55, 20]
When print(alist) is executed, it will output the sorted list:

[17, 20, 26, 31, 44, 54, 55, 77, 93]