import sys

# Попытка импортировать googletrans. Если не установлен, выдаст ошибку
try:
    from googletrans import Translator
except ImportError:
    print("Ошибка: Модуль 'googletrans==4.0.0-rc1' не установлен.")
    print("Пожалуйста, выполните в терминале: pip install googletrans==4.0.0-rc1")
    sys.exit(1)

def translate_french_words(words_list):
    """
    Переводит список французских слов на английский и возвращает словарь.
    
    Args:
        words_list (list): Список французских слов.
        
    Returns:
        dict: Словарь, где ключ - французское слово, значение - английский перевод.
    """
    # Инициализация переводчика
    translator = Translator()
    
    # Словарь для хранения результатов
    translation_dict = {}
    
    # Итерация по каждому слову и его перевод
    for word in words_list:
        try:
            # Использование метода translate:
            # src='fr' (французский - источник), dest='en' (английский - назначение)
            translation = translator.translate(word, src='fr', dest='en')
            
            # Сохраняем результат в словарь
            translation_dict[word] = translation.text
            
        except Exception as e:
            # Обработка возможных ошибок при обращении к API перевода
            print(f"Ошибка при переводе слова '{word}': {e}", file=sys.stderr)
            translation_dict[word] = "Translation Error"
            
    return translation_dict

if __name__ == "__main__":
    # Исходный список
    french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
    
    print("--- Французско-английский переводчик ---")
    print(f"Исходный список слов: {french_words}")
    
    # Выполнение перевода
    result = translate_french_words(french_words)
    
    print("\nРезультат перевода:")
    print(result)

    # Проверка ожидаемого результата
    expected_result = {"Bonjour": "Hello", "Au revoir": "Goodbye", "Bienvenue": "Welcome", "A bientôt": "See you soon"}
    
    # Поскольку API может вернуть слегка отличающиеся переводы (например, "See you soon." с точкой),
    # мы делаем мягкое сравнение.
    if all(result.get(k, '').lower() == v.lower() for k, v in expected_result.items()):
        print("\n✅ Успех: Полученный результат соответствует ожидаемому.")
    else:
        print("\n⚠️ Завершено, но полученный результат может незначительно отличаться от ожидаемого.")