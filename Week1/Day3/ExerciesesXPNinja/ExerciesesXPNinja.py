# Exercise 1 : Cars
# Instructions
# Copy the following string into your code: "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".
# Convert it into a list using Python (don’t do it by hand!).
# Print out a message saying how many manufacturers/companies are in the list.
# Print the list of manufacturers in reverse/descending order (Z-A).
# Using loops or list comprehension:
# Find out how many manufacturers’ names have the letter ‘o’ in them.
# Find out how many manufacturers’ names do not have the letter ‘i’ in them.

# Bonus: There are a few duplicates in this list:["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
# Remove these programmatically. (Hint: you can use set to help you).
# Print out the companies without duplicates, in a comma-separated string with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, …”), also print out a message saying how many companies are now in the list.

# Bonus: Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name.

# Initial data string
car_string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
print(f"Initial string: \"{car_string}\"")

# 1. Convert the string into a list
manufacturers = car_string.split(", ")

# 2. Print the number of manufacturers
num_manufacturers = len(manufacturers)
print(f"\nThere are **{num_manufacturers}** manufacturers/companies in the list.")

# 3. Print the list in reverse/descending order (Z-A)
manufacturers_za = sorted(manufacturers, reverse=True)
print(f"Manufacturers in descending (Z-A) order: {manufacturers_za}")

# 4. Find how many names have the letter ‘o’
# Using list comprehension for efficiency
o_count = len([name for name in manufacturers if 'o' in name.lower()])
print(f"Number of manufacturers' names containing the letter 'o': **{o_count}**")

# 5. Find how many names do not have the letter ‘i’
i_not_count = len([name for name in manufacturers if 'i' not in name.lower()])
print(f"Number of manufacturers' names that **do not** contain the letter 'i': **{i_not_count}**")

print("\n" + "="*50)

## Bonus 1: Remove Duplicates

duplicates_list = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
print(f"Bonus 1: Initial list with duplicates: {duplicates_list}")

# Use a set to automatically remove duplicates
unique_manufacturers_set = set(duplicates_list)

# Convert the set back to a list (optional, but necessary for joining)
unique_manufacturers_list = list(unique_manufacturers_set)

# Print as a comma-separated string
unique_string = ", ".join(unique_manufacturers_list)
print(f"Companies without duplicates: **{unique_string}**")

# Print the new count
new_count = len(unique_manufacturers_list)
print(f"There are now **{new_count}** unique companies in the list.")

print("\n" + "="*50)

## Bonus 2: Reverse Letters, Ascending Order (A-Z)

# Start with the original manufacturers list and sort it A-Z
manufacturers_az = sorted(manufacturers)

# Reverse the letters of each name using list comprehension
# name[::-1] is a slice that reverses the string
reversed_names_list = [name[::-1] for name in manufacturers_az]

print(f"Bonus 2: List sorted A-Z, with reversed letters: {reversed_names_list}")
print("="*50)