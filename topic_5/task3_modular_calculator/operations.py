def request_number(prompt):
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


def request_operation(available):
    symbols = ", ".join(available)
    while True:
        operation = input(f"Введіть операцію ({symbols}): ").strip()
        if operation in available:
            return operation
        print("Помилка: невідома операція.")


def perform_operation(available, operation, a, b):
    result = available[operation](a, b)
    if result is not None:
        print(f"Результат: {a} {operation} {b} = {result}")
