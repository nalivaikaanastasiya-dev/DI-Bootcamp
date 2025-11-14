# Mini-Project - Tic Tac Toe

# Key Python Topics:
# Lists (2D lists)
# Loops (while)
# Conditional statements (if, elif, else)
# Functions
# User input (input())
# String formatting

# 🛠️ What you will create
# A command-line Tic Tac Toe game that allows two players to take turns marking a 3x3 grid.

# tic-tac-toe

# Instructions:
# Tic Tac Toe is played on a 3x3 grid. Players take turns marking empty squares with their symbol (‘O’ or ‘X’). The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins. If all squares are filled and no player has three in a row, the game is a tie.

# Step 1: Representing the Game Board
# You’ll need a way to represent the 3x3 grid.
# A list of lists (a 2D list) is a good choice.
# Initially, each cell in the grid should be empty (e.g., represented by a space ‘ ‘).

# Step 2: Displaying the Game Board
# Create a function called display_board() to print the current state of the game board.
# The output should visually represent the 3x3 grid.
# Think about how to format the output to make it easy to read.

# Step 3: Getting Player Input
# Create a function called player_input(player) to get the player’s move.
# The function should ask the player to enter a position (e.g., row and column numbers).
# Validate the input to ensure it’s within the valid range and that the chosen cell is empty.
# Think about how to ask the user for input, and how to validate that input.

# Step 4: Checking for a Winner
# Create a function called check_win(board, player) to check if the current player has won.
# The function should check all possible winning combinations (rows, columns, diagonals).
# If a player has won, return True; otherwise, return False.
# Think about how to check every possible winning combination.

# Step 5: Checking for a Tie
# Create a function to check if the game has resulted in a tie.
# The function should check if all positions of the board are full, without a winner.

# Step 6: The Main Game Loop
# Create a function called play() to manage the game flow.
# Initialize the game board.
# Use a while loop to continue the game until there’s a winner or a tie.
# Inside the loop:
# Display the board.
# Get the current player’s input.
# Update the board with the player’s move.
# Check for a winner.
# Check for a tie.
# Switch to the next player.
# After the loop ends, display the final result (winner or tie).

# Tips:
# Consider creating helper functions to break down the logic into smaller, manageable parts.
# Follow the single responsibility principle: each function should do one thing and do it well.
# Think about how to switch between players.
# Think about how you will store the player’s symbol.

import random

# Step 1: Representing the Game Board
# We use a 3x3 list of lists. Each cell is initially empty (' ').
def create_board():
    """Initializes and returns a new 3x3 Tic Tac Toe board."""
    # We create the three rows manually to clearly show the board structure
    row1 = [' ', ' ', ' ']
    row2 = [' ', ' ', ' ']
    row3 = [' ', ' ', ' ']
    return [row1, row2, row3]

# Step 2: Displaying the Game Board
def display_board(board):
    """Prints the current state of the game board."""
    print("\n  0   1   2  <-- Columns")
    print(" +---+---+---+")
    # Using explicit indexing for simplicity
    print(f"0| {board[0][0]} | {board[0][1]} | {board[0][2]} |")
    print(" +---+---+---+")
    print(f"1| {board[1][0]} | {board[1][1]} | {board[1][2]} |")
    print(" +---+---+---+")
    print(f"2| {board[2][0]} | {board[2][1]} | {board[2][2]} |")
    print(" +---+---+---+")
    print("Rows ^\n")

# Helper function to check for a valid move
def is_valid_move(board, row, col):
    """Checks if the move is within range (0-2) and the cell is empty."""
    # Check that indices are in the range 0, 1, or 2
    if row < 0 or row > 2 or col < 0 or col > 2:
        print("Invalid range. Row and column must be between 0 and 2.")
        return False
        
    # Check that the cell is not already occupied
    if board[row][col] != ' ':
        print("This cell is already taken. Choose an empty cell.")
        return False
        
    return True

# Step 3: Getting Player Input
def player_input(board, player):
    """
    Prompts the player for their move (row and column) and validates it.
    Returns the tuple (row, col) for a valid move.
    """
    while True:
        try:
            # Ask for input in the form 'row,col'
            move_input = input(f"Player {player}, enter your move (row,col, e.g., 1,2): ")
            
            # Split the string and remove extra spaces
            parts = move_input.split(',')
            
            # Check that exactly two numbers were entered
            if len(parts) != 2:
                print("Invalid format. Please enter two numbers separated by a comma (e.g., 1,2).")
                continue
            
            # Convert parts to integers
            row = int(parts[0].strip())
            col = int(parts[1].strip())
            
            # Check the move using the helper function
            if is_valid_move(board, row, col):
                return row, col
        
        except ValueError:
            print("Invalid input. Please enter numbers only.")
        # No extra error handling needed, as is_valid_move checks the range

# Step 4: Checking for a Winner (The most "beginner" step - explicit check of all 8 lines)
def check_win(board, player):
    """
    Checks if the current player has won by explicitly checking 
    all 8 possible winning combinations.
    """
    # 1. Check Rows
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return True
    if board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return True
    if board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return True
        
    # 2. Check Columns
    if board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return True
    if board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return True
    if board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return True
        
    # 3. Check Diagonals
    # Top-left to bottom-right
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    
    # Top-right to bottom-left
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
        
    # If none of the checks worked
    return False

# Step 5: Checking for a Tie
def check_tie(board):
    """Checks if the board is full (a tie)."""
    # Using a nested loop, as beginners often do
    for row_index in range(3):
        for col_index in range(3):
            # If at least one empty cell is found, it's not a tie yet
            if board[row_index][col_index] == ' ':
                return False
    # If all cells have been checked and all are occupied
    return True

# Step 6: The Main Game Loop
def play():
    """Manages the overall game flow."""
    board = create_board()
    
    # Determine which player starts
    players = ['X', 'O']
    current_player = random.choice(players)
    print(f"Game Start! Player '{current_player}' goes first.")
    
    game_over = False
    
    while not game_over:
        
        # 1. Display the board
        display_board(board)
        
        # 2. Get the move and update the board
        row, col = player_input(board, current_player)
        board[row][col] = current_player
        
        # 3. Check for a winner
        if check_win(board, current_player):
            display_board(board)
            print(f"Player '{current_player}' wins! Congratulations!")
            game_over = True
            
        # 4. Check for a tie (only if no winner was found)
        elif check_tie(board):
            display_board(board)
            print("It's a tie! The board is full.")
            game_over = True
        
        # 5. Switch to the next player
        # We only do this if the game is not over
        if not game_over:
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'

# Start the game
if __name__ == "__main__":
    play()
