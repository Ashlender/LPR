a = int(input("Затраты на проезд: "))
b = int(input("Затраты на питание: "))
c = int(input("Затраты на квартиру: "))
total = a + b + c

with open("task2.txt", "w") as file:
    file.write(f"Итого: Проезд: {a} р. Питание: {b} р. Квартира: {c} р. Всего: {total} р.")

print(f"Итого: Проезд: {a} р. Питание: {b} р. Квартира: {c} р. Всего: {total} р.")
