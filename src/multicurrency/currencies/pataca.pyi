from decimal import Decimal
from multicurrency.pycurrency import Currency
from typing import Optional, Union

class Pataca(Currency):
    def __new__(cls, amount: Union[str, int, float, Decimal], pattern: Optional[str] = ...) -> Pataca: ...
    def __recreate__(self, amount: Union[str, int, float, Decimal]) -> Pataca: ...
