import sys
from menu_manager import MenuManager # Импортируем класс логики

# Глобальная переменная для экземпляра MenuManager
manager = None 

def load_manager():
    """
    Создает новый экземпляр MenuManager.
    """
    global manager
    manager = MenuManager()
    print(">>> Менеджер меню загружен. Данные взяты из файла.")
    return manager

def show_restaurant_menu(manager: MenuManager):
    """
    Выводит текущее меню ресторана, включая специальное меню, 
    и отрисовывает сердце.
    """
    # 1. Отрисовываем сердце
    manager.display_heart_of_stars()
    
    # 2. Основное меню
    print("\n" + "="*40)
    print(f"{'ОСНОВНОЕ МЕНЮ':^40}")
    print("="*40)
    print(f"{'НАИМЕНОВАНИЕ':<30} | {'ЦЕНА (RUB)':>8}")
    print("-"*40)
    
    items = manager.get_menu().get("items", [])
    if not items:
        print(f"{'Основное меню пусто.':^40}")
    else:
        for item in items:
            name = item.get('name', 'N/A')
            price = item.get('price', 0.0)
            print(f"{name:<30} | {price:>8.2f}")
    
    print("="*40)
    
    # 3. Меню Valentine's Day
    valentine_items = manager.get_menu().get("valentine_items", [])
    
    print("\n" + "♥"*40)
    print(f"{'СПЕЦИАЛЬНОЕ МЕНЮ НА ДЕНЬ СВ. ВАЛЕНТИНА':^40}")
    print("♥"*40)
    print(f"{'НАИМЕНОВАНИЕ':<30} | {'ЦЕНА (RUB)':>8}")
    print("-"*40)

    if not valentine_items:
        print(f"{'Специальное меню пока пусто.':^40}")
    else:
        for item in valentine_items:
            name = item.get('name', 'N/A')
            # Цена уже сохранена как float, но выводим ее в нужном формате XX,14
            price_str = f"{item.get('price', 0.0):.2f}".replace('.', ',')
            print(f"{name:<30} | {price_str:>8}")

    print("♥"*40)

def add_item_to_menu(manager: MenuManager):
    """
    Запрашивает у пользователя данные и передает их менеджеру для добавления 
    в ОСНОВНОЕ меню.
    """
    print("\n--- ДОБАВЛЕНИЕ ЭЛЕМЕНТА В ОСНОВНОЕ МЕНЮ ---")
    item_name = input("Введите название элемента: ").strip()
    
    if not item_name:
        print("❌ Название элемента не может быть пустым.")
        return

    while True:
        try:
            item_price_str = input("Введите цену элемента: ").strip().replace(',', '.')
            item_price = float(item_price_str)
            if item_price <= 0:
                print("❌ Цена должна быть положительным числом.")
                continue
            break
        except ValueError:
            print("❌ Неверный ввод. Цена должна быть числом.")

    manager.add_item(item_name, item_price)
    print(f"\n✅ Элемент '{item_name.capitalize()}' был успешно добавлен в текущее ОСНОВНОЕ меню.")

def add_valentine_item(manager: MenuManager):
    """
    Запрашивает у пользователя данные для Valentine's Day и передает их менеджеру 
    для валидации и добавления.
    """
    print("\n--- ДОБАВЛЕНИЕ ЭЛЕМЕНТА В МЕНЮ VALENTINE'S DAY ---")
    print("Требования к имени: начинается с 'V', слова с заглавной, союзы строчные, минимум две 'e', без цифр.")
    print("Требования к цене: формат XX,14.")
    
    item_name = input("Введите название Valentine's элемента: ").strip()
    item_price_str = input("Введите цену Valentine's элемента (XX,14): ").strip()

    # Валидация происходит внутри этого метода
    if manager.add_valentine_item(item_name, item_price_str):
        print(f"\n✅ Элемент '{item_name}' был успешно добавлен в специальное меню.")
    else:
        print("\n❌ Элемент НЕ БЫЛ добавлен, так как не прошел валидацию по правилам Дня Святого Валентина.")

def remove_item_from_menu(manager: MenuManager):
    """
    Удаляет элемент из ОСНОВНОГО меню.
    """
    print("\n--- УДАЛЕНИЕ ЭЛЕМЕНТА ИЗ ОСНОВНОГО МЕНЮ ---")
    item_name = input("Введите название элемента для удаления: ").strip()
    
    if not item_name:
        print("❌ Название элемента не может быть пустым.")
        return

    if manager.remove_item(item_name):
        print(f"\n✅ Элемент '{item_name.capitalize()}' был успешно удален из ОСНОВНОГО меню.")
    else:
        print(f"\n❌ Ошибка: Элемент '{item_name.capitalize()}' не найден в ОСНОВНОМ меню.")

def show_user_menu(manager: MenuManager):
    """
    Отображает меню программы и управляет основным циклом.
    """
    while True:
        print("\n" + "*"*40)
        print(f"{'МЕНЮ УПРАВЛЕНИЯ':^40}")
        print("*"*40)
        print("(a) Добавить элемент в ОСНОВНОЕ меню")
        print("(v) Добавить элемент в V-DAY меню (с валидацией)")
        print("(d) Удалить элемент из ОСНОВНОЕ меню")
        print("(s) Посмотреть меню (Включая V-DAY и сердце)")
        print("(x) Выход и сохранение")
        print("*"*40)
        
        choice = input("Введите ваш выбор: ").strip().lower()
        
        if choice == 'a':
            add_item_to_menu(manager)
        elif choice == 'v':
            add_valentine_item(manager) 
        elif choice == 'd':
            remove_item_from_menu(manager)
        elif choice == 's':
            show_restaurant_menu(manager) 
        elif choice == 'x':
            manager.save_to_file()
            print("\n========================================")
            print("✅ Меню успешно сохранено в restaurant_menu.json.")
            print("Программа завершена.")
            print("========================================")
            sys.exit(0)
        else:
            print("❌ Неверный ввод. Пожалуйста, используйте (a), (v), (d), (s) или (x).")

# --- Точка входа в программу ---
if __name__ == "__main__":
    menu_manager_instance = load_manager()
    show_user_menu(menu_manager_instance)