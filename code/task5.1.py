from task5 import area

def get_user_input():
    a = float(input("Введите длину стороны 'a': "))
    b = float(input("Введите длину стороны 'b': "))
    c = float(input("Введите длину стороны 'c': "))
    return a, b, c

if __name__ == "__main__":
    a, b, c = get_user_input()
    if a + b > c and a + c > b and b + c > a:
        area = area(a, b, c)
        print(f"Площадь треугольника: {area:.2f}")
    else:
        print("Треугольник с такими сторонами не существует.")