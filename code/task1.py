import re

path = "task1.txt"
with open(path, "r") as file:
    txt = re.findall(r'\w+', file.read())

print(f"Количество слов в статье: {len(txt)}\n"
      f"Самое распространённое слово: {max(set(txt), key=txt.count)}. "
      f"Встречается {txt.count('и')} раз")
