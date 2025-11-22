from game import Game

def get_user_menu_choice():
    print("\n--- Menu ---")
    print("1. Play a new game")
    print("2. Show scores")
    print("3. Quit")
    
    valid_choices = ['1', '2', '3']
    while True:
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice in valid_choices:
            return choice
        print("Invalid input. Please enter 1, 2, or 3.")

def print_results(results):
    wins = results.get("win", 0)
    losses = results.get("loss", 0)
    draws = results.get("draw", 0)

    print("\n--- Game Summary ---")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Draws: {draws}")
    
    total_games = wins + losses + draws
    print(f"Total games played: {total_games}")
    
    print("Thank you for playing!")

def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        user_choice = get_user_menu_choice()
        
        if user_choice == '1':
            game = Game()
            game_result = game.play()
            results[game_result] = results.get(game_result, 0) + 1
            
        elif user_choice == '2':
            print_results(results)
            
        elif user_choice == '3':
            print_results(results)
            break

if __name__ == "__main__":
    main()