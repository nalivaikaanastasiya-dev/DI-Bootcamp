# Exercise 2 : Giphy API #1

import requests

def fetch_and_process_gifs(query: str, rating: str, api_key: str, limit: int):
    """
    Конструирует URL, отправляет GET-запрос к Giphy API, 
    фильтрует результаты и возвращает количество отфильтрованных GIF-ов.
    
    :param query: Поисковый запрос (например, "hilarious").
    :param rating: Возрастной рейтинг (например, "g").
    :param api_key: Ключ GIPHY API.
    :param limit: Максимальное количество результатов для возврата API.
    :return: Длина списка GIF-ов с высотой > 100.
    """
    
    BASE_URL = "https://api.giphy.com/v1/gifs/search"
    
    # 1. Используем f-строку и переменные для построения URL
    url = (
        f"{BASE_URL}?q={query}"
        f"&rating={rating}"
        f"&api_key={api_key}"
        f"&limit={limit}" # Ограничиваем до первых 10 GIF-ов
    )
    
    print(f"Конструированный URL: {url}")
    print("Отправка запроса...")

    try:
        # Отправляем HTTP-запрос
        response = requests.get(url)
        
        # 2. Проверяем код состояния
        if response.status_code == 200:
            # 3. Возвращаем результат как JSON-объект
            data = response.json()
            
            # Получаем список GIF-ов
            gifs = data.get('data', [])
            
            # 4. Фильтруем GIF-ы: высота должна быть больше 100
            filtered_gifs = []
            
            for gif in gifs:
                # В Giphy данные об изображениях находятся в 'images' -> 'fixed_height'
                image_data = gif.get('images', {}).get('fixed_height', {})
                
                # 'height' хранится как строка, поэтому преобразуем в int для сравнения
                try:
                    height = int(image_data.get('height'))
                    if height > 100:
                        filtered_gifs.append(gif)
                except (TypeError, ValueError):
                    # Пропускаем GIF, если высота не указана или не является числом
                    continue
                    
            # 5. Возвращаем длину отфильтрованного объекта (списка)
            return len(filtered_gifs)

        else:
            print(f"Ошибка HTTP: Статус-код {response.status_code}")
            return 0

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return 0

# --- Настройки согласно заданию ---
API_KEY = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"
SEARCH_QUERY = "hilarious"
RATING = "g"
LIMIT = 10 # Запрос ограничен 10 результатами

# Запуск функции
result_length = fetch_and_process_gifs(
    query=SEARCH_QUERY, 
    rating=RATING, 
    api_key=API_KEY, 
    limit=LIMIT
)

if result_length > 0:
    print(f"\nОбщее количество GIF-ов (из первых {LIMIT} результатов), имеющих высоту более 100: {result_length}")
elif result_length == 0:
    print("\nНе найдено GIF-ов, соответствующих критериям.")

# Exercise 3 : Giphy API #2

import requests

# Константы API, предоставленные в задании
API_KEY = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"
SEARCH_URL = "https://api.giphy.com/v1/gifs/search"
TRENDING_URL = "https://api.giphy.com/v1/gifs/trending"

def get_gifs_from_api(url: str, params: dict, description: str):
    """
    Универсальная функция для отправки GET-запроса к Giphy API.
    
    :param url: URL API (Search или Trending).
    :param params: Словарь параметров запроса.
    :param description: Описание для вывода в консоль.
    :return: Словарь с данными JSON или None в случае ошибки.
    """
    print(f"\n--- Выполнение запроса: {description} ---")
    
    try:
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            print("✅ Запрос успешен (Status 200).")
            return response.json()
        else:
            print(f"❌ Ошибка HTTP: Статус-код {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"❌ Ошибка при выполнении запроса: {e}")
        return None

def main_gif_finder():
    """
    Основная логика программы: запрашивает поисковый термин, пытается выполнить поиск,
    используя Trending Endpoint, если поиск не удался.
    """
    
    # 1. Запрос поискового термина у пользователя
    search_term = input("Введите термин или фразу для поиска GIF-ов (напр., 'cats'): ").strip()
    
    # Флаг для определения, был ли выполнен успешный поиск
    search_successful = False
    
    if search_term:
        print(f"\nПопытка поиска GIF-ов по термину: '{search_term}'...")
        
        search_params = {
            "api_key": API_KEY,
            "q": search_term,
            "limit": 10, # Ограничиваем количество результатов для удобства
            "rating": "g"
        }
        
        # Выполняем запрос поиска
        search_data = get_gifs_from_api(SEARCH_URL, search_params, "Поиск по термину")
        
        if search_data and search_data.get('data'):
            gifs = search_data['data']
            if gifs:
                search_successful = True
                print(f"🎉 Найдены {len(gifs)} релевантных GIF-ов для '{search_term}'.")
                
                # Вывод результатов поиска
                print("\n--- РЕЗУЛЬТАТЫ ПОИСКА ---")
                print(f"Первые {len(gifs)} GIF-ов для '{search_term}':")
                for i, gif in enumerate(gifs):
                    # Печатаем название и прямую ссылку
                    title = gif.get('title', 'Без названия')
                    url = gif.get('url', 'N/A')
                    print(f"  {i+1}. {title} | URL: {url}")
                print("--------------------------")
                
    # 2. Логика отката (Fallback) к трендовым GIF-ам
    if not search_successful:
        
        # Сообщение о неудачном поиске
        if search_term:
            print(f"\n⚠️ Не удалось найти GIF-ы по запросу '{search_term}' или запрос вернул пустой результат.")
        else:
            print("\n⚠️ Поисковый термин не был введен.")
            
        print("➡️ Возвращаем трендовые GIF-ы дня в качестве альтернативы.")

        trending_params = {
            "api_key": API_KEY,
            "limit": 10, # Ограничиваем количество трендовых результатов
            "rating": "g"
        }
        
        # Выполняем запрос к трендовому API
        trending_data = get_gifs_from_api(TRENDING_URL, trending_params, "Получение трендовых GIF-ов")
        
        if trending_data and trending_data.get('data'):
            gifs = trending_data['data']
            print(f"🔥 Найдено {len(gifs)} трендовых GIF-ов.")
            
            # Вывод трендовых результатов
            print("\n--- ТРЕНДОВЫЕ GIF-Ы ДНЯ ---")
            for i, gif in enumerate(gifs):
                title = gif.get('title', 'Без названия')
                url = gif.get('url', 'N/A')
                print(f"  {i+1}. {title} | URL: {url}")
            print("--------------------------")
        else:
            print("❌ Критическая ошибка: Не удалось получить даже трендовые GIF-ы.")

if __name__ == "__main__":
    # Запуск основной функции
    main_gif_finder()