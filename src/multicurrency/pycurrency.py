# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Currency representation.

Representation of a currency value.

Simple usage example:

    >>> from multicurrency import Currency
    >>> euro = Currency(amount=1, alpha_code='EUR', symbol='€')
    >>> print(euro)
    1.00€

## Formatting

The `multicurrency.pycurrency.Currency` class allows you to create
and customize your own value formatting behaviors using the same
implementation as the built-in `format()` method.

The specification for the formatting feature is as follows:

    [dp][ds][gs][gp][spec]

The meaning of the various alignment options is as follows:

| Option | Type   | Meaning                                                                                                                    |
| :----- | :----- | :------------------------------------------------------------------------------------------------------------------------- |
| [dp]   | int+   | The number of decimal places (integer number with one or more digits). Must be grater or equal to 0 (zero).                |
| [ds]   | str{1} | The decimal sign (single non-digit character).                                                                             |
| [gs]   | str{1} | The grouping sign (single non-digit character).                                                                            |
| [gp]   | int+   | The number of digits to group the number by (integer number with one or more digits). Must be grater or equal to 0 (zero). |
| [spec] | str    | The formatting spec (a strig with the order of currency parts).                                                            |

All fields are optional although for the first four fields when setting
one the fields on the left of that are required to be set as well.

The available string currency parts for `[spec]` are:

| Part | Meaning                                                                                                                            |
|:-----|:-----------------------------------------------------------------------------------------------------------------------------------|
| %a   | The currency's amount as seen in the default representation of the currency (the numeral system of the currency's country).        |
| %A   | The currency's amount in (western) arabic numerals.                                                                                |
| %c   | The currency's alpha code (as seen on the international representation of the currency).                                           |
| %s   | The currency's symbol.                                                                                                             |
| %S   | The currency's localized symbol.                                                                                                   |
| %u   | The currency's unsign amount as seen in the default representation of the currency (the numeral system of the currency's country). |
| %U   | The currency's unsign amount in (western) arabic numerals.                                                                         |
| %-   | The currency's amount sign.                                                                                                        |
| %%   | The `%` symbol.                                                                                                                    |

Basic examples of how to use the `multicurrency.pycurrency.Currency`
formatting feature:

    >>> from multicurrency import Currency
    >>> euro = Currency(1000000*(1/7), alpha_code='EUR', symbol='€')
    >>> # Using the built-in `format()` method
    >>> format(euro, '4%a')
    '142,857.1429'
    >>> # Using the `'new' string` formating method
    >>> '{:4%a}'.format(euro)
    '142,857.1429'
    >>> # Using the `f-string` method
    >>> f'{euro:4%a}'
    '142,857.1429'

## Supported operations

Several operations are supported by the
`multicurrency.pycurrency.Currency` type.

### Absolute

Produces a new `multicurrency.pycurrency.Currency` with the absolute
value of the given `multicurrency.pycurrency.Currency`.

    >>> from multicurrency import Currency
    >>> c = abs(Currency(amount=-2))
    >>> print(c)
    2.00

### Addiction

Addiction is supported only between `multicurrency.pycurrency.Currency`
of the same type.

    >>> from multicurrency import Currency
    >>> c1 = Currency(amount=2)
    >>> c2 = Currency(amount=3)
    >>> print(c1 + c2)
    5.00

### Boolean

Produces 'True' for values of `multicurrency.pycurrency.Currency` other
than zero. 'False' otherwise

    >>> from multicurrency import Currency
    >>> bool(Currency(amount=0))
    False
    >>> bool(Currency(amount=1))
    True

### Ceiling

Produces a `multicurrency.pycurrency.Currency` rounded up to the nearest
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

Produces a `multicurrency.pycurrency.Currency` with the value of
the division of the currency by either an `int`, `float`, or
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

Produces a `multicurrency.pycurrency.Currency` rounded down to the
nearest integer.

    >>> from multicurrency import Currency
    >>> from math import floor
    >>> print(floor(Currency(1/7)))
    0.00

### Floordiv

Produces a `multicurrency.pycurrency.Currency` with the integral part
of the quotient of the division of the currency by either an `int`,
`float`, or `decimal.Decimal`.

    >>> from multicurrency import Currency
    >>> fd = Currency(7) // 2
    >>> print(fd)
    3.00

### Hash

Produces a hash representation of the
`multicurrency.pycurrency.Currency`.

    >>> from multicurrency import Currency
    >>> c = Currency(7, alpha_code='EUR', numeric_code='978')
    >>> hash(c) # doctest: +SKIP
    1166476495300974230

### Int

Produces an `int` with the value of the currency amount.

    >>> from multicurrency import Currency
    >>> int(Currency(1/7))
    0

### Mod

Produces a `multicurrency.pycurrency.Currency` with the value of the
remainder of the division of the currency by either an `int`, `float`,
or `decimal.Decimal`.

    >>> from multicurrency import Currency
    >>> m = Currency(7) % 2
    >>> print(m)
    1.00

### Multiplication

Multiplication is supported between `multicurrency.pycurrency.Currency`
and `int`, `float`, or `decimal.Decimal`.

    >>> from multicurrency import Currency
    >>> c = Currency(amount=2)
    >>> print(c * 2.5)
    5.00

### Round

Produces a `multicurrency.pycurrency.Currency` with the amount of the
currency rounded to a given precision.

    >>> from multicurrency import Currency
    >>> r = round(Currency(1/7), 3)
    >>> print(r.amount)
    0.143

### Subtraction

Subtraction is supported only between `multicurrency.pycurrency.Currency`
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

from decimal import Decimal
from re import (
    escape as _escape,
    compile as _compile,
    match as _match,
    sub as _sub)
from typing import Optional, Tuple, Union
from multicurrency.exceptions import (
    CurrencyInvalidDivision,
    CurrencyInvalidFormat,
    CurrencyInvalidMultiplication,
    CurrencyMismatchException,
    CurrencyTypeException)


Numerical = Union[int, float, Decimal]


class Currency:
    """Currency representation.

    This class is a generic representation of Money, a certain amount
    of currency value of a particular country.

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

    The `convertion` string, when set, will be used to replace the
    Western Arabic numerals - as well as the symbols - with the
    equivalent ones on the currency language. The string must be
    created with the numbers from 0 (zero) to 9 (nine) followed by the
    minus sign without any separation mark (e.g.: '0123456789-').

    The `pattern` string, when set, will have to be in the form
    `[dp][ds][gs][gp][format]`.

    The `pattern` fields are:
        [dp] (int+): The number of decimal places (integer number
            with one or more digits). Must be grater or equal to 0
            (zero).
        [ds] (char{1}): The decimal sign (single non-digit
            character).
        [gs] (char{1}): The grouping sign (single non-digit
            character).
        [gp] (int+): The number of digits to group the number by
            (integer number with one or more digits). Must be grater
            or equal to 0 (zero).
        [format] (str): The formatting pattern (a string with the
            order of the currency parts).

    The currency parts that can be used on the `format` string are:
        %a: The currency's amount as seen in the default
            representation of the currency (the numeral system of
            the currency's country).
        %A: The currency's amount in (western) arabic numerals.
        %c: The currency's alpha code (as seen on the international
            representation of the currency).
        %s: The currency's symbol.
        %S: The currency's localized symbol.
        %u: The currency's unsign amount as seen in the default
            representation of the currency (the numeral system of
            the currency's country).
        %U: The currency's unsign amount in (western) arabic numerals.
        %-: The currency's amount sign.
        %%: The `%` symbol.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        alpha_code (str, optionsl): Represented currency alpha code.
            Defaults to ''.
        numeric_code (str, optional): Represented currency numeric
            code. Defaults to 0.
        symbol (str, optional): Represented currency symbol. Defaults
            to ''.
        localized_symbol ((str, optional)): Represented currency
            localizedsymbol. Defaults to the value of `symbol`.
        convertion (str, optional): String with the numbers from 0 to 9
            followed by the minus ('-') sign. Defaults to ''.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%A%s'.
    """

    __slots__ = (
        '_amount',
        '_info')

    def __new__(
            cls,
            amount: Union[str, int, float, Decimal],
            alpha_code: Optional[str] = '',
            numeric_code: Optional[str] = '0',
            symbol: Optional[str] = '',
            localized_symbol: Optional[str] = '',
            convertion: Optional[str] = '',
            pattern: Optional[str] = r'2.,3%a%s') -> 'Currency':
        """Class creator.

        Returns:
            Currency: new opbject.

        Raises:
            CurrencyInvalidFormat: If `pattern` is not valid.
        """
        self = object.__new__(cls)
        self._amount = Decimal(amount)
        regxpr = (
            r'^(?P<decimal_places>\d+)'
            r'(?P<decimal_sign>[^\d%])'
            r'(?P<grouping_sign>[^\d%])'
            r'(?P<grouping_places>\d+)'
            r'(?P<format>.+)$')
        if _match(regxpr, pattern):
            self._info = (
                alpha_code,
                numeric_code,
                symbol,
                localized_symbol,
                convertion,
                pattern)
        else:
            raise CurrencyInvalidFormat()
        return self

    def __abs__(self) -> 'Currency':
        """Returns the absolute value.

        Returns:
            Currency: absolute value.
        """
        return self.__recreate__(abs(self._amount))

    def __add__(self, other: object) -> 'Currency':
        """Adds `other` to this.

        Args:
            other (object): Currency to add.

        Returns:
            Currency: result of the adding operation.

        Raises:
            CurrencyTypeException: If `other` not instance of
                'Currency'.
            CurrencyMismatchException: If `other.alpha_code` is
                differente from `alpha_code`.
        """
        if not isinstance(other, Currency):
            raise CurrencyTypeException()
        if self._info[0] != other.alpha_code:
            raise CurrencyMismatchException()
        return self.__recreate__(self._amount + other.amount)

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
        return self.__recreate__(self._amount.__ceil__())

    def __copy__(self) -> 'Currency':
        """Returns a copy of self.

        Returns:
            Currency: copy of this.
        """
        return self.__recreate__(self._amount)

    def __divmod__(self, other: Numerical) -> Tuple['Currency', 'Currency']:
        """Returns a pair with the quocient and remaider of the
        division by `other`.

        Args:
            other (Numerical): amount to divide by.

        Returns:
            Tuple[Currency, Currency]: quotient, remainder.

        Raises:
            CurrencyInvalidDivision: If `other` not of types
                `int`, `float` or `Decimal`.
            ZeroDivisionError: If dividing by zero
        """
        if not isinstance(other, (int, float, Decimal)):
            raise CurrencyInvalidDivision()
        if other == 0:
            raise ZeroDivisionError()
        quotient, remainder = self._amount.__divmod__(Decimal(other))
        return (
            self.__recreate__(quotient),
            self.__recreate__(remainder))

    def __eq__(self, other: object) -> bool:
        """Checks if two currencies are equal.

        Args:
            other (object): Currency to compare to.

        Returns:
            bool: True if equal. False otherwise.
        """
        if isinstance(other, self.__class__):
            return (
                (self._amount, self._info[0]) ==
                (other.amount, other.alpha_code))
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
        return self.__recreate__(self._amount.__floor__())

    def __floordiv__(self, other: Numerical) -> 'Currency':
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
            raise CurrencyInvalidDivision()
        if other == 0:
            raise ZeroDivisionError()
        return self.__recreate__(
            self._amount.__floordiv__(Decimal(other)))

    def __format__(self, fmt: str = '') -> str:
        """Returns the result of applying the formating specifications
        to the currency value.

        The supported formating specifications are:
            '[dp][ds][gs][gp][pattern]'

        The fields are:
            [dp] (int+): The number of decimal places (integer number
                with one or more digits).
            [ds] (char{1}): The decimal sign (single non-digit
                character).
            [gs] (char{1}): The grouping sign (single non-digit
                character).
            [gp] (int+): The number of digits to group the number by
                (integer number with one or more digits).
            [pattern] (str): The formatting pattern (a string with the
                order of currency parts).

        The currency parts that can be used on the `pattern` string are:
            %a: The currency's amount as seen in the default
                representation of the currency (the numeral system of
                the currency's country).
            %A: The currency's amount in (western) arabic numerals.
            %c: The currency's alpha code (as seen on the international
                representation of the currency).
            %s: The currency's symbol.
            %S: The currency's localized symbol.
            %u: The currency's unsign amount as seen in the default
                representation of the currency (the numeral system of
                the currency's country).
            %U: The currency's unsign amount in (western) arabic numerals.
            %-: The currency's amount sign.
            %%: The `%` symbol.

        All fields are optional although for the first four fields when
        setting one the fields on the left of that are required to be
        set as well.

        Args:
            fmt (str): formating specifications.

        Returns:
            str: Formated currency value.

        Raises:
            TypeError: If `fmt` not of type `str`.
        """
        if not isinstance(fmt, str):
            raise TypeError(f'must be str, not {type(fmt).__qualname__}.')
        regxpr = (
            r'^(?P<decimal_places>\d+)?'
            r'(?P<decimal_sign>[^\d%])?'
            r'(?P<grouping_sign>[^\d%])?'
            r'(?P<grouping_places>\d+)?'
            r'(?P<format>.+)?$')
        values = _match(regxpr, self._info[5]).groupdict()
        matches = _match(regxpr, fmt.strip())
        new_values = {k: v for k, v in matches.groupdict().items() if v}
        values = {**values, **new_values}
        decimal_places = int(values['decimal_places'])
        decimal_sign = values['decimal_sign']
        grouping_sign = values['grouping_sign']
        grouping_places = int(values['grouping_places'])
        currency_format = values['format']
        # parts = str(round(self._amount, decimal_places)).split('.')
        parts = f'{round(self._amount, decimal_places):f}'.split('.')
        parts[0] = _sub(
            rf'(\d)(?=(\d{{{grouping_places or -1}}})+$)',
            r'\1,',
            parts[0])
        amount = '.'.join(parts)
        converted = amount
        if self._info[4]:
            translator = dict(zip('0123456789-', self._info[4]))
            converted = ''.join([translator.get(c, c) for c in converted])
        converted = converted.replace('.', 'X').replace(
            ',', grouping_sign).replace('X', decimal_sign)
        amount_unsign = amount.lstrip('-')
        converted_unsign = converted.lstrip('-')
        rep = {
            '%s': self._info[2],
            '%S': self._info[3],
            '%c': self._info[0],
            '%a': converted,
            '%A': amount,
            '%u': converted_unsign,
            '%U': amount_unsign,
            '%-': '-' * self._amount.is_signed(),
            '%%': '%'}
        rep = dict((_escape(k), v) for k, v in rep.items())
        pattern = _compile('|'.join(rep.keys()))
        formatted = pattern.sub(
            lambda m: rep[_escape(m.group(0))],
            currency_format)
        return formatted

    def __ge__(self, other: object) -> bool:
        """Checks if self is greater or equal than `other`.

        Args:
            other (object): Currency to compare to.

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
            raise CurrencyTypeException()
        if self._info[0] != other.alpha_code:
            raise CurrencyMismatchException()
        return self._amount >= other.amount

    def __gt__(self, other: object) -> bool:
        """Checks if self is greater than `other`.

        Args:
            other (object): Currency to compare to.

        Returns:
            bool: True if is greater than `other`. False otherwise`.

        Raises:
            CurrencyTypeException: If `other` not instance of
                'Currency'.
            CurrencyMismatchException: If `other.alpha_code` is
                differente from `alpha_code`.
        """
        if not isinstance(other, self.__class__):
            raise CurrencyTypeException()
        if self._info[0] != other.alpha_code:
            raise CurrencyMismatchException()
        return self._amount > other.amount

    def __hash__(self) -> int:
        """Hash representation of this class.

        Returns:
            int: Hash value.
        """
        return hash((
            self.__class__,
            self._amount,
            self._info[0],
            self._info[1]))

    def __int__(self) -> int:
        """Integer representation.

        Returns:
            int: The currency value as an integer.
        """
        return int(self._amount)

    def __le__(self, other: object) -> bool:
        """Checks if self is less or equal than `other`.

        Args:
            other (object): Currency to compare to.

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
            raise CurrencyTypeException()
        if self._info[0] != other.alpha_code:
            raise CurrencyMismatchException()
        return self._amount <= other.amount

    def __lt__(self, other: object) -> bool:
        """Checks if self is less than `other`.

        Args:
            other (object): Currency to compare to.

        Returns:
            bool: True if is less than `other`. False otherwise.

        Raises:
            CurrencyTypeException: If `other` not instance of
                'Currency'.
            CurrencyMismatchException: If `other.alpha_code` is
                differente from `alpha_code`.
        """
        if not isinstance(other, self.__class__):
            raise CurrencyTypeException()
        if self._info[0] != other.alpha_code:
            raise CurrencyMismatchException()
        return self._amount < other.amount

    def __mod__(self, other: Numerical) -> 'Currency':
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
            raise CurrencyInvalidDivision()
        if other == 0:
            raise ZeroDivisionError()
        return self.__recreate__(self._amount.__mod__(Decimal(other)))

    def __mul__(self, other: Numerical) -> 'Currency':
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
            raise CurrencyInvalidMultiplication()
        return self.__recreate__(self._amount.__mul__(Decimal(other)))

    def __ne__(self, other: object) -> bool:
        """Checks if two currencies are different.

        Args:
            other (object): Currency to compare to.

        Returns:
            bool: True if different. False otherwise.
        """
        return not self == other

    def __neg__(self) -> 'Currency':
        """Returns a currency with the sign switched.

        Returns:
            Currency: Currency with the sign switched.
        """
        return self.__recreate__(self._amount.__neg__())

    def __pos__(self) -> 'Currency':
        """Returns a copy of self.

        Returns:
            Currency: copy of this.
        """
        return self.__recreate__(self._amount.__pos__())

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]) -> 'Currency':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, *self._info)

    def __reduce__(self) -> Tuple[type, Tuple[object, ...]]:
        """Returns a Tuple with this class "reduce value".

        Returns:
            Tuple[type, Tuple[object, ...]]: pickle representation of
                this currency.
        """
        return (self.__class__, (self._amount, *self._info))

    def __repr__(self) -> str:
        """String representation of this class.

        Returns:
            str: representation
        """
        return (
            f'{self.__class__.__name__}('
            f'amount: {self._amount}, '
            f'alpha_code: "{self._info[0]}", '
            f'numeric_code: "{self._info[1]}", '
            f'symbol: "{self._info[2]}", '
            f'localized_symbol: "{self._info[3]}", '
            f'convertion: "{self._info[4]}", '
            rf'pattern: "{self._info[5]}")')

    def __round__(self, precision: Optional[int] = None) -> 'Currency':
        """Round to the nearest integer, or to a given precision.

        Args:
            precision (int, optional): Precision. Defaults to `None`.

        Returns:
            Currency: rounded currency value.
        """
        return self.__recreate__(
            (self._amount.__round__(precision) if precision
                else self._amount.__round__()))

    def __rsub__(self, other: object) -> 'Currency':
        """Subtract this from `other`.

        Args:
            other (object): Currency to subtract from.

        Returns:
            Currency: result of the subtraction operation.

        Raises:
            CurrencyTypeException: If `other` not instance of
                'Currency'.
            CurrencyMismatchException: If `other.alpha_code` is
                differente from `alpha_code`.
        """
        if not isinstance(other, self.__class__):
            raise CurrencyTypeException()
        if self._info[0] != other.alpha_code:
            raise CurrencyMismatchException()
        return self.__recreate__(other.amount - self._amount)

    def __str__(self) -> str:
        """String value of this class.

        Returns:
            str: value
        """
        return self.__format__()

    def __sub__(self, other: object) -> 'Currency':
        """Subtract `other` from this.

        Args:
            other (object): Currency to subtract.

        Returns:
            Currency: result of the subtraction operation.

        Raises:
            CurrencyTypeException: If `other` not instance of
                'Currency'.
            CurrencyMismatchException: If `other.alpha_code` is
                differente from `alpha_code`.
        """
        if not isinstance(other, self.__class__):
            raise CurrencyTypeException()
        if self._info[0] != other.alpha_code:
            raise CurrencyMismatchException()
        return self.__recreate__(self._amount - other.amount)

    def __truediv__(self, other: Numerical) -> 'Currency':
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
        return self.__recreate__(
            self._amount.__truediv__(Decimal(other)))

    __deepcopy__: 'Currency' = __copy__
    __rmul__: 'Currency' = __mul__

    def international(self, precision: int = None) -> str:
        """String value of this class formated with the alpha code.

        Args:
            precision (int, optional): Precision. Defaults to the value
                prensent in the currency `pattern`. Values lower than 0
                (zero) will be converted to 0 (zero).

        Returns:
            str: value
        """
        if precision is None:
            regxpr = (
                r'^(?P<decimal_places>\d+)?'
                r'(?P<decimal_sign>[^\d%])?'
                r'(?P<grouping_sign>[^\d%])?'
                r'(?P<grouping_places>\d+)?'
                r'(?P<format>.+)?$')
            values = _match(regxpr, self._info[5]).groupdict()
            decimal_places = int(values['decimal_places'])
        else:
            decimal_places = max(precision, 0)
        # parts = str(round(self._amount, decimal_places)).split('.')
        parts = f'{round(self._amount, decimal_places):f}'.split('.')
        parts[0] = _sub(r'(\d)(?=(\d{3})+$)', r'\1,', parts[0])
        amount = '.'.join(parts)
        return f'{amount} {self._info[0]}'

    def is_signed(self) -> bool:
        """Check if the value of this class is preceded with the minus
        sign.

        Returns:
            bool: True if the value is negative. False otherwise.
        """
        return self._amount.is_signed()

    def localized(self, precision: int = None) -> str:
        """String value of this class formated with the
            `localized_symbol`.

        Args:
            precision (int, optional): Precision. Defaults to the value
                prensent in the currency `pattern`. Values lower than 0
                (zero) will be converted to 0 (zero).

        Returns:
            str: value
        """
        fmt = self._info[5]
        if precision is not None:
            precision = max(precision, 0)
            fmt = _sub(r'^\d+', f'{precision}', fmt)
        return format(self, fmt.replace('%s', '%S'))

    def precision(self, precision: int = None) -> str:
        """String value of this class formated with the `precision`
            value.

        Args:
            precision (int, optional): Precision. Defaults to the value
                prensent in the currency `pattern`. Values lower than 0
                (zero) will be converted to 0 (zero).

        Returns:
            str: value
        """
        if precision is not None:
            precision = max(precision, 0)
            return format(self, f'{precision}')
        return format(self)

    @property
    def amount(self) -> Decimal:
        """Decimal: amount."""
        return self._amount

    @property
    def alpha_code(self) -> str:
        """str: alpha_code."""
        return self._info[0]

    @property
    def numeric_code(self) -> str:
        """int: numeric_code."""
        return self._info[1]

    @property
    def symbol(self) -> str:
        """str: symbol."""
        return self._info[2]

    @property
    def localized_symbol(self) -> str:
        """str: localized_symbol."""
        return self._info[3]

    @property
    def convertion(self) -> str:
        """str: convertion."""
        return self._info[4]

    @property
    def pattern(self) -> str:
        """str: pattern."""
        return self._info[5]
