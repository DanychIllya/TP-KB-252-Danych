import logging

logger = logging.getLogger(__name__)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logger.warning("Спроба ділення на нуль: %s / %s", a, b)
        print("Помилка: ділити на нуль не можна.")
        return None
