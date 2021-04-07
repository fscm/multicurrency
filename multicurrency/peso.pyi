from .currency import Currency
from decimal import Decimal
from typing import Any, Optional, Union

class ArgentinePeso(Currency):
    def __new__(cls: Any, amount: Union[int, float, Decimal], decimal_places: int=..., decimal_sign: Optional[str]=..., grouping_sign: Optional[str]=..., international: bool=..., **other: Any) -> ArgentinePeso: ...

class ChileanPeso(Currency):
    def __new__(cls: Any, amount: Union[int, float, Decimal], decimal_places: int=..., decimal_sign: Optional[str]=..., grouping_sign: Optional[str]=..., international: bool=..., **other: Any) -> ChileanPeso: ...

class ColombianPeso(Currency):
    def __new__(cls: Any, amount: Union[int, float, Decimal], decimal_places: int=..., decimal_sign: Optional[str]=..., grouping_sign: Optional[str]=..., international: bool=..., **other: Any) -> ColombianPeso: ...

class CubanPeso(Currency):
    def __new__(cls: Any, amount: Union[int, float, Decimal], decimal_places: int=..., decimal_sign: Optional[str]=..., grouping_sign: Optional[str]=..., international: bool=..., **other: Any) -> CubanPeso: ...

class DominicanPeso(Currency):
    def __new__(cls: Any, amount: Union[int, float, Decimal], decimal_places: int=..., decimal_sign: Optional[str]=..., grouping_sign: Optional[str]=..., international: bool=..., **other: Any) -> DominicanPeso: ...

class MexicanPeso(Currency):
    def __new__(cls: Any, amount: Union[int, float, Decimal], decimal_places: int=..., decimal_sign: Optional[str]=..., grouping_sign: Optional[str]=..., international: bool=..., **other: Any) -> MexicanPeso: ...

class PhilippinePeso(Currency):
    def __new__(cls: Any, amount: Union[int, float, Decimal], decimal_places: int=..., decimal_sign: Optional[str]=..., grouping_sign: Optional[str]=..., international: bool=..., **other: Any) -> PhilippinePeso: ...

class PesoUruguayo(Currency):
    def __new__(cls: Any, amount: Union[int, float, Decimal], decimal_places: int=..., decimal_sign: Optional[str]=..., grouping_sign: Optional[str]=..., international: bool=..., **other: Any) -> PesoUruguayo: ...
