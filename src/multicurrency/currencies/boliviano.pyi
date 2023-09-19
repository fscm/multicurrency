from decimal import Decimal
from multicurrency.pycurrency import Currency
from typing import Optional, Self, Union

class Boliviano(Currency):
    def __new__(cls, amount: Union[str, float, Decimal], pattern: Optional[str] = ...) -> Self: ...
    def __recreate__(self, amount: Union[str, float, Decimal]) -> Self: ...
