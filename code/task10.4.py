def debug_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Вызывается функция: {func.__name__}")
        print(f"Аргументы: {args}, Ключевые аргументы: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

# Пример использования декоратора
@debug_decorator
def multiply(a, b):
    return a * b

@debug_decorator
def greet(name):
    return f"Привет, {name}!"

# Тесты
multiply_result = multiply(3, 4)
greet_result = greet("Анна")
