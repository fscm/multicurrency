from decimal import Decimal
from multicurrency.pycurrency import Currency
from typing import Optional, Self, Union

class IndianRupee(Currency):
    def __new__(cls, amount: Union[str, float, Decimal], pattern: Optional[str] = ...) -> Self: ...
    def __recreate__(self, amount: Union[str, float, Decimal]) -> Self: ...

class IndianRupeeBT(Currency):
    def __new__(cls, amount: Union[str, float, Decimal], pattern: Optional[str] = ...) -> Self: ...
    def __recreate__(self, amount: Union[str, float, Decimal]) -> Self: ...

class IndianRupeeIN(Currency):
    def __new__(cls, amount: Union[str, float, Decimal], pattern: Optional[str] = ...) -> Self: ...
    def __recreate__(self, amount: Union[str, float, Decimal]) -> Self: ...

class SriLankaRupee(Currency):
    def __new__(cls, amount: Union[str, float, Decimal], pattern: Optional[str] = ...) -> Self: ...
    def __recreate__(self, amount: Union[str, float, Decimal]) -> Self: ...

class MauritiusRupee(Currency):
    def __new__(cls, amount: Union[str, float, Decimal], pattern: Optional[str] = ...) -> Self: ...
    def __recreate__(self, amount: Union[str, float, Decimal]) -> Self: ...

class NepaleseRupee(Currency):
    def __new__(cls, amount: Union[str, float, Decimal], pattern: Optional[str] = ...) -> Self: ...
    def __recreate__(self, amount: Union[str, float, Decimal]) -> Self: ...

class PakistanRupee(Currency):
    def __new__(cls, amount: Union[str, float, Decimal], pattern: Optional[str] = ...) -> Self: ...
    def __recreate__(self, amount: Union[str, float, Decimal]) -> Self: ...

class SeychellesRupee(Currency):
    def __new__(cls, amount: Union[str, float, Decimal], pattern: Optional[str] = ...) -> Self: ...
    def __recreate__(self, amount: Union[str, float, Decimal]) -> Self: ...
