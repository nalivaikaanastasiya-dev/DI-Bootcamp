import random # Module: Used to select a random word from the list

# Word list for the game
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 

# Constants for game limits and parts
HANGMAN_PARTS = [
    "Head", 
    "Body", 
    "Left Arm", 
    "Right Arm", 
    "Left Leg", 
    "Right Leg"
]
MAX_MISSES = 6

def display_hangman(misses):
    """
    Function: Renders the gallows and body parts based on the number of misses.
    """
    gallows = [
        "  +---+",
        "  |   |",
        f"  {'O' if misses > 0 else ' ' }   |",  # Head (1 miss)
        f" {'/' if misses > 2 else ' '}{'|' if misses > 1 else ' '}{'\\' if misses > 3 else ' '}  |", # Body and Arms (misses 2, 3, 4)
        f" {'/' if misses > 4 else ' '} {'\\' if misses > 5 else ' '}  |",  # Legs (misses 5, 6)
        "      |",
        "========="
    ]
    return '\n'.join(gallows)

def hangman_game(chosen_word):
    """
    Main game function, encapsulating the game logic (Function).
    """
    
    # Initialize game variables
    word_to_guess = chosen_word.lower()
    
    # Creates the initial display, replacing letters with '*' but keeping spaces/symbols
    display = ['*' if char.isalpha() else char for char in word_to_guess]
    
    guessed_letters = [] # List to track letters already guessed
    misses_count = 0 
    game_over = False

    print("--- Starting the Hangman Game! ---")
    
    # Main game loop (Loops: while)
    while not game_over:
        
        current_display = "".join(display)
        print("\n" + "=" * 40)
        print(display_hangman(misses_count))
        print(f"Word: **{current_display}**")
        print(f"Misses: {misses_count} out of {MAX_MISSES} | Parts: {', '.join(HANGMAN_PARTS[:misses_count])}")
        print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")
        
        # Get and validate user input
        guess = input("Guess a letter: ").lower()
        
        # Input Validation (Conditionals: if/continue)
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter exactly ONE letter.")
            continue
        
        # Check if the letter was already guessed (Conditionals: if/continue)
        if guess in guessed_letters:
            print(f"You already guessed the letter '{guess}'. Try another.")
            continue
            
        # Add the guess to the tracked list
        guessed_letters.append(guess)
        
        # Process the guess
        if guess in word_to_guess: # Conditionals: Check for a correct guess
            print(f"Great! The letter '{guess}' is in the word.")
            # Update the display (Loops: for)
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    display[i] = guess
        else: # Conditionals: Handle an incorrect guess
            # Process a miss
            misses_count += 1
            print(f"Miss! The letter '{guess}' is not in the word. Part added: {HANGMAN_PARTS[misses_count - 1]}")
            
        
        # Check game end conditions (Conditionals: if/elif)
        
        # Win condition: no asterisks remain in the display
        if "*" not in display:
            game_over = True
            print("\n" + "=" * 40)
            print(f"CONGRATULATIONS! You guessed the word: **{word_to_guess}**")
        
        # Lose condition: maximum number of misses reached
        elif misses_count >= MAX_MISSES:
            game_over = True
            print("\n" + "=" * 40)
            print(display_hangman(misses_count))
            print(f"GAME OVER. The word was: **{word_to_guess}**")


# Start the game by calling the function with the randomly chosen word
hangman_game(word)