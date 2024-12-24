# Импорт необходимых модулей
import xmlrpc.client

# Создание прокси для сервера
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Определение функций для обращения к серверу
def perform_operation(operation, num1, num2):
    try:
        if operation == 1:
            result = proxy.add(num1, num2)
        elif operation == 2:
            result = proxy.subtract(num1, num2)
        elif operation == 3:
            result = proxy.multiply(num1, num2)
        elif operation == 4:
            result = proxy.divide(num1, num2)
        else:
            return "Неверный номер операции"
        return result
    except Exception as e:
        return f"Ошибка при выполнении операции: {e}"

# Основная функция
def main():
    while True:
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("X. Выйти из программы")
        choice = input("Введите номер операции (или X для выхода): ")
        if choice.lower() == 'x':
            print("Выход из программы...")
            break
        try:
            choice = int(choice)
            if choice in [1, 2, 3, 4]:
                num1 = input("Введите первую дробь в формате числитель/знаменатель: ")
                num2 = input("Введите вторую дробь в формате числитель/знаменатель: ")
                result = perform_operation(choice, num1, num2)
                print(f"Результат операции: {result}")
            else:
                print("Неверный номер операции. Пожалуйста, выберите от 1 до 4 или X для выхода.")
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите номер операции или X для выхода.")
        except Exception as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
