from decimal import Context, Decimal
from typing import Any, Optional, Tuple, Union

CurrencyContext: Context

class Currency:
    def __new__(cls, amount: Union[int, float, Decimal], alpha_code: Optional[str]=..., numeric_code: Optional[str]=..., symbol: Optional[str]=..., symbol_ahead: Optional[bool]=..., symbol_separator: Optional[str]=..., decimal_places: Optional[int]=..., decimal_sign: Optional[str]=..., grouping_sign: Optional[str]=..., convertion: Optional[str]=..., international: Optional[bool]=...) -> Currency: ...
    def __abs__(self) -> Currency: ...
    def __add__(self, other: Any) -> Currency: ...
    def __bool__(self) -> bool: ...
    def __ceil__(self) -> Currency: ...
    def __copy__(self) -> Currency: ...
    def __divmod__(self, other: Any) -> Tuple[Currency, Currency]: ...
    def __eq__(self, other: Any) -> bool: ...
    def __float__(self) -> float: ...
    def __floor__(self) -> Currency: ...
    def __floordiv__(self, other: Any) -> Currency: ...
    def __ge__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    def __int__(self) -> int: ...
    def __le__(self, other: Any) -> bool: ...
    def __lt__(self, other: Any) -> bool: ...
    def __mod__(self, other: Any) -> Currency: ...
    def __mul__(self, other: Any) -> Currency: ...
    def __ne__(self, other: Any) -> bool: ...
    def __neg__(self) -> Currency: ...
    def __pos__(self) -> Currency: ...
    def __reduce__(self) -> Tuple[type, Tuple[Any, ...]]: ...
    def __round__(self, precision: Optional[int]=...) -> Currency: ...
    def __rsub__(self, other: Any) -> Currency: ...
    def __sub__(self, other: Any) -> Currency: ...
    def __truediv__(self, other: Any) -> Currency: ...
    __deepcopy__: Currency = ...
    __rmul__: Currency = ...
    def is_signed(self) -> bool: ...
    def pstr(self, precision: int=...) -> str: ...
    @property
    def amount(self) -> Decimal: ...
    @property
    def numeric_code(self) -> str: ...
    @property
    def alpha_code(self) -> str: ...
    @property
    def convertion(self) -> str: ...
    @property
    def decimal_places(self) -> int: ...
    @property
    def decimal_sign(self) -> str: ...
    @property
    def grouping_sign(self) -> str: ...
    @property
    def international(self) -> bool: ...
    @property
    def symbol(self) -> str: ...
    @property
    def symbol_ahead(self) -> bool: ...
    @property
    def symbol_separator(self) -> str: ...
