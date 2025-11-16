# Exercise 1: Cat

# Key Python Topics:
# Classes and objects
# Object instantiation
# Attributes
# Functions

# Instructions:
# Use the provided Cat class to create three cat objects. Then, create a function to find the oldest cat and print its details.

# Step 1: Create Cat Objects
# Use the Cat class to create three cat objects with different names and ages.

# Step 2: Create a Function to Find the Oldest Cat
# Create a function that takes the three cat objects as input.
# Inside the function, compare the ages of the cats to find the oldest one.
# Return the oldest cat object.

# Step 3: Print the Oldest Cat’s Details
# Call the function to get the oldest cat.
# Print a formatted string: “The oldest cat is <cat_name>, and is <cat_age> years old.”
# Replace <cat_name> and <cat_age> with the oldest cat’s name and age.

# Example:

# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age

# # Step 1: Create cat objects
# # cat1 = create the object

# # Step 2: Create a function to find the oldest cat
# def find_oldest_cat(cat1, cat2, cat3):
#     # ... code to find and return the oldest cat ...

# # Step 3: Print the oldest cat's details

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat('Barsik', 1)
cat2 = Cat('Musya', 8)
cat3 = Cat("Tikva", 4)


def find_oldest_cat(cat1, cat2, cat3):
    list_of_cats=[cat1, cat2, cat3]
    oldest_cat = max(list_of_cats, key = lambda cat: cat.age)
    return oldest_cat

oldest_cat_object = find_oldest_cat(cat1, cat2, cat3)

print(f'Name: {oldest_cat_object.name}')
print(f'Age: {oldest_cat_object.age}')

# Exercise 2 : Dogs

# Goal: Create a Dog class, instantiate objects, call methods, and compare dog sizes.

# Key Python Topics:
# Classes and objects
# Object instantiation
# Methods
# Attributes
# Conditional statements (if)

# Instructions:
# Create a Dog class with methods for barking and jumping. Instantiate dog objects, call their methods, and compare their sizes.

# Step 1: Create the Dog Class
# Create a class called Dog.
# In the __init__ method, take name and height as parameters and create corresponding attributes.
# Create a bark() method that prints “<dog_name> goes woof!”.
# Create a jump() method that prints “<dog_name> jumps <x> cm high!”, where x is height * 2.

# Step 2: Create Dog Objects
# Create davids_dog and sarahs_dog objects with their respective names and heights.

# Step 3: Print Dog Details and Call Methods
# Print the name and height of each dog.
# Call the bark() and jump() methods for each dog.

# Step 4: Compare Dog Sizes

class Dog:
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height

    def bark(self):
        print(f'{self.name} Woof!')

    def jump(self):
        jump_distance = self.height*2
        print(f'{self.name} jumps {jump_distance} meters')

dog1 = Dog('Rex', 0.6)
dog2 = Dog('Sharik', 0.4)
dog3 = Dog('Muhtar', 0.8)

dog1.bark()
dog2.bark()

dog1.jump()
dog2.jump()

davids_dog = Dog('Yossi', 0.2)
sarahs_dog = Dog('Sima', 0.4)

davids_dog.bark()
sarahs_dog.bark()

davids_dog.jump()
sarahs_dog.jump()


# Exercise 3 : Who’s the song producer?

# Goal: Create a Song class to represent song lyrics and print them.

# Key Python Topics:
# Classes and objects
# Object instantiation
# Methods
# Lists

# Instructions:
# Create a Song class with a method to print song lyrics line by line.

# Step 1: Create the Song Class
# Create a class called Song.
# In the __init__ method, take lyrics (a list) as a parameter and create a corresponding attribute.
# Create a sing_me_a_song() method that prints each element of the lyrics list on a new line.

# Example:

# stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

# stairway.sing_me_a_song()

# Output: There’s a lady who’s sureall that glitters is goldand she’s buying a stairway to heaven

class Song():
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song([
    "There's a lady who's sure", 
    "all that glitters is gold", 
    "and she’s buying a stairway to heaven"
])

stairway.sing_me_a_song()

# Exercise 4 : Afternoon at the Zoo

# Goal:
# Create a Zoo class to manage animals. The class should allow adding animals, displaying them, selling them, and organizing them into alphabetical groups.

# Key Python Topics:
# Classes and objects
# Object instantiation
# Methods
# Lists
# Dictionaries (for grouping)
# String manipulation

# Instructions
# Step 1: Define the Zoo Class
# 1. Create a class called Zoo.
# 2. Implement the __init__() method:
# It takes a string parameter zoo_name, representing the name of the zoo.
# Initialize an empty list called animals to keep track of animal names.
# 3. Add a method add_animal(new_animal):
# This method adds a new animal to the animals list.
# Do not add the animal if it is already in the list.
# 4. Add a method get_animals():
# This method prints all animals currently in the zoo.
# 5. Add a method sell_animal(animal_sold):
# This method checks if a specified animal exists on the animals list and if so, remove from it.
# 6. Add a method sort_animals():
# This method sorts the animals alphabetically.
# It also groups them by the first letter of their name.
# The result should be a dictionary where:
# Each key is a letter.
# Each value is a list of animals that start with that letter.
# Example output:

# {
#    'B': ['Baboon', 'Bear'],
#    'C': ['Cat', 'Cougar'],
#    'G': ['Giraffe'],
#    'L': ['Lion'],
#    'Z': ['Zebra']
# }
# 7. Add a method get_groups():

# This method prints the grouped animals as created by sort_animals().
# Example output:

# B: ['Baboon', 'Bear']
# C: ['Cat', 'Cougar']
# G: ['Giraffe']
# ...


# Step 2: Create a Zoo Object
# Create an instance of the Zoo class and pass a name for the zoo.

# Step 3: Call the Zoo Methods
# Use the methods of your Zoo object to test adding, selling, displaying, sorting, and grouping animals.

# Example (No Internal Logic Provided)
# class Zoo:
#     def __init__(self, zoo_name):
#         pass

#     def add_animal(self, new_animal):
#         pass

#     def get_animals(self):
#         pass

#     def sell_animal(self, animal_sold):
#         pass

#     def sort_animals(self):
#         pass

#     def get_groups(self):
#         pass

# # Step 2: Create a Zoo instance
# brooklyn_safari = Zoo("Brooklyn Safari")

# # Step 3: Use the Zoo methods
# brooklyn_safari.add_animal("Giraffe")
# brooklyn_safari.add_animal("Bear")
# brooklyn_safari.add_animal("Baboon")
# brooklyn_safari.get_animals()
# brooklyn_safari.sell_animal("Bear")
# brooklyn_safari.get_animals()
# brooklyn_safari.sort_animals()
# brooklyn_safari.get_groups()


# Bonus: Modify the add_animal() method to get *args so you dont need to repeat the method each time for a new animal, you can pass multiple animals names separated by a comma.

import collections

class Zoo():
    def __init__(self, zoo_name: str):
        self.zoo_name = zoo_name
        self.animals =[]
        self.groups = {}

    def add_animals(self, *new_animals):
        added_count = 0
        for animal in new_animals:
            clean_animal = animal.strip().capitalize()
            if clean_animal and clean_animal not in self.animals:
                self.animals.append(clean_animal)
                added_count +=1
        if added_count>0:
                print(f'Added {added_count} new animal(s) to {self.zoo_name}')
        else:
                print('No new animals were added')

    def get_animals(self):
        print(f'\nCurrent animals in {self.zoo_name}({len(self.animals)})')
        if self.animals:
            print(', '.join(self.animals))
        else:
            print('The zoo is empty.')
     
    def sell_animal(self, animal_sold):
        clean_animal = animal_sold.strip().capitalize()
        if clean_animal in self.animals:
            self.animals.remove(clean_animal)
            self.sort_animals() 
            print(f'Sold: {clean_animal} has been removes.')
        else:
            print(f'Error: {clean_animal} is not cuttently in the zoo')


    def sort_animals(self):
      
        self.animals.sort()
        groups = collections.defaultdict(list)

        for animal in self.animals:
            first_letter = animal[0].upper()        
            groups[first_letter].append(animal)
            self.groups = dict(groups)
            print(" Animals sorted and grouped successfully.")

    def get_groups(self):
        print(f"\n--- Animal Groups in {self.zoo_name} ---")
        if self.groups:
            for letter, animal_list in self.groups.items():
                print(f"{letter}: {animal_list}")
        else:
            print("Groups are not yet generated. Please run sort_animals() first.")

brooklyn_safari = Zoo("Brooklyn Safari")

brooklyn_safari.add_animals("Giraffe", "Bear", "Baboon", "Cougar", "lion", "Zebra", "Cat")
brooklyn_safari.add_animals("Giraffe")

brooklyn_safari.get_animals()

print('selling an animal')
brooklyn_safari.sell_animal("bear")
brooklyn_safari.sell_animal("Rhinoceros")

brooklyn_safari.get_animals()

print('sorting and groupping')
brooklyn_safari.sort_animals()

brooklyn_safari.get_groups()