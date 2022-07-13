from decimal import Decimal
from multicurrency.pycurrency import Currency
from typing import Optional, Union

class MoldovanLeu(Currency):
    def __new__(cls, amount: Union[str, int, float, Decimal], pattern: Optional[str] = ...) -> MoldovanLeu: ...
    def __recreate__(self, amount: Union[str, int, float, Decimal]) -> MoldovanLeu: ...

class Leu(Currency):
    def __new__(cls, amount: Union[str, int, float, Decimal], pattern: Optional[str] = ...) -> Leu: ...
    def __recreate__(self, amount: Union[str, int, float, Decimal]) -> Leu: ...
