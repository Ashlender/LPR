from datetime import datetime  # Импорт класса datetime из модуля datetime
from math import sqrt  # Импорт функции sqrt из модуля math

# Определение функции main с использованием параметров словаря
def main(**kwargs): # Проход по каждой паре в словаре kwargs
    for key, value in kwargs.items():
        result = sqrt(value[0] ** 2 + value[1] ** 2) # Вычисление квадратного корня
        print(result) # вывод

if __name__ == '__main__':
    start_time = datetime.now() # текущее время
    main( # Вызов main с передачей словаря
        one=[10, 3],
        two=[5, 4],
        three=[15, 13],
        four=[93, 53],
        five=[133, 15]
    )
    time_costs = datetime.now() - start_time # рассчет время выполнения
    print(f"Время выполнения программы - {time_costs}") # время выполнения программы