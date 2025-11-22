import os
import sys

# Определяем директорию, в которой запущен этот скрипт (anagram_checker.py)
# Это гарантирует, что мы сможем найти 'sowpods.txt' независимо от текущей рабочей директории
def get_script_dir(filename):
    """Возвращает абсолютный путь к директории, где находится файл."""
    return os.path.dirname(os.path.abspath(filename))

# Имя файла словаря
WORD_LIST_FILENAME = 'sowpods.txt'
try:
    # Формируем полный абсолютный путь к файлу словаря
    SCRIPT_DIR = get_script_dir(__file__)
    FULL_FILE_PATH = os.path.join(SCRIPT_DIR, WORD_LIST_FILENAME)
except NameError:
    # Если __file__ недоступен, используем простой путь как запасной вариант
    FULL_FILE_PATH = WORD_LIST_FILENAME 


class AnagramChecker:
    """
    Класс для проверки слов и поиска анаграмм на основе заданного списка слов.
    """
    def __init__(self, file_path=FULL_FILE_PATH):
        """
        Инициализирует AnagramChecker, загружая список слов из файла.
        Все слова хранятся в нижнем регистре для регистронезависимого сравнения.
        """
        self.word_set = set()
        self.file_path = file_path
        
        # Проверка существования файла
        if not os.path.exists(self.file_path):
            # Теперь здесь будет выводиться полный абсолютный путь, что удобно для отладки
            print(f"КРИТИЧЕСКАЯ ОШИБКА: Файл списка слов не найден по пути: {self.file_path}")
            print("Пожалуйста, убедитесь, что 'sowpods.txt' находится в той же директории, что и скрипт.")
            return

        try:
            # Используем явное указание кодировки 'utf-8' для надежности чтения.
            with open(self.file_path, 'r', encoding='utf-8') as file:
                # Читаем все строки, удаляем пробелы/переводы строк и приводим к нижнему регистру
                for line in file:
                    word = line.strip().lower()
                    if word.isalpha(): # Убедимся, что это только буквы
                        self.word_set.add(word)
            
            print(f"LOG: Загружено {len(self.word_set)} слов для проверки.")

        except Exception as e:
            print(f"КРИТИЧЕСКАЯ ОШИБКА: Не удалось прочитать файл {self.file_path}. Детали: {e}")
            # Ensure the set is empty if reading fails critically
            self.word_set = set()

    def get_word_count(self):
        """Возвращает количество загруженных слов."""
        return len(self.word_set)
        
    def is_valid_word(self, word):
        """
        Проверяет, существует ли данное слово в списке слов.
        
        Args:
            word (str): Слово для проверки.

        Returns:
            bool: True, если слово существует, False в противном случае.
        """
        # Сравниваем в нижнем регистре
        return word.lower() in self.word_set

    def is_anagram(self, word1, word2):
        """
        Проверяет, являются ли два слова анаграммами друг друга.
        Слова должны иметь одинаковую длину и один и тот же набор символов.
        
        Args:
            word1 (str): Первое слово.
            word2 (str): Второе слово.

        Returns:
            bool: True, если слова являются анаграммами, False в противном случае.
        """
        # Сначала проверяем, что это не одно и то же слово
        if word1.lower() == word2.lower():
            return False
        
        # Анаграмма определяется путем сравнения отсортированных символов
        return sorted(word1.lower()) == sorted(word2.lower())

    def get_anagrams(self, word):
        """
        Находит все анаграммы для заданного слова в загруженном списке.
        
        Args:
            word (str): Слово, для которого ищутся анаграммы.

        Returns:
            list: Список анаграмм.
        """
        anagrams = []
        
        # Получаем отсортированную сигнатуру слова для сравнения
        word_signature = sorted(word.lower())
        
        for other_word in self.word_set:
            # Сначала быстро отфильтруем по длине
            if len(other_word) != len(word):
                continue

            # Проверяем, что это не то же самое слово, и является анаграммой
            if self.is_anagram(word, other_word):
                # Добавляем анаграмму в ее исходном виде (или с заглавной буквы)
                anagrams.append(other_word)
                
        return anagrams