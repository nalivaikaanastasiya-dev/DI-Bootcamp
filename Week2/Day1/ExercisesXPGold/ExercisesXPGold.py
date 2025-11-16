# Exercise 1 : Geometry
# Instructions
# Write a class called Circle that receives a radius as an argument (default is 1.0).
# Write two instance methods to compute perimeter and area.
# Write a method that prints the geometrical definition of a circle.

import math

class Circle:
    """
    Represents a circle defined by its radius. 
    Includes methods to calculate its perimeter and area, 
    and display its geometric definition.
    """
    
    def __init__(self, radius=1.0):
        """
        Initializes the Circle with a given radius.
        
        :param radius: The radius of the circle. Defaults to 1.0.
        :raises ValueError: If the radius is not a positive number.
        """
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius

    def get_perimeter(self):
        """
        Computes the perimeter (circumference) of the circle.
        Formula: Perimeter = 2 * pi * r
        
        :return: The calculated perimeter as a float.
        """
        return 2 * math.pi * self.radius

    def get_area(self):
        """
        Computes the area of the circle.
        Formula: Area = pi * r^2
        
        :return: The calculated area as a float.
        """
        return math.pi * (self.radius ** 2)

    def print_definition(self):
        """
        Prints the geometrical definition of a circle.
        """
        definition = (
            "A circle is a shape consisting of all points in a plane that are "
            "at a given distance (the radius) from a given point (the center). "
            "It is the boundary of a disk."
        )
        print("\n--- Geometrical Definition ---")
        print(definition)
        print("------------------------------")


# --- Testing the Circle Class ---

# 1. Create a circle with the default radius (1.0)
circle1 = Circle()
print(f"Circle 1 (Default Radius): {circle1.radius}")
print(f"Perimeter: {circle1.get_perimeter():.2f}")
print(f"Area: {circle1.get_area():.2f}")

# 2. Create a circle with a specific radius (5.5)
radius2 = 5.5
circle2 = Circle(radius2)
print(f"\nCircle 2 (Radius: {radius2}): {circle2.radius}")
print(f"Perimeter: {circle2.get_perimeter():.2f}")
print(f"Area: {circle2.get_area():.2f}")

# 3. Test the definition method
circle2.print_definition()

# 4. Demonstration of changing the radius (though often discouraged in real-world classes)
circle1.radius = 10.0
print(f"\nCircle 1 updated to Radius: {circle1.radius}")
print(f"New Area: {circle1.get_area():.2f}")

# 5. Example of handling invalid input (optional but good practice)
try:
    Circle(-2.0)
except ValueError as e:
    print(f"\nError: {e}")

# Exercise 2 : Custom List Class
# Instructions
# Create a class called MyList, the class should receive a list of letters.
# Add a method that returns the reversed list.
# Add a method that returns the sorted list.
# Bonus : Create a method that generates a second list with the same length as mylist. The list should be constructed with random numbers. (use list comprehension).

import random

class MyList:
    """
    A custom list class that stores a list of letters and provides 
    methods for common list operations like reversal and sorting.
    """
    
    def __init__(self, letters):
        """
        Initializes the MyList object with a list of letters.
        
        :param letters: A list containing character strings (letters).
        """
        self.letters = letters
        print(f"✅ MyList created with: {self.letters}")

    def get_reversed_list(self):
        """
        Returns a new list containing the elements in reverse order.
        
        :return: A new list that is the reverse of the original list.
        """
        # The slicing trick [::-1] creates a reversed copy of the list
        return self.letters[::-1]

    def get_sorted_list(self):
        """
        Returns a new list containing the elements sorted alphabetically.
        
        :return: A new, sorted list.
        """
        # .sorted() returns a new sorted list without modifying the original
        return sorted(self.letters)

    def generate_random_list(self, max_value=100):
        """
        (Bonus) Generates a second list of random integers.
        The new list has the same length as the original list (self.letters).
        
        :param max_value: The maximum possible random integer. Defaults to 100.
        :return: A list of random integers.
        """
        list_length = len(self.letters)
        # Using list comprehension to efficiently generate the random numbers
        random_list = [random.randint(1, max_value) for _ in range(list_length)]
        return random_list


# --- Demonstration and Testing ---

# 1. Instantiate the class
original_data = ['z', 'd', 'k', 'a', 'r', 'f']
my_list_instance = MyList(original_data)

# 2. Test the reversal method
reversed_result = my_list_instance.get_reversed_list()
print(f"\nOriginal List: {my_list_instance.letters}")
print(f"Reversed List: {reversed_result}")

# 3. Test the sorting method
sorted_result = my_list_instance.get_sorted_list()
print(f"Sorted List:   {sorted_result}")

# Verify the original list remains unchanged
print(f"Original List (After Ops): {my_list_instance.letters}")

# 4. Test the bonus method
random_result = my_list_instance.generate_random_list(max_value=50)
print(f"\nLength of original list: {len(my_list_instance.letters)}")
print(f"Generated Random List (same length): {random_result}")

# Exercise 3 : Restaurant Menu Manager

# Instructions
# The purpose of this exercise is to create a restaurant menu. The code will allow a manager to add and delete dishes.
# Create a python file called menu_manager.py.
# Create a class called MenuManager.
# Create a method __init__ that instantiates an attribute called menu. The menu attributes value will be all the current dishes (list of dictionaries). Each dish will be stored in a dictionary where the keys are name, price, spice level and gluten index (which value is a boolean).
# Here is a list of the dishes currently on the menu:

#     Soup – 10 – B - False
#     Hamburger – 15 - A - True
#     Salad – 18 - A - False
#     French Fries – 5 - C - False
#     Beef bourguignon– 25 - B - True

#     Meaning: For the spice level:
#        • A = not spicy,
#        • B = a little spicy,
#        • C = very spicy


# The dishes provided above should be the value of the menu attribute.
# Create a method called add_item(name, price, spice, gluten). This method will add new dishes to the menu.
# Create a method called update_item(name, price, spice, gluten). This method checks whether a dish is in the menu, if the dish exists then update it. If not notify the manager that the dish is not in the menu.
# Create a method called remove_item(name). This method should check if the dish is in the menu, if the dish exists then delete it and print the updated dictionary. If not notify the manager that the dish is not in the menu.

class MenuManager:
    """
    Manages the restaurant menu, allowing dishes to be added, 
    updated, and removed.
    """
    
    def __init__(self):
        """
        Instantiates the menu attribute with the current list of dishes.
        Spice level key: A=not spicy, B=a little spicy, C=very spicy
        """
        self.menu = [
            # name, price, spice level, gluten index (boolean)
            {"name": "Soup", "price": 10, "spice_level": "B", "gluten_index": False},
            {"name": "Hamburger", "price": 15, "spice_level": "A", "gluten_index": True},
            {"name": "Salad", "price": 18, "spice_level": "A", "gluten_index": False},
            {"name": "French Fries", "price": 5, "spice_level": "C", "gluten_index": False},
            {"name": "Beef bourguignon", "price": 25, "spice_level": "B", "gluten_index": True},
        ]
        print("✅ MenuManager initialized with initial dishes.")

    def add_item(self, name: str, price: int, spice: str, gluten: bool):
        """
        Adds a new dish to the menu.

        :param name: Name of the dish (string).
        :param price: Price of the dish (integer).
        :param spice: Spice level (A, B, or C).
        :param gluten: Gluten index (True/False).
        """
        new_dish = {
            "name": name.title(), # Standardize capitalization
            "price": price,
            "spice_level": spice.upper(),
            "gluten_index": gluten,
        }
        self.menu.append(new_dish)
        print(f"\n➕ SUCCESSFULLY ADDED: {name.title()} to the menu.")

    def update_item(self, name: str, price: int, spice: str, gluten: bool):
        """
        Updates an existing dish on the menu if it is found.

        :param name: Name of the dish to update (string).
        :param price: New price of the dish (integer).
        :param spice: New spice level (A, B, or C).
        :param gluten: New gluten index (True/False).
        """
        name_title = name.title()
        
        # Iterate through the menu to find the dish
        for dish in self.menu:
            if dish["name"] == name_title:
                # Dish found, update its attributes
                dish["price"] = price
                dish["spice_level"] = spice.upper()
                dish["gluten_index"] = gluten
                print(f"\n🔄 SUCCESSFULLY UPDATED: {name_title} details.")
                return
        
        # If the loop finishes without finding the dish
        print(f"\n❌ NOT FOUND: Dish '{name_title}' is not currently in the menu.")

    def remove_item(self, name: str):
        """
        Removes a dish from the menu if it is found.

        :param name: Name of the dish to remove (string).
        """
        name_title = name.title()
        
        # We need to find the dish's index or object to remove it
        for i, dish in enumerate(self.menu):
            if dish["name"] == name_title:
                # Dish found, remove it using its index
                removed_dish = self.menu.pop(i)
                print(f"\n🗑️ SUCCESSFULLY REMOVED: {removed_dish['name']}.")
                print("\nUpdated Menu:")
                print(self.menu)
                return
        
        # If the loop finishes without finding the dish
        print(f"\n❌ NOT FOUND: Dish '{name_title}' is not currently in the menu.")

    def display_menu(self):
        """Helper method to neatly display the current menu."""
        print("\n==================================")
        print("     CURRENT RESTAURANT MENU")
        print("==================================")
        print(f"{'NAME':<20}{'PRICE':<8}{'SPICE':<8}{'GLUTEN'}")
        print("-" * 45)
        for dish in self.menu:
            gluten_status = "Yes" if dish['gluten_index'] else "No"
            print(f"{dish['name']:<20}${dish['price']:<7}{dish['spice_level']:<8}{gluten_status}")
        print("==================================")


# --- Demonstration ---

manager = MenuManager()

# 1. Display the initial menu
manager.display_menu()

# 2. Test add_item
manager.add_item("Tacos", 12, "C", False)
manager.add_item("Grilled Chicken", 20, "A", False)
manager.display_menu()

# 3. Test update_item (Success)
manager.update_item("Soup", 12, "A", False)
manager.display_item("Soup") # Check the specific item update
manager.display_menu()

# 4. Test update_item (Failure)
manager.update_item("Pizza", 30, "A", True)

# 5. Test remove_item (Success)
manager.remove_item("Hamburger")

# 6. Test remove_item (Failure)
manager.remove_item("Tuna Sandwich")

# 7. Final menu display
manager.display_menu()