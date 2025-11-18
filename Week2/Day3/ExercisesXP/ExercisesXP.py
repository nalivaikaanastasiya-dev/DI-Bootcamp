# Exercise 1: Currencies

class Currency:

    def __init__(self, currency, amount):
        self.currency = currency.lower()
        self.amount = amount

    def __str__(self):
        currency_label = self.currency
        if self.amount != 1:
            currency_label += 's'
            
        return f'{self.amount} {currency_label}'

    def __repr__(self):
        return self.__str__()
    
    def __int__(self):
        return int(self.amount)


    def __add__(self, other):
        
        if isinstance(other, Currency):
        
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            
            new_amount = self.amount + other.amount
            return Currency(self.currency, new_amount)
            
        elif isinstance(other, (int, float)):
            return self.amount + other
            
        else:
            return NotImplemented

    def __iadd__(self, other):
        
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            
            self.amount += other.amount
            
        elif isinstance(other, (int, float)):
            self.amount += other
            
        else:
            return NotImplemented
            
        return self

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(f"print(c1): {c1}")           
print(f"print(int(c1)): {int(c1)}") 
print(f"print(repr(c1)): {repr(c1)}") 
print(f"print(c1 + 5): {c1 + 5}")   
print(f"print(c1 + c2): {c1 + c2}") 
print(f"print(c1) до +=: {c1}")     

print("In-place Operations")
c1 += 5                             
print(f"c1 += 5: {c1}")            

c1 += c2                          
print(f"c1 += c2: {c1}")         

print("Error testing")
try:
    print(c1 + c3)
except TypeError as e:
    print(f"print(c1 + c3): TypeError: {e}")

# Exercise 3: String module

import random
import string

all_letters = string.ascii_letters

random_string = ''

for _ in range(5):
    random_char = random.choice(all_letters)
    
    random_string += random_char

print(f"String of all lerrrs: {all_letters}")
print(f"Random string of length 5: {random_string}")

# Exercise 4: Current Date

import datetime

def display_current_date():
    current_date_time = datetime.datetime.now()
    current_date = current_date_time.date()

    print (f'Current date: {current_date}')

display_current_date()

# Exercise 5: Amount of time left until January 1st


import datetime

def time_until_new_year():
    now = datetime.datetime.now()
    next_year = now.year + 1
    jan_1st = datetime.datetime(next_year, 1, 1, 0, 0, 0)
    time_left = jan_1st - now
    total_seconds = time_left.total_seconds()
    days = time_left.days
    hours = int(total_seconds // (60 * 60) % 24)
    minutes = int(total_seconds // 60 % 60)
    seconds = int(total_seconds % 60)

    print("Time to 1 of January:")
    print(f"Current date and time {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"New year gonna be:   {jan_1st.strftime('%Y-%m-%d %H:%M:%S')}")
    print("-------------------------")
    print(f"Time left: {days} days, {hours} hours, {minutes} minut and {seconds} seconds.")

time_until_new_year()

# Exercise 6: Birthday and minutes

import datetime

def calculate_minutes_lived_user_input():
    DATE_FORMAT = "%d-%m-%Y"
    birthdate_str = input (f'Please write your birthday date in a format {DATE_FORMAT}: ')
    now = datetime.datetime.now()
    try:
        birthdate = datetime.datetime.strptime(birthdate_str, DATE_FORMAT)
    except ValueError:
        print(f"\nInput error: Invalid date format. Please ensure you used the format {DATE_FORMAT} (e.g., 25-12-1990).")
        return
    if birthdate > now:
        print("\nError: Date of birth cannot be in the future. Please try again.")
        return
    time_lived = now - birthdate
    total_seconds = time_lived.total_seconds()
    minutes_lived = total_seconds / 60

    print(f"ТCurrent date:  {now.strftime(DATE_FORMAT)}")
    print(f"You have lived: {int(minutes_lived):,} minuts!")

calculate_minutes_lived_user_input()

# Exercise 7: Faker Module

from faker import Faker

fake = Faker('en_US')

users []

def generate_fake_users (num_users_to_generate):

    print(f"Generating {num_users_to_generate} fake users...")

    for _ in range (num_users_to_generate):
        user_data = {
            "name": fake.name(),            
            "address": fake.address(),      
            "language_code": fake.language_code() 
        }
        user.uppend(user_data)

number_of_users = 5
generate_fake_users (number_of_users)

print("\nGenerated Users Dictionaries")

for i, user in enumerate(users):
    print(f"User {i+1}:")
    print(f"Name: {user['name']}")
    print(f"Address: {user['address']}")
    print(f"Language Code: {user['language_code']}")
    print("-" * 20)

print("\nFull List:")
print(users)
