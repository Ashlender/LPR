from math import sqrt

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

def Formula(a, b, c):
    p = (a + b + c) / 2
    S = sqrt(p * (p - a) * (p - b) * (p - c))
    return S

resOne = Formula(max(one), max(two), max(three))
resTwo = Formula(min(one), min(two), min(three))

maximum = (max(one), max(two), max(three))
minimum = (min(one), min(two), min(three))

print(f"S первого треугольника: {resOne}")
print(f"S второго треугольника: {resTwo}")
print(f"Максимальные стороны: {maximum}")
print(f"Минимальные стороны: {minimum}")