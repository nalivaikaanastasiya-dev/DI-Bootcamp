import json
import os
import re # Импорт модуля для работы с регулярными выражениями

class MenuManager:
    """
    Класс для управления данными меню.
    Отвечает за загрузку, сохранение, добавление и удаление элементов меню, 
    используя JSON-файл в качестве постоянного хранилища.
    """
    FILE_PATH = "restaurant_menu.json"

    def __init__(self):
        """
        Конструктор: Загружает меню из файла при создании экземпляра.
        """
        # Инициализируем оба списка: для основного меню и для Valentine's Day
        self.menu = {"items": [], "valentine_items": []} 
        self._load_menu()

    def _load_menu(self):
        """
        Приватный метод для загрузки меню из файла JSON.
        """
        if not os.path.exists(self.FILE_PATH):
            self.save_to_file() 
            return

        try:
            with open(self.FILE_PATH, 'r', encoding='utf-8') as file:
                self.menu = json.load(file)
            # Убедимся, что ключ valentine_items существует после загрузки
            if "valentine_items" not in self.menu:
                self.menu["valentine_items"] = []
        except json.JSONDecodeError:
            print(f"Внимание: Файл {self.FILE_PATH} пуст или поврежден. Использование пустого меню.")
            self.menu = {"items": [], "valentine_items": []}
        except Exception as e:
            print(f"Ошибка при загрузке меню: {e}")

    def get_menu(self):
        """
        Возвращает текущее меню (полный словарь).
        """
        return self.menu

    def add_item(self, name: str, price: float):
        """
        Добавляет новый элемент в основное меню (не сохраняя в файл).
        """
        new_item = {
            "name": name.strip().capitalize(),
            "price": float(price)
        }
        self.menu["items"].append(new_item)
        
    def remove_item(self, name: str) -> bool:
        """
        Удаляет элемент из основного меню по имени (не сохраняя в файл).
        """
        name_to_remove = name.strip().capitalize()
        items_list = self.menu["items"]
        
        try:
            index_to_remove = next(
                i for i, item in enumerate(items_list) 
                if item["name"] == name_to_remove
            )
            del items_list[index_to_remove]
            return True
        except StopIteration:
            return False
            
    # --- НОВЫЕ МЕТОДЫ ДЛЯ VALENTINE'S DAY ---
    
    def validate_valentine_item(self, name: str, price: str) -> bool:
        """
        Проверяет имя и цену на соответствие правилам Valentine's Day с использованием 
        регулярных выражений и логики.
        """
        
        # 1. Валидация ЦЕНЫ (XX,14)
        price_pattern = r'^\d{2},14$' 
        if not re.fullmatch(price_pattern, price):
            print(f"❌ Цена не соответствует паттерну XX,14 (две цифры, затем запятая, затем 14): {price}")
            return False

        # 2. Валидация ИМЕНИ
        name = name.strip()
        
        # Проверка на отсутствие цифр
        if bool(re.search(r'\d', name)):
            print("❌ Имя не должно содержать цифры.")
            return False

        # Проверка на наличие минимум двух 'e'
        if name.lower().count('e') < 2:
            print("❌ Имя должно содержать минимум две буквы 'e'.")
            return False

        # Проверка структуры заглавных/строчных букв
        words = name.split()
        
        # Проверка, что первое слово начинается с 'V'
        if not words or not words[0].startswith('V'):
            print("❌ Первое слово должно начинаться с заглавной 'V'.")
            return False

        # Проверка форматирования слов
        connection_words = ["of", "and", "the", "with", "for", "to"]
        
        for i, word in enumerate(words):
            if not word: continue
            
            # Проверка соединительных слов (должны быть строчными)
            if word.lower() in connection_words:
                if word != word.lower():
                    print(f"❌ Соединительное слово '{word}' должно быть полностью строчным.")
                    return False
            
            # Проверка обычных слов (должны начинаться с заглавной)
            else:
                if word != word.capitalize():
                    print(f"❌ Слово '{word}' должно начинаться с заглавной буквы (кроме соединительных слов).")
                    return False
        
        return True # Валидация пройдена
        
    def add_valentine_item(self, name: str, price: str) -> bool:
        """
        Добавляет элемент в список Valentine's Day, если он прошел валидацию.
        """
        if not self.validate_valentine_item(name, price):
            return False
            
        # Замена запятой на точку для правильного сохранения float
        price_float = float(price.replace(',', '.'))
        
        new_item = {
            "name": name.strip(),
            "price": price_float
        }
        self.menu["valentine_items"].append(new_item)
        return True

    def save_to_file(self):
        """
        Сохраняет текущее меню в файл JSON.
        """
        try:
            with open(self.FILE_PATH, 'w', encoding='utf-8') as file:
                json.dump(self.menu, file, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Критическая ошибка при сохранении файла: {e}")
            
    def display_heart_of_stars(self):
        """
        Отображает сердце, сделанное из звездочек (*).
        """
        print("\n" + "❤" * 50)
        heart = """
            *** ***
           ***** *****
          ***************
          ***************
          ***************
           *************
            ***********
             *********
              *******
               *****
                ***
                 *
        """
        print(heart)
        print("❤" * 50)