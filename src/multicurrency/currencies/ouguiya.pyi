from decimal import Decimal
from multicurrency.pycurrency import Currency
from typing import Optional, Union

class Ouguiya(Currency):
    def __new__(cls, amount: Union[str, int, float, Decimal], pattern: Optional[str] = ...) -> Ouguiya: ...
    def __recreate__(self, amount: Union[str, int, float, Decimal]) -> Ouguiya: ...
