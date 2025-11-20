import sys
from menu_manager import MenuManager # Импорт класса логики

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
    Выводит текущее меню ресторана.
    """
    print("\n" + "="*40)
    print(f"{'МЕНЮ РЕСТОРАНА':^40}")
    print("="*40)
    print(f"{'НАИМЕНОВАНИЕ':<30} | {'ЦЕНА (RUB)':>8}")
    print("-"*40)
    
    items = manager.get_menu().get("items", [])
    if not items:
        print(f"{'Меню пока пусто.':^40}")
        print("="*40)
        return

    for item in items:
        name = item.get('name', 'N/A')
        price = item.get('price', 0.0)
        print(f"{name:<30} | {price:>8.2f}")
    
    print("="*40)

def add_item_to_menu(manager: MenuManager):
    """
    Запрашивает у пользователя имя и цену и вызывает manager.add_item().
    """
    print("\n--- ДОБАВЛЕНИЕ ЭЛЕМЕНТА ---")
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
    print(f"\n✅ Элемент '{item_name.capitalize()}' был успешно добавлен в текущее меню.")

def remove_item_from_menu(manager: MenuManager):
    """
    Запрашивает у пользователя имя элемента и вызывает manager.remove_item().
    """
    print("\n--- УДАЛЕНИЕ ЭЛЕМЕНТА ---")
    item_name = input("Введите название элемента для удаления: ").strip()
    
    if not item_name:
        print("❌ Название элемента не может быть пустым.")
        return

    if manager.remove_item(item_name):
        print(f"\n✅ Элемент '{item_name.capitalize()}' был успешно удален из текущего меню.")
    else:
        print(f"\n❌ Ошибка: Элемент '{item_name.capitalize()}' не найден в меню.")

def show_user_menu(manager: MenuManager):
    """
    Отображает меню программы и управляет основным циклом.
    """
    while True:
        print("\n" + "*"*40)
        print(f"{'МЕНЮ УПРАВЛЕНИЯ':^40}")
        print("*"*40)
        print("(a) Добавить элемент")
        print("(d) Удалить элемент")
        print("(v) Посмотреть меню")
        print("(x) Выход и сохранение")
        print("*"*40)
        
        choice = input("Введите ваш выбор: ").strip().lower()
        
        if choice == 'a':
            add_item_to_menu(manager)
        elif choice == 'd':
            remove_item_from_menu(manager)
        elif choice == 'v':
            show_restaurant_menu(manager)
        elif choice == 'x':
            # Сохранение перед выходом
            manager.save_to_file()
            print("\n========================================")
            print("✅ Меню успешно сохранено в restaurant_menu.json.")
            print("Программа завершена.")
            print("========================================")
            sys.exit(0)
        else:
            print("❌ Неверный ввод. Пожалуйста, используйте (a), (d), (v) или (x).")

# --- Точка входа в программу ---
if __name__ == "__main__":
    menu_manager_instance = load_manager()
    show_user_menu(menu_manager_instance)