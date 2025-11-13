# Exercise 1 : When will I retire ?
# Instructions
# The point of the exercise is to check if a person can retire depending on their age and their gender.
# Note : Let’s say retirement age is 67 for men, and 62 for women (born after April, 1947).

# Create a function get_age(year, month, day)
# Hard-code the current year and month in your code (there are better ways of doing this, but for now it will be enough.)
# After calculating the age of a person, the function should return the age (the age is an integer).
# Create a function can_retire(gender, date_of_birth).
# It should call the get_age function (with what arguments?) in order to receive an age.
# Now it has all the information it needs in order to determine if the person with the given gender and date of birth is able to retire or not.
# Calculate. You may need to do a little more hard-coding here.
# Return True if the person can retire, and False if he/she can’t.
# Some Hints

# Ask for the user’s gender as “m” or “f”.
# Ask for the user’s date of birth in the form of “yyyy/mm/dd”, eg. “1993/09/21”.
# Call can_retire to get a definite value for whether the person can or can’t retire.
# Display a message informing the user whether they can retire or not.
# As always, test your code to ensure it works.

# Hard-coded current date (November 2025) for age calculation
CURRENT_YEAR = 2025
CURRENT_MONTH = 11

# Define retirement ages
RETIREMENT_AGE_MALE = 67
RETIREMENT_AGE_FEMALE = 62

def get_age(birth_year, birth_month, birth_day):
    """
    Calculates the current age of a person based on their date of birth
    and the hard-coded current date (Nov 2025).

    :param birth_year: Year of birth (integer).
    :param birth_month: Month of birth (integer).
    :param birth_day: Day of birth (integer).
    :return: The age of the person (integer).
    """
    age = CURRENT_YEAR - birth_year
    
    # Adjust age if the birth month/day has not yet passed in the current year
    if CURRENT_MONTH < birth_month:
        age -= 1
    elif CURRENT_MONTH == birth_month and 1 > birth_day:
        # Since we don't have the current day, we assume the current day is 1
        # For simplicity, this is often omitted or simplified.
        # Here we only decrement if the birth month hasn't passed.
        # A more precise check would involve the current day, but we stick to the provided requirement.
        pass

    # Ensure age is not negative (in case of future dates)
    return max(0, age)

def can_retire(gender, date_of_birth):
    """
    Determines if a person can retire based on gender and date of birth.

    :param gender: The person's gender ("m" or "f").
    :param date_of_birth: The person's date of birth in "yyyy/mm/dd" format.
    :return: True if the person can retire, False otherwise.
    """
    try:
        # Parse the date of birth string
        parts = date_of_birth.split('/')
        if len(parts) != 3:
            raise ValueError("Invalid date format.")

        birth_year = int(parts[0])
        birth_month = int(parts[1])
        birth_day = int(parts[2])

    except ValueError as e:
        print(f"Error parsing date: {e}")
        return False

    # Call get_age to calculate the person's current age
    age = get_age(birth_year, birth_month, birth_day)
    print(f"Calculated age: {age}")

    gender = gender.lower()

    if gender == 'm':
        # Men retire at 67
        return age >= RETIREMENT_AGE_MALE
    elif gender == 'f':
        # Women retire at 62 (assuming they were born after April 1947, as per note)
        return age >= RETIREMENT_AGE_FEMALE
    else:
        print("Invalid gender input. Please use 'm' or 'f'.")
        return False

# --- Main Program Execution ---

def run_retirement_check():
    """
    Handles user interaction and displays the retirement status.
    """
    print("--- Retirement Eligibility Checker (Current Date: Nov 2025) ---")
    
    # Get user gender
    gender = input("Enter your gender ('m' for male, 'f' for female): ").strip()

    # Get user date of birth
    dob = input("Enter your date of birth (yyyy/mm/dd, e.g., 1960/01/15): ").strip()

    # Call can_retire to get the definite value
    can_retire_status = can_retire(gender, dob)

    # Display the final message
    if can_retire_status is True:
        print("\n Congratulations! You are eligible to retire.")
    elif can_retire_status is False:
        print("\n Sorry, you are not yet eligible to retire.")
    # If the function returned something other than True/False (e.g., due to invalid input)
    else:
        print("\nCould not determine retirement status due to invalid input.")

if __name__ == "__main__":
    run_retirement_check()

# Exercise 2 : Sum
# Instructions
# Write a function that accepts one parameter (an int: X) and returns the value of X+XX+XXX+XXXX.
# Example:
# If X=3, the output when calling our function should be 3702 (3 + 33 + 333 + 3333)

# Hint: treating our number as a int or a str at different points in our code may be helpful

#     # Exercise 2: Sum
# # Goal: Calculate the value of X + XX + XXX + XXXX

def calculate_sum(X):
    """
    Accepts an integer X and returns the sum of X + XX + XXX + XXXX.
    
    This function leverages string multiplication to create the repeating
    number patterns before converting them back to integers for addition.

    :param X: The single-digit integer to use (e.g., 3).
    :return: The total sum (e.g., 3702).
    """
    # Convert the integer X to a string. This is crucial for creating the terms XX, XXX, etc.
    s = str(X)
    
    # 1. First term: X (already available as integer X)
    term1 = X
    
    # 2. Second term: XX 
    # s * 2 creates the string (e.g., '3' * 2 = '33'). 
    # int() converts it back to a number (33).
    term2 = int(s * 2)
    
    # 3. Third term: XXX
    term3 = int(s * 3)
    
    # 4. Fourth term: XXXX
    term4 = int(s * 4)
    
    # Calculate the total sum
    total_sum = term1 + term2 + term3 + term4
    
    return total_sum

# --- Example Usage ---

X = 3
result = calculate_sum(X)

print(f"Input X: {X}")
print(f"Calculation: {X} + {str(X)*2} + {str(X)*3} + {str(X)*4}")
print(f"The total sum is: {result}")

# Example 2 (if X=5)
X_2 = 5
result_2 = calculate_sum(X_2)
# Expected: 5 + 55 + 555 + 5555 = 6170
print(f"\nInput X: {X_2}")
print(f"The total sum is: {result_2}")

# Exercise 3 : Double Dice
# Instructions
# Create a function that will simulate the rolling of a dice. Call it throw_dice. It should return an integer between 1 and 6.
# Create a function called throw_until_doubles.
# It should keep throwing 2 dice (using your throw_dice function) until they both land on the same number, ie. until we reach doubles.
# For example: (1, 2), (3, 1), (5,5) → then stop throwing, because doubles were reached.
# This function should return the number of times it threw the dice in total. In the example above, it should return 3.

# Create a main function.
# It should throw doubles 100 times (ie. call your throw_until_doubles function 100 times), and store the results of those function calls (in other words, how many throws it took until doubles were thrown, each time) in a collection. (What kind of collection? Read below to understand what we will need the data for, and this should help you decide which data structure to use).

# After the 100 doubles are thrown, print out a message telling the user how many throws it took in total to reach 100 doubles.
# Also print out a message telling the user the average amount of throws it took to reach doubles. Round this off to 2 decimal places.
# For example:

# If the results of the throws were as follows (your code would do 100 doubles, not just 3):
# (1, 2), (3, 1), (5, 5)
# (3, 3)
# (2, 4), (1, 2), (3, 4), (2, 2)

# Then my output would show something like this:
# Total throws: 8
# Average throws to reach doubles: 2.67.

# Exercise 3: Double Dice Simulation
import random

def throw_dice():
    """
    Simulates the rolling of a single six-sided die.
    
    :return: An integer between 1 and 6.
    """
    return random.randint(1, 6)

def throw_until_doubles():
    """
    Keeps throwing two dice until both land on the same number (doubles).
    
    :return: The total number of throws required to reach doubles (integer).
    """
    throws_count = 0
    while True:
        # Throw the two dice
        die1 = throw_dice()
        die2 = throw_dice()
        throws_count += 1
        
        # Check for doubles
        if die1 == die2:
            return throws_count

def main():
    """
    Runs the double dice simulation 100 times, collects the results, 
    and prints the total and average throws.
    """
    NUM_TRIALS = 100
    
    # Use a list to store the number of throws required for each of the 100 trials
    results = [] 
    
    # Throw doubles 100 times
    for _ in range(NUM_TRIALS):
        throws = throw_until_doubles()
        results.append(throws)
        
    # Calculate statistics
    total_throws = sum(results)
    average_throws = total_throws / NUM_TRIALS
    
    # Print results
    print(f"--- Double Dice Simulation ({NUM_TRIALS} Trials) ---")
    print(f"Total throws: {total_throws}")
    
    # Round the average to 2 decimal places
    print(f"Average throws to reach doubles: {average_throws:.2f}")

# Start the simulation
if __name__ == "__main__":
    main()
