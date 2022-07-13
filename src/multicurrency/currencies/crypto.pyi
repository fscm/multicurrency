from decimal import Decimal
from multicurrency.pycurrency import Currency
from typing import Optional, Union

class EOS(Currency):
    def __new__(cls, amount: Union[str, int, float, Decimal], pattern: Optional[str] = ...) -> EOS: ...
    def __recreate__(self, amount: Union[str, int, float, Decimal]) -> EOS: ...

class Ethereum(Currency):
    def __new__(cls, amount: Union[str, int, float, Decimal], pattern: Optional[str] = ...) -> Ethereum: ...
    def __recreate__(self, amount: Union[str, int, float, Decimal]) -> Ethereum: ...

class Bitcoin(Currency):
    def __new__(cls, amount: Union[str, int, float, Decimal], pattern: Optional[str] = ...) -> Bitcoin: ...
    def __recreate__(self, amount: Union[str, int, float, Decimal]) -> Bitcoin: ...

class StellarLumens(Currency):
    def __new__(cls, amount: Union[str, int, float, Decimal], pattern: Optional[str] = ...) -> StellarLumens: ...
    def __recreate__(self, amount: Union[str, int, float, Decimal]) -> StellarLumens: ...

class Monero(Currency):
    def __new__(cls, amount: Union[str, int, float, Decimal], pattern: Optional[str] = ...) -> Monero: ...
    def __recreate__(self, amount: Union[str, int, float, Decimal]) -> Monero: ...

class Ripple(Currency):
    def __new__(cls, amount: Union[str, int, float, Decimal], pattern: Optional[str] = ...) -> Ripple: ...
    def __recreate__(self, amount: Union[str, int, float, Decimal]) -> Ripple: ...

class Tezos(Currency):
    def __new__(cls, amount: Union[str, int, float, Decimal], pattern: Optional[str] = ...) -> Tezos: ...
    def __recreate__(self, amount: Union[str, int, float, Decimal]) -> Tezos: ...

class Zcash(Currency):
    def __new__(cls, amount: Union[str, int, float, Decimal], pattern: Optional[str] = ...) -> Zcash: ...
    def __recreate__(self, amount: Union[str, int, float, Decimal]) -> Zcash: ...