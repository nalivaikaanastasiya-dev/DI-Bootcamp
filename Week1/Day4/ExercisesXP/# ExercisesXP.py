# Exercise 1: What Are You Learning?
# Goal: Create a function that displays a message about what you’re learning.

# Step 1: Define a Function
# Define a function named display_message().
# This function should not take any parameters.

# Step 2: Print a Message
# For example: “I am learning about functions in Python.”

# Step 3: Call the Function
# This will execute the code inside the function and print your message.

# Expected Output:
# I am learning about functions in Python.

def display_message():
    print('I am learning about functions in Python.')

display_message()

# Exercise 2: What’s Your Favorite Book?
# Goal: Create a function that displays a message about a favorite book.

# Step 1: Define a Function with a Parameter
# Define a function named favorite_book().
# This function should accept one parameter called title.

# Step 2: Print a Message with the Title
# The function needs to output a message like “One of my favorite books is <title>”.

# Step 3: Call the Function with an Argument
# Call the favorite_book() function and provide a book title as an argument.
# For example: favorite_book("Alice in Wonderland").

def favorite_book(title):
    print('One of my favorite books is', title)
favorite_book('Alice in Wonderland')

# Exercise 3: Some Geography
# Goal: Create a function that describes a city and its country.

# Step 1: Define a Function with Parameters ok
# Define a function named describe_city().
# This function should accept two parameters: city and country.
# Give the country parameter a default value, such as “Unknown”.

# Step 2: Print a Message
# Inside the function, set up the code to display a sentence like “ is in “.
# Replace <city> and <country> with the parameter values.

# Step 3: Call the Function
# Call the describe_city() function with different city and country combinations.
# Try calling it with and without providing the country argument to see the default value in action.
# Example: describe_city("Reykjavik", "Iceland") and describe_city("Paris").

# Expected Output:

# Reykjavik is in Iceland.
# Paris is in Unknown.

def describe_city(city, country='Unknown'):
    print(f'{city} is in {country}.')
describe_city("Reykjavik", "Iceland")
describe_city('Paris')

# Exercise 4: Random
# Goal: Create a function that generates random numbers and compares them.

# Step 1: Import the random Module
# At the beginning of your script, use import random to access the random number generation functions.

# Step 2: Define a Function with a Parameter
# Create a function that accepts a number between 1 and 100 as a parameter.

# Step 3: Generate a Random Number
# Inside the function, use random.randint(1, 100) to generate a random integer between 1 and 100.

# Step 4: Compare the Numbers
# If they are the same, print a success message. Otherwise, print a fail message and display both numbers.

# Step 5: Call the Function
# Call the function with a number between 1 and 100.

# Expected Output:

# Success! (if the numbers match)
# Fail! Your number: 50, Random number: 23 (if they don't match)

import random

# Step 2: Define a Function with a Parameter
def compare_random_number(user_input):
    """
    Generates a random number between 1 and 100 and compares it
    to the provided user number.

    :param user_input: The number provided by the user (expected between 1 and 100).
    """
    # Step 3: Generate a Random Number
    random_number = random.randint(1, 100)

    # Step 4: Compare the Numbers
    if user_input == random_number:
        print("Success! The numbers match.")
    else:
        # Display both numbers upon failure
        print(f"Fail! Your number: {user_input}, Random number: {random_number}")

# --- Program Execution ---

# Step 5: Call the Function
# Example 1: Calling the function with a number (e.g., 50)
print("--- Check 1 (Input: 50) ---")
compare_random_number(50)

# Exercise 5: Let’s Create Some Personalized Shirts!
# Goal: Create a function to describe a shirt’s size and message, with default values.

# Step 1: Define a Function with Parameters
# Define a function called make_shirt().
# This function should accept two parameters: size and text.

# Step 2: Print a Summary Message
# Set up the function to display a sentence summarizing the shirt’s size and message.

# Step 3: Call the Function

# Step 4: Modify the Function with Default Values
# Modify the make_shirt() function so that size has a default value of “large” and text has a default value of “I love Python”.

# Step 5: Call the Function with Default and Custom Values
# Call make_shirt() to make a large shirt with the default message.
# Call make_shirt() to make a medium shirt with the default message.
# Call make_shirt() to make a shirt of any size with a different message.

# Step 6 (Bonus): Keyword Arguments
# Call make_shirt() using keyword arguments (e.g., make_shirt(size="small", text="Hello!")).

# Expected Output:
# The size of the shirt is large and the text is I love Python.
# The size of the shirt is medium and the text is I love Python.
# The size of the shirt is small and the text is Custom message.

# Step 1 and 4: Define the make_shirt() function with parameters
# size and text, where size defaults to "large" and text defaults to "I love Python".
def make_shirt(size="large", text="I love Python"):
    """
    Prints a message describing the shirt's size and the text 
    printed on it.
    """
    # Step 2: Print the summary message
    print(f"The size of the shirt is {size} and the text is {text}.")


# ----------------------------------------------------------------------
# Step 5: Calling the function using default and custom values
# ----------------------------------------------------------------------

print("--- 1. Call with default parameters (size='large', text='I love Python') ---")
# 5a: Call to create a large shirt with the default message.
make_shirt()

print("\n--- 2. Call with one positional argument (size='medium') ---")
# 5b: Call to create a medium shirt with the default message.
# The 'medium' argument overrides the default size value.
make_shirt("medium")

print("\n--- 3. Call with two positional arguments (custom size and text) ---")
# 5c: Call to create a shirt of any size with a different message.
make_shirt("small", "Custom message.")


# ----------------------------------------------------------------------
# Step 6 (Bonus): Calling the function using Keyword Arguments
# ----------------------------------------------------------------------

print("\n--- 4. Call using Keyword Arguments ---")
# We can explicitly specify which argument equals which value for clarity.
make_shirt(text="I enjoy coding!", size="extra-large")

# Exercise 6: Magicians…
# Goal: Modify a list of magician names and display them in different ways.

# Step 1: Create a List of Magician Names
# Create a list called magician_names with the given names:
# ['Harry Houdini', 'David Blaine', 'Criss Angel']

# Step 2: Create a Function to Display Magicians
# Create a function called show_magicians() that takes the magician_names list as a parameter.
# Inside the function, iterate through the list and print each magician’s name.

# Step 3: Create a Function to Modify the List
# Create a function called make_great() that takes the magician_names list as a parameter.
# Inside the function, use a for loop to iterate through the list and add “the Great” before each magician’s name.

# Step 4: Call the Functions
# Call make_great() to modify the list.
# Call show_magicians() to display the modified list.

# Expected Output:
# Harry Houdini the Great
# David Blaine the Great
# Criss Angel the Great

# Step 1: Create a List of Magician Names
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# Step 2: Create a Function to Display Magicians
def show_magicians(magicians):
    """
    Takes a list of magician names and prints each name.
    """
    print("--- Current List of Magicians ---")
    for magician in magicians:
        print(magician)

# Step 3: Create a Function to Modify the List
def make_great(magicians):
    """
    Modifies the list by adding ' the Great' to each magician's name.
    
    Note: We iterate using indices (range(len(magicians))) to modify 
    the original list in place.
    """
    for i in range(len(magicians)):
        # Modify the element at index i
        magicians[i] = magicians[i] + " the Great"

# ----------------------------------------------------------------------
# Step 4: Call the Functions
# ----------------------------------------------------------------------

# 4a: Call make_great() to modify the list
make_great(magician_names)

# 4b: Call show_magicians() to display the modified list
show_magicians(magician_names)

# Exercise 7: Temperature Advice
# Goal: Generate a random temperature and provide advice based on the temperature range.

# Step 1: Create the get_random_temp() Function
# Create a function called get_random_temp() that returns a random integer between -10 and 40 degrees Celsius.

# Step 2: Create the main() Function
# Create a function called main(). Inside this function:
# Call get_random_temp() to get a random temperature.
# Store the temperature in a variable and print a friendly message like:
# “The temperature right now is 32 degrees Celsius.”

# Step 3: Provide Temperature-Based Advice
# Inside main(), provide advice based on the temperature:
# Below 0°C: e.g., “Brrr, that’s freezing! Wear some extra layers today.”
# Between 0°C and 16°C: e.g., “Quite chilly! Don’t forget your coat.”
# Between 16°C and 23°C: e.g., “Nice weather.”
# Between 24°C and 32°C: e.g., “A bit warm, stay hydrated.”
# Between 32°C and 40°C: e.g., “It’s really hot! Stay cool.”

# Step 4: Floating-Point Temperatures (Bonus)
# Modify get_random_temp() to return a random floating-point number using random.uniform() for more accurate temperature values.

# Step 5: Month-Based Seasons (Bonus)
# Instead of directly generating a random temperature, ask the user for a month (1-12) and determine the season using if/elif conditions.
# Modify get_random_temp() to return temperatures specific to each season.

# Expected Output:
# The temperature right now is 32 degrees Celsius.
# It's really hot! Stay cool.

import random

# Define temperature ranges for Northern Hemisphere seasons (Bonus Step 5)
# Using broad ranges for demonstration of functionality.
SEASON_RANGES = {
    "Winter": (-10.0, 8.0),   # Months 12, 1, 2
    "Spring": (5.0, 20.0),    # Months 3, 4, 5
    "Summer": (25.0, 40.0),   # Months 6, 7, 8
    "Autumn": (10.0, 25.0)    # Months 9, 10, 11
}

# Step 1 & 4 & 5: Function to get a random temperature based on the season
def get_random_temp(season):
    """
    Returns a random floating-point temperature within the range 
    defined for the given season. (Bonus Step 4: Floating-Point)
    """
    if season in SEASON_RANGES:
        min_temp, max_temp = SEASON_RANGES[season]
        # Use random.uniform() for floating-point temperatures
        return random.uniform(min_temp, max_temp)
    else:
        # Fallback range if season determination fails
        return random.uniform(10.0, 30.0)

# Step 3: Helper function to provide advice based on temperature
def get_advice(temp):
    """
    Provides clothing and activity advice based on the temperature range.
    """
    if temp < 0:
        return "Brrr, that’s freezing! Wear some extra layers today and cover all exposed skin."
    elif 0 <= temp <= 16:
        return "Quite chilly! Don’t forget your coat and maybe a warm hat."
    elif 17 <= temp <= 23:
        return "Nice weather! Perfect for light layers or a simple jacket."
    elif 24 <= temp <= 32:
        return "A bit warm. Stay hydrated and seek shade during the hottest part of the day."
    else: # temp > 32 (up to 40)
        return "It’s really hot! Stay cool, drink lots of water, and limit strenuous outdoor activity."


# Step 2 & 5: Main function
def main():
    """
    Handles user input, determines the season, gets the random temperature, 
    and provides advice.
    """
    
    # --- Step 5 Bonus: Ask for Month and Determine Season ---
    try:
        month_input = input("Enter the current month number (1 for Jan, 12 for Dec): ")
        month = int(month_input)
        
        if not 1 <= month <= 12:
            print("Invalid month number entered. Please enter a number between 1 and 12.")
            return

        # Determine season based on month number
        if month in [12, 1, 2]:
            season = "Winter"
        elif month in [3, 4, 5]:
            season = "Spring"
        elif month in [6, 7, 8]:
            season = "Summer"
        else: # 9, 10, 11
            season = "Autumn"
            
    except ValueError:
        print("Invalid input. Please enter a numerical month (e.g., 6 for June).")
        return

    # Call get_random_temp() based on the season (Step 2)
    temperature = get_random_temp(season)
    
    # Format temperature to one decimal place for clean output
    formatted_temp = f"{temperature:.1f}"

    # Print the friendly message (Step 2)
    print(f"\nBased on month {month}, the detected season is **{season}**.")
    print(f"The temperature right now is **{formatted_temp}°C**.")

    # Provide temperature-based advice (Step 3)
    advice = get_advice(temperature)
    print(advice)


if __name__ == "__main__":
    main()
