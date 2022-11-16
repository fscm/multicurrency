# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Currency system.

The multicurrency module provides support for currency operations. It
supports several different currencies.

For a list of supported currencies see the `multicurrency.currencies`
submodule.

The currencies supported by this module were created with information
(alphabetic code, numeric code, and minor unit size) from ISO-4217
except for the cryptocurrencies that are not represented in the
ISO-4217. Information on cryptocurrencies was collected on other
sources.

## Usage

Simple usage example:

    >>> from multicurrency import Euro
    >>> euro = Euro(1000)
    >>> print(euro)
    1.000,00 €
    >>> print(euro + Euro(0.50))
    1.000,50 €

Unsupported currencies can be represented by creating a generic
`multicurrency.pycurrency.Currency` object with the desired settings.

    >>> from multicurrency import Currency
    >>> bitcoin = Currency(
    ...     amount=1000,
    ...     alpha_code='XBT',
    ...     numeric_code='0',
    ...     symbol='₿',
    ...     localized_symbol='₿',
    ...     convertion='',
    ...     pattern='8.,3%-%s%u')
    >>> print(bitcoin)
    ₿1,000.00000000

To help working with unsupported currencies the settings can be defined
in a dictionary and used when needed:

    >>> from multicurrency import Currency
    >>> settings = {
    ...     'alpha_code':'XBT',
    ...     'numeric_code':'0',
    ...     'symbol':'₿',
    ...     'localized_symbol':'₿',
    ...     'convertion':'',
    ...     'pattern':'8.,3%-%s%u'}
    >>> bitcoin = Currency(1000, **settings)
    >>> print(bitcoin)
    ₿1,000.00000000

Currencies can also be represented with the ISO 4217 three-letter code
instead of the `symbol`.

    >>> from multicurrency import Euro
    >>> euro = Euro(1000)
    >>> print(euro.international())
    1,000.00 EUR

## Localization

The multicurrency library allows you to obtain a localized version of
the currency representation:

    >>> from multicurrency import TaiwanDollar, USDollar
    >>> tw_dollar = TaiwanDollar('27.65')
    >>> us_dollar = USDollar('1')
    >>> print(us_dollar.localized(), '=', tw_dollar.localized())
    US$1.00 = TW$27.65

## Precision

The multicurrency library uses `decimal.Decimal` (to represent the
`amount` value) which has a user alterable precision and rounding
settings (defaulting to `28` places and `ROUND_HALF_EVEN` respectively).

To change the default precision value of a currency one can simply
use the `precision` method provided by that currency (up to the value
of the `decimal.Decimal` precision minus 3):

    >>> from multicurrency import Euro
    >>> for precision in [-1, 0, 1, 2, 3, 4, 5, 6, 25]:
    ...     result = Euro(1_000/7)
    ...     print(result.precision(precision))
    143 €
    143 €
    142,9 €
    142,86 €
    142,857 €
    142,8571 €
    142,85714 €
    142,857143 €
    142,8571428571428612031013472 €

If a larger precision is required the default `decimal.Context`
precision value will have to be changed:

    >>> from decimal import localcontext
    >>> from multicurrency import Euro
    >>> with localcontext() as context:
    ...     precision = 50
    ...     context.prec = precision + 3
    ...     result = Euro(1_000/7)
    ...     print(result.precision(50))
    142,85714285714286120310134720057249069213867187500000 €

To change the rounding method the default `decimal.Context` rounding
value needs to be changed:

    >>> from decimal import localcontext
    >>> from multicurrency import Euro
    >>> with localcontext() as context:
    ...     for rounding in [
    ...             'ROUND_CEILING',
    ...             'ROUND_DOWN',
    ...             'ROUND_FLOOR',
    ...             'ROUND_HALF_DOWN',
    ...             'ROUND_HALF_EVEN',
    ...             'ROUND_HALF_UP',
    ...             'ROUND_UP',
    ...             'ROUND_05UP']:
    ...         context.rounding = rounding
    ...         result = Euro(1_000/7)
    ...         print(f'{rounding:16}', result.precision(3))
    ROUND_CEILING    142,858 €
    ROUND_DOWN       142,857 €
    ROUND_FLOOR      142,857 €
    ROUND_HALF_DOWN  142,857 €
    ROUND_HALF_EVEN  142,857 €
    ROUND_HALF_UP    142,857 €
    ROUND_UP         142,858 €
    ROUND_05UP       142,857 €

## Formatting

The `multicurrency.pycurrency.Currency` class allows you to create
and customize your own value formatting behaviors using the same
implementation as the built-in `format()` method.

The specification for the formatting feature is as follows:

    `[dp][ds][gs][gp][format]`

The meaning of the various alignment options is as follows:

| Option   | Type    | Meaning                                                                                                                   |
|:---------|:--------|:--------------------------------------------------------------------------------------------------------------------------|
| [dp]     | int+    | The number of decimal places (integer number with one or more digits). Must be grater or equal to 0 (zero.)               |
| [ds]     | char{1} | The decimal sign (single non-digit character).                                                                            |
| [gs]     | char{1} | The grouping sign (single non-digit character).                                                                           |
| [gp]     | int+    | The number of digits to group the number by (integer number with one or more digits).Must be grater or equal to 0 (zero.) |
| [format] | str     | The formatting pattern (a string with the order of the currency parts).                                                   |

All fields are optional although for the first four fields when setting
one the fields on the left of that are required to be set as well.

The available string currency parts for `[format]` are:

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

    Using the built-in `format()` method

        >>> from multicurrency import Euro
        >>> euro = Euro(1000000*(1/7))
        >>> format(euro, '4%a')
        '142.857,1429'

    Using the `'new' string` formating method

        >>> from multicurrency import Euro
        >>> euro = Euro(1000000*(1/7))
        >>> '{:4%a}'.format(euro)
        '142.857,1429'

    Using the `f-string` method

        >>> from multicurrency import Euro
        >>> euro = Euro(1000000*(1/7))
        >>> f'{euro:4%a}'
        '142.857,1429'

Some more examples of the `multicurrency.pycurrency.Currency` formatting
feature usage (using the `f-string` method):

    >>> from multicurrency import Euro
    >>> euro = Euro(1000000*(1/7))
    >>> print(euro)
    142.857,14 €

    >>> print(f'{euro}')
    142.857,14 €

    >>> print(f'{euro:_}')
    142.857_14 €

    >>> print(f'{euro:.,}')
    142,857.14 €

    >>> print(f'{euro:4.,}')
    142,857.1429 €

    >>> print(f'{euro:4.,2}')
    14,28,57.1429 €

    >>> print(f'{euro:_2}')
    14.28.57_14 €

    >>> print(f'{euro:.,2}')
    14,28,57.14 €

    >>> print(f'{euro:3%a}')
    142.857,143

    >>> print(f'{euro:3_%a}')
    142.857_143

    >>> print(f'{euro:3#_%a}')
    142_857#143

    >>> print(f'{euro:3.,2%a}')
    14,28,57.143

    >>> print(f'{euro:3.,4%a}')
    14,2857.143

    >>> print(f'{euro:.,4%a}')
    14,2857.14

    >>> print(f'{euro:%a}')
    142.857,14

    >>> print(f'{euro:%a\u00A0%c}')
    142.857,14 EUR

    >>> print(f'{euro:%a %c}')
    142.857,14 EUR

## Operations

Several operations are supported by the several library classes.

* Absolute

    Produces the absolute value of a given currency.

        >>> from multicurrency import Euro
        >>> euro = abs(Euro(-2))
        >>> print(euro)
        2,00 €

* Addiction

    Addiction is supported only between currencies of the same type.

        >>> from multicurrency import Euro
        >>> euro1 = Euro(2.5)
        >>> euro2 = Euro(3)
        >>> print(euro1 + euro2)
        5,50 €

* Boolean

    Produces 'True' for values of currency other than zero. 'False'
    otherwise.

        >>> from multicurrency import Euro
        >>> bool(Euro(0))
        False
        >>> bool(Euro(1))
        True

* Ceiling

    Produces a new currency rounded up to the nearest integer.

        >>> from multicurrency import Euro
        >>> from math import ceil
        >>> print(ceil(Euro(1/7)))
        1,00 €

* Copy

    Produces a copy of itself.

        >>> from multicurrency import Euro
        >>> from copy import copy
        >>> euro = copy(Euro(1/7))
        >>> print(euro)
        0,14 €

* Division

    Produces a new currency with the value of the division of the
    currency by either an `int`, `float`, or `decimal.Decimal`.

        >>> from multicurrency import Euro
        >>> euro = Euro(7) / 2
        >>> print(euro)
        3,50 €

* Divmod

    Produces a tuple consisting of the currencies with the quotient and
    the remainder of the division of the currency by either an `int`,
    `float`, or `decimal.Decimal`.

        >>> from multicurrency import Euro
        >>> q, r = divmod(Euro(7), 2)
        >>> print(q, r)
        3,00 € 1,00 €

* Float

    Produces a `float` with the value of the currency amount.

        >>> from multicurrency import Euro
        >>> float(Euro(1/7))
        0.14285714285714285

* Flooring

    Produces a new currency rounded down to the nearest integer.

        >>> from multicurrency import Euro
        >>> from math import floor
        >>> print(floor(Euro(7/2)))
        3,00 €

* Floordiv

    Produces a new currency with the integral part of the quotient of
    the division of the currency by either an `int`, `float`, or
    `decimal.Decimal`.

        >>> from multicurrency import Euro
        >>> q = Euro(7) // 2
        >>> print(q)
        3,00 €

* Hash

    Produces a hash representation of the
    `multicurrency.pycurrency.Currency`.

        >>> from multicurrency import Euro
        >>> hash(Euro(7)) # doctest: +SKIP
        1166476495300974230

* Int

    Produces an `int` with the value of the currency amount.

        >>> from multicurrency import Euro
        >>> int(Euro(7/2))
        3

* Mod

    Produces a new currency with the value of the remainder of the
    division of the currency by either an `int`, `float`, or
    `decimal.Decimal`.

        >>> from multicurrency import Euro
        >>> r = Euro(7) % 2
        >>> print(r)
        1,00 €

* Multiplication

    Multiplication is supported only between a currency and an `int`,
    `float`, or `decimal.Decimal`.

        >>> from multicurrency import Euro
        >>> print(Euro(2) * 2.5)
        5,00 €

* Round

    Produces a new currency with the amount of the currency rounded to
    a given precision.

        >>> from multicurrency import Euro
        >>> r = round(Euro(1/7), 3)
        >>> print(r.amount)
        0.143

* Subtraction

    Subtraction is supported only between currencies of the same type.

        >>> from multicurrency import Euro
        >>> euro1 = Euro(2)
        >>> euro2 = Euro(3)
        >>> print(euro1 - euro2)
        -1,00 €

* Other Operations

    This library also supports the basic comparison operations between
    two objects of the same currency.

        >>> from multicurrency import Euro
        >>> euro1 = Euro(2)
        >>> euro2 = Euro(3)
        >>> euro1 > euro2
        False
        >>> euro1 >= euro2
        False
        >>> euro1 < euro2
        True
        >>> euro1 <= euro2
        True
        >>> euro1 == euro2
        False
        >>> euro1 != euro2
        True

"""

from multicurrency.pycurrency import Currency
from multicurrency.exceptions import (
    CurrencyException,
    CurrencyInvalidDivision,
    CurrencyInvalidFormat,
    CurrencyInvalidMultiplication,
    CurrencyInvalidOperation,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies import *


__version__: str = '2.0.2'
