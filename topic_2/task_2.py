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

if operation == "1":
    print("Результат:", add(a, b))
elif operation == "2":
    print("Результат:", subtract(a, b))
elif operation == "3":
    print("Результат:", multiply(a, b))
elif operation == "4":
    print("Результат:", divide(a, b))
else:
    print("Помилка: невідома операція!")
