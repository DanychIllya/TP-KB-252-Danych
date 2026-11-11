import logging
import os

from calculator import Calculator

LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "calc.log")


class CalculatorApp:

    def __init__(self, calculator):
        self.calculator = calculator

    def request_number(self, prompt):
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

    def request_operation(self):
        symbols = ", ".join(self.calculator.symbols)
        while True:
            symbol = input(f"Введіть операцію ({symbols}): ").strip()
            if self.calculator.has_operation(symbol):
                return symbol
            print("Помилка: невідома операція.")

    def run(self):
        print("Калькулятор. Для завершення введіть exit замість числа.")
        while True:
            a = self.request_number("Введіть перше число: ")
            if a is None:
                break
            symbol = self.request_operation()
            b = self.request_number("Введіть друге число: ")
            if b is None:
                break
            try:
                result = self.calculator.calculate(a, symbol, b)
                print(f"Результат: {a} {symbol} {b} = {result}")
            except ZeroDivisionError as error:
                print(f"Помилка: {error}.")

        print("\nІсторія обчислень:")
        for record in self.calculator.history:
            print(" ", record)
        print("Роботу завершено.")


def main():
    logging.basicConfig(
        filename=LOG_FILE,
        encoding="utf-8",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
    )
    CalculatorApp(Calculator()).run()


if __name__ == "__main__":
    main()
