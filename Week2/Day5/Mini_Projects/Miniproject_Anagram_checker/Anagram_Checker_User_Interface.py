from anagram_checker import AnagramChecker

def get_user_input():
    """
    Отображает меню, получает ввод от пользователя и выполняет базовую валидацию.
    
    Returns:
        str or None: Очищенное и проверенное слово или None, если пользователь выбрал выход.
    """
    print("\n------------------------------------------------------")
    print("Добро пожаловать в Анаграмма-Чекер!")
    print("1. Введите слово для проверки (или 'ВЫХОД' для завершения).")
    print("------------------------------------------------------")

    user_input = input("Ваш ввод: ").strip()

    if user_input.upper() == "ВЫХОД":
        return None

    # 1. Проверка на пустой ввод
    if not user_input:
        print("\nОШИБКА: Ввод не может быть пустым.")
        return False

    # 2. Проверка на несколько слов
    if ' ' in user_input:
        print("\nОШИБКА: Разрешено вводить только одно слово.")
        return False

    # 3. Проверка на только алфавитные символы
    if not user_input.isalpha():
        print("\nОШИБКА: Допускаются только алфавитные символы (без цифр или спецсимволов).")
        return False

    # Возвращаем очищенное (без пробелов по краям) слово
    return user_input

def display_results(word, is_valid, anagrams):
    """
    Отображает результаты проверки и поиска анаграмм в удобном формате.
    """
    print("\n==================================================")
    print(f'ВАШЕ СЛОВО: "{word.upper()}"')
    
    if is_valid:
        print("-> Это допустимое английское слово.")
    else:
        print("-> Это НЕДОПУСТИМОЕ слово (не найдено в словаре).")
        
    if anagrams:
        # Преобразуем список в строку с заглавной буквы для лучшего отображения
        formatted_anagrams = ", ".join([a.capitalize() for a in anagrams])
        print(f"Анаграммы для вашего слова ({len(anagrams)}): {formatted_anagrams}.")
    else:
        print("Анаграмм для вашего слова не найдено.")
        
    print("==================================================")


def main():
    """
    Основная функция, управляющая пользовательским интерфейсом.
    """
    try:
        # Создаем экземпляр AnagramChecker
        checker = AnagramChecker()
    except Exception as e:
        print(f"Не удалось инициализировать AnagramChecker. Проверьте 'anagram_checker.py'.")
        print(f"Детали ошибки: {e}")
        return

    # Проверка, что словарь загружен
    word_count = checker.get_word_count()
    if word_count == 0:
        print("\nКРИТИЧЕСКАЯ ОШИБКА: Словарь пуст. Проверьте, что 'sowpods.txt' существует и не пуст.")
        return
    else:
        # Информационное сообщение для пользователя
        print(f"\nINFO: Загружено слов: {word_count}.")

    while True:
        word_input = get_user_input()

        if word_input is None:
            print("\nСпасибо за использование Anagram Checker. До свидания!")
            break
        
        if word_input is False:
            continue
            
        # Теперь, когда ввод проверен, используем класс AnagramChecker
        
        # 1. Проверяем, является ли слово допустимым
        is_valid = checker.is_valid_word(word_input)
        
        # 2. Находим все анаграммы
        # Мы используем исходный ввод, но checker будет работать с нижним регистром
        anagrams_found = checker.get_anagrams(word_input)
        
        # 3. Отображаем результаты
        display_results(word_input, is_valid, anagrams_found)


if __name__ == "__main__":
    main()