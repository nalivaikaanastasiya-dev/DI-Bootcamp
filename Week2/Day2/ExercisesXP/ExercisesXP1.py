# Exercise 3: Dogs Domesticated

# Goal: Create a PetDog class that inherits from Dog and adds training and tricks.

# Instructions:

# Step 1: Import the Dog Class
# In a new Python file, import the Dog class from the previous exercise.

# Step 2: Create the PetDog Class
# Create a class called PetDog that inherits from the Dog class.
# Add a trained attribute to the __init__ method, with a default value of False.
# trained means that the dog is trained to do some tricks.
# Implement a train() method that prints the output of bark() and sets trained to True.
# Implement a play(*args) method that prints “<dog_names> all play together”.
# *args on this method is a list of dog instances.
# Implement a do_a_trick() method that prints a random trick if trained is True.
# Use this list for the ramdom tricks:
# tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
# Choose a random index from it each time the method is called.

# Step 3: Test PetDog Methods
# Create instances of the PetDog class and test the train(), play(*args), and do_a_trick() methods.

# Example:

# # In a new file
# # import the Dog class

# class PetDog(Dog):
#     def __init__(self, name, age, weight): <mark> no need to put the details in the function, you are giving the solution</mark>
#         super().__init__(name, age, weight)
#         self.trained = False

#     def train(self): <mark> no need to put the details in the function, you are giving the solution</mark>
#         print(self.bark())
#         self.trained = True

#     def play(self, *args):
#         # ... code to print play message ...

#     def do_a_trick(self): <mark> no need to put the details in the function, you are giving the solution</mark>
#         if self.trained:
#             tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
#             print(f"{self.name} {random.choice(tricks)}")

# # Test PetDog methods
# my_dog = PetDog("Fido", 2, 10)
# my_dog.train()
# my_dog.play("Buddy", "Max")
# my_dog.do_a_trick()

from ExercisesXP import Dog

import random

class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained=trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = [self.name]
        for dog in args:
            if isinstance(dog, Dog):
                dog_names.append(dog.name)
            else:
                dog_names.append(str(dog))
        
        if len(dog_names) <= 2:
            names_string = " and ".join(dog_names)
        else:
            names_string = ", ".join(dog_names[:-1]) + f", and {dog_names[-1]}"
            
        print(f"{names_string} all play together")

    def do_a_trick(self):
    
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            trick = random.choice(tricks) 
            print(f"{self.name} {trick}.")
        else:
            print(f"{self.name} Not trained yet")       

Rex = PetDog("Rex", 3, 8) 
Muhtar = PetDog("Muhtar", 2, 1) 
Sharik = PetDog("Sharik", 6, 12) 
Lord = PetDog("Lord", 8, 16)

print(f"\nInitial status for {Rex.name}: Trained={Rex.trained}")

print("\n Training Rex")
Rex.train()
print(f"Status after training: Trained={Rex.trained}")
print("Rex performs tricks")
Rex.do_a_trick()
Rex.do_a_trick()

print("\nMuhtar (Untrained) attempts a trick")
Muhtar.do_a_trick()

print("\nDogs Play")

Lord.play(Lord, Sharik)

Rex.play("Muhtar", "Rex")