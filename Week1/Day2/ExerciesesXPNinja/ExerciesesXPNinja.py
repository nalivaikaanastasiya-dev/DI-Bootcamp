# Exercise 1: Formula

# Write a program that calculates and prints a value according to this given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# Ask the user for a comma-separated string of numbers, use each number from the user as D in the formula and return all the results
# For example, if the user inputs: 100,150,180
# The output should be:
# 18,22,24

import math

C = 50
H = 30

# Get user input, split by comma, and remove extra spaces
D_values = input("Enter comma-separated numbers: ").split(',')

results = []

for D in D_values:
    D = int(D.strip())  # convert input to integer after stripping whitespace
    Q = math.sqrt((2 * C * D) / H)
    results.append(str(round(Q)))

print(','.join(results))

# Exercise 2 : List of integers

# Given a list of 10 integers to analyze. For example:
#     [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
#     [44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
#     [3, 21, 76, 53, 9, -82, -3, 49, 1, 76] 
#     [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]

# 1. Store the list of numbers in a variable.
# 2. Print the following information:
# a. The list of numbers – printed in a single line
# b. The list of numbers – sorted in descending order (largest to smallest)
# c. The sum of all the numbers
# 3. A list containing the first and the last numbers.
# 4. A list of all the numbers greater than 50.
# 5. A list of all the numbers smaller than 10.
# 6. A list of all the numbers squared – eg. for [1, 2, 3] you would print “1 4 9”.
# 7. The numbers without any duplicates – also print how many numbers are in the new list.
# 8. The average of all the numbers.
# 9. The largest number.
# 10.The smallest number.
# 11. Bonus: Find the sum, average, largest and smallest number without using built in functions.
# 12. Bonus: Instead of using pre-defined lists of numbers, ask the user for 10 numbers between -100 and 100. Ask the user for an integer between -100 and 100 – repeat this question 10 times. Each number should be added into a variable that you created earlier.
# 13. Bonus: Instead of asking the user for 10 integers, generate 10 random integers yourself. Make sure that these random integers are between -100 and 100.
# 14. Bonus: Instead of always generating 10 integers, let the amount of integers also be random! Generate a random positive integer no smaller than 50.
# 15. Bonus: Will the code work when the number of random numbers is not equal to 10?

import random
from collections import Counter

numbers = []
for i in range(10):
    while True:
        try:
            num = int(input(f"Enter number {i+1} (between -100 and 100): "))
            if -100 <= num <= 100:
                numbers.append(num)
                break
            else:
                print("Number out of range, try again.")
        except ValueError:
            print("Invalid input, please enter an integer.")

print("Original list:", numbers)

sorted_desc = sorted(numbers, reverse=True)
print("Sorted descending:", sorted_desc)

total = sum(numbers)
print("Sum of numbers:", total)

first_last = [numbers[0], numbers[-1]]
print("First and last:", first_last)

greater_than_50 = [x for x in numbers if x > 50]
print("Numbers > 50:", greater_than_50)

less_than_10 = [x for x in numbers if x < 10]
print("Numbers < 10:", less_than_10)

squares = [str(x**2) for x in numbers]
print("Numbers squared:", ' '.join(squares))

unique_numbers = list(set(numbers))
print("Unique numbers:", unique_numbers)
print("Count of unique numbers:", len(unique_numbers))

average = total / len(numbers)
print("Average:", average)

max_num = max(numbers)
print("Max:", max_num)

min_num = min(numbers)
print("Min:", min_num)

sum_b = 0
max_b = None
min_b = None
for n in numbers:
    sum_b += n
    if max_b is None or n > max_b:
        max_b = n
    if min_b is None or n < min_b:
        min_b = n
avg_b = sum_b / len(numbers)
print("Bonus sum:", sum_b)
print("Bonus max:", max_b)
print("Bonus min:", min_b)
print("Bonus average:", avg_b)

counter = Counter(numbers)
duplicates = sum(1 for c in counter.values() if c > 1)
print("Number of duplicated numbers:", duplicates)

# Exercise 3: Working on a paragraph
# Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
# Paste it to your code, and store it in a variable.
# Let’s analyze the paragraph. Print out a nicely formatted message saying:
# How many characters it contains (this one is easy…).
# How many sentences it contains.
# How many words it contains.
# How many unique words it contains.
# Bonus: How many non-whitespace characters it contains.
# Bonus: The average amount of words per sentence in the paragraph.
# Bonus: the amount of non-unique words in the paragraph.

import re

paragraph = """Python is a versatile programming language that is widely used in various fields such as web development, data analysis, artificial intelligence, and more. Its simple syntax makes it popular among beginners and experienced programmers alike."""

num_chars = len(paragraph)

sentences = re.split(r'[.!?]', paragraph)
sentences = [s.strip() for s in sentences if s.strip()]
num_sentences = len(sentences)

words = paragraph.split()
num_words = len(words)

unique_words = set(words)
num_unique_words = len(unique_words)

non_whitespace_chars = len(re.findall(r'\S', paragraph))

average_words_per_sentence = num_words / num_sentences if num_sentences != 0 else 0

from collections import Counter
word_counts = Counter(words)
repeated_words_count = sum(1 for count in word_counts.values() if count > 1)

print(f"Number of characters: {num_chars}")
print(f"Number of sentences: {num_sentences}")
print(f"Number of words: {num_words}")
print(f"Number of unique words: {num_unique_words}")
print(f"Number of non-whitespace characters: {len(re.findall(r'\\S', paragraph))}")
print(f"Average words per sentence: {average_words_per_sentence:.2f}")
print(f"Number of repeated words: {repeated_words_count}")

# Exercise 4 : Frequency Of The Words

# Write a program that prints the frequency of the words from the input.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
#     2:2
#     3.:1
#     3?:1
#     New:1
#     Python:5
#     Read:1
#     and:1
#     between:1
#     choosing:1
#     or:2
#     to:1

text = input("Enter a sentence: ")
words = text.split()
result_words = []

for word in words:
    if word in result_words:
        continue
    count = 0
    for w in words:
        if w == word:
            count += 1
    print(f"{word}:{count}")
    result_words.append(word)