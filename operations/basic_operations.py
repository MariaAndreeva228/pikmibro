# operations/basic_operations.py
# Разработчик: Мария
# Ветка: feature/basic-operations

def add(a, b):
    """Сложение двух чисел"""
    return a + b

def subtract(a, b):
    """Вычитание двух чисел"""
    return a - b

def multiply(a, b):
    """Умножение двух чисел"""
    return a * b

def divide(a, b):
    """Деление двух чисел с проверкой на ноль"""
    if b == 0:
        raise ValueError("Ошибка: Деление на ноль невозможно!")
    return a / b

def power(a, b):
    """Возведение в степень"""
    return a ** b

if name == "main":
    # Тест базовых операций
    print("Тестирование базовых операций:")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"4 * 3 = {multiply(4, 3)}")
    print(f"10 / 2 = {divide(10, 2)}")
    print(f"2 ^ 3 = {power(2, 3)}")
    
    # Тест обработки ошибок
    try:
        divide(10, 0)
    except ValueError as e:
        print(f"Поймана ошибка: {e}")