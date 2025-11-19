# Exercise 1: Random Sentence Generator

import random
import sys
import os

try:
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    SCRIPT_DIR = os.getcwd()

WORD_FILE_PATH = os.path.join(SCRIPT_DIR, "words.txt")

def get_words_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            return words

    except FileNotFoundError:
        print(f"\nError: File '{file_path}' not found.")
        print("Ensure that 'words.txt' is located next to the script file.")
        sys.exit(1)

    except Exception as e:
        print(f"\n[GENERAL ERROR] An unexpected error occurred while reading the file: {e}")
        sys.exit(1)

def get_random_sentence(length):
    word_list = get_words_from_file(WORD_FILE_PATH)
    
    if not word_list:
        return "Cannot generate sentence: word list is empty."

    random_words = []
    for _ in range(length):
        word = random.choice(word_list)
        random_words.append(word)

    sentence = ' '.join(random_words)
    sentence = sentence.lower()
    
    if sentence:
        sentence = sentence.capitalize() + '.'
        
    return sentence

def main():
    print("The program creates a random sentence from words in the 'words.txt' file.")
    print("The sentence length must be between 2 and 20 words.")
    
    user_input = input("Enter the desired sentence length (2 to 20): ")

    length = None
    
    # Input Validation
    try: 
        length = int(user_input)
    except ValueError:
        print('\n[INPUT ERROR] Length must be an integer.')
        sys.exit(1)

    MIN_LEN = 2
    MAX_LEN = 20

    if not (MIN_LEN <= length <= MAX_LEN):
        print(f'\n[INPUT ERROR] Length must be in the range from {MIN_LEN} to {MAX_LEN}.')
        sys.exit(1)

    # Sentence Generation
    try: 
        random_sentence = get_random_sentence(length)

        print(f'Sentence of {length} words generated:')
        print(random_sentence)

    except Exception as e:
        print(f'\n[GENERAL ERROR] An unexpected error occurred: {e}')
        sys.exit(1)

if __name__ == '__main__':
    main()

# Exercise 2: Working with JSON

import json
import os
import sys

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

try:
    data = json.loads(sampleJson)
    print("--- Step 1: JSON loaded successfully ---")
except json.JSONDecodeError as e:
    print(f"Error loading JSON: {e}")
    sys.exit(1)

try:
    salary_value = data["company"]["employee"]["payable"]["salary"]
    print(f"Step 2: Accessed Salary Value: {salary_value}")
except KeyError as e:
    print(f"Error accessing nested key: Key {e} not found.")
    sys.exit(1)


employee_dict = data["company"]["employee"]
new_birth_date = "2025-11-19"
employee_dict["birth_date"] = new_birth_date
print(f"Step 3: Added 'birth_date': {new_birth_date} to 'employee' dictionary.")

output_file_path = "modified_data.json"
try:
    with open(output_file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Step 4: Modified JSON saved successfully to '{output_file_path}'")

except IOError as e:
    print(f"Error saving file: {e}")
    sys.exit(1)

print("\n--- Modified Dictionary Structure (Python view) ---")
print(data)