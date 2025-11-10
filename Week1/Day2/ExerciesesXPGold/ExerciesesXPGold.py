# Exercise 1: Concatenate lists
# Write code that concatenates two lists together without using the + sign.

list_1=['g', 'l', 'l']
list_2=['j', 'd', 'd']
list_1.extend(list_2)
print(list_1)

# Exercise 2: Range of numbers
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.

for num in range(1500, 2501):
    if num%5==0 and num%7 == 0:
        print(num)

# Exercise 3: Check the index
# Using this variable
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.
# Example: if input is 'Cortana' we should be printing the index 1

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
your_name = input('Enter your name: ')

if your_name in names:
    index = names.index(your_name)
    print('Index:', index)
else:
    print('Name not found in the list.')

# Exercise 4: Greatest Number

# Ask the user for 3 numbers and print the greatest number.

# Test Data
# Input the 1st number: 25
# Input the 2nd number: 78
# Input the 3rd number: 87

# The greatest number is: 87

input_1=input('Print the first number: ')
input_2=input('Print the second number: ')
input_3=input('Print the third number: ')
list_input=[input_1, input_2, input_3]
print('The greatest number is: ', max(list_input))

# Exercise 5: The Alphabet

# Create a string of all the letters in the alphabet
# Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.

import string

alphabet = string.ascii_lowercase

vowels = "aeiou"

for letter in alphabet:
    if letter in vowels:
        print(f"The letter '{letter}' is a vowel.")
    else:
        print(f"The letter '{letter}' is a consonant.")

# Exercise 6: Words and letters

# Ask a user for 7 words, store them in a list named words.
# Ask the user for a single character, store it in a variable called letter.
# Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
# If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.

words_input=input('Print 7 words: ')
words=words_input.split()
letter=input('Print a letter: ')
for word in words:
    if letter in word:
        print(f'The letter', {letter}, 'found at index', {word.index(letter)}, 'in the word ',{word},'.')
    else:
        print(f'Sorry, the letter ', {letter}, 'is not in the word ', {word},'.')

# Exercise 7: Min, Max, Sum

# Create a list of numbers from one to one million and then use min() and max() to make sure your list actually starts at one and ends at one million. Use the sum() function to see how quickly Python can add a million numbers.

numbers = list(range(1, 1000001))
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))

# Exercise 8 : List and Tuple

# Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.
# Suppose the following input is supplied to the program: 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

numbers_input = input("Enter a sequence of comma-separated numbers: ")
numbers_list = numbers_input.split(',')
numbers_tuple = tuple(numbers_list)
print(numbers_list)
print(numbers_tuple)

# Exercise 9 : Random number

# Ask the user to input a number from 1 to 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# If the user guesses the correct number print a message that says Winner.
# If the user guesses the wrong number print a message that says better luck next time.
# Bonus: use a loop that allows the user to keep guessing until they want to quit.
# Bonus 2: on exiting the loop tally up and display total games won and lost.

import random

won = 0
lost = 0

while True:
    guess = input("Guess a number from 1 to 9, or type 'quit' to stop: ")
    if guess == 'quit':
        break
    if not guess.isdigit() or not (1 <= int(guess) <= 9):
        print("Enter a number from 1 to 9.")
        continue

    number = random.randint(1, 9)
    if int(guess) == number:
        print("Winner!")
        won += 1
    else:
        print("Better luck next time!")
        lost += 1

# После выхода из цикла выводим счет
print("Wins:", won)
print("Losses:", lost)