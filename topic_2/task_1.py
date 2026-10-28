import math

def discriminant(a, b, c):
    return b**2 - 4*a*c

def sqrt(a, b, c):
    if a == 0:
        print("Це не квадратне рівняння")
        return

    D = discriminant(a, b, c)

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print("Два корені:", x1, "і", x2)
    elif D == 0:
        x = -b / (2*a)
        print("Один корінь:", x)
    else:
        print("Дійсних коренів немає")

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
c = float(input("Введіть c: "))

sqrt(a, b, c)
