EXIT_COMMANDS = ("exit", "quit", "q")


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


def is_number(text):
    """Перевіряє, чи можна рядок перетворити на число (без винятків)."""
    text = text.strip()
    if text.startswith("-"):
        text = text[1:]
    return text.replace(".", "", 1).isdigit()


def is_exit(text):
    return text.strip().lower() in EXIT_COMMANDS


def main():
    print("Калькулятор. Для завершення введіть exit (або quit, q).")

    while True:
        first = input("Введіть перше число: ")
        if is_exit(first):
            break
        if not is_number(first):
            print("Це не число, спробуйте ще раз.")
            continue

        operation = input("Введіть операцію (+, -, *, /): ").strip()
        if is_exit(operation):
            break
        if operation not in OPERATIONS:
            print("Невідома операція, спробуйте ще раз.")
            continue

        second = input("Введіть друге число: ")
        if is_exit(second):
            break
        if not is_number(second):
            print("Це не число, спробуйте ще раз.")
            continue

        a, b = float(first), float(second)
        if operation == "/" and b == 0:
            print("Ділити на нуль не можна.")
            continue

        result = OPERATIONS[operation](a, b)
        print(f"Результат: {a} {operation} {b} = {result}")

    print("Роботу калькулятора завершено.")


main()
