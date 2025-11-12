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
