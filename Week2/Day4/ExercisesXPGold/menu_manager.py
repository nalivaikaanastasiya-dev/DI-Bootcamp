import json
import os

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
        self.menu = {"items": []}
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
        except json.JSONDecodeError:
            # Обработка пустого или некорректного JSON
            print(f"Внимание: Файл {self.FILE_PATH} пуст или поврежден. Использование пустого меню.")
            self.menu = {"items": []}
        except Exception as e:
            print(f"Ошибка при загрузке меню: {e}")

    def get_menu(self):
        """
        Возвращает текущее меню (полный словарь).
        """
        return self.menu

    def add_item(self, name: str, price: float):
        """
        Добавляет новый элемент в меню (не сохраняя в файл).
        """
        # Приводим имя к стандартному виду для удобства поиска
        new_item = {
            "name": name.strip().capitalize(),
            "price": float(price)
        }
        self.menu["items"].append(new_item)
        
    def remove_item(self, name: str) -> bool:
        """
        Удаляет элемент из меню по имени (не сохраняя в файл).
        
        Возвращает True, если элемент был найден и удален, False в противном случае.
        """
        name_to_remove = name.strip().capitalize()
        items_list = self.menu["items"]
        
        # Находим индекс элемента, который нужно удалить
        try:
            index_to_remove = next(
                i for i, item in enumerate(items_list) 
                if item["name"] == name_to_remove
            )
            # Удаляем элемент, используя оператор del
            del items_list[index_to_remove]
            return True
        except StopIteration:
            # Элемент не найден
            return False

    def save_to_file(self):
        """
        Сохраняет текущее меню в файл JSON.
        """
        try:
            with open(self.FILE_PATH, 'w', encoding='utf-8') as file:
                # Сериализуем словарь Python в JSON с красивым форматированием (indent=4)
                json.dump(self.menu, file, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Критическая ошибка при сохранении файла: {e}")