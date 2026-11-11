from abc import ABC, abstractmethod


class Operation(ABC):

    symbol = ""

    @abstractmethod
    def execute(self, a, b):

    def __str__(self):
        return f"Операція '{self.symbol}'"


class Add(Operation):
    symbol = "+"

    def execute(self, a, b):
        return a + b


class Subtract(Operation):
    symbol = "-"

    def execute(self, a, b):
        return a - b


class Multiply(Operation):
    symbol = "*"

    def execute(self, a, b):
        return a * b


class Divide(Operation):
    symbol = "/"

    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError("ділити на нуль не можна")
        return a / b