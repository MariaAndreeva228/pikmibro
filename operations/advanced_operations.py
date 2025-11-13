

import math

def square_root(a):
    """Квадратный корень числа"""
    if a < 0:
        raise ValueError("Ошибка: Невозможно извлечь корень из отрицательного числа!")
    return math.sqrt(a)

def square(a):
    """Квадрат числа"""
    return a ** 2

def percentage(a, b):
    """Процент от числа: a * b / 100"""
    return (a * b) / 100

def factorial(a):
    """Факториал числа"""
    if a < 0:
        raise ValueError("Ошибка: Факториал отрицательного числа не определен!")
    if not isinstance(a, int):
        a = int(a)  # Преобразуем в целое число для факториала
    if a == 0:
        return 1
    return math.factorial(a)

def logarithm(a, base=10):
    """Логарифм числа по основанию"""
    if a <= 0:
        raise ValueError("Ошибка: Логарифм определен только для положительных чисел!")
    if base <= 0 or base == 1:
        raise ValueError("Ошибка: Основание логарифма должно быть положительным и не равным 1!")
    return math.log(a, base)

def modulus(a, b):
    """Остаток от деления"""
    if b == 0:
        raise ValueError("Ошибка: Деление на ноль в операции остатка!")
    return a % b

# Тестирование функций (можно удалить в финальной версии)
if __name__ == "__main__":
    print("Тестирование продвинутых операций:")
    print(f"√25 = {square_root(25)}")
    print(f"5² = {square(5)}")
    print(f"20% от 150 = {percentage(150, 20)}")
    print(f"5! = {factorial(5)}")
    print(f"log₁₀(100) = {logarithm(100, 10)}")
    print(f"10 % 3 = {modulus(10, 3)}")
    
    # Тест обработки ошибок
    try:
        square_root(-4)
    except ValueError as e:
        print(f"Поймана ошибка: {e}")