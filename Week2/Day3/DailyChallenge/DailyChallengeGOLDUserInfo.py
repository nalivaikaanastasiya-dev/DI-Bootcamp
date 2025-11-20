import sys

def get_user_input(num_inputs):
    """
    Запрашивает у пользователя данные (Имя, Возраст, Счет) указанное количество раз
    и возвращает список кортежей.
    """
    data_list = []
    print(f"--- Введите {num_inputs} записей (Имя, Возраст, Счет) ---")
    
    for i in range(1, num_inputs + 1):
        print(f"\nЗапись #{i}:")
        
        # 1. Запрос имени (строка)
        while True:
            name = input("Введите Имя: ").strip()
            if name:
                break
            print("Имя не может быть пустым. Попробуйте снова.")

        # 2. Запрос возраста (целое число)
        while True:
            try:
                age_str = input("Введите Возраст (целое число): ").strip()
                age = int(age_str)
                if age >= 0:
                    break
                print("Возраст не может быть отрицательным.")
            except ValueError:
                print("Ошибка: Возраст должен быть целым числом.")

        # 3. Запрос счета (целое число)
        while True:
            try:
                score_str = input("Введите Счет (целое число): ").strip()
                score = int(score_str)
                if 0 <= score <= 100: # Дополнительная проверка на разумность счета
                    break
                print("Счет должен быть целым числом от 0 до 100.")
            except ValueError:
                print("Ошибка: Счет должен быть целым числом.")

        # Добавляем исходные строковые представления возраста и счета, 
        # чтобы соответствовать требуемому формату вывода
        data_list.append((name, age_str, score_str))
        
    return data_list

def sort_data_by_priority(data_list):
    """
    Сортирует список кортежей с использованием лямбда-функции 
    по приоритету: Имя (str) > Возраст (int) > Счет (int).
    """
    # Лямбда-функция:
    # x[0] - Имя (сортируется как str)
    # int(x[1]) - Возраст (преобразуется в int для числовой сортировки)
    # int(x[2]) - Счет (преобразуется в int для числовой сортировки)
    # Сортировка по возрастанию (ASC) по всем трем полям.
    
    sorting_key = lambda x: (x[0], int(x[1]), int(x[2]))
    
    # Используем метод .sort() для сортировки списка на месте
    data_list.sort(key=sorting_key)
    
    return data_list

if __name__ == "__main__":
    
    # Устанавливаем требуемое количество вводов
    NUMBER_OF_INPUTS = 5
    
    # 1. Получение данных от пользователя
    user_data = get_user_input(NUMBER_OF_INPUTS)
    
    print("\n" + "=" * 50)
    print("Исходный список (до сортировки):")
    print(user_data)
    
    # 2. Сортировка данных с помощью лямбда-функции
    # (Обратите внимание: мы передаем mutable список, который будет отсортирован на месте)
    sorted_data = sort_data_by_priority(user_data)
    
    # 3. Вывод результата
    print("-" * 50)
    print("Отсортированный список (Имя > Возраст > Счет):")
    print(sorted_data)
    print("=" * 50)
    
    # Демонстрация на примере входных данных из задания (для проверки)
    print("\n--- Проверка с примером из задания ---")
    example_input = [
        ('Tom', '19', '80'),
        ('John', '20', '90'),
        ('Jony', '17', '91'),
        ('Jony', '17', '93'),
        ('Json', '21', '85'),
    ]
    
    print("Исходные данные примера:")
    print(example_input)
    
    sort_data_by_priority(example_input)
    
    print("\nОтсортированные данные примера:")
    print(example_input)



### Обзор Лямбда-функции


sorting_key = lambda x: (x[0], int(x[1]), int(x[2]))