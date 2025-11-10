from datetime import date
import sys

def run_birthday_checker_print_by_line():
    """
    Main function that asks for the birthdate, calculates the age, 
    and draws the cake by printing each line separately.
    """
    print("Birthday Program")

    while True:
        birthdate_str = input("Please enter your birthdate in the format DD/MM/YYYY: ")
        
        try:
            day, month, year = map(int, birthdate_str.split('/'))
            birth_date = date(year, month, day)
            break
        except ValueError:
            print("Error: Please use the format DD/MM/YYYY (e.g., 01/01/2000) and ensure the date is valid. Try again.")
            
    today = date.today()
    age = today.year - birth_date.year
    
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
        

    candles_count = age % 10
    
    is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    print(f"\nYour current age is: **{age}** years.")
    print(f"Your cake will have **{candles_count}** candles.")
    
    candles_line = "i" * candles_count
    top_line = "   ___" + candles_line.center(5).replace(' ', '_') + "___"

    def draw_cake_lines(top_line):
        """Function to print the cake line by line."""
        print(top_line) 
        print("      |:H:a:p:p:y:|") 
        print("    __|___________|__")
        print("   |^^^^^^^^^^^^^^^^^|")
        print("   |:B:i:r:t:h:d:a:y:|")
        print("   |                 |")
        print("   ~~~~~~~~~~~~~~~~~~~")

    if is_leap_year:
        print("\nSUPER BONUS! You were born in a leap year, you get two cakes!")
        
        print("\n--- Cake 1 ---")
        draw_cake_lines(top_line)
        
        print("\n--- Cake 2 ---")
        draw_cake_lines(top_line)
    else:
        print("\nYour celebratory cake:\n")
        draw_cake_lines(top_line)

if __name__ == "__main__":
    try:
        run_birthday_checker_print_by_line()
    except KeyboardInterrupt:
        print("\nProgram terminated.")
        sys.exit(0)