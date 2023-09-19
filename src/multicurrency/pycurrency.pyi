from decimal import Decimal
from typing import Optional, Self, Tuple, Union

Numerical = Union[float, Decimal]

class Currency:
    def __new__(cls, amount: Union[str, float, Decimal], alpha_code: Optional[str] = ..., numeric_code: Optional[str] = ..., symbol: Optional[str] = ..., localized_symbol: Optional[str] = ..., convertion: Optional[str] = ..., pattern: Optional[str] = ...) -> Self: ...
    def __abs__(self) -> Self: ...
    def __add__(self, other: object) -> Self: ...
    def __bool__(self) -> bool: ...
    def __ceil__(self) -> Self: ...
    def __copy__(self) -> Self: ...
    def __divmod__(self, other: Numerical) -> Tuple[Self, Self]: ...
    def __eq__(self, other: object) -> bool: ...
    def __float__(self) -> float: ...
    def __floor__(self) -> Self: ...
    def __floordiv__(self, other: Numerical) -> Self: ...
    def __format__(self, fmt: str = ...) -> str: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __mod__(self, other: Numerical) -> Self: ...
    def __mul__(self, other: Numerical) -> Self: ...
    def __ne__(self, other: object) -> bool: ...
    def __neg__(self) -> Self: ...
    def __pos__(self) -> Self: ...
    def __recreate__(self, amount: Union[str, float, Decimal]) -> Self: ...
    def __reduce__(self) -> Tuple[type, Tuple[object, ...]]: ...
    def __round__(self, precision: Optional[int] = ...) -> Self: ...
    def __rsub__(self, other: object) -> Self: ...
    def __sub__(self, other: object) -> Self: ...
    def __truediv__(self, other: Numerical) -> Self: ...
    __deepcopy__: Currency
    __rmul__: Currency
    def international(self, precision: Optional[int] = ...) -> str: ...
    def is_signed(self) -> bool: ...
    def localized(self, precision: Optional[int] = ...) -> str: ...
    def precision(self, precision: Optional[int] = ...) -> str: ...
    @property
    def amount(self) -> Decimal: ...
    @property
    def alpha_code(self) -> str: ...
    @property
    def numeric_code(self) -> str: ...
    @property
    def symbol(self) -> str: ...
    @property
    def localized_symbol(self) -> str: ...
    @property
    def convertion(self) -> str: ...
    @property
    def pattern(self) -> str: ...
