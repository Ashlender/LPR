x = input("Введите предложение: ")

with open("task4.txt", "r") as file:
    txt = file.read().split()

for zap in txt:
    ct = len(zap) * '*'
    x = x.lower().replace(zap.lower(), ct)
print(x)
