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