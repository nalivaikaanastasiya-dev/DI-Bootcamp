def reverse_sentence():
    """
    Reads a line of text, reverses the order of the words, and prints the result.
    
    Example:
    Input: "You have entered a wrong domain"
    Output: "domain wrong a entered have You"
    """
    # 1. Get input from the user (using input() for Python 3)
    print("Enter the sentence to reverse:")
    input_sentence = input()
    
    # 2. Split the sentence into a list of words (splits by space)
    words = input_sentence.split()
    
    # 3. Reverse the order of the words list using slicing [::-1]
    reversed_words = words[::-1]
    
    # 4. Join the reversed list back into a single string, separated by spaces
    reversed_sentence = " ".join(reversed_words)
    
    # 5. Print the reversed sentence
    print(reversed_sentence)

if __name__ == "__main__":
    reverse_sentence()