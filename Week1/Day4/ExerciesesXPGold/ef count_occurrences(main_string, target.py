def count_occurrences(main_string, target_char):
    """
    Counts the number of times a target character appears in a string.

    :param main_string: The string to search within.
    :param target_char: The single character to count.
    :return: The count of occurrences (integer).
    """
    # Using the built-in string count() method for efficient counting
    count = main_string.count(target_char)
    
    # Print the result in the requested format
    print(f"String: {main_string}\nCharacter: {target_char}{count}\n")
    return count

# --- Examples from the request ---

# Example 1
print("--- Example 1 ---")
# The target character is 'o'
count_occurrences("Programming is cool!", "o")

# Example 2
print("--- Example 2 ---")
# The target character is 'y'
count_occurrences("This is a great example", "y")

# Example 3: A custom example for demonstration
print("--- Example 3: Custom ---")
count_occurrences("The quick brown fox jumps over the lazy dog.", "e")