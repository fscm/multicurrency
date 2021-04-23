from .currency import Currency
from decimal import Decimal
from typing import Any, Optional, Union

class ArgentinePeso(Currency):
    def __new__(cls: Any, amount: Union[int, float, Decimal], decimal_places: Optional[int]=..., decimal_sign: Optional[str]=..., grouping_sign: Optional[str]=..., international: Optional[bool]=..., symbol_ahead: Optional[bool]=..., symbol_separator: Optional[str]=..., **other: Any) -> ArgentinePeso: ...

class ChileanPeso(Currency):
    def __new__(cls: Any, amount: Union[int, float, Decimal], decimal_places: Optional[int]=..., decimal_sign: Optional[str]=..., grouping_sign: Optional[str]=..., international: Optional[bool]=..., symbol_ahead: Optional[bool]=..., symbol_separator: Optional[str]=..., **other: Any) -> ChileanPeso: ...

class ColombianPeso(Currency):
    def __new__(cls: Any, amount: Union[int, float, Decimal], decimal_places: Optional[int]=..., decimal_sign: Optional[str]=..., grouping_sign: Optional[str]=..., international: Optional[bool]=..., symbol_ahead: Optional[bool]=..., symbol_separator: Optional[str]=..., **other: Any) -> ColombianPeso: ...

class CubanPeso(Currency):
    def __new__(cls: Any, amount: Union[int, float, Decimal], decimal_places: Optional[int]=..., decimal_sign: Optional[str]=..., grouping_sign: Optional[str]=..., international: Optional[bool]=..., symbol_ahead: Optional[bool]=..., symbol_separator: Optional[str]=..., **other: Any) -> CubanPeso: ...

class DominicanPeso(Currency):
    def __new__(cls: Any, amount: Union[int, float, Decimal], decimal_places: Optional[int]=..., decimal_sign: Optional[str]=..., grouping_sign: Optional[str]=..., international: Optional[bool]=..., symbol_ahead: Optional[bool]=..., symbol_separator: Optional[str]=..., **other: Any) -> DominicanPeso: ...

class MexicanPeso(Currency):
    def __new__(cls: Any, amount: Union[int, float, Decimal], decimal_places: Optional[int]=..., decimal_sign: Optional[str]=..., grouping_sign: Optional[str]=..., international: Optional[bool]=..., symbol_ahead: Optional[bool]=..., symbol_separator: Optional[str]=..., **other: Any) -> MexicanPeso: ...

class PhilippinePeso(Currency):
    def __new__(cls: Any, amount: Union[int, float, Decimal], decimal_places: Optional[int]=..., decimal_sign: Optional[str]=..., grouping_sign: Optional[str]=..., international: Optional[bool]=..., symbol_ahead: Optional[bool]=..., symbol_separator: Optional[str]=..., **other: Any) -> PhilippinePeso: ...

class PesoUruguayo(Currency):
    def __new__(cls: Any, amount: Union[int, float, Decimal], decimal_places: Optional[int]=..., decimal_sign: Optional[str]=..., grouping_sign: Optional[str]=..., international: Optional[bool]=..., symbol_ahead: Optional[bool]=..., symbol_separator: Optional[str]=..., **other: Any) -> PesoUruguayo: ...
