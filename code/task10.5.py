class CustomException(Exception):
    def __init__(self, message="Произошла ошибка"):
        self.message = message
        super().__init__(self.message)



def function_one(value):
    try:
        if value < 0:
            raise CustomException("Значение не может быть отрицательным")
        else:
            print("Функция one выполнилась успешно")
    except CustomException as e:
        print(f"Ошибка: {e}")


def function_two():
    try:
        print("Функция two выполнилась успешно")
        # Генерация исключения
        raise CustomException("Пример ошибки в функции two")
    except CustomException as e:
        print(f"Ошибка: {e}")

# Тесты
function_one(5)     # Выполнится успешно
function_one(-3)    # Вызовет исключение
function_two()      # Вызовет исключение
