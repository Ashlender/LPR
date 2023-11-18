data = input("Введите числа: ")

numb = list(map(float, data.split()))

avg = sum(numb) / len(numb)

result_text = f"Среднее значение: {avg:.2f}.\n"
if avg > 100:
    result_text += "Более 100"

with open("task5.txt", "w") as file:
    file.write(result_text)

print("Результат записан в файл")
