from typing import Any, TypeVar

Currency = TypeVar('Currency', bound='Currency')

class CurrencyException(Exception): ...

class CurrencyInvalidDivision(CurrencyException, TypeError):
    def __init__(self, first: Currency, second: Any) -> None: ...

class CurrencyInvalidMultiplication(CurrencyException, TypeError):
    def __init__(self, first: Currency, second: Any) -> None: ...

class CurrencyInvalidOperation(CurrencyException, TypeError):
    def __init__(self, operation: str, element: Any) -> None: ...

class CurrencyMismatchException(CurrencyException, ValueError):
    def __init__(self, first: str, second: str) -> None: ...

class CurrencyTypeException(CurrencyException, TypeError):
    def __init__(self, first: Any, second: Any) -> None: ...
