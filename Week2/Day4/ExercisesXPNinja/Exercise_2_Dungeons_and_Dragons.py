# Exercise 2 : Dungeons & Dragons

import random
import json
import os
from typing import List, Dict, Any

class Character:
    """
    Класс, представляющий персонажа Dungeons & Dragons.
    Отвечает за генерацию шести атрибутов с использованием правила 4d6 (отбросить наименьшее).
    """

    def __init__(self, name: str, age: int):
        """
        Инициализирует персонажа, устанавливает имя и возраст, и генерирует атрибуты.
        """
        self.name = name
        self.age = age
        self.attributes = self.generate_stats()

    def roll_4d6(self) -> int:
        """
        Имитирует бросок четырех шестигранных кубиков (4d6), 
        отбрасывает наименьший результат и возвращает сумму трех наибольших.
        """
        # Бросаем 4 кубика (d6)
        rolls = [random.randint(1, 6) for _ in range(4)]
        
        # Сортируем броски, чтобы наименьший оказался первым
        rolls.sort()
        
        # Суммируем три наибольших результата (элементы с индекса 1 до конца)
        score = sum(rolls[1:])
        
        return score

    def generate_stats(self) -> Dict[str, int]:
        """
        Генерирует оценки для шести основных атрибутов персонажа.
        """
        attributes = {
            "Strength": self.roll_4d6(),
            "Dexterity": self.roll_4d6(),
            "Constitution": self.roll_4d6(),
            "Intelligence": self.roll_4d6(),
            "Wisdom": self.roll_4d6(),
            "Charisma": self.roll_4d6(),
        }
        return attributes

    def to_dict(self) -> Dict[str, Any]:
        """
        Возвращает данные персонажа в виде словаря для экспорта в JSON.
        """
        return {
            "name": self.name,
            "age": self.age,
            "attributes": self.attributes
        }

    def __str__(self) -> str:
        """
        Возвращает данные персонажа в виде отформатированной строки для TXT.
        """
        stats_str = "\n".join([f"  {attr:<14}: {score}" 
                               for attr, score in self.attributes.items()])
                               
        return f"--- Персонаж: {self.name} (Возраст: {self.age}) ---\n" \
               f"Атрибуты:\n{stats_str}\n"

class Game:
    """
    Класс, управляющий процессом создания персонажей и экспортом данных.
    """

    def __init__(self):
        self.players: List[Character] = []
        self.file_basename = "dnd_characters"

    def start_game(self):
        """
        Запрашивает количество игроков и собирает данные о персонажах.
        """
        print("--- Dungeons & Dragons: Генератор Персонажей ---")
        
        while True:
            try:
                num_players = int(input("Введите количество игроков: "))
                if num_players <= 0:
                    print("❌ Количество игроков должно быть положительным числом.")
                    continue
                break
            except ValueError:
                print("❌ Неверный ввод. Пожалуйста, введите целое число.")

        for i in range(num_players):
            print(f"\n[Создание Персонажа {i+1} из {num_players}]")
            
            name = input("Введите имя персонажа: ").strip()
            if not name:
                name = f"Герой_{i+1}"
                
            while True:
                try:
                    age = int(input("Введите возраст персонажа: "))
                    if age <= 0:
                        print("❌ Возраст должен быть положительным числом.")
                        continue
                    break
                except ValueError:
                    print("❌ Неверный ввод. Пожалуйста, введите возраст в виде числа.")

            # Создаем экземпляр Character, который автоматически генерирует атрибуты
            new_character = Character(name, age)
            self.players.append(new_character)
            print(f"\n✅ Персонаж '{name}' успешно создан!")
            print(str(new_character))

    def export_data(self):
        """
        Экспортирует данные персонажей в форматы TXT и JSON.
        """
        if not self.players:
            print("\nНет созданных персонажей для экспорта.")
            return

        # 1. Экспорт в JSON
        json_filepath = f"{self.file_basename}.json"
        json_data = [player.to_dict() for player in self.players]
        
        try:
            with open(json_filepath, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, indent=4, ensure_ascii=False)
            print(f"\n✅ Данные экспортированы в JSON: {json_filepath}")
        except IOError as e:
            print(f"❌ Ошибка записи JSON-файла: {e}")

        # 2. Экспорт в TXT
        txt_filepath = f"{self.file_basename}.txt"
        
        try:
            with open(txt_filepath, 'w', encoding='utf-8') as f:
                f.write("D&D Атрибуты Персонажей\n")
                f.write("=" * 40 + "\n")
                
                for i, player in enumerate(self.players):
                    f.write(str(player) + "\n")
                    if i < len(self.players) - 1:
                        f.write("-" * 40 + "\n")

            print(f"✅ Данные экспортированы в TXT: {txt_filepath}")
        except IOError as e:
            print(f"❌ Ошибка записи TXT-файла: {e}")

# --- Точка входа в программу ---
if __name__ == "__main__":
    dnd_game = Game()
    dnd_game.start_game()
    dnd_game.export_data()