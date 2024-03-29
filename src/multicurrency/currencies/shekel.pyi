from decimal import Decimal
from multicurrency.pycurrency import Currency
from typing import Self

class NewIsraeliShekel(Currency):
    def __new__(cls, amount: str | float | Decimal, pattern: str | None = ...) -> Self: ...
    def __recreate__(self, amount: str | float | Decimal) -> Self: ...

class NewIsraeliShekelIL(Currency):
    def __new__(cls, amount: str | float | Decimal, pattern: str | None = ...) -> Self: ...
    def __recreate__(self, amount: str | float | Decimal) -> Self: ...

class NewIsraeliShekelPS(Currency):
    def __new__(cls, amount: str | float | Decimal, pattern: str | None = ...) -> Self: ...
    def __recreate__(self, amount: str | float | Decimal) -> Self: ...
