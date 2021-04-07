from .currency import Currency
from decimal import Decimal
from typing import Any, Optional, Union

class KenyanShilling(Currency):
    def __new__(cls: Any, amount: Union[int, float, Decimal], decimal_places: int=..., decimal_sign: Optional[str]=..., grouping_sign: Optional[str]=..., international: bool=..., **other: Any) -> KenyanShilling: ...

class SomaliShilling(Currency):
    def __new__(cls: Any, amount: Union[int, float, Decimal], decimal_places: int=..., decimal_sign: Optional[str]=..., grouping_sign: Optional[str]=..., international: bool=..., **other: Any) -> SomaliShilling: ...

class TanzanianShilling(Currency):
    def __new__(cls: Any, amount: Union[int, float, Decimal], decimal_places: int=..., decimal_sign: Optional[str]=..., grouping_sign: Optional[str]=..., international: bool=..., **other: Any) -> TanzanianShilling: ...

class UgandaShilling(Currency):
    def __new__(cls: Any, amount: Union[int, float, Decimal], decimal_places: int=..., decimal_sign: Optional[str]=..., grouping_sign: Optional[str]=..., international: bool=..., **other: Any) -> UgandaShilling: ...
