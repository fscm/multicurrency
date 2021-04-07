from .currency import Currency
from decimal import Decimal
from typing import Any, Optional, Union

class NorthKoreanWon(Currency):
    def __new__(cls: Any, amount: Union[int, float, Decimal], decimal_places: int=..., decimal_sign: Optional[str]=..., grouping_sign: Optional[str]=..., international: bool=..., **other: Any) -> NorthKoreanWon: ...

class SouthKoreanWon(Currency):
    def __new__(cls: Any, amount: Union[int, float, Decimal], decimal_places: int=..., decimal_sign: Optional[str]=..., grouping_sign: Optional[str]=..., international: bool=..., **other: Any) -> SouthKoreanWon: ...
