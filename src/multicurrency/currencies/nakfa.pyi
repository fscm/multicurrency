from decimal import Decimal
from multicurrency.pycurrency import Currency
from typing import Self

class Nakfa(Currency):
    def __new__(cls, amount: str | float | Decimal, pattern: str | None = ...) -> Self: ...
    def __recreate__(self, amount: str | float | Decimal) -> Self: ...
