import logging
import os

import functions
import operations

LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "calc.log")

logging.basicConfig(
    filename=LOG_FILE,
    filemode="a",
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
)
logger = logging.getLogger(__name__)

AVAILABLE_OPERATIONS = {
    "+": functions.add,
    "-": functions.subtract,
    "*": functions.multiply,
    "/": functions.divide,
}


def main():
    logger.info("Програму запущено")
    print("Калькулятор. Для завершення введіть exit замість числа.")
    print(f"Журнал дій записується у файл: {LOG_FILE}")

    while True:
        a = operations.request_number("Введіть перше число: ")
        if a is None:
            break

        operation = operations.request_operation(AVAILABLE_OPERATIONS)

        b = operations.request_number("Введіть друге число: ")
        if b is None:
            break

        operations.perform_operation(AVAILABLE_OPERATIONS, operation, a, b)

    logger.info("Програму завершено")
    print("Роботу завершено.")


if __name__ == "__main__":
    main()
