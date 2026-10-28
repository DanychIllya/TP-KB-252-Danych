def discriminant(a, b, c):
    return b ** 2 - 4 * a * c
 
 
if __name__ == "__main__":
    a = float(input("Введіть a: "))
    b = float(input("Введіть b: "))
    c = float(input("Введіть c: "))
 
    d = discriminant(a, b, c)
    print("Дискримінант D =", d)
 
    if d > 0:
        print("Рівняння має два дійсні корені.")
    elif d == 0:
        print("Рівняння має один дійсний корінь.")
    else:
        print("Дійсних коренів немає.")
