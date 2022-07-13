from decimal import Decimal
from multicurrency.pycurrency import Currency
from typing import Optional, Union

class BahrainiDinar(Currency):
    def __new__(cls, amount: Union[str, int, float, Decimal], pattern: Optional[str] = ...) -> BahrainiDinar: ...
    def __recreate__(self, amount: Union[str, int, float, Decimal]) -> BahrainiDinar: ...

class AlgerianDinar(Currency):
    def __new__(cls, amount: Union[str, int, float, Decimal], pattern: Optional[str] = ...) -> AlgerianDinar: ...
    def __recreate__(self, amount: Union[str, int, float, Decimal]) -> AlgerianDinar: ...

class IraqiDinar(Currency):
    def __new__(cls, amount: Union[str, int, float, Decimal], pattern: Optional[str] = ...) -> IraqiDinar: ...
    def __recreate__(self, amount: Union[str, int, float, Decimal]) -> IraqiDinar: ...

class JordanianDinar(Currency):
    def __new__(cls, amount: Union[str, int, float, Decimal], pattern: Optional[str] = ...) -> JordanianDinar: ...
    def __recreate__(self, amount: Union[str, int, float, Decimal]) -> JordanianDinar: ...

class KuwaitiDinar(Currency):
    def __new__(cls, amount: Union[str, int, float, Decimal], pattern: Optional[str] = ...) -> KuwaitiDinar: ...
    def __recreate__(self, amount: Union[str, int, float, Decimal]) -> KuwaitiDinar: ...

class LibyanDinar(Currency):
    def __new__(cls, amount: Union[str, int, float, Decimal], pattern: Optional[str] = ...) -> LibyanDinar: ...
    def __recreate__(self, amount: Union[str, int, float, Decimal]) -> LibyanDinar: ...

class SerbianDinarXK(Currency):
    def __new__(cls, amount: Union[str, int, float, Decimal], pattern: Optional[str] = ...) -> SerbianDinarXK: ...
    def __recreate__(self, amount: Union[str, int, float, Decimal]) -> SerbianDinarXK: ...

class SerbianDinarSR(Currency):
    def __new__(cls, amount: Union[str, int, float, Decimal], pattern: Optional[str] = ...) -> SerbianDinarSR: ...
    def __recreate__(self, amount: Union[str, int, float, Decimal]) -> SerbianDinarSR: ...

class TunisianDinar(Currency):
    def __new__(cls, amount: Union[str, int, float, Decimal], pattern: Optional[str] = ...) -> TunisianDinar: ...
    def __recreate__(self, amount: Union[str, int, float, Decimal]) -> TunisianDinar: ...
