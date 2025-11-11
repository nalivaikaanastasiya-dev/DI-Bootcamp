#  Exercise 1: Converting Lists into Dictionaries
# Instructions
# You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.

# Lists:
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# Expected Output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

my_dictionary = dict(zip(keys, values))

print(my_dictionary)

# Exercise 2: Cinemax #2
# Write a program that calculates the total cost of movie tickets for a family based on their ages.

# Family members’ ages are stored in a dictionary.
# The ticket pricing rules are as follows:
# Under 3 years old: Free
# 3 to 12 years old: $10
# Over 12 years old: $15

# Family Data:
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# Loop through the family dictionary to calculate the total cost.
# Print the ticket price for each family member.
# Print the total cost at the end.

# Bonus:
# Allow the user to input family members’ names and ages, then calculate the total ticket cost.

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0

PRICE_CHILD = 10  
PRICE_ADULT = 15  
PRICE_FREE = 0    

print("--- Individual Ticket Prices ---")

for name, age in family.items():
    price = 0
    if age < 3:
        price = PRICE_FREE
        print(f"{name.capitalize()} (Age {age}): Free")
    elif age <= 12: 
        price = PRICE_CHILD
        print(f"{name.capitalize()} (Age {age}): ${price}")
    else:  
        price = PRICE_ADULT
        print(f"{name.capitalize()} (Age {age}): ${price}")

    total_cost += price

print("\n------------------------------")
print(f" Total Ticket Cost: ${total_cost}")

 """Calculates the total ticket cost based on age rules."""
    total_cost = 0
    PRICE_CHILD = 10
    PRICE_ADULT = 15

    print("\n--- Individual Ticket Prices (Your Family) ---")
    for name, age in family_dict.items():
        price = 0
        if age < 3:
            price = 0
            print(f"{name.capitalize()} (Age {age}): Free")
        elif age <= 12:
            price = PRICE_CHILD
            print(f"{name.capitalize()} (Age {age}): ${price}")
        else:
            price = PRICE_ADULT
            print(f"{name.capitalize()} (Age {age}): ${price}")
        
        total_cost += price
        
    print("\n-------------------------------------------")
    print(f" Total Ticket Cost: ${total_cost}")

user_family = {}
print("\n" + "="*40)
print("\n--- 2️ Enter Your Family Members (Bonus Feature) ---")

while True:
    name = input("Enter family member's name (or type 'done' to finish): ").strip()
    
    if name.lower() == 'done':
        break
    
    try:
        age_input = input(f"Enter {name}'s age: ").strip()
        age = int(age_input)
        
        if age < 0:
            print("Age cannot be negative. Please try again.")
            continue
            
        user_family[name] = age
        print(f"Added {name} (Age: {age}).")
        
    except ValueError:
        print("Invalid age entered. Please enter a valid number.")

if user_family:
    calculate_total_cost(user_family)
else:
    print("No family members were entered for the user input section.")

# Exercise 3: Zara

# Create and manipulate a dictionary that contains information about the Zara brand.

# Brand Information:
# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green

# Create a dictionary called brand with the provided data.
# Modify and access the dictionary as follows:
# Change the value of number_stores to 2.
# Print a sentence describing Zara’s clients using the type_of_clothes key.
# Add a new key country_creation with the value Spain.
# Check if international_competitors exists and, if so, add “Desigual” to the list.
# Delete the creation_date key.
# Print the last item in international_competitors.
# Print the major colors in the US.
# Print the number of keys in the dictionary.
# Print all keys of the dictionary.

# Bonus:
# Create another dictionary called more_on_zara with creation_date and number_stores. Merge this dictionary with the original brand dictionary and print the result.

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": ["blue"],
        "Spain": ["red"],
        "US": ["pink", "green"]
    }
}

print("--- Initial Dictionary ---")
print(brand)
print("-" * 30)

brand["number_stores"] = 2

clients = ", ".join(brand["type_of_clothes"])
print(f"Zara's clients: {clients}.")

brand["country_creation"] = "Spain"

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
    print("Competitor 'Desigual' added.")

del brand["creation_date"]

last_comp = brand["international_competitors"][-1]
print(f"Last competitor: {last_comp}")

us_colors = ", ".join(brand["major_color"]["US"])
print(f"Major colors in the US: {us_colors}")

print(f"Total keys: {len(brand)}")

print(f"Keys: {list(brand.keys())}")

print("\n" + "=" * 40)
print("--- ⭐ Bonus: Merging ---")

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 7000
}

brand.update(more_on_zara)

print("\nMerged Dictionary:")
print(brand)

# Exercise 4: Disney Characters
# You are given a list of Disney characters. Create three dictionaries based on different patterns as shown below:

# Character List:
# users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# Expected Results:
# 1. Create a dictionary that maps characters to their indices:
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
# 2. Create a dictionary that maps indices to characters:
# {0: "Mickey", 1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
# 3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

print("Character List:", users)
print("-" * 40)

dict_char_to_index = {
    character: index 
    for index, character in enumerate(users)
}
print("1. Character to Index:")
print(dict_char_to_index)

dict_index_to_char = dict(enumerate(users))
print("\n2. Index to Character:")
print(dict_index_to_char)

sorted_users = sorted(users)

dict_sorted_char_to_index = {
    character: index 
    for index, character in enumerate(sorted_users)
}
print("\n3. Sorted Character to Index:")
print(dict_sorted_char_to_index)