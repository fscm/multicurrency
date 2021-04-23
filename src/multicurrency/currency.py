# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Currency representation.

Representation of a currency value.

Simple usage example:

    >>> from multicurrency import Currency
    >>> euro = Currency(amount=1, alpha_code='EUR', symbol='€')
    >>> print(euro)
    €1.00

## Supported operations

Several operations are supported by the `multicurrency.currency.Currency`
type.

### Absolute

Produces the absolute value of a given `multicurrency.currency.Currency`.

    >>> from multicurrency import Currency
    >>> c = abs(Currency(amount=-2))
    >>> print(c)
    2.00

### Addiction

Addiction is supported only between `multicurrency.currency.Currency`
of the same type.

    >>> from multicurrency import Currency
    >>> c1 = Currency(amount=2)
    >>> c2 = Currency(amount=3)
    >>> print(c1 + c2)
    5.00

### Boolean

Produces 'True' for values of `multicurrency.currency.Currency` other
than zero. 'False' otherwise

    >>> from multicurrency import Currency
    >>> bool(Currency(amount=0))
    False
    >>> bool(Currency(amount=1))
    True

### Ceiling

Produces a `multicurrency.currency.Currency` rounded up to the nearest
integer.

    >>> from multicurrency import Currency
    >>> from math import ceil
    >>> print(ceil(Currency(1/7)))
    1.00

### Copy

Produces a copy of itself.

    >>> from multicurrency import Currency
    >>> from copy import copy
    >>> c = copy(Currency(1/7))
    >>> print(c)
    0.14

### Division

Produces a `multicurrency.currency.Currency` with the value of the
division of the currency by either an `int`, `float`, or
`decimal.Decimal`.

    >>> from multicurrency import Currency
    >>> d = Currency(7) / 2
    >>> print(d)
    3.50

### Divmod

Produces a tuple consisting of the currencies with the quotient and
the remainder of the division of the currency by either an `int`,
`float`, or `decimal.Decimal`.

    >>> from multicurrency import Currency
    >>> q, r = divmod(Currency(7), 2)
    >>> print(q, r)
    3.00 1.00

### Float

Produces a `float` with the value of the currency amount.

    >>> from multicurrency import Currency
    >>> float(Currency(1/7))
    0.14285714285714285

### Flooring

Produces a `multicurrency.currency.Currency` rounded down to the
nearest integer.

    >>> from multicurrency import Currency
    >>> from math import floor
    >>> print(floor(Currency(1/7)))
    0.00

### Floordiv

Produces a `multicurrency.currency.Currency` with the integral part of
the quotient of the division of the currency by either an `int`,
`float`, or `decimal.Decimal`.

    >>> from multicurrency import Currency
    >>> fd = Currency(7) // 2
    >>> print(fd)
    3.00

### Hash

Produces a hash representation of the `multicurrency.currency.Currency`.

    >>> from multicurrency import Currency
    >>> hash(Currency(amount=7, alpha_code='EUR', numeric_code='978'))
    1166476495300974230

### Int

Produces an `int` with the value of the currency amount.

    >>> from multicurrency import Currency
    >>> int(Currency(1/7))
    0

### Mod

Produces a `multicurrency.currency.Currency` with the value of the
remainder of the division of the currency by either an `int`, `float`,
or `decimal.Decimal`.

    >>> from multicurrency import Currency
    >>> m = Currency(7) % 2
    >>> print(m)
    1.00

### Multiplication

Multiplication is supported between `multicurrency.currency.Currency`
and `int`, `float`, or `decimal.Decimal`.

    >>> from multicurrency import Currency
    >>> c = Currency(amount=2)
    >>> print(c * 2.5)
    5.00

### Round

Produces a `multicurrency.currency.Currency` with the amount of the
currency rounded to a given precision.

    >>> from multicurrency import Currency
    >>> r = round(Currency(1/7), 3)
    >>> print(r.amount)
    0.143

### Subtraction

Subtraction is supported only between `multicurrency.currency.Currency`
of the same type.

    >>> from multicurrency import Currency
    >>> c1 = Currency(amount=2)
    >>> c2 = Currency(amount=3)
    >>> print(c1 - c2)
    -1.00

## Other Operations

This type also supports the basic comparison operations between two
objects of the same currency.

    >>> from multicurrency import Currency
    >>> c1 = Currency(amount=2)
    >>> c2 = Currency(amount=3)
    >>> c1 > c2
    False
    >>> c1 >= c2
    False
    >>> c1 < c2
    True
    >>> c1 <= c2
    True
    >>> c1 == c2
    False
    >>> c1 != c2
    True
"""

from decimal import Decimal, Context
from typing import Any, Optional, Union
from .exceptions import (
    CurrencyInvalidDivision,
    CurrencyInvalidMultiplication,
    CurrencyMismatchException,
    CurrencyTypeException)


CurrencyContext: Context = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()
"""Currency Context.
The environment for arithmetic operations involving `Currency`. This
context manages the operations precision and the rounding method.

Args:
    prec (int): Precision. Defaults to `28`.
    rounding (str): Rounding method. Defaults to `ROUND_HALF_EVEN`.
        Possible values are:

        * ROUND_CEILING: Round towards Infinity.
        * ROUND_DOWN: Round towards zero.
        * ROUND_FLOOR: Round towards negative Infinity.
        * ROUND_HALF_DOWN: Round to nearest with ties going towards zero.
        * ROUND_HALF_EVEN: Round to nearest with ties going to nearest
            even integer.
        * ROUND_HALF_UP: Round to nearest with ties going away from zero.
        * ROUND_UP: Round away from zero.
        * ROUND_05UP: Round away from zero if last digit after rounding
            towards zero would have been 0 or 5; otherwise round
            towards zero.

.. warning::
    Precision values (`prec`) lower than `3` may produce unexpected
    resutls.

Usage example:

    >>> from multicurrency import CurrencyContext
    >>> CurrencyContext.prec = 4
    >>> CurrencyContext.rounding = 'ROUND_HALF_UP'
    >>> print(CurrencyContext.prec, CurrencyContext.rounding)
    4 ROUND_HALF_UP
"""


class Currency:
    """Currency representation.

    This class is a generic representation of Money, a certain amount
    of currency value of a particular country.

    Values in this class will be represented, by default, with 2 (two)
    decimal places and rounded awat from zero if the last significant
    The value (`amount`) represented by this class is by default
    showned with 2 (two) decimal places and rounded away from zero if
    the last significant digit is greater than 5 (five), towards zero
    if less than 5 (five). When the last significant digit is 5 (five)
    the preceding digit is examined, even values cause the result to be
    rounded down and odd digits cause the result to be rounded up.

    The `alpha_code` should be set accordingly to the three-letter
    numeric code defined by the ISO-4217 for the represented language.

    The `numeric_code` argument should be set accordingly to the
    three-digit numeric code defined by the ISO-4217 for the
    represented language.

    The `symbol`, when set, will be used to identify the currency when
    printing out the value.

    The `decimal_places` value must be greater or equal to 0 (zero).
    Negative values will be converter to 0 (zero).

    The `convertion` string, when set, will be used to replace the
    Western Arabic numerals - as well as the symbols - with the
    equivalent ones on the currency language. The string must be
    created with the numbers from 0 (zero) to 9 (nine) followed by the
    minus sign without any separation mark (e.g.: '0123456789-').

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        alpha_code (str, optionsl): Represented currency alpha code.
            Defaults to ''.
        numeric_code (str, optional): Represented currency numeric
            code. Defaults to 0.
        symbol (str, optional): Represented currency symbol. Defaults
            to ''.
        symbol_separator (str, optional): Separation between the symbol
            and the value. Defaults to ''.
        symbol_ahead (bool, optional): True if symbol goes ahead of the
            value. False otherwise. Defaults to False.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 2,
        decimal_sign (str, optional): Decimal symbol. Defaults to '.'.
        grouping_sign (str, optional): Grouping symbol. Defaults to ','.
        international (bool, optional): Identifies the currency using
            the 'currency' value instead of the 'symbol'. Defaults to
            False.
        convertion (str, optional): String with the numbers from 0 to 9
            followed by the minus ('-') sign. Defaults to ''.
    """

    __slots__ = [
        '_alpha_code',
        '_amount',
        '_convertion',
        '_decimal_places',
        '_decimal_sign',
        '_grouping_sign',
        '_international',
        '_numeric_code',
        '_symbol',
        '_symbol_ahead',
        '_symbol_separator']

    def __new__(
            cls,
            amount: Union[int, float, Decimal],
            alpha_code: Optional[str] = '',
            numeric_code: Optional[str] = '0',
            symbol: Optional[str] = '',
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '',
            decimal_places: Optional[int] = 2,
            decimal_sign: Optional[str] = '.',
            grouping_sign: Optional[str] = ',',
            convertion: Optional[str] = '',
            international: Optional[bool] = False) -> 'Currency':
        """Class creator.

        Returns:
            Currency: new opbject.
        """
        self = object.__new__(cls)
        self._amount = CurrencyContext.create_decimal(str(amount))
        self._alpha_code = alpha_code
        self._decimal_places = max(decimal_places, 0)
        self._decimal_sign = decimal_sign
        self._grouping_sign = grouping_sign
        self._international = international
        self._numeric_code = numeric_code
        self._symbol = symbol
        self._symbol_ahead = symbol_ahead
        self._symbol_separator = symbol_separator
        self._convertion = convertion
        return self

    def __abs__(self) -> 'Currency':
        """Returns the absolute value.

        Args:
            rnd (bool, optional): Defaults to `True`.

        Returns:
            Currency: absolute value.
        """
        return self.__class__(
            amount=abs(self._amount),
            alpha_code=self._alpha_code,
            numeric_code=self._numeric_code,
            symbol=self._symbol,
            symbol_ahead=self._symbol_ahead,
            symbol_separator=self._symbol_separator,
            decimal_places=self._decimal_places,
            decimal_sign=self._decimal_sign,
            grouping_sign=self._grouping_sign,
            convertion=self._convertion,
            international=self._international)

    def __add__(self, other: Any) -> 'Currency':
        """Adds `other` to this.

        Args:
            other (multicurrency.currency.Currency): Currency to add.

        Returns:
            Currency: result of the adding operation.

        Raises:
            CurrencyTypeException: If `other` not instance of
                'Currency'.
            CurrencyMismatchException: If `other.alpha_code` is
                differente from `alpha_code`.
        """
        if not isinstance(other, Currency):
            raise CurrencyTypeException(self, other)
        if self._alpha_code != other.alpha_code:
            raise CurrencyMismatchException(self._alpha_code, other.alpha_code)
        return self.__class__(
            amount=self._amount + other.amount,
            alpha_code=self._alpha_code,
            numeric_code=self._numeric_code,
            symbol=self._symbol,
            symbol_ahead=self._symbol_ahead,
            symbol_separator=self._symbol_separator,
            decimal_places=self._decimal_places,
            decimal_sign=self._decimal_sign,
            grouping_sign=self._grouping_sign,
            convertion=self._convertion,
            international=self._international)

    def __bool__(self) -> bool:
        """Standard truth testing for this class.

        Returns:
            bool: False if value is zero. True otherwise.
        """
        return bool(self._amount)

    def __ceil__(self) -> 'Currency':
        """Returns the ceiling.

        Returns:
            Currency: result of the ceiling operation.
        """
        return self.__class__(
            amount=self._amount.__ceil__(),
            alpha_code=self._alpha_code,
            numeric_code=self._numeric_code,
            symbol=self._symbol,
            symbol_ahead=self._symbol_ahead,
            symbol_separator=self._symbol_separator,
            decimal_places=self._decimal_places,
            decimal_sign=self._decimal_sign,
            grouping_sign=self._grouping_sign,
            convertion=self._convertion,
            international=self._international)

    def __copy__(self) -> 'Currency':
        """Returns a copy of self.

        Returns:
            Currency: copy of this.
        """
        return self.__class__(
            amount=self._amount,
            alpha_code=self._alpha_code,
            numeric_code=self._numeric_code,
            symbol=self._symbol,
            symbol_ahead=self._symbol_ahead,
            symbol_separator=self._symbol_separator,
            decimal_places=self._decimal_places,
            decimal_sign=self._decimal_sign,
            grouping_sign=self._grouping_sign,
            convertion=self._convertion,
            international=self._international)

    def __divmod__(self, other: Any) -> tuple['Currency', 'Currency']:
        """Returns a pair with the quocient and remaider of the
        division by `other`.

        Args:
            other (Numerical): amount to divide by.

        Returns:
            tuple['Currency', 'Currency']: quotient, remainder.

        Raises:
            CurrencyInvalidDivision: If `other` not of types
                `int`, `float` or `Decimal`.
            ZeroDivisionError: If dividing by zero
        """
        if not isinstance(other, (int, float, Decimal)):
            raise CurrencyInvalidDivision(self, other)
        if other == 0:
            raise ZeroDivisionError()
        quotient, remainder = self._amount.__divmod__(
            CurrencyContext.create_decimal(str(other)))
        return (
            self.__class__(
                amount=quotient,
                alpha_code=self._alpha_code,
                numeric_code=self._numeric_code,
                symbol=self._symbol,
                symbol_ahead=self._symbol_ahead,
                symbol_separator=self._symbol_separator,
                decimal_places=self._decimal_places,
                decimal_sign=self._decimal_sign,
                grouping_sign=self._grouping_sign,
                convertion=self._convertion,
                international=self._international),
            self.__class__(
                amount=remainder,
                alpha_code=self._alpha_code,
                numeric_code=self._numeric_code,
                symbol=self._symbol,
                symbol_ahead=self._symbol_ahead,
                symbol_separator=self._symbol_separator,
                decimal_places=self._decimal_places,
                decimal_sign=self._decimal_sign,
                grouping_sign=self._grouping_sign,
                convertion=self._convertion,
                international=self._international))

    def __eq__(self, other: Any) -> bool:
        """Checks if two currencies are equal.

        Args:
            other (Any): Currency to compare to.

        Returns:
            bool: True if equal. False otherwise.
        """
        # if isinstance(other, Currency):
        if isinstance(other, self.__class__):
            return (
                (self.amount == other.amount) and
                (self._alpha_code == other.alpha_code))
        return False

    def __float__(self) -> float:
        """Float representation.

        Returns:
            float: The currency value as float.
        """
        return float(self._amount)

    def __floor__(self) -> 'Currency':
        """Returns the flooring.

        Returns:
            Currency: result of the flooring operation.
        """
        return self.__class__(
            amount=self._amount.__floor__(),
            alpha_code=self._alpha_code,
            numeric_code=self._numeric_code,
            symbol=self._symbol,
            symbol_ahead=self._symbol_ahead,
            symbol_separator=self._symbol_separator,
            decimal_places=self._decimal_places,
            decimal_sign=self._decimal_sign,
            grouping_sign=self._grouping_sign,
            convertion=self._convertion,
            international=self._international)

    def __floordiv__(self, other: Any) -> 'Currency':
        """Returns the integral part of the quotient of the division
        by `other`.

        Args:
            other (Numerical): amount to divide by.

        Returns:
            Currency: Integer quotient resulting from the division.

        Raises:
            CurrencyInvalidDivision: If `other` not of types
                `int`, `float` or `Decimal`.
            ZeroDivisionError: If dividing by zero
        """
        if not isinstance(other, (int, float, Decimal)):
            raise CurrencyInvalidDivision(self, other)
        if other == 0:
            raise ZeroDivisionError()
        return self.__class__(
            amount=self._amount.__floordiv__(
                CurrencyContext.create_decimal(str(other))),
            alpha_code=self._alpha_code,
            numeric_code=self._numeric_code,
            symbol=self._symbol,
            symbol_ahead=self._symbol_ahead,
            symbol_separator=self._symbol_separator,
            decimal_places=self._decimal_places,
            decimal_sign=self._decimal_sign,
            grouping_sign=self._grouping_sign,
            convertion=self._convertion,
            international=self._international)

    def __ge__(self, other: Any) -> bool:
        """Checks if self is greater or equal than `other`.

        Args:
            other (Any): Currency to compare to.

        Returns:
            bool: True if is greater or equal than `other`. False
                otherwise.

        Raises:
            CurrencyTypeException: If `other` not instance of
                'Currency'.
            CurrencyMismatchException: If `other.alpha_code` is
                differente from `alpha_code`.
        """
        if not isinstance(other, self.__class__):
            raise CurrencyTypeException(self, other)
        if self._alpha_code != other.alpha_code:
            raise CurrencyMismatchException(self._alpha_code, other.alpha_code)
        return self._amount >= other.amount

    def __gt__(self, other: Any) -> bool:
        """Checks if self is greater than `other`.

        Args:
            other (Any): Currency to compare to.

        Returns:
            bool: True if is greater than `other`. False otherwise`.

        Raises:
            CurrencyTypeException: If `other` not instance of
                'Currency'.
            CurrencyMismatchException: If `other.alpha_code` is
                differente from `alpha_code`.
        """
        if not isinstance(other, self.__class__):
            raise CurrencyTypeException(self, other)
        if self._alpha_code != other.alpha_code:
            raise CurrencyMismatchException(self._alpha_code, other.alpha_code)
        return self._amount > other.amount

    def __hash__(self) -> int:
        """Hash representation of this class.

        Returns:
            int: Hash value.
        """
        return hash((self._amount, self._alpha_code, self._numeric_code))

    def __int__(self) -> int:
        """Integer representation.

        Returns:
            int: The currency value as an integer.
        """
        return int(self._amount)

    def __le__(self, other: Any) -> bool:
        """Checks if self is less or equal than `other`.

        Args:
            other (Any): Currency to compare to.

        Returns:
            bool: True if is less or equal than `other`. False
                otherwise.

        Raises:
            CurrencyTypeException: If `other` not instance of
                'Currency'.
            CurrencyMismatchException: If `other.alpha_code` is
                differente from `alpha_code`.
        """
        if not isinstance(other, self.__class__):
            raise CurrencyTypeException(self, other)
        if self._alpha_code != other.alpha_code:
            raise CurrencyMismatchException(self._alpha_code, other.alpha_code)
        return self._amount <= other.amount

    def __lt__(self, other: Any) -> bool:
        """Checks if self is less than `other`.

        Args:
            other (Any): Currency to compare to.

        Returns:
            bool: True if is less than `other`. False otherwise.

        Raises:
            CurrencyTypeException: If `other` not instance of
                'Currency'.
            CurrencyMismatchException: If `other.alpha_code` is
                differente from `alpha_code`.
        """
        if not isinstance(other, self.__class__):
            raise CurrencyTypeException(self, other)
        if self._alpha_code != other.alpha_code:
            raise CurrencyMismatchException(self._alpha_code, other.alpha_code)
        return self._amount < other.amount

    def __mod__(self, other: Any) -> 'Currency':
        """Returns the remainder of the division by `other`.

        Args:
            other (Numerical): amount to divide by.

        Returns:
            Currency: Remainder resulting from the division.

        Raises:
            CurrencyInvalidDivision: If `other` not of types
                `int`, `float` or `Decimal`.
            ZeroDivisionError: If dividing by zero
        """
        if not isinstance(other, (int, float, Decimal)):
            raise CurrencyInvalidDivision(self, other)
        if other == 0:
            raise ZeroDivisionError()
        return self.__class__(
            amount=self._amount.__mod__(
                CurrencyContext.create_decimal(str(other))),
            alpha_code=self._alpha_code,
            numeric_code=self._numeric_code,
            symbol=self._symbol,
            symbol_ahead=self._symbol_ahead,
            symbol_separator=self._symbol_separator,
            decimal_places=self._decimal_places,
            decimal_sign=self._decimal_sign,
            grouping_sign=self._grouping_sign,
            convertion=self._convertion,
            international=self._international)

    def __mul__(self, other: Any) -> 'Currency':
        """Returns the multiplication by `other`.

        Args:
            other (Numerical): amount to multiply by.

        Returns:
            Currency: Result of the multiplication operation.

        Raises:
            CurrencyInvalidMultiplication: If `other` not of types
                `int`, `float` or `Decimal`.
        """
        if not isinstance(other, (int, float, Decimal)):
            raise CurrencyInvalidMultiplication(self, other)
        return self.__class__(
            amount=self._amount * CurrencyContext.create_decimal(str(other)),
            alpha_code=self._alpha_code,
            numeric_code=self._numeric_code,
            symbol=self._symbol,
            symbol_ahead=self._symbol_ahead,
            symbol_separator=self._symbol_separator,
            decimal_places=self._decimal_places,
            decimal_sign=self._decimal_sign,
            grouping_sign=self._grouping_sign,
            convertion=self._convertion,
            international=self._international)

    def __ne__(self, other: Any) -> bool:
        """Checks if two currencies are different.

        Args:
            other (Any): Currency to compare to.

        Returns:
            bool: True if different. False otherwise.
        """
        return not self == other

    def __neg__(self) -> 'Currency':
        """Returns a currency with the sign switched.

        Returns:
            Currency: Currency with the sign switched.
        """
        return self.__class__(
            amount=self._amount.__neg__(),
            alpha_code=self._alpha_code,
            numeric_code=self._numeric_code,
            symbol=self._symbol,
            symbol_ahead=self._symbol_ahead,
            symbol_separator=self._symbol_separator,
            decimal_places=self._decimal_places,
            decimal_sign=self._decimal_sign,
            grouping_sign=self._grouping_sign,
            convertion=self._convertion,
            international=self._international)

    def __pos__(self) -> 'Currency':
        """Returns a copy of self.

        Returns:
            Currency: copy of this.
        """
        return self.__class__(
            amount=self._amount.__pos__(),
            alpha_code=self._alpha_code,
            numeric_code=self._numeric_code,
            symbol=self._symbol,
            symbol_ahead=self._symbol_ahead,
            symbol_separator=self._symbol_separator,
            decimal_places=self._decimal_places,
            decimal_sign=self._decimal_sign,
            grouping_sign=self._grouping_sign,
            convertion=self._convertion,
            international=self._international)

    def __reduce__(self) -> tuple[type, tuple[Any, ...]]:
        """.

        Returns:
            tuple[type, tuple[Any, ...]]: pickle representation of this
                currency.
        """
        return (
            self.__class__,
            (
                self._amount,
                self._alpha_code,
                self._numeric_code,
                self._symbol,
                self._symbol_ahead,
                self._symbol_separator,
                self._decimal_places,
                self._decimal_sign,
                self._grouping_sign,
                self._convertion,
                self._international))

    def __repr__(self) -> str:
        """String representation of this class.

        Returns:
            str: representation
        """
        return (
            f'{self.__class__.__name__}('
            f'amount: {self._amount}, '
            f'alpha_code: "{self._alpha_code}", '
            f'symbol: "{self._symbol}", '
            f'symbol_ahead: {self._symbol_ahead}, '
            f'symbol_separator: "{self._symbol_separator}", '
            f'numeric_code: "{self._numeric_code}", '
            f'decimal_places: "{self._decimal_places}", '
            f'decimal_sign: "{self._decimal_sign}", '
            f'grouping_sign: "{self._grouping_sign}", '
            f'convertion: "{self._convertion}", '
            f'international: {self._international})')

    def __round__(self, precision: Optional[int] = None) -> 'Currency':
        """Round to the nearest integer, or to a given precision.

        Args:
            precision (int, optional): Precision. Defaults to `None`.

        Returns:
            Currency: rounded currency value.
        """
        return self.__class__(
            amount=(self._amount.__round__(precision) if precision
                    else self._amount.__round__()),
            alpha_code=self._alpha_code,
            numeric_code=self._numeric_code,
            symbol=self._symbol,
            symbol_ahead=self._symbol_ahead,
            symbol_separator=self._symbol_separator,
            decimal_places=self._decimal_places,
            decimal_sign=self._decimal_sign,
            grouping_sign=self._grouping_sign,
            convertion=self._convertion,
            international=self._international)

    def __str__(self) -> str:
        """String value of this class.

        Returns:
            str: value
        """
        p = self._decimal_places
        converted = f'{round(self._amount, p):,.{p}f}'
        if self._international:
            return f'{self._alpha_code} {converted}'
        if self._convertion:
            t = dict(zip('0123456789-', self._convertion))
            converted = ''.join([t.get(c, c) for c in converted])
        converted = converted.replace('.', 'X').replace(
            ',', self._grouping_sign).replace('X', self._decimal_sign)
        if self._symbol_ahead:
            return f'{self._symbol}{self._symbol_separator}{converted}'
        return f'{converted}{self._symbol_separator}{self._symbol}'

    def __sub__(self, other: Any) -> 'Currency':
        """Subtract `other` from this.

        Args:
            other (multicurrency.currency.Currency): Currency to subtract.

        Returns:
            Currency: result of the subtraction operation.

        Raises:
            CurrencyTypeException: If `other` not instance of
                'Currency'.
            CurrencyMismatchException: If `other.alpha_code` is
                differente from `alpha_code`.
        """
        if not isinstance(other, self.__class__):
            raise CurrencyTypeException(self, other)
        if self._alpha_code != other.alpha_code:
            raise CurrencyMismatchException(self._alpha_code, other.alpha_code)
        return self.__class__(
            amount=self._amount - other.amount,
            alpha_code=self._alpha_code,
            numeric_code=self._numeric_code,
            symbol=self._symbol,
            symbol_ahead=self._symbol_ahead,
            symbol_separator=self._symbol_separator,
            decimal_places=self._decimal_places,
            decimal_sign=self._decimal_sign,
            grouping_sign=self._grouping_sign,
            convertion=self._convertion,
            international=self._international)

    def __truediv__(self, other: Any) -> 'Currency':
        """Divide this currency by `other`.

        Args:
            other (Numerical): amount to divide by.

        Returns:
            Currency: result of the division operation.

        Raises:
            CurrencyInvalidDivision: If `other` not of types
                `int`, `float` or `Decimal`.
            ZeroDivisionError: If dividing by zero
        """
        if not isinstance(other, (int, float, Decimal)):
            raise CurrencyInvalidDivision(self, other)
        if other == 0:
            raise ZeroDivisionError()
        return self.__class__(
            amount=self._amount.__truediv__(
                CurrencyContext.create_decimal(str(other))),
            alpha_code=self._alpha_code,
            numeric_code=self._numeric_code,
            symbol=self._symbol,
            symbol_ahead=self._symbol_ahead,
            symbol_separator=self._symbol_separator,
            decimal_places=self._decimal_places,
            decimal_sign=self._decimal_sign,
            grouping_sign=self._grouping_sign,
            convertion=self._convertion,
            international=self._international)

    __rmul__: 'Currency' = __mul__

    def is_signed(self) -> bool:
        """Check if the value of this class is preceded with the minus
        sign.

        Returns:
            bool: True if the value is negative. False otherwise.
        """
        return self._amount.is_signed()

    def pstr(self, precision: int = 2) -> str:
        """String value of this class formated with
            `CurrencyContext` precision value (`prec`).

        Args:
            precision (int, optional): Precision. Defaults to `2`.
                Values lower than 0 (zero) will be converted to 0
                (zero).

        Returns:
            str: value
        """
        p = max(precision, 0)
        converted = f'{round(self._amount, p):,.{p}f}'
        if self._international:
            return f'{self._alpha_code} {converted}'
        if self._convertion:
            t = dict(zip('0123456789-', self._convertion))
            converted = ''.join([t.get(c, c) for c in converted])
        converted = converted.replace('.', 'X').replace(
            ',', self._grouping_sign).replace('X', self._decimal_sign)
        if self._symbol_ahead:
            return f'{self._symbol}{self._symbol_separator}{converted}'
        return f'{converted}{self._symbol_separator}{self._symbol}'

    @property
    def amount(self) -> Decimal:
        """Decimal: amount."""
        return self._amount

    @property
    def numeric_code(self) -> str:
        """str: numeric_code."""
        return self._numeric_code

    @property
    def alpha_code(self) -> str:
        """str: alpha_code."""
        return self._alpha_code

    @property
    def convertion(self) -> str:
        """str: convertion."""
        return self._convertion

    @property
    def decimal_places(self) -> int:
        """int: decimal_places."""
        return self._decimal_places

    @property
    def decimal_sign(self) -> str:
        """str: decimal_sign."""
        return self._decimal_sign

    @property
    def grouping_sign(self) -> str:
        """str: grouping_sign."""
        return self._grouping_sign

    @property
    def international(self) -> bool:
        """bool: international."""
        return self._international

    @property
    def symbol(self) -> str:
        """str: symbol."""
        return self._symbol

    @property
    def symbol_ahead(self) -> bool:
        """bool: symbol_ahead."""
        return self._symbol_ahead

    @property
    def symbol_separator(self) -> str:
        """str: symbol_separator."""
        return self._symbol_separator
