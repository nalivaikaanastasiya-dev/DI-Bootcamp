import random

class Farm:
    """
    Класс, представляющий ферму и управляющий учетом животных.
    """
    
    def __init__(self, farm_name):
        """
        Конструктор класса Farm. Инициализирует имя фермы и пустой словарь для животных.
        
        :param farm_name: Название фермы (строка).
        """
        self.name = farm_name        # Атрибут для хранения названия фермы
        self.animals = {}            # Словарь для хранения животных: {'тип_животного': количество}

    
    def add_animal(self, animal_type=None, count=1, **kwargs):
        """
        Добавляет животных на ферму. Поддерживает два формата вызова:
        1. Позиционные аргументы: add_animal('cow', 5)
        2. Именованные аргументы (**kwargs): add_animal(horse=2, duck=4)
        
        :param animal_type: Тип животного (необязательно, если используются kwargs).
        :param count: Количество добавляемых животных (по умолчанию 1).
        :param kwargs: Дополнительные животные в формате 'тип'=количество.
        """
        
        # 1. Обработка позиционного аргумента (animal_type)
        if animal_type:
            # Получаем текущее количество (или 0, если животного еще нет) и добавляем count
            self.animals[animal_type] = self.animals.get(animal_type, 0) + count

        # 2. Обработка именованных аргументов (kwargs)
        for animal, quantity in kwargs.items():
            # Получаем текущее количество и добавляем quantity
            self.animals[animal] = self.animals.get(animal, 0) + quantity

    def get_animal_types(self):
        """
        Возвращает отсортированный по алфавиту список всех видов животных на ферме.
        
        :return: Отсортированный список ключей словаря self.animals.
        """
        return sorted(self.animals.keys())

    def get_info(self):
        """
        Возвращает полный, аккуратно отформатированный отчет о ферме.
        Вывод соответствует примеру: имя, список животных с количеством, "E-I-E-I-0!".
        
        :return: Полная строка отчета.
        """
        # Начало отчета: Название фермы
        output = f"{self.name}'s farm\n"
        
        # Получаем список животных, отсортированный для красивого вывода
        sorted_animals = self.get_animal_types()

        # Формируем список животных и их количества
        for animal in sorted_animals:
            count = self.animals[animal]
            # f-строка для форматирования столбцов:
            # {animal:<5} - выравнивание по левому краю, ширина 5 символов
            # {count:>3} - выравнивание по правому краю, ширина 3 символа
            output += f"{animal:<5} : {count:>3}\n"

        # Завершающая фраза с отступом
        output += "    E-I-E-I-0!\n"
        return output

    def get_short_info(self):
        """
        Возвращает краткую информацию о ферме в формате предложения, 
        например: "McDonald’s farm has cows, goats and sheeps.".
        
        :return: Краткая строка отчета.
        """
        animal_types = self.get_animal_types()
        
        names_for_sentence = []
        # Шаг 1: Определяем форму слова (единственное/множественное) для каждого животного
        for animal in animal_types:
            count = self.animals[animal]
            
            # Если количество > 1 и слово не заканчивается на 's', добавляем 's'
            plural_name = animal + 's' if count > 1 and animal[-1] != 's' else animal
            
            names_for_sentence.append(plural_name)

        # Шаг 2: Формируем строку перечисления (с запятыми и "and")
        if not names_for_sentence:
            # Случай: нет животных
            animal_list_str = "no animals"
        elif len(names_for_sentence) == 1:
            # Случай: только один вид животного (добавляем 's' для грамматики)
            # Например, 'cow' -> 'cows'
            animal_list_str = names_for_sentence[0] + 's' 
        else:
            # Случай: два и более животных
            last_animal = names_for_sentence[-1]                  # Последнее животное
            rest_of_animals = ', '.join(names_for_sentence[:-1])  # Все, кроме последнего, через запятую
            # Объединяем, используя " and "
            animal_list_str = f"{rest_of_animals} and {last_animal}"
            
        # Шаг 3: Собираем финальное предложение
        return f"{self.name}'s farm has {animal_list_str}."

# ----------------------------------------------------
#               ДЕМОНСТРАЦИЯ И ТЕСТИРОВАНИЕ
# ----------------------------------------------------

# Создание объекта фермы
macdonald = Farm("McDonald")


# Добавление животных по частям (старый формат вызова)
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep') # Обновляем sheep: 1 + 1 = 2
macdonald.add_animal('goat', 12)


# Добавление нескольких животных сразу (новый формат с kwargs)
macdonald.add_animal(horse=2, duck=4)

print("\n--- Полный отчет (get_info) ---")
print(macdonald.get_info())

print("\n--- Список видов (get_animal_types) ---")
print(macdonald.get_animal_types())

print("\n--- Краткий отчет (get_short_info) ---")
print(macdonald.get_short_info())