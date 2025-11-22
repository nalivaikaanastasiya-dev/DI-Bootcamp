import pyowm
from pyowm.utils import formatting
import matplotlib.pyplot as plt
import datetime
import pytz
import numpy as np
import sys 
import os

OWM_API_KEY = "f6e4b2e1fa28a788fb642c22f9a8e033"

def get_city_id_and_coords(owm, location_name):
    """
    Получает ID города и его координаты по названию.
    Использует двухэтапный подход для надежного получения координат.
    """
    print("LOG: Шаг 1: Поиск ID города...")
    try:
        registry = owm.city_id_registry()
        list_of_tuples = registry.ids_for(location_name)
        
        if not list_of_tuples:
            print(f"Местоположение не найдено: {location_name}")
            return None, None, None, None

        # Шаг 1: Берем только ID и Имя (самые стабильные данные)
        city_id = list_of_tuples[0][0]
        city_name = list_of_tuples[0][1]
        
        print(f"LOG: ID города получен ({city_id}). Запрос координат через Weather Manager...")

        # Шаг 2: Получаем координаты (lat/lon) надежным способом
        mgr = owm.weather_manager()
        observation = mgr.weather_at_id(city_id)
        location = observation.location
        
        lat = location.lat
        lon = location.lon
        
        print(f"LOG: Город найден: Координаты={lat}, {lon}")
        
        return city_id, city_name, lat, lon
        
    except Exception as e:
        print(f"КРИТИЧЕСКАЯ ОШИБКА (get_city_id_and_coords): Не удалось найти или обработать данные города. Подробности: {e}")
        return None, None, None, None

def display_current_weather(owm, city_id, city_name):
    """
    Отображает текущую погоду: температуру, ветер, восход/закат.
    """
    print("LOG: Шаг 2: Запрос текущей погоды...")
    try:
        mgr = owm.weather_manager()
        observation = mgr.weather_at_id(city_id)
        weather = observation.weather
        
        print("\n--- ТЕКУЩАЯ ПОГОДА ---")
        print(f"Местоположение: {city_name}")
        
        temp_data = weather.temperature('celsius')
        print(f"Статус: {weather.status}")
        print(f"Текущая температура: {temp_data['temp']:.1f}°C")
        print(f"Ощущается как: {temp_data['feels_like']:.1f}°C")
        
        wind_data = weather.wind()
        print(f"Скорость ветра: {wind_data['speed']} м/с")
        
        sunrise_ts = weather.sunrise_time()
        sunset_ts = weather.sunset_time()

        print(f"Восход солнца: {formatting.timeformat(sunrise_ts, 'iso', utc=False)}")
        print(f"Закат солнца: {formatting.timeformat(sunset_ts, 'iso', utc=False)}")

    except Exception as e:
        print(f"ОШИБКА: Не удалось получить текущую погоду. Возможно, проблема с ключом или сетью. Подробности: {e}")

def display_five_day_forecast(owm, city_id, city_name):
    """
    Отображает прогноз на 5 дней (первые 10 интервалов).
    """
    print("LOG: Шаг 4: Запрос 5-дневного прогноза...")
    try:
        mgr = owm.weather_manager()
        forecast = mgr.forecast_at_id(city_id, '3h')
        
        print(f"\n--- ПРОГНОЗ НА 5 ДНЕЙ ДЛЯ {city_name.upper()} (3-часовые интервалы) ---")
        
        forecast_items = forecast.forecast.weathers[:10]
        
        for weather in forecast_items:
            timestamp = formatting.timeformat(weather.reference_time(), 'iso', utc=False)
            temp = weather.temperature('celsius')['temp']
            status = weather.status
            print(f"[{timestamp}] Температура: {temp:.1f}°C, Статус: {status}")

    except Exception as e:
        print(f"ОШИБКА: Не удалось получить 5-дневный прогноз. Подробности: {e}")

def get_air_pollution(owm, lat, lon):
    """
    Получает и отображает данные о загрязнении воздуха (AQI и CO) по координатам.
    """
    print("LOG: Шаг 3: Запрос данных о загрязнении воздуха...")
    try:
        apm = owm.air_pollution_manager()
        pollution = apm.air_quality_at_coords(lat, lon)
        
        aqi = pollution.aqi
        co = pollution.co
        
        print("\n--- ДАННЫЕ О ЗАГРЯЗНЕНИИ ВОЗДУХА (AQI) ---")
        
        aqi_map = {1: "Хорошо", 2: "Удовлетворительно", 3: "Умеренно", 4: "Плохо", 5: "Очень Плохо"}
        aqi_status = aqi_map.get(aqi, "Неизвестно")
        
        print(f"Индекс Качества Воздуха (AQI): {aqi} ({aqi_status})")
        print(f"Концентрация CO: {co:.2f} µg/m³")
            
    except Exception as e:
        print(f"ОШИБКА: Не удалось получить данные о загрязнении воздуха. Подробности: {e}")

# --- БОНУС: Функции для Построения Графика Влажности ---

def get_three_day_humidity_data(owm, city_id):
    """
    Собирает данные о максимальной влажности на следующие 3 дня для графика.
    """
    try:
        mgr = owm.weather_manager()
        forecast = mgr.forecast_at_id(city_id, '3h')
        
        now = datetime.datetime.now(pytz.utc).date()
        forecast_by_day = {}
        
        for weather in forecast.forecast:
            dt_utc = datetime.datetime.fromtimestamp(weather.reference_time(), tz=pytz.utc)
            date_str = dt_utc.strftime("%Y-%m-%d")
            
            if (dt_utc.date() - now).days < 3:
                humidity = weather.humidity
                if date_str not in forecast_by_day:
                    forecast_by_day[date_str] = []
                forecast_by_day[date_str].append(humidity)

        humidity_data = {}
        for date_str, humidities in sorted(forecast_by_day.items()):
            max_humidity = max(humidities)
            humidity_data[date_str] = max_humidity
            
        return humidity_data

    except Exception as e:
        print(f"ОШИБКА: Не удалось получить данные о влажности для графика. Подробности: {e}")
        return {}

def init_plot(ax, title, ylabel):
    """
    Стилизует оси, заголовок и добавляет сетку на график.
    """
    ax.set_title(title, fontsize=16, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=14)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.grid(axis='y', linestyle='--', alpha=0.7)

def write_humidity_on_bar_chart(ax, bars, humidity_values):
    """
    Добавляет значения влажности (%) над столбцами.
    """
    for bar, humidity in zip(bars, humidity_values):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2., 1.02 * height,
                f'{humidity}%',
                ha='center', va='bottom', fontsize=12, fontweight='bold')

def plot_humidity_forecast(owm, city_id, city_name):
    """
    Строит гистограмму максимальной влажности на 3 дня.
    """
    print("LOG: Шаг 5: Запуск функции построения графика...")
    humidity_data = get_three_day_humidity_data(owm, city_id)
    
    if not humidity_data:
        print("Невозможно построить график из-за отсутствия данных прогноза.")
        return

    dates = [datetime.datetime.strptime(d, "%Y-%m-%d").strftime("%a, %b %d") for d in humidity_data.keys()]
    humidity_values = list(humidity_data.values())

    fig, ax = plt.subplots(figsize=(10, 6))

    bars = ax.bar(dates, humidity_values, color=['#2a9d8f', '#264653', '#e76f51'], width=0.6, edgecolor='black', linewidth=1.5)

    init_plot(ax, f"Прогноз максимальной влажности на 3 дня для {city_name}", "Максимальная влажность (%)")
    
    write_humidity_on_bar_chart(ax, bars, humidity_values)
    
    ax.set_ylim(0, 100)
    
    plt.tight_layout()
    print("LOG: Отображение графического окна. Если вы его не видите, проверьте панель задач.")
    plt.show() 

# --- ГЛАВНАЯ ФУНКЦИЯ ---

def main():
    """
    Основная функция программы, управляющая всем рабочим процессом.
    """
    # 1. Проверка API-ключа
    if OWM_API_KEY == "ВАШ_КЛЮЧ_API_ЗДЕСЬ":
        print("\n===================================================")
        print("ОШИБКА: ОТСУТСТВУЕТ API КЛЮЧ! ПОЖАЛУЙСТА, ИСПРАВЬТЕ.")
        print("===================================================\n")
        return

    print("LOG: Проверка API-ключа прошла успешно. Продолжение работы.")

    # 2. Инициализация PyOWM
    try:
        owm = pyowm.OWM(OWM_API_KEY)
        print("LOG: Инициализация PyOWM прошла успешно.")
    except Exception as e:
        print(f"КРИТИЧЕСКАЯ ОШИБКА: Не удалось инициализировать OWM. Проверьте соединение или ключ. Подробности: {e}")
        return
    
    # 3. Запрос города
    location_name = input("Введите название города (например, Paris, FR; London, UK): ")
    
    # 4. Получение ID и координат
    city_id, city_name, lat, lon = get_city_id_and_coords(owm, location_name)

    if city_id is None:
        return # Выход, если город не найден

    # 5. Вывод всех данных
    display_current_weather(owm, city_id, city_name)
    
    if lat is not None and lon is not None:
        get_air_pollution(owm, lat, lon)
        
    display_five_day_forecast(owm, city_id, city_name)

    # 6. Запуск графика (Бонус)
    plot_humidity_forecast(owm, city_id, city_name)

if __name__ == "__main__":
    # Установка кодировки для корректного отображения кириллицы в консоли Windows
    if sys.platform.startswith('win'):
        os.system('chcp 65001') 
    main()