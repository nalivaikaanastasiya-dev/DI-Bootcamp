# Challenge 1: Sorting

# Instructions:
# Write a Python program that takes a single string of words as input, where the words are separated by commas (e.g., ‘apple,banana,cherry’). The program should output these words sorted in alphabetical order, with the sorted words also separated by commas.

# Step 1: Get Input
# Use the input() function to get a string of words from the user.
# The words will be separated by commas.

# Step 2: Split the String

# Step 3: Sort the List

# Step 4: Join the Sorted List

# Step 5: Print the Result
# Print the resulting comma-separated string.

# Expected Output:
# If the input is without,hello,bag,world, the output should be bag,hello,without,world.

def sort_comma_separated_words():
    """
    Takes a comma-separated string of words, sorts them alphabetically,
    and prints the result as a comma-separated string.
    """
    # Get a single string of words from the user.
    print("Example input: without,hello,bag,world")
    user_input = input("Enter words separated by commas: ")

    # Check if the input is empty or only contains spaces before processing
    if not user_input.strip():
        print("Error: Input cannot be empty.")
        return

    # Convert the single input string into a list of words using the comma (',')
    # as the delimiter.
    word_list = user_input.split(',')

    # Clean up any potential extra whitespace around the words during splitting
    cleaned_word_list = [word.strip() for word in word_list]

    # Use the built-in 'sorted()' function to sort the list alphabetically.
    # Note: Sorting is based on ASCII value (case-sensitive by default).
    sorted_words = sorted(cleaned_word_list)

    # Join the list of sorted words back into a single string, using the 
    # comma (',') as the separator.
    result_string = ','.join(sorted_words)

    print("\n--- Output ---")
    print(result_string)

# Execute the function when the script is run
if __name__ == "__main__":
    sort_comma_separated_words()

# Challenge 2: Longest Word

# Instructions:
# Write a function that takes a sentence as input and returns the longest word in the sentence. If there are multiple longest words, return the first one encountered. Characters like apostrophes, commas, and periods should be considered part of the word.

# Step 1: Define the Function
# Define a function that takes a string (the sentence) as a parameter.

# Step 2: Split the Sentence into Words

# Step 3: Initialize Variables

# Step 4: Iterate Through the Words

# Step 5: Compare Word Lengths

# Step 6: Return the Longest Word

# Expected Output:
# longest_word("Margaret's toy is a pretty doll.") should return "Margaret's".
# longest_word("A thing of beauty is a joy forever.") should return "forever.".
# longest_word("Forgetfulness is by all means powerless!") should return "Forgetfulness".

# Key Python Topics:
# Functions
# Strings
# .split() method
# Loops (for)
# Conditional statements (if)
# String length (len())

# Step 1: Define the Function
def longest_word(sentence):
    # Step 2: Split the Sentence into Words
    words = sentence.split()

    # Step 3: Initialize Variables
    longest = ""

    # Step 4: Iterate Through the Words
    for word in words:
        # Step 5: Compare Word Lengths
        if len(word) > len(longest):
            longest = word

    # Step 6: Return the Longest Word
    return longest


# ✅ Expected Output
print(longest_word("Margaret's toy is a pretty doll."))  # → "Margaret's"
print(longest_word("A thing of beauty is a joy forever."))  # → "forever."
print(longest_word("Forgetfulness is by all means powerless!"))  # → "Forgetfulness"