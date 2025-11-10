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

print("Wins:", won)
print("Losses:", lost)