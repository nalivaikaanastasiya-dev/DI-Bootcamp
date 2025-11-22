import datetime
from typing import List, Optional, Dict, TYPE_CHECKING

# Используем TYPE_CHECKING для избежания циклических импортов в аннотациях типов
if TYPE_CHECKING:
    class Airport:
        pass
    class Airline:
        pass
    class Flight:
        pass

class Airline:
    """
    Представляет авиакомпанию.
    """
    def __init__(self, id_code: str, name: str):
        """
        Инициализирует авиакомпанию.
        :param id_code: Двухбуквенный код авиакомпании (например, "AA").
        :param name: Полное название авиакомпании.
        """
        self.id: str = id_code
        self.name: str = name
        self.planes: List['Airplane'] = []
        
    def __repr__(self):
        return f"Airline(ID: {self.id}, Name: {self.name})"

class Airport:
    """
    Представляет аэропорт и управляет его расписанием и самолетами на земле.
    """
    def __init__(self, city_code: str, city_name: str):
        """
        Инициализирует аэропорт.
        :param city_code: Трехбуквенный код города (например, "JFK").
        :param city_name: Название города.
        """
        self.city: str = city_code
        self.city_name: str = city_name
        self.planes: List['Airplane'] = []  # Самолеты, находящиеся в данный момент в аэропорту
        self.scheduled_departures: List['Flight'] = []  # Будущие вылеты
        self.scheduled_arrivals: List['Flight'] = []  # Будущие прилеты

    def add_plane(self, plane: 'Airplane'):
        """Добавляет самолет на список припаркованных самолетов."""
        if plane not in self.planes:
            self.planes.append(plane)

    def remove_plane(self, plane: 'Airplane'):
        """Удаляет самолет из списка припаркованных самолетов (вылет)."""
        if plane in self.planes:
            self.planes.remove(plane)

    def sort_flights(self):
        """Сортирует списки рейсов по дате/времени."""
        self.scheduled_departures.sort(key=lambda f: f.date)
        self.scheduled_arrivals.sort(key=lambda f: f.date)

    def schedule_flight(self, destination: 'Airport', dt: datetime.datetime, airline: 'Airline') -> Optional['Flight']:
        """
        Находит доступный самолет и планирует новый рейс.

        :param destination: Аэропорт назначения.
        :param dt: Дата и время вылета (datetime.datetime).
        :param airline: Авиакомпания, для которой планируется рейс.
        :return: Объект Flight или None, если самолет не найден.
        """
        # 1. Поиск доступного самолета
        available_plane: Optional['Airplane'] = None
        
        # Перебираем самолеты этой авиакомпании, которые находятся в текущем аэропорту
        for plane in [p for p in self.planes if p.company is airline]:
            if plane.available_on_date(dt.date(), self):
                available_plane = plane
                break
        
        if not available_plane:
            print(f"ERROR: No available plane for {airline.id} at {self.city} on {dt.date()}")
            return None

        # 2. Создание рейса
        new_flight = Flight(
            date=dt,
            destination=destination,
            origin=self,
            plane=available_plane,
            airline=airline
        )

        # 3. Обновление расписания самолета
        available_plane.next_flights.append(new_flight)
        available_plane.next_flights.sort(key=lambda f: f.date)

        # 4. Обновление расписания аэропортов
        self.scheduled_departures.append(new_flight)
        destination.scheduled_arrivals.append(new_flight)
        self.sort_flights()
        destination.sort_flights()
        
        print(f"SUCCESS: Scheduled {new_flight.id} ({new_flight.plane.id}) from {self.city} to {destination.city} on {dt}")
        return new_flight

    def info(self, start_date: datetime.date, end_date: datetime.date):
        """
        Отображает все запланированные вылеты в заданном диапазоне дат.
        
        :param start_date: Начальная дата (включительно).
        :param end_date: Конечная дата (включительно).
        """
        print(f"\n--- Расписание вылетов из {self.city} ({self.city_name}) ---")
        found = False
        for flight in self.scheduled_departures:
            flight_date = flight.date.date()
            if start_date <= flight_date <= end_date:
                print(f"  {flight}")
                found = True
            elif flight_date > end_date:
                # Список отсортирован, можно прекращать поиск
                break
        
        if not found:
            print(f"  Нет запланированных вылетов с {start_date} по {end_date}.")
        print("-------------------------------------------------")
        
    def __repr__(self):
        return f"Airport({self.city}, Planes: {len(self.planes)})"


class Airplane:
    """
    Представляет самолет.
    """
    id_counter: int = 100

    def __init__(self, company: 'Airline', current_location: 'Airport'):
        """
        Инициализирует самолет.
        :param company: Авиакомпания, которой принадлежит самолет.
        :param current_location: Аэропорт текущего местоположения.
        """
        self.id: int = Airplane.id_counter
        Airplane.id_counter += 1
        self.company: 'Airline' = company
        self.current_location: 'Airport' = current_location
        self.next_flights: List['Flight'] = []
        
        # Добавляем самолет в список самолетов авиакомпании и в аэропорт
        company.planes.append(self)
        current_location.add_plane(self)

    def fly(self, destination: 'Airport'):
        """
        Заставляет самолет взлететь и приземлиться, если запланирован рейс.
        
        :param destination: Аэропорт назначения.
        """
        now = datetime.datetime.now().date()
        
        # Ищем следующий запланированный рейс, который соответствует сегодняшнему дню и месту назначения
        target_flight = None
        
        # Проверяем только рейсы, запланированные на сегодня, чтобы соблюсти правило "один полет в день"
        for flight in self.next_flights:
            if flight.date.date() == now and flight.destination is destination and flight.origin is self.current_location:
                target_flight = flight
                break
        
        if target_flight:
            print(f"\n--- Полет самолета {self.id} ({self.company.id}) ---")
            print(f"Flight ID: {target_flight.id}")
            target_flight.take_off()
            
            # Имитация времени полета
            # В реальной системе это должно быть отдельное событие
            print(f"  ... В полете к {destination.city}...")
            
            target_flight.land()
            print(f"--- Полет завершен ---")
        else:
            print(f"WARNING: No flight scheduled for {self.current_location.city} to {destination.city} today ({now}).")

    def location_on_date(self, date: datetime.date) -> Optional['Airport']:
        """
        Возвращает местоположение самолета на заданную дату.
        
        :param date: Дата для проверки.
        :return: Объект Airport или None, если местоположение неизвестно.
        """
        last_known_location = self.current_location
        
        for flight in self.next_flights:
            flight_date = flight.date.date()
            if flight_date < date:
                # Считаем, что самолет достиг места назначения в день полета
                last_known_location = flight.destination
            elif flight_date == date:
                # В день полета самолет находится в аэропорту вылета до момента вылета
                return flight.origin 
            elif flight_date > date:
                # Если следующий полет позже, он все еще находится в последнем известном месте
                return last_known_location
        
        # Если нет будущих рейсов, он остается в последнем известном месте
        return last_known_location

    def available_on_date(self, date: datetime.date, location: 'Airport') -> bool:
        """
        Проверяет, может ли самолет лететь из заданного места в заданную дату.
        
        :param date: Дата полета (datetime.date).
        :param location: Аэропорт вылета.
        :return: True, если самолет может лететь, False в противном случае.
        """
        # 1. Проверка: Один полет в день?
        for flight in self.next_flights:
            if flight.date.date() == date:
                # Уже есть полет, запланированный на эту дату
                return False

        # 2. Проверка: Где самолет будет находиться в эту дату?
        if self.location_on_date(date) is location:
            return True
        else:
            return False

    def __repr__(self):
        return f"Airplane(ID: {self.id}, Company: {self.company.id}, Location: {self.current_location.city})"


class Flight:
    """
    Представляет запланированный или завершенный рейс.
    """
    def __init__(self, date: datetime.datetime, destination: 'Airport', origin: 'Airport', plane: 'Airplane', airline: 'Airline'):
        """
        Инициализирует рейс.
        :param date: Дата и время вылета (datetime.datetime).
        :param destination: Аэропорт назначения.
        :param origin: Аэропорт отправления.
        :param plane: Используемый самолет.
        :param airline: Авиакомпания.
        """
        self.date: datetime.datetime = date
        self.destination: 'Airport' = destination
        self.origin: 'Airport' = origin
        self.plane: 'Airplane' = plane
        self.airline: 'Airline' = airline
        
        # ID: [OriginCityCode][AirlineCode][DateString]
        date_str = date.strftime("%Y%m%d")
        self.id: str = f"{origin.city}{airline.id}{date_str}"

    def take_off(self):
        """Удаляет самолет из списка припаркованных самолетов аэропорта отправления."""
        print(f"  [Take Off] Flight {self.id} departing from {self.origin.city}...")
        self.origin.remove_plane(self.plane)

    def land(self):
        """
        Изменяет местоположение самолета и добавляет его в список 
        припаркованных самолетов аэропорта назначения.
        """
        # 1. Обновляем местоположение самолета
        self.plane.current_location = self.destination
        
        # 2. Добавляем самолет в новый аэропорт
        self.destination.add_plane(self.plane)
        
        # 3. Удаляем рейс из списка будущих рейсов самолета
        if self in self.plane.next_flights:
            self.plane.next_flights.remove(self)
            
        print(f"  [Land] Flight {self.id} arrived at {self.destination.city}. Plane {self.plane.id} is now located there.")

    def __repr__(self):
        return f"Flight(ID: {self.id}, Date: {self.date.strftime('%Y-%m-%d %H:%M')}, Route: {self.origin.city} -> {self.destination.city}, Plane: {self.plane.id})"


# --- ТЕСТОВЫЙ КОД ---

def test_air_management_system():
    # 1. Инициализация сущностей
    print("--- Инициализация системы ---")
    
    # Авиакомпании
    delta = Airline("DL", "Delta Airlines")
    united = Airline("UA", "United Airlines")

    # Аэропорты
    jfk = Airport("JFK", "New York")
    lax = Airport("LAX", "Los Angeles")
    mia = Airport("MIA", "Miami")
    
    # Самолеты
    plane_dl1 = Airplane(delta, jfk)
    plane_dl2 = Airplane(delta, jfk)
    plane_ua1 = Airplane(united, lax)
    
    print(f"Planes at JFK: {[p.id for p in jfk.planes]}") # Ожидается [100, 101]
    print(f"Planes at LAX: {[p.id for p in lax.planes]}") # Ожидается [102]

    # Даты для планирования
    today = datetime.datetime.now().date()
    tomorrow = today + datetime.timedelta(days=1)
    day_after_tomorrow = today + datetime.timedelta(days=2)
    
    dt_today_pm = datetime.datetime.combine(today, datetime.time(15, 0))
    dt_tomorrow_am = datetime.datetime.combine(tomorrow, datetime.time(9, 30))
    dt_tomorrow_pm = datetime.datetime.combine(tomorrow, datetime.time(18, 0))
    dt_day_after_am = datetime.datetime.combine(day_after_tomorrow, datetime.time(10, 0))

    # 2. Планирование рейсов
    print("\n--- Планирование рейсов (schedule_flight) ---")
    
    # Рейс 1: DL из JFK сегодня
    f1 = jfk.schedule_flight(lax, dt_today_pm, delta)
    
    # Рейс 2: UA из LAX завтра
    f2 = lax.schedule_flight(jfk, dt_tomorrow_am, united)
    
    # Рейс 3: DL из JFK завтра
    f3 = jfk.schedule_flight(mia, dt_tomorrow_pm, delta)
    
    # Рейс 4: DL из LAX послезавтра (будет использовать самолет 100, если f1 завершится)
    f4 = lax.schedule_flight(jfk, dt_day_after_am, delta) # Должен провалиться, т.к. plane_dl2 в JFK, а plane_dl1 в полете

    print("\n--- Проверка доступности и местоположения ---")
    
    # Plane 100 (DL1): JFK -> LAX сегодня.
    print(f"DL1 available for JFK tomorrow? {plane_dl1.available_on_date(tomorrow, jfk)}") # False (Будет в LAX)
    print(f"DL1 available for LAX tomorrow? {plane_dl1.available_on_date(tomorrow, lax)}") # True (Но уже занят f3) - ОШИБКА: f3 из JFK.
    print(f"DL1 location on {tomorrow}: {plane_dl1.location_on_date(tomorrow)}") # Ожидается LAX
    
    # Проверка ограничения "один полет в день"
    print(f"Attempting to schedule another DL flight from JFK today (plane DL2):")
    jfk.schedule_flight(mia, dt_today_pm, delta) # Ожидается, что не найдет самолет, т.к. DL1 занят, а DL2 остается доступным
    
    # 3. Вывод расписания
    jfk.info(today, day_after_tomorrow)

    # 4. Имитация полета (fly)
    print("\n--- Имитация полетов (fly) ---")
    
    # Имитация полета f1 (JFK -> LAX)
    if f1:
        plane_dl1.fly(lax)
    
    print(f"Plane {plane_dl1.id} current location after flight: {plane_dl1.current_location.city}") # Ожидается LAX
    print(f"Planes at JFK after departure: {[p.id for p in jfk.planes]}") # Ожидается [101]
    print(f"Planes at LAX after arrival: {[p.id for p in lax.planes]}") # Ожидается [102, 100]
    
    # Имитация полета f2 (LAX -> JFK) - должен провалиться, т.к. это завтра
    plane_ua1.fly(jfk)
    
    # Проверка, что рейс f4 может быть запланирован сейчас, если бы DL1 был доступен
    print(f"\nDL1 location on {day_after_tomorrow}: {plane_dl1.location_on_date(day_after_tomorrow)}") # Ожидается MIA, т.к. f3 запланирован
    
if __name__ == "__main__":
    test_air_management_system()