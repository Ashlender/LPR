# Импорт необходимых модулей
from datetime import datetime  # Импорт класса datetime из модуля datetime
from math import sqrt  # Импорт функции sqrt из модуля math

# Определение функции main с использованием параметров kwargs
def main(**kwargs):
    # Проход по каждой паре ключ-значение в словаре
    for key, value in kwargs.items():
        # Вычисление квадратного корня
        result = sqrt(value[0] ** 2 + value[1] ** 2)
        # Вывод результата
        print(result)
# Этот блок кода будет выполнен только в случае, если файл запускается напрямую
if __name__ == '__main__':
    # Запись текущего времени перед выполнением функции main
    start_time = datetime.now()
    # Вызов функции main с передачей словаря аргументов
    main(
        one=[10, 3],
        two=[5, 4],
        three=[15, 13],
        four=[93, 53],
        five=[133, 15]
    )
    # Рассчет времени выполнения
    time_costs = datetime.now() - start_time
    # Вывод времени выполнения
    print(f"Время выполнения программы - {time_costs}")
