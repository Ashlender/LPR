def calculate_average(*args):
    if not args:
        return 0
    total = sum(args)
    average = total / len(args)
    return average

if __name__ == "__main__":
    user_input = input("Введите числа: ")
    numbers = [float(num) for num in user_input.split()]
    result = calculate_average(*numbers)
    print(f"Среднее арифметическое: {result}")


