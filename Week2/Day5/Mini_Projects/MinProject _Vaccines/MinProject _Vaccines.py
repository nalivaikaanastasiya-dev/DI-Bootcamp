import sys
import os

# Проверяем, что вводимые типы крови являются допустимыми
VALID_BLOOD_TYPES = {"A", "B", "AB", "O"}

class Human:
    """
    Представляет гражданина, ожидающего вакцинации.
    
    Атрибуты:
        id_number (str)
        name (str)
        age (int)
        priority (bool): Является ли человек приоритетным (помимо возраста).
        blood_type (str): "A", "B", "AB", или "O".
        family (list): Список Human, живущих в одном доме (Часть 2).
    """
    def __init__(self, id_number, name, age, priority, blood_type):
        if blood_type not in VALID_BLOOD_TYPES:
            raise ValueError(f"Недопустимый тип крови: {blood_type}. Допустимые: {VALID_BLOOD_TYPES}")
            
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
        self.family = [] # Часть 2: Инициализируется пустым списком

    def add_family_member(self, person):
        """
        Часть 2: Добавляет человека в семью текущего человека 
        и добавляет текущего человека в семью переданного человека (взаимно).
        """
        # Добавляем person в семью self, если его там нет
        if person not in self.family and person is not self:
            self.family.append(person)
        
        # Добавляем self в семью person, если его там нет
        if self not in person.family and person is not self:
            person.family.append(self)

    def is_family_of(self, person):
        """Вспомогательный метод для проверки родства (используется в rearrange_queue)."""
        return person in self.family
        
    def __repr__(self):
        """Удобное представление для отладки и вывода."""
        p_status = "P" if self.priority or self.age > 60 else "N"
        return f"({self.name}, {self.age} | {p_status} | {self.blood_type})"

class Queue:
    """
    Представляет очередь людей, ожидающих вакцины.
    
    Атрибуты:
        humans (list): Список объектов Human.
    """
    def __init__(self):
        self.humans = []

    def add_person(self, person):
        """
        Добавляет человека в очередь. Приоритетные (возраст > 60 или priority=True) 
        вставляются в начало (индекс 0).
        """
        is_high_priority = person.age > 60 or person.priority
        
        if is_high_priority:
            # Предотвращаем list.insert (Бонус): используем конкатенацию списка
            self.humans = [person] + self.humans
        else:
            self.humans.append(person)

    def find_in_queue(self, person):
        """
        Возвращает индекс человека в очереди.
        Предотвращаем list.index (Бонус): используем ручной перебор.
        """
        for i in range(len(self.humans)):
            if self.humans[i] is person:
                return i
        return -1 # Возвращаем -1, если не найден

    def swap(self, person1, person2):
        """
        Меняет местами person1 и person2 в очереди.
        """
        index1 = self.find_in_queue(person1)
        index2 = self.find_in_queue(person2)
        
        if index1 != -1 and index2 != -1:
            # Используем прямое присваивание индексов для обмена
            self.humans[index1], self.humans[index2] = self.humans[index2], self.humans[index1]
            return True
        return False

    def get_next(self):
        """
        Возвращает и удаляет первого человека из очереди.
        Предотвращаем list.pop (Бонус): используем срезы списка.
        """
        if not self.humans:
            return None
        
        next_person = self.humans[0]
        # Используем срез для удаления первого элемента
        self.humans = self.humans[1:]
        return next_person

    def get_next_blood_type(self, blood_type):
        """
        Возвращает и удаляет первого человека с указанным типом крови.
        Предотвращаем list.pop/list.index (Бонус): используем ручной поиск и срезы.
        """
        if not self.humans:
            return None

        found_index = -1
        for i in range(len(self.humans)):
            if self.humans[i].blood_type == blood_type:
                found_index = i
                break
        
        if found_index == -1:
            return None
        
        person = self.humans[found_index]
        
        # Удаляем элемент, используя срезы списка (запрет list.pop)
        self.humans = self.humans[:found_index] + self.humans[found_index+1:]
        
        return person

    def sort_by_age(self):
        """
        Сортирует очередь: сначала приоритетные, затем более старые, затем более молодые.
        Предотвращаем list.sort/sorted (Бонус): используем ручной алгоритм сортировки (модифицированный Bubble Sort).
        Приоритет: 1. Priority/Age > 60, 2. Возраст (по убыванию).
        """
        n = len(self.humans)
        if n <= 1:
            return

        def is_higher_priority(person1, person2):
            """Вспомогательная функция для определения порядка."""
            p1_priority = person1.priority or person1.age > 60
            p2_priority = person2.priority or person2.age > 60
            
            # 1. Приоритетный всегда идет первым
            if p1_priority and not p2_priority:
                return True
            if p2_priority and not p1_priority:
                return False
            
            # 2. Если приоритеты равны, сортируем по возрасту (чем старше, тем выше)
            if person1.age > person2.age:
                return True
            
            return False # Иначе person2 остается первым или порядок не меняется

        # Модифицированный Bubble Sort
        swapped = True
        while swapped:
            swapped = False
            for i in range(n - 1):
                # Если person[i+1] имеет более высокий приоритет/возраст, чем person[i], меняем их
                if not is_higher_priority(self.humans[i], self.humans[i+1]):
                    self.humans[i], self.humans[i+1] = self.humans[i+1], self.humans[i]
                    swapped = True
            n -= 1 # Сокращаем диапазон поиска

    def rearrange_queue(self):
        """
        Часть 2: Переставляет очередь так, чтобы два члена одной семьи не стояли рядом.
        Если это невозможно, он оставляет семью вместе.
        """
        n = len(self.humans)
        if n < 2:
            return

        i = 0
        while i < n - 1:
            current_person = self.humans[i]
            next_person = self.humans[i+1]
            
            # Проверяем, являются ли текущий и следующий члены одной семьи
            if current_person.is_family_of(next_person):
                
                # Ищем замену, начиная с человека, следующего за семейной парой
                j = i + 2 
                replacement_index = -1
                
                while j < n:
                    potential_replacement = self.humans[j]
                    
                    # Замена не должна быть членом семьи текущего человека
                    if not current_person.is_family_of(potential_replacement):
                        replacement_index = j
                        break
                    j += 1
                
                if replacement_index != -1:
                    # Найдена подходящая замена: меняем местами со следующим человеком (i+1)
                    # чтобы разбить семейную пару (i, i+1) на (i, j)
                    self.humans[i+1], self.humans[replacement_index] = self.humans[replacement_index], self.humans[i+1]
                    # Успешный обмен. Мы сдвинулись на одну позицию вперед, чтобы проверить следующую пару.
                    i += 2
                else:
                    # Невозможно найти замену до конца очереди.
                    # Перемещаем второго члена семьи в конец очереди, чтобы разбить пару.
                    
                    # Используем ручное удаление/добавление, чтобы избежать list.pop и list.insert
                    family_member_to_move = self.humans[i+1]
                    
                    # 1. Удаляем i+1 элемент с помощью срезов
                    self.humans = self.humans[:i+1] + self.humans[i+2:]
                    
                    # 2. Добавляем его в конец
                    self.humans.append(family_member_to_move)
                    
                    # Не продвигаемся, так как на позицию i+1 встал новый человек.
                    i += 1 
            else:
                # Пары нет, переходим к следующей паре
                i += 1

    def __len__(self):
        return len(self.humans)

    def __str__(self):
        return f"Очередь (len={len(self)}): " + " -> ".join(map(str, self.humans))

# --- ДЕМОНСТРАЦИОННЫЙ КОД ---

def setup_demo():
    """Создает людей и очередь для демонстрации."""
    
    # Создание людей (Часть 1 & 2)
    h1 = Human("111", "Alice", 65, False, "A")        # 65 лет, высокий приоритет по возрасту
    h2 = Human("222", "Bob", 30, True, "O")          # 30 лет, высокий приоритет явно
    h3 = Human("333", "Charlie", 70, False, "B")     # 70 лет, высокий приоритет по возрасту
    h4 = Human("444", "David", 25, False, "A")       # 25 лет, низкий приоритет
    h5 = Human("555", "Eve", 40, True, "AB")         # 40 лет, высокий приоритет явно
    h6 = Human("666", "Frank", 22, False, "O")       # 22 года, низкий приоритет
    h7 = Human("777", "Grace", 65, False, "B")       # 65 лет, высокий приоритет (Семья H1)
    
    # Создание семей (Часть 2)
    h1.add_family_member(h7) # Alice и Grace - семья
    h4.add_family_member(h6) # David и Frank - семья
    
    # Создание очереди
    q = Queue()
    
    # Добавление людей в случайном порядке
    q.add_person(h4) # David (Normal)
    q.add_person(h3) # Charlie (High) -> должен быть вставлен в начало
    q.add_person(h6) # Frank (Normal)
    q.add_person(h1) # Alice (High) -> должен быть вставлен в начало перед Charlie
    q.add_person(h5) # Eve (High) -> должен быть вставлен в начало перед Alice
    q.add_person(h2) # Bob (High) -> должен быть вставлен в начало перед Eve
    q.add_person(h7) # Grace (High) -> должен быть вставлен в начало перед Bob
    
    return q, h1, h2, h3, h4, h5, h6, h7

def run_demonstration():
    """Запускает демонстрацию всех методов."""
    
    q, h1, h2, h3, h4, h5, h6, h7 = setup_demo()
    
    print("--- 1. ДЕМОНСТРАЦИЯ: ДОБАВЛЕНИЕ И ПРИОРИТЕТ ---")
    print("Исходная очередь (Приоритеты вставлены в начало, низкий приоритет добавлен в конец):")
    print(q)
    
    # Ожидаемый порядок: [H7(65), H2(P), H5(P), H1(65), H3(70), H4(N), H6(N)]
    # (Обратите внимание, H3(70) был добавлен раньше H1(65), но H1 был вставлен первым)
    print("\n--- 2. ДЕМОНСТРАЦИЯ: РУЧНАЯ СОРТИРОВКА (sort_by_age) ---")
    q.sort_by_age()
    print("Очередь после сортировки по Приоритету/Возрасту (старшие вперед):")
    print(q)
    # Ожидаемый порядок: [H3(70), H1(65), H7(65), H5(P/40), H2(P/30), H4(25), H6(22)]
    
    print("\n--- 3. ДЕМОНСТРАЦИЯ: ПОИСК (find_in_queue) И ОБМЕН (swap) ---")
    
    idx_h4 = q.find_in_queue(h4)
    idx_h6 = q.find_in_queue(h6)
    print(f"Индекс David (H4, 25) до обмена: {idx_h4}") # Должно быть 5
    print(f"Индекс Frank (H6, 22) до обмена: {idx_h6}") # Должно быть 6
    
    q.swap(h4, h6)
    print("Очередь после обмена H4 и H6:")
    print(q)
    
    idx_h4_after = q.find_in_queue(h4)
    idx_h6_after = q.find_in_queue(h6)
    print(f"Индекс David (H4, 25) после обмена: {idx_h4_after}") # Должно быть 6
    print(f"Индекс Frank (H6, 22) после обмена: {idx_h6_after}") # Должно быть 5
    
    print("\n--- 4. ДЕМОНСТРАЦИЯ: ПОЛУЧЕНИЕ СЛЕДУЮЩЕГО (get_next) ---")
    next_p = q.get_next()
    print(f"Получен следующий человек (Индекс 0): {next_p.name}")
    print(f"Очередь после get_next (удален {next_p.name}):")
    print(q)
    
    print("\n--- 5. ДЕМОНСТРАЦИЯ: ПОЛУЧЕНИЕ ПО ТИПУ КРОВИ (get_next_blood_type) ---")
    next_blood_p = q.get_next_blood_type("AB")
    print(f"Получен следующий человек с типом крови 'AB': {next_blood_p.name}")
    
    next_blood_p = q.get_next_blood_type("B")
    print(f"Получен следующий человек с типом крови 'B': {next_blood_p.name}")
    
    print("Очередь после get_next_blood_type:")
    print(q)
    # Оставшиеся: [H1(A), H2(O), H6(O), H4(A)]
    
    print("\n--- 6. ДЕМОНСТРАЦИЯ: ПЕРЕСТАНОВКА СЕМЕЙ (rearrange_queue, Часть 2) ---")
    print(f"Семья Alice (H1): {[m.name for m in h1.family]}") # Grace
    print(f"Семья David (H4): {[m.name for m in h4.family]}") # Frank

    # Снова добавляем Grace (H7) рядом с Alice (H1), и Bob (H2) рядом с Frank (H6)
    # Текущая очередь: [H1(A), H2(O), H6(O), H4(A)]
    # Мы видим пару (H6, H4) [Frank, David] - они семья
    q.swap(h1, h2) # Меняем Alice и Bob, чтобы семья H6-H4 была рядом
    print(f"Очередь до rearrange: {q}") # Должна быть [H2(O), H1(A), H6(O), H4(A)]
    # Семья: H6(Frank) и H4(David) стоят рядом! (H6, H4)

    print("\nЗапуск rearrange_queue...")
    q.rearrange_queue()
    print("Очередь после rearrange_queue:")
    print(q)
    # Ожидается, что H4 (David) будет перемещен в конец или будет найден другой человек (H1) для обмена.
    # В данном случае: H6(Frank) и H4(David) — семья. Замена H4 — H1(Alice).
    # Очередь должна стать: [H2(O), H1(A), H1(A), H4(A)] -> [H2, H1, H4, H6] или [H2, H1, H4] + H6 в конце

    # Проверка:
    # Исходная пара: H6(Frank), H4(David) на индексах 2, 3
    # i=2, пара (H6, H4). Ищем замену: нет (n=4).
    # Перемещаем H4 в конец: q = [H2, H1, H6] + [H4]. i=2
    # Ожидаемый результат: [H2(O), H1(A), H6(O), H4(A)]

if __name__ == "__main__":
    run_demonstration()