def TupleRemove(Tuple, line):
    if line in Tuple:
        Tuple = tuple(filter(lambda x: x != line, Tuple))
    print(Tuple)


if __name__ == "__main__":
    line = input("Входные данные: ")
    inputList = [int(k) for k in line if k.isdigit()]
    if inputList:
        lastElement = inputList.pop()
        TupleRemove(inputList, lastElement)
    else:
        print("Введенные данные не содержат цифр.")
