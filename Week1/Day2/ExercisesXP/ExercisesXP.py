#Exercise 1: Favorite Numbers

#Create a set called my_fav_numbers and populate it with your favorite numbers.
#Add two new numbers to the set.
#Remove the last number you added to the set.
#Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
#Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
#Note: Sets are unordered collections, so ensure no duplicate numbers are added.

my_fav_numbers={2, 7, 9, 12}
my_fav_numbers.add(31)
my_fav_numbers.add(45)
my_fav_numbers.remove(45)
friend_fav_numbers={98, 65, 14, 56}
our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)

print("My favorite numbers:", my_fav_numbers)
print("Friend's favorite numbers:", friend_fav_numbers)
print("Our favorite numbers:", our_fav_numbers)

#Exercise 2: Tuple
#Given a tuple of integers, try to add more integers to the tuple.
#Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.

tuple = (1, 2, 3)
new_elements = (4, 5)
extended_tuple = tuple + new_elements
print(extended_tuple)

#Exercise 3: List Manipulation

#You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#Remove "Banana" from the list.
#Remove "Blueberries" from the list.
#Add "Kiwi" to the end of the list.
#Add "Apples" to the beginning of the list.
##Empty the list.
#Print the final state of the list.

basket=['Banana', 'Apples', 'Oranges', 'Blueberries']
basket.remove('Banana')
basket.remove('Blueberries')
basket.append('Kiwi')
basket.insert(0, 'Apples')
count_apples = basket.count("Apples")
basket.clear()
print("Final list:", basket)

# Exercise 4: Floats

# Recap: What is a float? What’s the difference between a float and an integer?
# Create a list containing the following sequence of mixed types: floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.
# Think: Can you generate this sequence using a loop or another method?

sequence = []
start = 1.5
end = 5.0
step = 0.5

value = start
while value < end:
    sequence.append(value)
    value += step

print(sequence)

# Exercise 5: For Loop

# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even.

for i in range(1, 21):
    print(i)

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# Exercise 6: While Loop

# Use an input to ask the user to enter their name.
# Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
# hint: check for the method isdigit()
# if the input is incorrect, keep asking for the correct input until it is correct
# if the input is correct print “thank you” and break the loop

while True:
    name = input("Enter your name: ")
    if not any(c.isdigit() for c in name) and len(name) >= 3:
        print("Thank you!")
        break
    else:
        print("Give the correct name.")

# Exercise 7: Favorite Fruits

# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print:
# "You chose a new fruit. I hope you enjoy it!"

favorite_fruits = input("Enter your favorite fruit/fruits (separate by spaces): ").split()
fruit = input("Enter the name of a fruit: ")

if fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

# Exercise 8: Pizza Toppings

# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.

toppings = []
base_price = 10
topping_price = 2.5

while True:
    topping = input("Enter a topping for the pizza (or type 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    toppings.append(topping)
    print("Adding " + topping + " to your pizza.")

print("\nYour pizza includes the following toppings:")
for t in toppings:
    print("- " + t)

total_price = base_price + len(toppings) * topping_price
print("Total price: $" + str(total_price))

# Exercise 9: Cinemax Tickets

# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.

ages = []
total_cost = 0

while True:
    age_input = input("Enter the age of each family member, type'done' to finish): ")
    if age_input.lower() == 'done':
        break

    try:
        age = int(age_input)
        ages.append(age)
    except ValueError:
        print("Please enter a valid number.")
        
for age in ages:
    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15
    total_cost += cost

print("Total ticket cost is: $", total_cost)

# Bonus:

# Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
# Write a program to:
# Ask for each person’s age.
# Remove anyone who isn’t allowed to watch.
# Print the final list of attendees.

names = []

while True:
    entry = input("Enter name and age separated by a comma, print 'done' to finish): ")
    if entry.lower() == 'done':
        break
    try:
        name, age_str = entry.split(',')
        name = name.strip()
        age = int(age_str.strip())
        if 16 <= age <= 21:
            names.append(name)
    except ValueError:
        print("Incorrect format. Please try again: name, age.")

print("Allowed attendees:", ', '.join(names))