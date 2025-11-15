# Exercise 1

# Draw the following pattern using for loops:
#   *
#  ***
# *****

def draw_pyramid_pattern(rows):
    
    for i in range(1, rows + 1):

        spaces = rows - i
        print(" " * spaces, end="")

        stars = 2 * i - 1
        print("*" * stars)

draw_pyramid_pattern(3)

# Draw the following pattern using for loops:
#     *
#    **
#   ***
#  ****
# *****

def draw_right_triangle(rows):
   
       for i in range(1, rows + 1):
        
        spaces = rows - i
        print(" " * spaces, end="")

        stars = i
        print("*" * stars)

draw_right_triangle(5)

# Draw the following pattern using for loops:
# *
# **
# ***
# ****
# *****
# *****
#  ****
#   ***
#    **
#     *

def draw_growing_triangle(rows):
    
    for i in range(1, rows + 1):
        stars = i
        print("*" * stars)

def draw_inverted_triangle(rows):
    for i in range(rows, 0, -1):
        
        spaces = rows - i
        print(" " * spaces, end="")

        stars = i
        print("*" * stars)

n = 5

draw_growing_triangle(n)

draw_inverted_triangle(n)

# Exercise 2

# Analyse this code before executing it. Write some commnts next to each line. Write the value of each variable and their changes, and add the final output. Try to understand the purpose of this program.
# my_list = [2, 24, 12, 354, 233]
# for i in range(len(my_list) - 1):
#     minimum = i
#     for j in range( i + 1, len(my_list)):
#         if(my_list[j] < my_list[minimum]):
#             minimum = j
#             if(minimum != i):
#                 my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
# print(my_list)

my_list = [2, 24, 12, 354, 233] # The list that needs to be sorted (порядок по возрастанию)

# Outer loop: iterates over each position 'i' in the list where 
# the next smallest element will be placed. It runs up to the second-to-last element.
for i in range(len(my_list) - 1):
    minimum = i  # Initially assume the element at the current position 'i' is the minimum
    
    # Inner loop: searches for the actual smallest element in the 
    # remaining unsorted part of the list (starting from i + 1).
    for j in range(i + 1, len(my_list)):
        # Compares the element at 'j' with the current minimum element
        if(my_list[j] < my_list[minimum]):
            minimum = j  # If a smaller element is found, update the index of the minimum
            
            # Checks if a new minimum index was found
            if(minimum != i):
                # Swaps the element at the current position 'i' with the 
                # smallest element found so far (at index 'minimum').
                # This moves the smallest element into its correct sorted position.
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
                
# Print the final list after the sorting process is complete
print(my_list)