import logging

logger = logging.getLogger(__name__)


def request_number(prompt):
    while True:
        try:
            text = input(prompt)
            if text.strip().lower() == "exit":
                logger.info("Користувач ввів команду exit")
                return None
            number = float(text)
            logger.info("Введено число: %s", number)
            return number
        except ValueError:
            logger.error("Некоректне введення числа: %r", text)
            print("Помилка: потрібно ввести число.")
        except (EOFError, KeyboardInterrupt):
            logger.warning("Введення перервано користувачем")
            print("\nВведення перервано.")
            return None


def request_operation(available):
    symbols = ", ".join(available)
    while True:
        operation = input(f"Введіть операцію ({symbols}): ").strip()
        if operation in available:
            logger.info("Обрано операцію: %s", operation)
            return operation
        logger.error("Невідома операція: %r", operation)
        print("Помилка: невідома операція.")


def perform_operation(available, operation, a, b):
    logger.info("Виконується: %s %s %s", a, operation, b)
    result = available[operation](a, b)
    if result is None:
        logger.warning("Операція %s %s %s не має результату", a, operation, b)
    else:
        logger.info("Результат: %s %s %s = %s", a, operation, b, result)
        print(f"Результат: {a} {operation} {b} = {result}")
