def lineSequence():
    line = input("Введите последовательность чисел: ")
    while len(line) <= 15:
        print("Нужно минимум 15 символов.")
        line = input("Введите последовательность чисел: ")
    return line


def top_3(sequence):
    numbers = list(map(int, sequence))
    y = {x: numbers.count(x) for x in range(10)}
    print(y)


if __name__ == "__main__":
    user_sequence = lineSequence()
    top_3(user_sequence)
