import random
import sys

class Game:
    """
    Класс, управляющий логикой игры "Камень-Ножницы-Бумага".
    """
    
    # Константы для игры
    ITEMS = ["камень", "ножницы", "бумага"]
    
    # Правила игры: ключ побеждает значение
    # Например: 'ножницы' побеждают 'бумага'
    RULES = {
        "камень": "ножницы",
        "ножницы": "бумага",
        "бумага": "камень"
    }

    def get_user_item(self):
        """
        Запрашивает у пользователя выбор и выполняет валидацию ввода.
        Возвращает выбранный предмет в нижнем регистре.
        """
        while True:
            prompt = f"Выберите предмет ({'/'.join(self.ITEMS)}): "
            user_choice = input(prompt).strip().lower()
            
            if user_choice in self.ITEMS:
                return user_choice
            else:
                print(f"❌ Неверный ввод. Пожалуйста, выберите из: {', '.join(self.ITEMS)}.")

    def get_computer_item(self):
        """
        Случайным образом выбирает предмет для компьютера.
        """
        computer_choice = random.choice(self.ITEMS)
        return computer_choice

    def get_game_result(self, user_item, computer_item):
        """
        Определяет результат игры: "win", "draw" или "loss".
        
        Args:
            user_item (str): Выбор пользователя.
            computer_item (str): Выбор компьютера.
            
        Returns:
            str: "win", "draw" или "loss".
        """
        if user_item == computer_item:
            return "draw"
        
        # Проверяем, побеждает ли предмет пользователя предмет компьютера согласно RULES
        # Если RULES[user_item] == computer_item, значит user_item побеждает computer_item
        if self.RULES.get(user_item) == computer_item:
            return "win"
        else:
            return "loss"

    def play(self):
        """
        Проводит один раунд игры.
        
        Returns:
            str: Результат игры ("win", "draw" или "loss").
        """
        # 1. Получаем выбор
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        
        # 2. Определяем результат
        result = self.get_game_result(user_item, computer_item)
        
        # 3. Печатаем результат
        print("\n" + "~" * 40)
        print(f"Ваш выбор: {user_item.capitalize()}")
        print(f"Выбор компьютера: {computer_item.capitalize()}")
        
        if result == "win":
            print("🎉 Вы ВЫИГРАЛИ!")
        elif result == "loss":
            print("😢 Вы ПРОИГРАЛИ.")
        else:
            print("🤝 НИЧЬЯ!")
            
        print("~" * 40)
        
        return result