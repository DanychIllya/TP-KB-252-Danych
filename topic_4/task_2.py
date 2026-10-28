def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    """Ділить a на b. Якщо b дорівнює нулю, повідомляє про помилку
    та повертає None."""
    try:
        return a / b
    except ZeroDivisionError:
        print("Помилка: ділити на нуль не можна.")
        return None


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def request_number(prompt):
    """Запитує число, доки користувач не введе коректне значення.
    Повертає None, якщо користувач ввів exit."""
    while True:
        try:
            text = input(prompt)
            if text.strip().lower() == "exit":
                return None
            return float(text)
        except ValueError:
            print("Помилка: потрібно ввести число.")
        except (EOFError, KeyboardInterrupt):
            print("\nВведення перервано.")
            return None


def main():
    print("Калькулятор. Для завершення введіть exit замість числа.")
    while True:
        a = request_number("Введіть перше число: ")
        if a is None:
            break

        operation = input("Введіть операцію (+, -, *, /): ").strip()
        if operation not in OPERATIONS:
            print("Помилка: невідома операція.")
            continue

        b = request_number("Введіть друге число: ")
        if b is None:
            break

        result = OPERATIONS[operation](a, b)
        if result is not None:
            print(f"Результат: {a} {operation} {b} = {result}")
    print("Роботу завершено.")


main()
