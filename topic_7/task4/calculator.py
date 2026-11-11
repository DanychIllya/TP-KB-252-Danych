import logging

from operations import Add, Subtract, Multiply, Divide

logger = logging.getLogger(__name__)


class Calculator:
    def __init__(self, operations=None):
        self._operations = {}
        self.history = []
        for operation in operations or [Add(), Subtract(), Multiply(), Divide()]:
            self.register(operation)

    def register(self, operation):
        """Додає операцію до калькулятора (можна додати власну)."""
        self._operations[operation.symbol] = operation

    @property
    def symbols(self):
        return list(self._operations)

    def has_operation(self, symbol):
        return symbol in self._operations

    def calculate(self, a, symbol, b):
        """Виконує обчислення, записує його в історію та журнал."""
        if symbol not in self._operations:
            raise ValueError(f"невідома операція {symbol!r}")
        try:
            result = self._operations[symbol].execute(a, b)
        except ZeroDivisionError:
            logger.warning("Ділення на нуль: %s %s %s", a, symbol, b)
            raise
        record = f"{a} {symbol} {b} = {result}"
        self.history.append(record)
        logger.info("Обчислено: %s", record)
        return result
