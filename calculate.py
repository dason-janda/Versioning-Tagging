import logging

logger = logging.getLogger(__name__)


def calculate(operation, a, b):
    logger.debug("calculate called with operation=%r, a=%r, b=%r", operation, a, b)

    if not isinstance(operation, str):
        logger.warning("Invalid operation type: %s", type(operation).__name__)
        return "Error: Operation must be a string"
    operation = operation.strip().lower()

    for value in (a, b):
        if isinstance(value, bool) or not isinstance(value, (int)):
            logger.warning("Invalid operand %r of type %s", value, type(value).__name__)
            return "Error: Operands must be numbers"

    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
        if b == 0:
            logger.error("Attempted division by zero: %r / %r", a, b)
            return "Error: Cannot divide by zero"
        result = a // b
    elif operation == '%':
        result = a % b
    else:
        logger.warning("Unsupported operation: %r", operation)
        return "Error: Unsupported operation"

    logger.info("%r %s %r = %r", a, operation, b, result)
    return result

# Example usage
if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    print(calculate('+', 5, 3))        # Output: 8
    print(calculate('-', 5, 3))   # Output: 2
    print(calculate('*', 5, 3))   # Output: 15
    print(calculate('/', 5, 3))     # Output: 1.666...
    print(calculate('/', 5, 0))     # Error
    print(calculate('+', '5', 3))      # Error: Operands must be numbers
    print(calculate(None, 5, 3))         # Error: Operation must be a string
