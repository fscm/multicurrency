from .currency import Currency
from decimal import Decimal
from typing import Any, Optional, Union

class IcelandKrona(Currency):
    def __new__(cls: Any, amount: Union[int, float, Decimal], decimal_places: Optional[int]=..., decimal_sign: Optional[str]=..., grouping_sign: Optional[str]=..., international: Optional[bool]=..., symbol_ahead: Optional[bool]=..., symbol_separator: Optional[str]=..., **other: Any) -> IcelandKrona: ...

class SwedishKrona(Currency):
    def __new__(cls: Any, amount: Union[int, float, Decimal], decimal_places: Optional[int]=..., decimal_sign: Optional[str]=..., grouping_sign: Optional[str]=..., international: Optional[bool]=..., symbol_ahead: Optional[bool]=..., symbol_separator: Optional[str]=..., **other: Any) -> SwedishKrona: ...
