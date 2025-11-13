
git checkout dev
git pull origin dev
git checkout -b feature/user-interface

# Создает структуру файлов
mkdir -p operations
touch operations/__init__.py
# Вставляет код в calculator.py

# Затем:
git add calculator.py operations/__init__.py
git commit -m "feat: add user interface, menu system and application logic"
git push origin feature/user-interface


# calculator.py
# Разработчик: nnnn
# Ветка: feature/user-interface

from operations.basic_operations import add, subtract, multiply, divide, power
from operations.advanced_operations import (
    square_root, square, percentage, 
    factorial, logarithm, modulus
)

def display_menu():
    """Отображение главного меню калькулятора"""
    print("\n" + "="*50)
    print("           🧮 КАЛЬКУЛЯТОР v3.0")
    print("="*50)
    print("1. ➕ Базовые операции (+, -, *, /, ^)")
    print("2. 🧩 Продвинутые операции (√, x², %, !, log, mod)")
    print("3. ❌ Выход")
    print("="*50)

def display_basic_operations():
    """Отображение доступных базовых операций"""
    print("\n--- 🔧 Базовые операции ---")
    print("+ : Сложение")
    print("- : Вычитание") 
    print("* : Умножение")
    print("/ : Деление")
    print("^ : Возведение в степень")

def display_advanced_operations():
    """Отображение доступных продвинутых операций"""
    print("\n--- 🚀 Продвинутые операции ---")
    print("sqrt  : Квадратный корень")
    print("square: Квадрат числа")
    print("%     : Процент от числа")
    print("fact  : Факториал")
    print("log   : Логарифм")
    print("mod   : Остаток от деления")

def get_number_input(prompt):
    """Безопасный ввод числа с обработкой ошибок"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Ошибка: Пожалуйста, введите корректное число!")

def get_integer_input(prompt):
    """Безопасный ввод целого числа для факториала"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Ошибка: Пожалуйста, введите целое число!")

def handle_basic_operations():
    """Обработка базовых операций калькулятора"""
    display_basic_operations()
    
    operation = input("\nВыберите операцию: ").strip()
    
    if operation not in ['+', '-', '*', '/', '^']:
        print("❌ Неизвестная операция!")
        return
    
    try:
        num1 = get_number_input("Введите первое число: ")
        
        if operation == '^':
            num2 = get_number_input("Введите степень: ")
        else:
            num2 = get_number_input("Введите второе число: ")
        
        result = None
        operation_symbol = operation
        
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        elif operation == '^':
            result = power(num1, num2)
            operation_symbol = '^'
        
        print(f"✅ Результат: {num1} {operation_symbol} {num2} = {result}")
        
    except ValueError as e:
        print(f"❌ Ошибка: {e}")
    except Exception as e:
        print(f"❌ Неожиданная ошибка: {e}")

def handle_advanced_operations():
    """Обработка продвинутых операций калькулятора"""
    display_advanced_operations()
    
    operation = input("\nВыберите операцию: ").strip().lower()
    
    if operation not in ['sqrt', 'square', '%', 'fact', 'log', 'mod']:
        print("❌ Неизвестная операция!")
        return
    
    try:
        if operation in ['sqrt', 'square', 'fact']:
            # Унарные операции (требуют одно число)
            if operation == 'fact':
                num1 = get_integer_input("Введите целое число: ")
            else:
                num1 = get_number_input("Введите число: ")
            
            if operation == 'sqrt':
                result = square_root(num1)
                print(f"✅ Результат: √{num1} = {result}")
            elif operation == 'square':
                result = square(num1)
                print(f"✅ Результат: {num1}² = {result}")
            elif operation == 'fact':
                result = factorial(num1)
                print(f"✅ Результат: {num1}! = {result}")
                
        else:
            # Бинарные операции (требуют два числа)
            num1 = get_number_input("Введите первое число: ")
            
            if operation == '%':
                percent = get_number_input("Введите процент: ")
                result = percentage(num1, percent)
                print(f"✅ Результат: {percent}% от {num1} = {result}")
            elif operation == 'log':
                base_input = input("Введите основание логарифма (по умолчанию 10): ").strip()
                base = float(base_input) if base_input else 10
                result = logarithm(num1, base)
                print(f"✅ Результат: log{base}({num1}) = {result}")
            elif operation == 'mod':
                num2 = get_number_input("Введите второе число: ")
                result = modulus(num1, num2)
                print(f"✅ Результат: {num1} mod {num2} = {result}")
        
    except ValueError as e:
        print(f"❌ Ошибка: {e}")
    except Exception as e:
        print(f"❌ Неожиданная ошибка: {e}")

def show_welcome_message():
    """Показать приветственное сообщение"""
    print("="*60)
    print("           🎉 Добро пожаловать в Калькулятор v3.0!")
    print("="*60)
    print("Этот калькулятор разработан командой из 3 разработчиков:")
    print("• Алексей - базовые операции")
    print("• Мария   - продвинутые операции") 
    print("• Иван    - пользовательский интерфейс")
    print("="*60)

def main():
    """Главная функция приложения"""
    show_welcome_message()
    
    while True:
        display_menu()
        choice = input("Выберите опцию (1-3): ").strip()
        
        if choice == '1':
            handle_basic_operations()
        elif choice == '2':
            handle_advanced_operations()
        elif choice == '3':
            print("\n👋 До свидания! Спасибо за использование калькулятора!")
            break
        else:
            print("❌ Неверный выбор! Пожалуйста, выберите 1, 2 или 3.")
        
        # Пауза перед следующим шагом
        input("\nНажмите Enter для продолжения...")

# Точка входа в программу
if name == "main":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Программа прервана пользователем. До свидания!")
    except Exception as e:
        print(f"\n❌ Критическая ошибка: {e}")