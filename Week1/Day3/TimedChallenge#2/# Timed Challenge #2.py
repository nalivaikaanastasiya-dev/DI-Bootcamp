# Timed Challenge #2
# Last Updated: October 7th, 2025

# Perfect number
# A perfect number is a positive integer that is equal to the sum of its divisors.
# However, the number itself is not included in the sum.

# Ask the user for a number and print whether or not it is a perfect number. If yes, print True else False.
# Hint: Google perfect numbers
# Example

# Input -- Enter the number:6
# Output -- True

# Input -- Enter the number:10
# Output --  False

# Here is the starter python code

# x = int(input('Enter the Number:')) 

# #write down your logic here 


x = int(input('Enter the Number:')) 

# Variable to store the sum of proper divisors
sum_of_divisors = 0

# A perfect number must be positive
if x > 0:
    # Find divisors from 1 up to x-1
    for i in range(1, x):
        # Check if i is a divisor of x
        if x % i == 0:
            sum_of_divisors += i
            
    # A perfect number is a positive integer that is equal to the sum of its 
    # positive divisors, excluding the number itself.
    if sum_of_divisors == x:
        print(True)
    else:
        print(False)
else:
    # Negative numbers are not considered perfect numbers
    print(False)