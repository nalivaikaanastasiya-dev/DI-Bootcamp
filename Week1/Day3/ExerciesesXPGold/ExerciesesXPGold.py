# Exercise 1: Birthday Look-up
# Instructions
# Create a variable called birthdays. Its value should be a dictionary.
# Initialize this variable with birthdays of 5 people of your choice. For each entry in the dictionary, the key should be the person’s name, and the value should be their birthday. Tip : Use the format “YYYY/MM/DD”.
# Print a welcome message for the user. Then tell them: “You can look up the birthdays of the people in the list!”“
# Ask the user to give you a person’s name and store the answer in a variable.
# Get the birthday of the name provided by the user.
# Print out the birthday with a nicely-formatted message.

# 1. Create and initialize the birthdays dictionary
birthdays = {
    "Alice": "1995/03/15",
    "Bob": "1988/11/22",
    "Charlie": "2001/07/30",
    "Diana": "1999/01/08",
    "Eve": "1990/05/25"
}

# 2. Print welcome message and instructions
print(" Welcome to the Birthday Look-up Service! ")
print("---------------------------------------------")
print("You can look up the birthdays of the following people:")

# Print the list of available names for the user
print(", ".join(birthdays.keys()))
print("---------------------------------------------")

# 3. Ask the user for a person's name
person_name = input("Enter a person's name to find their birthday: ").strip().title()

# 4. Get and print the birthday
if person_name in birthdays:
    # Get the birthday value from the dictionary
    birthday = birthdays[person_name]
    
    # Print the result with a nice message
    print(f"\n {person_name}'s birthday is on **{birthday}**.")
else:
    # Handle cases where the name is not found
    print(f"\n Sorry, I don't have the birthday information for **{person_name}**.")

# Exercise 2: Birthdays Advanced
# Instructions
# Before asking the user to input a person’s name print out all of the names in the dictionary.
# If the person that the user types is not found in the dictionary, print an error message (“Sorry, we don’t have the birthday information for <person’s name>”)

    birthdays = {
    "Alice": "1995/03/15",
    "Bob": "1988/11/22",
    "Charlie": "2001/07/30",
    "Diana": "1999/01/08",
    "Eve": "1990/05/25"
}

# Print welcome message and available names
print(" Welcome to the Advanced Birthday Look-up Service! ")
print("-------------------------------------------------------")
print("I have birthday information for these people:")

# Print all names in the dictionary
name_list = ", ".join(birthdays.keys())
print(f"**{name_list}**")

print("-------------------------------------------------------")

# Ask the user for a person's name
person_name = input("Enter a person's name to find their birthday: ").strip().title()

# Check if the name exists in the dictionary and print the result
if person_name in birthdays:
    # Name found: Retrieve and print the birthday
    birthday = birthdays[person_name]
    print(f"\n **{person_name}**'s birthday is on **{birthday}**.")
else:
    # Name not found: Print the specified error message
    print(f"\n Sorry, we don’t have the birthday information for **{person_name}**.")

# Exercise 3: Add Your Own Birthday
# Instructions
# Add this new code: before asking the user to input a person’s name to look up, ask the user to add a new birthday:
# Ask the user for a person’s name – store it in a variable.
# Ask the user for this person’s birthday (in the format “YYYY/MM/DD”) - store it in a variable.
# Now add this new data into your dictionary.
# Make sure that if the user types any name that exists in the dictionary – including the name that he entered himself – the corresponding birthday is found and displayed.

# Create and initialize the birthdays dictionary
birthdays = {
    "Alice": "1995/03/15",
    "Bob": "1988/11/22",
    "Charlie": "2001/07/30",
    "Diana": "1999/01/08",
    "Eve": "1990/05/25"
}

print(" Welcome to the Birthday Look-up Service! ")
print("---------------------------------------------")

# --- 1. Add New Birthday Section ---
print(">>> First, let's add a new person to the list! <<<")

# Ask for the new person's name
new_name = input("Enter the NAME of the person to add: ").strip().title()

# Ask for the new person's birthday (using the specified format)
new_bday = input("Enter their BIRTHDAY (format YYYY/MM/DD): ").strip()

# Add the new data to the dictionary
birthdays[new_name] = new_bday

print(f"\n✅ Successfully added **{new_name}** to the list.")
print("---------------------------------------------")

# --- 2. Look-up Section (Advanced) ---

print("Now, you can look up any birthday, including the one you just added.")
print("I have information for these people:")

# Print all names (including the newly added one)
name_list = ", ".join(birthdays.keys())
print(f"**{name_list}**")
print("---------------------------------------------")

# Ask the user for a person's name to look up
person_name = input("Enter a person's name to find their birthday: ").strip().title()

# Check if the name exists and print the result
if person_name in birthdays:
    # Name found: Retrieve and print the birthday
    birthday = birthdays[person_name]
    print(f"\n✅ **{person_name}**'s birthday is on **{birthday}**.")
else:
    # Name not found: Print the specified error message
    print(f"\n Sorry, we don’t have the birthday information for **{person_name}**.")

# Exercise 4: Fruit Shop
# Instructions
# items = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }
# Using the dictionary above, each key-value pair represents an item and its price - print all the items and their prices in a sentence.
# Using the dictionary below, each value are dictionaries containing both the price and the amount of items in stock -
# write some code to calculate how much it would cost to buy everything in stock.
# items = {
#     "banana": {"price": 4 , "stock":10},
#     "apple": {"price": 2, "stock":5},
#     "orange": {"price": 1.5 , "stock":24},
#     "pear": {"price": 3 , "stock":1}

# Part 1: Simple Price List Dictionary
items_price_list = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

print("--- Part 1: Item and Price Listing ---")

# Iterate through the dictionary and print each item and its price in a sentence
for item, price in items_price_list.items():
    print(f"The price of one **{item}** is **${price:.2f}**.")

print("\n" + "="*40 + "\n")


# Part 2: Advanced Stock and Price Dictionary
items_stock_list = {
    "banana": {"price": 4, "stock": 10},
    "apple": {"price": 2, "stock": 5},
    "orange": {"price": 1.5, "stock": 24},
    "pear": {"price": 3, "stock": 1}
}

print("--- Part 2: Total Cost Calculation ---")

total_cost = 0

# Iterate through the dictionary
for item, data in items_stock_list.items():
    # Extract price and stock for the current item
    price = data["price"]
    stock = data["stock"]
    
    # Calculate the cost for all units of this item
    item_total = price * stock
    
    # Add to the overall total
    total_cost += item_total
    
    print(f"**{item.title()}**: {stock} in stock @ ${price:.2f} each = **${item_total:.2f}**")

print("--------------------------------------")
# Print the final total cost
print(f"The total cost to buy everything in stock is: **${total_cost:.2f}**")