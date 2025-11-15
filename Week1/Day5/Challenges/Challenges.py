# Exercise 1
# Instructions
# Write a script that inserts an item at a defined index in a list.

original_list = ['History', 'Math', 'Physics', 'CompSci']
new_item = 'Art'
index_to_insert = 2
print(f'Original list: {', '.join(original_list)}')
print(f'Item to insert: {new_item}, at index: {index_to_insert}')
original_list.insert(index_to_insert, new_item)
print(f'New list: {', '.join(original_list)}')

# Exercise 2
# Instructions
# Write a script that counts the number of spaces in a string.

string_1 = 'I love you, baby And if it"s quite all right I need you, baby To warm these lonely nights I love you, baby Trust in me when I say\n'
print(
f'String:  {string_1}'
f'Number of spaces: {string_1.count(' ')}'
)

# Exercise 3
# Instructions
# Write a script that calculates the number of upper case letters and lower case letters in a string.

string_1='I love you, baby And if it"s quite all right'
upper_case=0
lower_case=0
for char in string_1:
    if char.isupper():
        upper_case=upper_case+1
    elif char.islower():
        lower_case=lower_case+1
print(
    f'Text: {string_1}\n'
    f'Letters in upper case: {upper_case}\n'
    f'Letters in lowercase: {lower_case}'

# Exercise 4
# Instructions
# Write a function to find the sum of an array without using the built in function:

# >>>my_sum([1,5,4,2])
# >>>12

def my_sum(input_array):
    total=0
    for number in input_array:
        total+=number
    return total

test_list = [1, 5, 4, 2]
result=my_sum(test_list)
print(
    f'list: {test_list}\n'
    f'Sum = {result}'
)

# Exercise 5
# Instructions
# Write a function to find the max number in a list

# >>>find_max([0,1,3,50])
# >>>50

def max_num(input_array):
    max_number=0
    for number in input_array:
        if number > max_number:
            max_number=number
    return max_number

test_list = [0, 1, 3, 50]
result=max_num(test_list)
print(
    f'list: {test_list}\n'
    f'Max number = {result}'
)

# Exercise 6
# Instructions
# Write a function that returns factorial of a number

# >>>factorial(4)
# >>>24

def factorial(input_num):
    total=1
    for num in range(1, input_num+1):
        total=total*num
    return total

test_number = 4
result=factorial(test_number)
print(
    f'Number: {test_number}\n'
    f'Factorial = {result}'
)

# Exercise 7
# Instructions
# Write a function that counts an element in a list (without using the count method):

# >>>list_count(['a','a','t','o'],'a')
# >>>2

def get_most_frequent_element(input_list):
    counts_dict={}
    for item in input_list:
        counts_dict[item]=counts_dict.get(item, 0)+1
    if not counts_dict:
        return (None, 0)

    most_frequent_item=max(counts_dict, key=counts_dict.get)
    max_count=counts_dict[most_frequent_item]
    return (most_frequent_item, max_count)

test_list=['a','a','t','o']
frequent_item, max_count=get_most_frequent_element(test_list)
print(f"list_count({test_list}, '{frequent_item}')")
print(f" {max_count}")

# Exercise 8
# Instructions
# Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:

# >>>norm([1,2,2])
# >>>3

import math

def calculate_l2_norm(input_list):
    
    sum_of_squares=0
    for number in input_list:
        sum_of_squares+=number**2

    return math.sqrt(sum_of_squares)

test_list=[1,2,2]
result = int(calculate_l2_norm(test_list))
print(
    f'nom {test_list}\n'
    f'{result}'
)

# Exercise 9
# Instructions
# Write a function to find if an array is monotonic (sorted either ascending of descending)

# >>>is_mono([7,6,5,5,2,0])
# >>>True

# >>>is_mono([2,3,3,3])
# >>>True

# >>>is_mono([1,2,0,4])
# >>>False

def is_mono(input_list):
    n=len(input_list)
    if n<= 1:
        return True
    is_increasing = True
    is_decreasing = True
    
    for i in range(n-1):
        if input_list[i]>input_list[i+1]:
            is_increasing = False
        if input_list[i]<input_list[i+1]:
            is_decreasing = False
        
    return is_increasing or is_decreasing

return_list1=[7,6,5,5,2,0]
result_1=is_mono(return_list1)
print(f'is mon ({return_list1})\n'
      f'{result_1}'
)

return_list2=[2,3,3,3]
result_2=is_mono(return_list2)
print(f'is mon ({return_list2})\n'
      f'{result_2}'
)

return_list3=[1,2,0,4]
result_3=is_mono(return_list3)
print(f'is mon ({return_list3})\n'
      f'{result_3}'
)

# Exercise 10
# Instructions
# Write a function that prints the longest word in a list.

def get_the_longest_item(input_list):
    if not input_list:
        return None
        
    longest_item = max(input_list, key=len)
    
    return longest_item

test_list=['Alice','Arturito','Tanya','OJ']
longest_item=get_the_longest_item(test_list)
print(f"list: ({test_list}, '{longest_item}')")

# Exercise 11
# Instructions
# Given a list of integers and strings, put all the integers in one list, and all the strings in another one.

def split_list(input_list):

    int_list=[]
    letter_list=[]

    for char in input_list:
        if type(char) == int:
            int_list.append(char)
        elif type(char) == str:
            letter_list.append(char)

    return int_list, letter_list

input_list = [2, 3, 'l', 'u', 4, 'd', 9]
int_list, letter_list = split_list(input_list)
print(
    f'Original list: {input_list}\n'
    f'Integer list: {int_list}\n'
    f'Letter list: {letter_list}'
)

# Exercise 12
# Instructions
# Write a function to check if a string is a palindrome:

# >>>is_palindrome('radar')
# >>>True

# >>>is_palindrome('John)
# >>>False

def is_polindrom(text):
    normalized_text = ''.join(filter(str.isalnum, text)).lower()
    return normalized_text == normalized_text[::-1]

text_test = ['madam',
            'dog',
            'level',
            'hello'
            ]

print(f'Original text: {text_test}')
for text in text_test:
     result = is_polindrom(text)
     print(
     f'Text: {text}\n'
     f' Is Palidrom: {result}'
     )
# Exercise 13
# Instructions
# Write a function that returns the amount of words in a sentence with length > k:

# >>>sentence = 'Do or do not there is no try'
# >>>k=2
# >>>sum_over_k(sentence,k)
# >>>3

def sum_over_k(sentense, key):

    words = sentense.split()
    words_count = 0

    for word in words:

        if len(word)>key:
            words_count += 1
    return words_count

sentence='Do or do not there is no try'
key = 2
words_count = sum_over_k(sentence, key)

print(
    f'Original sentence: {sentence}\n'
    f'Key: {key}\n'
    f'Sum over key: {words_count}'
)

# Exercise 14
# Instructions
# Write a function that returns the average value in a dictionary (assume the values are numeric):

# >>>dict_avg({'a': 1,'b':2,'c':8,'d': 1})
# >>>3

import statistics
def dict_avg(input_dict):
    values_list = list(input_dict.values())
    if not values_list:
        return None
    return statistics.mean(values_list)

dict_my = {'a': 1,'b':2,'c':8,'d': 1}
average = dict_avg(dict_my)
print(
    f'{dict_my}\n'
    f'{average}'
)

# Exercise 15
# Instructions
# Write a function that returns common divisors of 2 numbers:

# >>>common_div(10,20)
# >>>[2,5,10]

import math
def common_div(a, b):

    min_num=min(a,b)
    common_divisors = []
    for i in range(1, min_num + 1):
        if a % i == 0 and b % i == 0:
            common_divisors.append(i)
    return common_divisors

my_tuple = (10, 20)
list_divs = common_div(my_tuple[0], my_tuple[1])

print(
    f'common_div{my_tuple}\n'
    f'{list_divs}'
)

# Exercise 16
# Instructions
# Write a function that test if a number is prime:

# >>>is_prime(11)
# >>>True

import math
def is_prime(a):

    for i in range(2, a):
        if a %  i == 0:
            return False   
    return True

a=11
result = is_prime(a)

print(
    f'is_prime ({a})\n'
    f'{result}'
)

# Exercise 17
# Instructions
# Write a function that prints elements of a list if the index and the value are even:

# >>>weird_print([1,2,2,3,4,5])
# >>>[2,4]

def filter_even_index_and_value(input_list):
   
    filtered_values = [
        value 
        for index, value in enumerate(input_list) 
        if index % 2 == 0 and value % 2 == 0
    ]
    return filtered_values

weird_print=[1,2,2,3,4,5]
value = filter_even_index_and_value(weird_print)

print(
    f'Original list: {weird_print}\n'
    f'Filtered values: {value}'
)

# Exercise 18
# Instructions
# Write a function that accepts an undefined number of keyworded arguments and return the count of different types:

# >>>type_count(a=1,b='string',c=1.0,d=True,e=False)
# >>>int: 1, str:1 , float:1, bool:2

def type_count(**kwargs):
    
    type_counts = {}

    for value in kwargs.values():
        type_name = str(type(value)).split("'")[1]
        type_counts[type_name] = type_counts.get(type_name, 0) + 1
        
    return type_counts

result_dict = type_count(a=1, b='string', c=1.0, d=True, e=False)
output_string = ', '.join([f"{k}: {v}" for k, v in result_dict.items()])

print(f"type_count(a=1,b='string',c=1.0,d=True,e=False)')")
print(f'{output_string}')

# Exercise 19
# Instructions
# Write a function that mimics the builtin .split() method for strings.

# By default the function uses whitespace but it should be able to take an argument for any character and split with that argument.

def my_split(text, delimiter=' '):
  
    if not text:
        return []

    result = []
    
    if delimiter == ' ':
        current_word = ""

        text = text.strip() 
        
        for char in text:
            
            if char.isspace():
                
                if current_word:
                    result.append(current_word)
                current_word = ""
            else:
                current_word += char
        
        if current_word:
            result.append(current_word)
            
   
    else:
        start_index = 0
        delimiter_length = len(delimiter)
        
        while True:
    
            delimiter_index = text.find(delimiter, start_index)
            
            if delimiter_index == -1:
                result.append(text[start_index:])
                break

            result.append(text[start_index:delimiter_index])
            
            start_index = delimiter_index + delimiter_length
            
    return result

sentence_1 = "  Один \t Два   Три  "
print(f"По умолчанию: {my_split(sentence_1)}") 

data_2 = ",a,,b,"
print(f"По запятой: {my_split(data_2, delimiter=',')}") 

data_3 = "Начало--Середина--Конец"
print(f"По '--': {my_split(data_3, delimiter='--')}")

# Exercise 20
# Instructions
# Convert a string into password format.

# Example:
# input : "mypassword"
# output: "***********"
def mask_password(text):
    if not isinstance(text, str):
        return ""
    length = len(text)
    masked_string='*'*length
    return masked_string

input='mypassword'
output=mask_password(input)

print(
    f'Input: {input}\n'
    f'Output: {output}'
)
