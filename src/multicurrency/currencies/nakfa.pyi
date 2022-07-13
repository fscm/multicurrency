from decimal import Decimal
from multicurrency.pycurrency import Currency
from typing import Optional, Union

class Nakfa(Currency):
    def __new__(cls, amount: Union[str, int, float, Decimal], pattern: Optional[str] = ...) -> Nakfa: ...
    def __recreate__(self, amount: Union[str, int, float, Decimal]) -> Nakfa: ...
