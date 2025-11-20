# Exercise 1 : Temperature

import abc
import sys

# --- Базовый класс (Абстрактный класс) ---
# Он устанавливает интерфейс, которому должны следовать все наследники (Принцип LSP)

class Temperature(abc.ABC):
    """
    Абстрактный базовый класс для всех шкал температур.
    Определяет необходимый интерфейс конвертации.
    """
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Значение температуры должно быть числом.")
        self.value = value

    @abc.abstractmethod
    def to_celsius(self):
        """Конвертирует температуру в Цельсий."""
        pass

    @abc.abstractmethod
    def to_kelvin(self):
        """Конвертирует температуру в Кельвин."""
        pass

    @abc.abstractmethod
    def to_fahrenheit(self):
        """Конвертирует температуру в Фаренгейт."""
        pass

# --- Подклассы (Конкретные реализации) ---
# Каждый класс отвечает только за конвертацию ИЗ СВОЕЙ шкалы (Принцип SRP)

class Celsius(Temperature):
    """
    Класс для работы со шкалой Цельсия.
    """
    def to_celsius(self):
        return self.value

    def to_kelvin(self):
        return self.value + 273.15

    def to_fahrenheit(self):
        return (self.value * 9/5) + 32

class Kelvin(Temperature):
    """
    Класс для работы со шкалой Кельвина.
    """
    def to_celsius(self):
        return self.value - 273.15

    def to_kelvin(self):
        return self.value

    def to_fahrenheit(self):
        # (K - 273.15) * 9/5 + 32
        return (self.value - 273.15) * 9/5 + 32

class Fahrenheit(Temperature):
    """
    Класс для работы со шкалой Фаренгейта.
    """
    def to_celsius(self):
        # (F - 32) * 5/9
        return (self.value - 32) * 5/9

    def to_kelvin(self):
        # ((F - 32) * 5/9) + 273.15
        return (self.value - 32) * 5/9 + 273.15

    def to_fahrenheit(self):
        return self.value

# --- Демонстрация использования ---

def main():
    print("--- Демонстрация конвертера температур ---")
    
    # 1. Температура в Цельсиях (температура кипения воды)
    c_temp = Celsius(100.0)
    print("\nИсходная температура: 100.0 °C")
    print(f"  В Кельвинах: {c_temp.to_kelvin():.2f} K")
    print(f"  В Фаренгейтах: {c_temp.to_fahrenheit():.2f} °F")

    # 2. Температура в Кельвинах (абсолютный ноль)
    k_temp = Kelvin(0.0)
    print("\nИсходная температура: 0.0 K (Абсолютный ноль)")
    print(f"  В Цельсиях: {k_temp.to_celsius():.2f} °C")
    print(f"  В Фаренгейтах: {k_temp.to_fahrenheit():.2f} °F")

    # 3. Температура в Фаренгейтах (температура тела)
    f_temp = Fahrenheit(98.6)
    print("\nИсходная температура: 98.6 °F (Нормальная температура тела)")
    print(f"  В Цельсиях: {f_temp.to_celsius():.2f} °C")
    print(f"  В Кельвинах: {f_temp.to_kelvin():.2f} K")
    
if __name__ == "__main__":
    try:
        main()
    except TypeError as e:
        print(f"Ошибка ввода: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

# Exercise 2: In the Quantum Realm

import random
import math
import sys

class QuantumParticle:
    """
    Моделирует квантовую частицу с позицией, импульсом и спином.
    Включает эффекты возмущения при измерении и квантовую запутанность.
    """
    
    # Константы для диапазона измерений
    MIN_POS = 1
    MAX_POS = 10000
    MIN_MOMENTUM = 0.0
    MAX_MOMENTUM = 1.0
    
    def __init__(self, x=None, y=None, p=None):
        """
        Инициализирует частицу со случайными или заданными начальными значениями.
        
        Args:
            x (int/float, optional): Начальная позиция.
            y (int/float, optional): Начальный импульс.
            p (float, optional): Начальный спин (1/2 или -1/2).
        """
        # Инициализация с заданными или случайными значениями
        self._position = x if x is not None else random.randint(self.MIN_POS, self.MAX_POS)
        self._momentum = y if y is not None else random.uniform(self.MIN_MOMENTUM, self.MAX_MOMENTUM)
        self._spin = p if p is not None else random.choice([0.5, -0.5])
        
        # Атрибут для хранения ссылки на запутанного партнера
        self._entangled_partner = None

    def __repr__(self):
        """
        Реализует осмысленное строковое представление частицы.
        """
        entangled_status = (
            f", Запутан с {self._entangled_partner.name}" 
            if self._entangled_partner else ""
        )
        return (
            f"<QuantumParticle: Позиция={self._position:.2f}, "
            f"Импульс={self._momentum:.2f}, Спин={self._spin:.1f}{entangled_status}>"
        )

    def _disturb(self):
        """
        Реализует возмущение, происходящее при каждом измерении.
        Случайным образом изменяет позицию и импульс.
        """
        # Возмущение позиции: новое случайное целое число
        self._position = random.randint(self.MIN_POS, self.MAX_POS)
        # Возмущение импульса: новое случайное число с плавающей точкой
        self._momentum = random.uniform(self.MIN_MOMENTUM, self.MAX_MOMENTUM)
        
        print('Quantum Interferences!!')

    def position(self):
        """
        Измерение позиции. Вызывает возмущение.
        Возвращает новое (измеренное) значение позиции.
        """
        self._disturb()
        # Позиция после возмущения - это и есть результат измерения
        return self._position

    def momentum(self):
        """
        Измерение импульса. Вызывает возмущение.
        Возвращает новое (измеренное) значение импульса.
        """
        self._disturb()
        # Импульс после возмущения - это и есть результат измерения
        return self._momentum

    def spin(self):
        """
        Измерение спина. Вызывает возмущение и реализует запутанность.
        Возвращает новое (измеренное) значение спина.
        """
        self._disturb()
        
        # 1. Генерируем случайный спин для текущей частицы
        new_spin = random.choice([0.5, -0.5])
        self._spin = new_spin

        # 2. Если частица запутана, обновляем спин партнера на противоположный
        if self._entangled_partner:
            partner = self._entangled_partner
            
            # Спин партнера должен быть противоположным (self._spin * -1)
            partner._spin = self._spin * -1 
            
            print('Spooky Action at a Distance !!')
        
        return self._spin
    
    def entangle(self, partner):
        """
        Устанавливает квантовую запутанность между двумя частицами.
        
        Args:
            partner (QuantumParticle): Другая частица.
        """
        # Проверка, что партнер является экземпляром QuantumParticle
        if not isinstance(partner, QuantumParticle):
            print(f"Ошибка: Невозможно запутать частицу с объектом типа {type(partner).__name__}. Только с QuantumParticle.")
            return

        # Устанавливаем двустороннюю связь
        self._entangled_partner = partner
        partner._entangled_partner = self
        
        # Устанавливаем случайные имена для демонстрации (если они еще не установлены)
        if not hasattr(self, 'name'):
             self.name = f"P{id(self) % 100}"
        if not hasattr(partner, 'name'):
             partner.name = f"P{id(partner) % 100}"
        
        print(f"Частица {self.name} теперь в квантовой запутанности с Частицей {partner.name}")
        print('Spooky Action at a Distance !!')

# --- Демонстрация использования ---

if __name__ == "__main__":
    
    # 1. Создание и измерение одиночной частицы
    p_solo = QuantumParticle()
    p_solo.name = "P_Solo"
    
    print("=" * 40)
    print("ДЕМО 1: Измерение одиночной частицы")
    print(p_solo)
    
    print("\nИзмерение позиции P_Solo:")
    pos = p_solo.position()
    print(f"  -> Измеренная позиция: {pos}")
    print(p_solo)

    print("\nИзмерение импульса P_Solo:")
    mom = p_solo.momentum()
    print(f"  -> Измеренный импульс: {mom}")
    print(p_solo)
    
    print("\nИзмерение спина P_Solo:")
    sp = p_solo.spin()
    print(f"  -> Измеренный спин: {sp}")
    print(p_solo)
    
    # 2. Демонстрация запутанности и действия на расстоянии
    p1 = QuantumParticle(x=1, y=0.1, p=0.5)
    p2 = QuantumParticle(x=2, y=0.9, p=-0.5)
    p1.name = "P1"
    p2.name = "P2"
    
    print("\n" + "=" * 40)
    print("ДЕМО 2: Квантовая запутанность")
    print(f"Начальное состояние P1: {p1}")
    print(f"Начальное состояние P2: {p2}")

    # Запутывание
    p1.entangle(p2)
    
    # Измерение спина P1 - должно вызвать изменение спина P2
    print("\nИзмерение спина P1:")
    p1_spin_result = p1.spin()
    print(f"  -> Спин P1 измерен: {p1_spin_result}")

    # Проверяем состояние обеих частиц
    print("\nКонечное состояние:")
    print(f"  P1 (измеренный): {p1}")
    print(f"  P2 (обновленный): {p2}")
    
    # Проверка, что спины противоположны
    if p1._spin == p2._spin * -1:
        print("✅ Проверка: Спины противоположны (Запутанность сработала).")
    else:
        print("❌ Проверка: Спины не противоположны.")
        
    # Демонстрация проверки типа
    print("\nПроверка: Попытка запутать с объектом другого типа:")
    p1.entangle("Не частица")