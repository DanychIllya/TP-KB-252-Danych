import functions
import operations

AVAILABLE_OPERATIONS = {
    "+": functions.add,
    "-": functions.subtract,
    "*": functions.multiply,
    "/": functions.divide,
}


def main():
    print("Калькулятор. Для завершення введіть exit замість числа.")

    while True:
        a = operations.request_number("Введіть перше число: ")
        if a is None:
            break

        operation = operations.request_operation(AVAILABLE_OPERATIONS)

        b = operations.request_number("Введіть друге число: ")
        if b is None:
            break

        operations.perform_operation(AVAILABLE_OPERATIONS, operation, a, b)

    print("Роботу завершено.")


if __name__ == "__main__":
    main()
