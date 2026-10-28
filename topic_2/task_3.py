
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Помилка: ділення на нуль!"

a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

print("Виберіть операцію:")
print("1 - Додавання")
print("2 - Віднімання")
print("3 - Множення")
print("4 - Ділення")

operation = input("Ваш вибір: ")

match operation:
    case "1":
        print("Результат:", add(a, b))
    case "2":
        print("Результат:", subtract(a, b))
    case "3":
        print("Результат:", multiply(a, b))
    case "4":
        print("Результат:", divide(a, b))
    case _:
        print("Помилка: невідома операція!")
