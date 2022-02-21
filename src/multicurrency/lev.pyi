from ._currency import Currency
from decimal import Decimal
from typing import Optional, Union

class BulgarianLev(Currency):
    def __new__(cls, amount: Union[int, float, Decimal], decimal_places: Optional[int] = ..., decimal_sign: Optional[str] = ..., grouping_places: Optional[int] = ..., grouping_sign: Optional[str] = ..., international: Optional[bool] = ..., symbol_ahead: Optional[bool] = ..., symbol_separator: Optional[str] = ..., **other) -> BulgarianLev: ...
