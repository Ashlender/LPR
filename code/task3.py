import re

with open("task3.txt", "w") as file:
    file.write(f"Beautiful is better than ugly. \n"
               f"Explicit is better than implicit. \n"
               f"Simple is better than complex. \n"
               f"Complex is better than complicated.")

with open("task3.txt", "r") as file:
    lines = len(file.readlines())

with open("task3.txt", "r") as file:
    content = file.read().replace('\n', '')
    words = len(re.findall(r'\b\w+\b', content))
    letters = len(re.sub(r'[^a-zA-Z]', '', content))

print(f"Input file contains: {letters} letters, {words} words, {lines} lines.")
