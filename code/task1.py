line = input("Введите числа: ")
List = [int(num) for num in line.split()]
Tuple = tuple(List)
print(f"Список: {List} \nКортеж: {Tuple}")
