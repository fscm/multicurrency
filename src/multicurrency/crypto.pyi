from ._currency import Currency
from decimal import Decimal
from typing import Optional, Union

class EOS(Currency):
    def __new__(cls, amount: Union[int, float, Decimal], decimal_places: Optional[int] = ..., decimal_sign: Optional[str] = ..., grouping_places: Optional[int] = ..., grouping_sign: Optional[str] = ..., international: Optional[bool] = ..., symbol_ahead: Optional[bool] = ..., symbol_separator: Optional[str] = ..., **other) -> EOS: ...

class Ethereum(Currency):
    def __new__(cls, amount: Union[int, float, Decimal], decimal_places: Optional[int] = ..., decimal_sign: Optional[str] = ..., grouping_places: Optional[int] = ..., grouping_sign: Optional[str] = ..., international: Optional[bool] = ..., symbol_ahead: Optional[bool] = ..., symbol_separator: Optional[str] = ..., **other) -> Ethereum: ...

class Bitcoin(Currency):
    def __new__(cls, amount: Union[int, float, Decimal], decimal_places: Optional[int] = ..., decimal_sign: Optional[str] = ..., grouping_places: Optional[int] = ..., grouping_sign: Optional[str] = ..., international: Optional[bool] = ..., symbol_ahead: Optional[bool] = ..., symbol_separator: Optional[str] = ..., **other) -> Bitcoin: ...

class StellarLumens(Currency):
    def __new__(cls, amount: Union[int, float, Decimal], decimal_places: Optional[int] = ..., decimal_sign: Optional[str] = ..., grouping_places: Optional[int] = ..., grouping_sign: Optional[str] = ..., international: Optional[bool] = ..., symbol_ahead: Optional[bool] = ..., symbol_separator: Optional[str] = ..., **other) -> StellarLumens: ...

class Monero(Currency):
    def __new__(cls, amount: Union[int, float, Decimal], decimal_places: Optional[int] = ..., decimal_sign: Optional[str] = ..., grouping_places: Optional[int] = ..., grouping_sign: Optional[str] = ..., international: Optional[bool] = ..., symbol_ahead: Optional[bool] = ..., symbol_separator: Optional[str] = ..., **other) -> Monero: ...

class Ripple(Currency):
    def __new__(cls, amount: Union[int, float, Decimal], decimal_places: Optional[int] = ..., decimal_sign: Optional[str] = ..., grouping_places: Optional[int] = ..., grouping_sign: Optional[str] = ..., international: Optional[bool] = ..., symbol_ahead: Optional[bool] = ..., symbol_separator: Optional[str] = ..., **other) -> Ripple: ...

class Tezos(Currency):
    def __new__(cls, amount: Union[int, float, Decimal], decimal_places: Optional[int] = ..., decimal_sign: Optional[str] = ..., grouping_places: Optional[int] = ..., grouping_sign: Optional[str] = ..., international: Optional[bool] = ..., symbol_ahead: Optional[bool] = ..., symbol_separator: Optional[str] = ..., **other) -> Tezos: ...

class Zcash(Currency):
    def __new__(cls, amount: Union[int, float, Decimal], decimal_places: Optional[int] = ..., decimal_sign: Optional[str] = ..., grouping_places: Optional[int] = ..., grouping_sign: Optional[str] = ..., international: Optional[bool] = ..., symbol_ahead: Optional[bool] = ..., symbol_separator: Optional[str] = ..., **other) -> Zcash: ...
