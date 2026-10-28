def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def request_data():
    """Запитує в користувача два числа та операцію.
    Повертає кортеж (a, operation, b) або None, якщо введення завершено."""
    while True:
        try:
            first = input("Введіть перше число (exit - вихід): ")
            if first.strip().lower() == "exit":
                return None
            a = float(first)

            operation = input("Введіть операцію (+, -, *, /): ").strip()
            if operation not in OPERATIONS:
                raise KeyError(operation)

            second = input("Введіть друге число: ")
            b = float(second)

            return a, operation, b
        except ValueError:
            print("Помилка: потрібно ввести число, наприклад 5 або 3.14.")
        except KeyError as error:
            print(f"Помилка: невідома операція {error}. Доступні: +, -, *, /.")
        except (EOFError, KeyboardInterrupt):
            print("\nВведення перервано.")
            return None


def main():
    print("Калькулятор. Для завершення введіть exit замість першого числа.")
    while True:
        data = request_data()
        if data is None:
            break
        a, operation, b = data
        try:
            result = OPERATIONS[operation](a, b)
            print(f"Результат: {a} {operation} {b} = {result}")
        except ZeroDivisionError:
            print("Помилка: ділення на нуль.")
    print("Роботу завершено.")


main()
