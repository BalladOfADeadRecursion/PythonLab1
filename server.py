# Импорт необходимых модулей
from xmlrpc.server import SimpleXMLRPCServer
from fractions import Fraction

# Серверные функции
def add(num1, num2):
    frac1 = Fraction(num1)
    frac2 = Fraction(num2)
    result = frac1 + frac2
    return str(result)

def subtract(num1, num2):
    frac1 = Fraction(num1)
    frac2 = Fraction(num2)
    result = frac1 - frac2
    return str(result)

def multiply(num1, num2):
    frac1 = Fraction(num1)
    frac2 = Fraction(num2)
    result = frac1 * frac2
    return str(result)

def divide(num1, num2):
    frac1 = Fraction(num1)
    frac2 = Fraction(num2)
    result = frac1 / frac2
    return str(result)

# Создание сервера
server = SimpleXMLRPCServer(("localhost", 8000))
print("Сервер запущен на порту 8000...")

# Регистрация функций
server.register_function(add, 'add')
server.register_function(subtract, 'subtract')
server.register_function(multiply, 'multiply')
server.register_function(divide, 'divide')

# Запуск сервера
server.serve_forever()
