def TupleRemove(Tuple, line):
    if Tuple.count(line) >= 2:
        startIndex = Tuple.index(line)
        endIndex = Tuple.index(line, 2) + 1
        myTuple = Tuple[startIndex:endIndex]
        print(tuple(myTuple))
    elif line in Tuple:
        startIndex = Tuple.index(line)
        myTuple = Tuple[startIndex:]
        print(tuple(myTuple))
    else:
        print(tuple())


if __name__ == "__main__":
    line = input("Входные данные: ")

    inputList = [int(k) for k in line if k.isdigit()]

    if inputList:
        last_element = inputList.pop()
        TupleRemove(inputList, last_element)
    else:
        print("Введенные данные не содержат цифр.")
