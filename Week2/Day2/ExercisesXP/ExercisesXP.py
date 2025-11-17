# Exercise 1: Pets

# Instructions:
# Use the provided Pets and Cat classes to create a Siamese breed, instantiate cat objects, and use the Pets class to manage them.
# See the example below, before diving in.

# Step 1: Create the Siamese Class
# Create a class called Siamese that inherits from the Cat class.
# You can add any specific attributes or methods for the Siamese breed, or leave it as is if there are no unique behaviors.

# Step 2: Create a List of Cat Instances
# Create a list called all_cats that contains instances of Bengal, Chartreux, and Siamese cats.
# Example: all_cats = [bengal_obj, chartreux_obj, siamese_obj]
# Give each cat a name and age.

# Step 3: Create a Pets Instance
# Create an instance of the Pets class called sara_pets, passing the all_cats list as an argument.

# Step 4: Take Cats for a Walk
# Call the walk() method on the sara_pets instance.
# This should print the result of calling the walk() method on each cat in the list.

# Example:

# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'


# Step 1: Create the Siamese class

# Step 2: Create a list of cat instances

# Step 3: Create a Pets instance of the list of cat instances

# sara_pets = Pets(all_cats)

# Step 4: Take cats for a walk
# sara_pets.walk()

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat(Pets):
    is_lazy = True
    def __init__(self, animals, name, age, lazy):
        super().__init__(animals)
        self.name = name
        self.age = age
        self.lazy = lazy

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def __init__(self, name, age, animals='Cat', lazy=True, color='grey'):
        super().__init__(animals, name, age, lazy)
        self.color = color

    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def __init__(self, name, age, animals='Cat', lazy=False, pretty=True):
        super().__init__(animals, name, age, lazy)
        self.pretty = pretty

    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def __init__(self, name, age, animals='Cat', lazy=True, house_cat=True):
        super().__init__(animals, name, age, lazy)
        self.house_cat = house_cat

    def sing(self, sounds):
        return f'{sounds}'

bengal_obj=Bengal('Gigi',8)
chartreux_obj=Chartreux('Musya', 5)
siamese_obj=Siamese('Tikva', 1)

all_cats = [bengal_obj, chartreux_obj, siamese_obj]

sara_pets=Pets(all_cats)

sara_pets.walk()

# Exercise 2: Dogs

# Goal: Create a Dog class with methods for barking, running speed, and fighting.

# Instructions:

# Step 1: Create the Dog Class
# Create a class called Dog with name, age, and weight attributes.
# Implement a bark() method that returns “<dog_name> is barking”.
# Implement a run_speed() method that returns weight / age * 10.
# Implement a fight(other_dog) method that returns a string indicating which dog won the fight, based on run_speed * weight.

# Step 2: Create Dog Instances
# Create three instances of the Dog class with different names, ages, and weights.

# Step 3: Test Dog Methods
# Call the bark(), run_speed(), and fight() methods on the dog instances to test their functionality.

# Example (Conceptual, No Direct Solution):

# class Dog:
#     def __init__(self, name, age, weight):
#         # ... code to initialize attributes ...

#     def bark(self):
#         # ... code to return bark message ...

#     def run_speed(self):
#         # ... code to return run speed ...

#     def fight(self, other_dog):
#         # ... code to determine and return winner ...

# # Step 2: Create dog instances
# #... your code here

# # Step 3: Test dog methods
# print(dog1.bark())
# print(dog2.run_speed())
# print(dog1.fight(dog2))

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return 0.0 if self.age == 0 else (self.weight / self.age) * 10

    def fight(self, other_dog):
        self_speed = self.run_speed()
        self_power = self_speed * self.weight
        
        other_speed = other_dog.run_speed()
        other_power = other_speed * other_dog.weight
        
        if self_power > other_power:
            winner_name = self.name
        elif other_power > self_power:
            winner_name = other_dog.name
        else:
            return f"{self.name} and {other_dog.name} fought to a draw"
        return f"Winner is {winner_name} with power {max(self_power, other_power):.2f}."

dog1=Dog('Rex', 8, 10)
dog2=Dog('Muhtar', 2, 6)
dog3=Dog('Sharik', 6, 8)

print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))

# Exercise 4: Family and Person Classes

# Goal:
# Practice working with classes and object interactions by modeling a family and its members

# Key Python Topics:

# Classes and objects
# Instance methods
# Object interaction
# Lists and loops
# Conditional statements (if/else)
# String formatting (f-strings)

# Instructions:

# Step 1: Create the Person Class
# Define a Person class with the following attributes:
# first_name
# age
# last_name (string, should be initialized as an empty string)
# Add a method called is_18():
# It should return True if the person is 18 or older, otherwise False.

# Step 2: Create the Family Class
# Define a Family class with:
# A last_name attribute
# A members list that will store Person objects (should be initialized as an empty list)
# Add a method called born(first_name, age):
# It should create a new Person object with the given first name and age.
# It should assign the family’s last name to the person.
# It should add this new person to the members list.
# Add a method called check_majority(first_name):
# It should search the members list for a person with that first_name.
# If the person exists, call their is_18() method.
# If the person is over 18, print:
# "You are over 18, your parents Jane and John accept that you will go out with your friends"
# Otherwise, print:
# "Sorry, you are not allowed to go out with your friends."
# Add a method called family_presentation():
# It should print the family’s last name.
# Then, it should print each family member’s first name and age.


# Expected Behavior:
# Once implemented, your program should allow you to:

# Create a family with a last name.
# Add members to the family using the born() method.
# Use check_majority() to see if someone is allowed to go out.
# Display family information with family_presentation().
# Don’t forget to test your classes by creating an instance of Family, adding members, and calling each method to see the expected output.

class Person:
    def __init__(self, first_name, age, last_name:str=''):
        self.first_name=first_name
        self.age=age
        self.last_name=last_name

    def is_18(self):
        return self.age >= 18
    def __str__(self):
        return f'{self.first_name} {self.last_name} (Age: {self.age})'

class Family:
    def __init__(self, last_name: str):
        self.last_name=last_name
        self.members=[]

    def born(self, first_name: str, age: int):
        new_person=Person(first_name=first_name, age=age, last_name=self.last_name)
        self.members.append(new_person)
        print(f"Welcome! {first_name} {self.last_name}, age {age}, has been born in the family.")

    def check_majority(self, first_name: str):
            found_person = None
            for member in self.members:
                if member.first_name == first_name:
                 found_person = member
                break

            if found_person:
                print(f'\nChecking majority for {found_person.first_name} {found_person.last_name}')
                if found_person.is_18():
                    print(f"You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print(f'Sorry, you are not allowed to go out with your friends.')
            else:
                print(f'\n Error: Person with first name "{first_name}" not found in the family.')

    def family_presentation(self):
        print("\n" + "="*40)
        print(f'Family Presentation: The {self.last_name} Famil')
        print("="*40)
        if self.members:
            for member in self.members:
                    print(f'  - {member.first_name}: Age {member.age}')
        else:
            print('(No members currently in the family.)')
        print("="*40)



print('Testing the Family and Person Classes')

Ivanov_family = Family('Ivanov')
print(f'Successfully created the {Ivanov_family.last_name} family.')

Ivanov_family.born('John', 45)  
Ivanov_family.born('Jane', 42) 
Ivanov_family.born('Mary', 20) 
Ivanov_family.born('Jack', 16)

Ivanov_family.family_presentation()

Ivanov_family.check_majority('Mary')

Ivanov_family.check_majority('Jack')

Ivanov_family.check_majority("Robert")

