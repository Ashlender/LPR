def sum_of_numb(numbers):

    return sum(num for num in numbers if num % 2 == 0)

numb = input("Введите список целых чисел через пробел: ")
numbers = [int(num) for num in numb.split()]
result = sum_of_numb(numbers)
print(f"Сумма четных чисел в списке {numbers}: {result}")
