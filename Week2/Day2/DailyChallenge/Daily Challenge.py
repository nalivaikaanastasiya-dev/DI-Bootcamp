# Daily Challenge : Pagination

# Key Python Topics:

# Classes and Objects
# Constructors and instance attributes
# List slicing and indexing
# Method chaining (return self)
# Type casting (int())
# Conditional logic
# Custom exception

# Instructions: Pagination System

# Goal:

# Create a Pagination class that simulates a basic pagination system.

# Step 1: Create the Pagination Class
# Define a class called Pagination to represent paginated content.
# It should optionally accept a list of items and a page size when initialized.

# Step 2: Implement the __init__ Method
# Accept two optional parameters:
# items (default None): a list of items
# page_size (default 10): number of items per page
# Behavior:
# If items is None, initialize it as an empty list.
# Save page_size and set current_idx (current page index) to 0.
# Calculate total number of pages using math.ceil.

# Step 3: Implement the get_visible_items() Method
# This method returns the list of items visible on the current page.
# Use slicing based on the current_idx and page_size.

# Step 4: Implement Navigation Methods
# These methods should help navigate through pages:
# go_to_page(page_num)
# → Goes to the specified page number (1-based indexing).
# → If page_num is out of range, raise a ValueError.
# first_page()
# → Navigates to the first page.
# last_page()
# → Navigates to the last page.
# next_page()
# → Moves one page forward (if not already on the last page).
# previous_page()
# → Moves one page backward (if not already on the first page).
# Note:
# Pages are indexed internally from 0, but user input is expected to start at 1.
# All navigation methods (except go_to_page) should return self to allow method chaining.

# Bonus
# Step 5: Add a Custom __str__() Method
# This magic method should return a string displaying the items on the current page, each on a new line.
# Example:
# alphabetList = list("abcdefghijklmnopqrstuvwxyz")
# p = Pagination(alphabetList, 4)
# print(str(p))
# # Output:
# # a
# # b
# # c
# # d

# Step 6: Test Your Code
# Use the following test cases:
# alphabetList = list("abcdefghijklmnopqrstuvwxyz")
# p = Pagination(alphabetList, 4)
# print(p.get_visible_items())
# # ['a', 'b', 'c', 'd']
# p.next_page()
# print(p.get_visible_items())
# # ['e', 'f', 'g', 'h']
# p.last_page()
# print(p.get_visible_items())
# # ['y', 'z']
# p.go_to_page(10)
# print(p.current_idx + 1)
# # Output: ValueError
# p.go_to_page(0)
# # Raises ValueError

# Bonus: upgrade your code by changing the return statement in a way that will allor you to concatenate methods like this:
# p.nextPage().nextPage().nextPage().getVisibleItems()
# output: [‘m’, ‘n’, ‘o’, ‘p’]

import math

class Pagination:
    def __init__(self, items=None,  page_size=10):
        self.items = items if items is not None else []
        self.page_size=int(page_size)
        self.current_idx = 0
        if not self.items:
            self.total_pages = 0
        else:
            self.total_pages=math.ceil(len(self.items)/self.page_size)
    def get_visible_items(self):
        start_index = self.current_idx*self.page_size
        end_index = start_index + self.page_size
        return self.items[start_index:end_index]

    def go_to_page (self, page_num):
        try:
            page_num  =int(page_num)
        except ValueError:
            raise ValueError('The page number must be an integer.')

        if page_num < 1 or page_num > self.total_pages:
            if not self.total_pages and page_num == 1:
                self.current_idx = 0
                return
            raise ValueError('The page number must be from 1 to {self.total_pages} (inclusive).')

        self.current_idx = page_num - 1
    def first_page(self):
        if self.total_pages > 0:
            self.current_idx = 0
        return self

    def last_page(self):
        if self.total_pages > 0:
            self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page (self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    def __str__(self):
        return '\n'.join(str(item) for item in self.get_visible_items())


alphabetList = list('abcdefghijklmnopqrstuvwxyz')
p = Pagination(alphabetList, 4)

print('Initial state')
print(f'Total pages: {p.total_pages}')
print(f'Current index: (Page 1): {p.current_idx + 1}')
print(f'Visible elements: {p.get_visible_items()}')

print('Next page')
p.next_page()
print(f'Current index (Psge 2): {p.current_idx + 1}')
print(f'Visible elements: {p.get_visible_items()}')

print('\n Last page')
p.last_page()
print(f'Current index (Page 7): {p.current_idx + 1}')
print(f'Visible elements: {p.get_visible_items()}')

print('\n Go to page (3)')
p.go_to_page(3)
print(f'Current index (Page 3): {p.current_idx + 1}')
print(f'Visible elements: {p.get_visible_items()}')

p.first_page()
print('\nMethod Chaining (Next x 3)')
p.next_page().next_page().next_page()
print(f'Current Index (Page 4): {p.current_idx + 1}')
print(f'Visible Items: {p.get_visible_items()}')

print('\n Error Handling (go_to_page) ')
try:
    p.go_to_page(10)
except ValueError as e:
    print(f'Caught expected error for page 10: {e}')

try:
    p.go_to_page(0)
except ValueError as e:
    print(f'Caught expected error for page 0: {e}')