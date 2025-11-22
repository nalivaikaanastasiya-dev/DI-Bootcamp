import random

class Game:
    def __init__(self):
        self.items = ["rock", "paper", "scissors"]
        self.rules = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }

    def get_user_item(self):
        while True:
            user_choice = input("Select an item (rock/paper/scissors): ").lower()
            if user_choice in self.items:
                return user_choice
            print("Invalid choice. Please select rock, paper, or scissors.")

    def get_computer_item(self):
        return random.choice(self.items)

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif self.rules[user_item] == computer_item:
            return "win"
        else:
            return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(f"You selected: {user_item}")
        print(f"The computer selected: {computer_item}")

        if result == "win":
            print("You win!")
        elif result == "loss":
            print("You lose!")
        else:
            print("It's a draw!")
            
        return result