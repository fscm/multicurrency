# multicurrency

Currency representation.

## Synopsis

The multicurrency module provides support for currency operations. It supports
several different currencies.

The currencies supported by this module were created with information
(alphabetic code, numeric code, and minor unit size) from ISO-4217.

## Prerequisites

Python, version 3.6 or above, needs to be installed on your local computer.
Python setup can be found [here](https://www.python.org/downloads/).

## Installation

The simplest way to install this library is using pip:

```shell
pip3 install multicurrency
```

## Documentation

Full module documentation can be found
[here](http://fscm.github.io/multicurrency).

## Usage

Simple usage example:

```python
>>> from multicurrency import Euro
>>> euro = Euro(1000)
>>> print(euro)
1.000,00 €
>>> print(euro + Euro(0.50))
1.000,50 €
```

Unsupported currencies can be represented by creating a generic `Currency`
object with the desired settings.

```python
>>> from multicurrency import Currency
>>> bitcoin = Currency(
...     amount=1000,
...     alpha_code='XBT',
...     numeric_code='0',
...     symbol='₿',
...     symbol_ahead=True,
...     symbol_separator='',
...     decimal_places=8,
...     decimal_sign='.',
...     grouping_sign=',')
>>> print(bitcoin)
₿1,000.00000000
```

To help working with unsupported currencies the settings can be defined in a
dictionary and used when needed:

```python
>>> from multicurrency import Currency
>>> settings = {
...     'alpha_code':'XBT',
...     'numeric_code':'0',
...     'symbol':'₿',
...     'symbol_ahead':True,
...     'symbol_separator':'',
...     'decimal_places':8,
...     'decimal_sign':'.',
...     'grouping_sign':','}
>>> bitcoin = Currency(1000, **settings)
>>> print(bitcoin)
₿1,000.00000000
```

Currencies can also be represented with the ISO 4217 three-letter code instead
of the `symbol`.

```python
>>> from multicurrency import Euro
>>> euro = Euro(1000, international=True)
>>> print(euro)
EUR 1,000.00
```

## Localization

The multicurrency library allows you to obtain a localized version of the
currency representation:

```python
>>> from multicurrency import TaiwanDollar, USDollar
>>> tw_dollar = TaiwanDollar('27.65')
>>> us_dollar = USDollar('1')
>>> print(us_dollar.localized(), '=', tw_dollar.localized())
US$1.00 = TW$27.65
```

## Precision

The multicurrency library has a user alterable precision (defaulting to 28
places) which can be as large as needed for a given problem:

```python
>>> from multicurrency import CurrencyContext, Euro
>>> for precision in [1, 2, 3, 4, 5, 6]:
...     CurrencyContext.prec = precision
...     result = Euro(1) / 7
...     print(result.precision(precision))
0,1 €
0,14 €
0,143 €
0,1429 €
0,14286 €
0,142857 €
```

It also has a user alterable rounding method (defaulting to ROUND_HALF_EVEN)
which can be changed as needed:

```python
>>> from multicurrency import CurrencyContext, Euro
>>> CurrencyContext.prec = 4
>>> for rounding in [
...         'ROUND_CEILING',
...         'ROUND_DOWN',
...         'ROUND_FLOOR',
...         'ROUND_HALF_DOWN',
...         'ROUND_HALF_EVEN',
...         'ROUND_HALF_UP',
...         'ROUND_UP',
...         'ROUND_05UP']:
...     CurrencyContext.rounding = rounding
...     result = Euro(1) / 7
...     print(f'{rounding:16}', result.precision(4))
...
ROUND_CEILING    0,1429 €
ROUND_DOWN       0,1428 €
ROUND_FLOOR      0,1428 €
ROUND_HALF_DOWN  0,1429 €
ROUND_HALF_EVEN  0,1429 €
ROUND_HALF_UP    0,1429 €
ROUND_UP         0,1429 €
ROUND_05UP       0,1428 €
```

Default values can be restored with:

```python
>>> from multicurrency import (
...     CurrencyContext,
...     DEFAULT_PRECISION,
...     DEFAULT_ROUNDING)
>>> CurrencyContext.prec = DEFAULT_PRECISION
>>> CurrencyContext.rounding = DEFAULT_ROUNDING
>>> print(CurrencyContext.prec, CurrencyContext.rounding)
28 ROUND_HALF_EVEN
```

Supported rounding methods are described on the `CurrencyContext` class.

## Formatting

The `Currency` class allows you to create and customize your own value
formatting behaviors using the same implementation as the built-in `format()`
method.

The specification for the formatting feature is as follows:

```null
[dp][ds][gs][gp][spec]
```

The meaning of the various alignment options is as follows:

| Option | Type   | Meaning                                                                               |
|:-------|:-------|:--------------------------------------------------------------------------------------|
| [dp]   | int+   | The number of decimal places (integer number with one or more digits).                |
| [ds]   | str{1} | The decimal sign (single non-digit character).                                        |
| [gs]   | str{1} | The grouping sign (single non-digit character).                                       |
| [gp]   | int+   | The number of digits to group the number by (integer number with one or more digits). |
| [spec] | str    | The formatting spec (a strig with the order of currency parts).                       |

All fields are optional although for the first four fields when setting
one the fields on the left of that are required to be set as well.

The available string currency parts for `[spec]` are:

| Part | Meaning                                                                                                                     |
|:-----|:----------------------------------------------------------------------------------------------------------------------------|
| %a   | The currency's amount as seen in the default representation of the currency (the numeral system of the currency's country). |
| %A   | The currency's amount in (western) arabic numerals.                                                                         |
| %c   | The currency's alpha code (as seen on the international representation of the currency).                                    |
| %s   | The currency's symbol.                                                                                                      |
| %_   | The currency's symbol separator.                                                                                            |

Basic examples of how to use the `Currency` formatting feature:

```python
# Using the built-in `format()` method
>>> from multicurrency import Euro
>>> euro = Euro(1000000*(1/7))
>>> format(euro, '4%a')
'142.857,1429'
```

```python
# Using the `'new' string` formating method
>>> from multicurrency import Euro
>>> euro = Euro(1000000*(1/7))
>>> '{:4%a}'.format(euro)
'142.857,1429'
```

```python
# Using the `f-string` method
>>> from multicurrency import Euro
>>> euro = Euro(1000000*(1/7))
>>> f'{euro:4%a}'
'142.857,1429'
```

Some more examples of the `Currency` formatting feature usage (using the
`f-string` method):

```python
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

>>> print(f'{euro:3.,}')
142,857.143 €

>>> print(f'{euro:3.,2}')
14,28,57.143 €

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

>>> print(f'{euro:%a%_%c}')
142.857,14 EUR

>>> print(f'{euro:%a %c}')
142.857,14 EUR
```

## Operations

Several operations are supported by the several library classes.

* Absolute

    Produces the absolute value of a given currency.

    ```python
    >>> from multicurrency import Euro
    >>> euro = abs(Euro(-2))
    >>> print(euro)
    2,00 €
    ```

* Addiction

    Addiction is supported only between currencies of the same type.

    ```python
    >>> from multicurrency import Euro
    >>> euro1 = Euro(2.5)
    >>> euro2 = Euro(3)
    >>> print(euro1 + euro2)
    5,50 €
    ```

* Boolean

    Produces 'True' for values of currency other than zero. 'False' otherwise.

    ```python
    >>> from multicurrency import Euro
    >>> bool(Euro(0))
    False
    >>> bool(Euro(1))
    True
    ```

* Ceiling

    Produces a new currency rounded up to the nearest integer.

    ```python
    >>> from multicurrency import Euro
    >>> from math import ceil
    >>> print(ceil(Euro(1/7)))
    1,00 €
    ```

* Copy

    Produces a copy of itself.

    ```python
    >>> from multicurrency import Euro
    >>> from copy import copy
    >>> euro = copy(Euro(1/7))
    >>> print(euro)
    0,14 €
    ```

* Division

    Produces a new currency with the value of the division of the currency by
    either an `int`, `float`, or `Decimal`.

    ```python
    >>> from multicurrency import Euro
    >>> euro = Euro(7) / 2
    >>> print(euro)
    3,50 €
    ```

* Divmod

    Produces a tuple consisting of the currencies with the quotient and the
    remainder of the division of the currency by either an `int`, `float`, or
    `Decimal`.

    ```python
    >>> from multicurrency import Euro
    >>> q, r = divmod(Euro(7), 2)
    >>> print(q, r)
    3,00 € 1,00 €
    ```

* Float

    Produces a `float` with the value of the currency amount.

    ```python
    >>> from multicurrency import Euro
    >>> float(Euro(1/7))
    0.14285714285714285
    ```

* Flooring

    Produces a new currency rounded down to the nearest integer.

    ```python
    >>> from multicurrency import Euro
    >>> from math import floor
    >>> print(floor(Euro(7/2)))
    3,00 €
    ```

* Floordiv

    Produces a new currency with the integral part of the quotient of the
    division of the currency by either an `int`, `float`, or `Decimal`.

    ```python
    >>> from multicurrency import Euro
    >>> q = Euro(7) // 2
    >>> print(q)
    €3,00
    ```

* Hash

    Produces a hash representation of the `Currency`.

    ```python
    >>> from multicurrency import Euro
    >>> hash(Euro(7))
    1166476495300974230
    ```

* Int

    Produces an `int` with the value of the currency amount.

    ```python
    >>> from multicurrency import Euro
    >>> int(Euro(7/2))
    3
    ```

* Mod

    Produces a new currency with the value of the remainder of the division of
    the currency by either an `int`, `float`, or `Decimal`.

    ```python
    >>> from multicurrency import Euro
    >>> r = Euro(7) % 2
    >>> print(r)
    1,00 €
    ```

* Multiplication

    Multiplication is supported only between a currency and an `int`, `float`,
    or `Decimal`.

    ```python
    >>> from multicurrency import Euro
    >>> print(Euro(2) * 2.5)
    5,00 €
    ```

* Round

    Produces a new currency with the amount of the currency rounded to a given
    precision.

    ```python
    >>> from multicurrency import Euro
    >>> r = round(Euro(1/7), 3)
    >>> print(r.amount)
    0.143
    ```

* Subtraction

    Subtraction is supported only between currencies of the same type.

    ```python
    >>> from multicurrency import Euro
    >>> euro1 = Euro(2)
    >>> euro2 = Euro(3)
    >>> print(euro1 - euro2)
    -1,00 €
    ```

* Other Operations

    This library also supports the basic comparison operations between two
    objects of the same currency.

    ```python
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
    ```

## Supported Currencies

List of supported currencies (and default format):

* `Afghani` (؋ ۱۲۳٬۴۵۶٫۷۹ | ؋ ۱۲۳٬۴۵۶٫۷۹ | AFN 123,456.79),
* `AlgerianDinar` (123.456,79 د.ج. | 123.456,79 د.ج. | DZD 123,456.79),
* `ArgentinePeso` ($ 123.456,79 | AR$ 123.456,79 | ARS 123,456.79),
* `ArmenianDram` (123 456,79 Դ | 123 456,79 Դ | AMD 123,456.79),
* `ArubanFlorin` (ƒ123,456.79 | ƒ123,456.79 | AWG 123,456.79),
* `AustralianDollar` ($123,456.79 | $123,456.79 | AUD 123,456.79),
* `AustralianDollarAU` ($123,456.79 | AU$123,456.79 | AUD 123,456.79),
* `AustralianDollarCC` ($123,456.79 | CC$123,456.79 | AUD 123,456.79),
* `AustralianDollarKI` ($123,456.79 | KI$123,456.79 | AUD 123,456.79),
* `AustralianDollarMR` ($123,456.79 | NR$123,456.79 | AUD 123,456.79),
* `AustralianDollarTV` ($123,456.79 | TV$123,456.79 | AUD 123,456.79),
* `AzerbaijanianManat` (123.456,79 ₼ | 123.456,79 ₼ | AZN 123,456.79),
* `BahamianDollar` ($123,456.79 | BS$123,456.79 | BSD 123,456.79),
* `BahrainiDinar` (د.ب. ١٢٣٬٤٥٦٫٧٨٩ | د.ب. ١٢٣٬٤٥٦٫٧٨٩ | BHD 123,456.789),
* `Baht` (฿123,456.79 | ฿123,456.79 | THB 123,456.79),
* `Balboa` (B/. 123,456.79 | B/. 123,456.79 | PAB 123,456.79),
* `BarbadosDollar` ($123,456.79 | BB$123,456.79 | BBD 123,456.79),
* `BelarusianRuble` (123 456,79 Br | 123 456,79 Br | BYN 123,456.79),
* `BelizeDollar` ($123,456.79 | BZ$123,456.79 | BZD 123,456.79),
* `BermudianDollar` ($123,456.79 | BM$123,456.79 | BMD 123,456.79),
* `BolivarFuerte` (Bs.F. 123.456,79 | Bs.F. 123.456,79 | VEF 123,456.79),
* `Boliviano` (Bs. 123.456,79 | Bs. 123.456,79 | BOB 123,456.79),
* `BrazilianReal` (R$ 123.456,79 | R$ 123.456,79 | BRL 123,456.79),
* `BruneiDollar` ($ 123.456,79 | $ 123.456,79 | BND 123,456.79),
* `BruneiDollarBN` ($ 123.456,79 | BN$ 123.456,79 | BND 123,456.79),
* `BruneiDollarSG` ($ 123.456,79 | SG$ 123.456,79 | BND 123,456.79),
* `BulgarianLev` (123456,79 лв. | 123456,79 лв. | BGN 123,456.79),
* `BurundiFranc` (123 457 ₣ | 123 457 BI₣ | BIF 123,457),
* `CFAFrancBCEAO` (123 457 ₣ | 123 457 ₣ | XOF 123,457),
* `CFAFrancBCEAO_BF` (123 457 ₣ | 123 457 BF₣ | XOF 123,457),
* `CFAFrancBCEAO_BJ` (123 457 ₣ | 123 457 BJ₣ | XOF 123,457),
* `CFAFrancBCEAO_CI` (123 457 ₣ | 123 457 CI₣ | XOF 123,457),
* `CFAFrancBCEAO_GW` (123 457 ₣ | 123 457 GW₣ | XOF 123,457),
* `CFAFrancBCEAO_ML` (123 457 ₣ | 123 457 ML₣ | XOF 123,457),
* `CFAFrancBCEAO_NG` (123 457 ₣ | 123 457 NG₣ | XOF 123,457),
* `CFAFrancBCEAO_SN` (123 457 ₣ | 123 457 SN₣ | XOF 123,457),
* `CFAFrancBCEAO_TG` (123 457 ₣ | 123 457 TG₣ | XOF 123,457),
* `CFAFrancBEAC` (123 457 ₣ | 123 457 ₣ | XAF 123,457),
* `CFAFrancBEAC_CD` (123 457 ₣ | 123 457 CD₣ | XAF 123,457),
* `CFAFrancBEAC_CF` (123 457 ₣ | 123 457 CF₣ | XAF 123,457),
* `CFAFrancBEAC_CM` (123 457 ₣ | 123 457 CM₣ | XAF 123,457),
* `CFAFrancBEAC_GA` (123 457 ₣ | 123 457 GA₣ | XAF 123,457),
* `CFAFrancBEAC_GQ` (123 457 ₣ | 123 457 GQ₣ | XAF 123,457),
* `CFAFrancBEAC_TD` (123 457 ₣ | 123 457 TD₣ | XAF 123,457),
* `CFPFranc` (123 457 ₣ | 123 457 ₣ | XPF 123,457),
* `CFPFrancNC` (123 457 ₣ | 123 457 NC₣ | XPF 123,457),
* `CFPFrancPF` (123 457 ₣ | 123 457 PF₣ | XPF 123,457),
* `CFPFrancWF` (123 457 ₣ | 123 457 WF₣ | XPF 123,457),
* `CanadianDollarEN` ($123,456.79 | CA$123,456.79 | CAD 123,456.79),
* `CanadianDollarFR` (123 456,79 $ | 123 456,79 CA$ | CAD 123,456.79),
* `CapeVerdeEscudo` (123 456$79 | 123 456$79 | CVE 123,456.79),
* `CaymanIslandsDollar` ($123,456.79 | KY$123,456.79 | KYD 123,456.79),
* `Cedi` (₵123,456.79 | ₵123,456.79 | GHS 123,456.79),
* `ChileanPeso` ($123.457 | CL$123.457 | CLP 123,457),
* `ColombianPeso` ($ 123.456,79 | CO$ 123.456,79 | COP 123,456.79),
* `CongoleseFranc` (123 456,79 ₣ | 123 456,79 CD₣ | CDF 123,456.79),
* `CordobaOro` (C$123,456.79 | C$123,456.79 | NIO 123,456.79),
* `CostaRicanColon` (₡123 456,79 | ₡123 456,79 | CRC 123,456.79),
* `CroatianKuna` (123.456,79 Kn | 123.456,79 Kn | HRK 123,456.79),
* `CubanPeso` ($123,456.79 | CU$123,456.79 | CUP 123,456.79),
* `CzechKoruna` (123 456,79 Kč | 123 456,79 Kč | CZK 123,456.79),
* `Dalasi` (D 123,456.79 | D 123,456.79 | GMD 123,456.79),
* `DanishKrone` (123.456,79 kr | 123.456,79 kr | DKK 123,456.79),
* `Denar` (123.456,79 ден. | 123.456,79 ден. | MKD 123,456.79),
* `DjiboutiFranc` (123 457 ₣ | 123 457 DJ₣ | DJF 123,457),
* `Dobra` (123.456,79 Db | 123.456,79 Db | STN 123,456.79),
* `DominicanPeso` ($123,456.79 | DO$123,456.79 | DOP 123,456.79),
* `Dong` (123.457 ₫ | 123.457 ₫ | VND 123,457),
* `EasternCaribbeanDollar` ($123,456.79 | $123,456.79 | XCD 123,456.79),
* `EasternCaribbeanDollarAG` ($123,456.79 | AG$123,456.79 | XCD 123,456.79),
* `EasternCaribbeanDollarAI` ($123,456.79 | AI$123,456.79 | XCD 123,456.79),
* `EasternCaribbeanDollarDM` ($123,456.79 | DM$123,456.79 | XCD 123,456.79),
* `EasternCaribbeanDollarGD` ($123,456.79 | GD$123,456.79 | XCD 123,456.79),
* `EasternCaribbeanDollarKN` ($123,456.79 | KN$123,456.79 | XCD 123,456.79),
* `EasternCaribbeanDollarLC` ($123,456.79 | LC$123,456.79 | XCD 123,456.79),
* `EasternCaribbeanDollarMS` ($123,456.79 | MS$123,456.79 | XCD 123,456.79),
* `EasternCaribbeanDollarVC` ($123,456.79 | VC$123,456.79 | XCD 123,456.79),
* `EgyptianPound` (ج.م. ١٢٣٬٤٥٦٫٧٩ | ج.م. ١٢٣٬٤٥٦٫٧٩ | EGP 123,456.79),
* `EthiopianBirr` (ብር 123,456.79 | ብር 123,456.79 | ETB 123,456.79),
* `Euro` (123.456,79 € | 123.456,79 € | EUR 123,456.79),
* `EuroAD` (123.456,79 € | 123.456,79 AD€ | EUR 123,456.79),
* `EuroAT` (€ 123.456,79 | AT€ 123.456,79 | EUR 123,456.79),
* `EuroBE` (€ 123.456,79 | BE€ 123.456,79 | EUR 123,456.79),
* `EuroCY` (123.456,79 € | 123.456,79 CY€ | EUR 123,456.79),
* `EuroDE` (123.456,79 € | 123.456,79 DE€ | EUR 123,456.79),
* `EuroEE` (123 456,79 € | 123 456,79 EE€ | EUR 123,456.79),
* `EuroES` (123.456,79 € | 123.456,79 ES€ | EUR 123,456.79),
* `EuroFI` (123 456,79 € | 123 456,79 FI€ | EUR 123,456.79),
* `EuroFR` (123 456,79 € | 123 456,79 FR€ | EUR 123,456.79),
* `EuroGR` (123.456,79 € | 123.456,79 GR€ | EUR 123,456.79),
* `EuroIE` (€123,456.79 | IR€123,456.79 | EUR 123,456.79),
* `EuroIT` (123.456,79 € | 123.456,79 IT€ | EUR 123,456.79),
* `EuroLT` (123 456,79 € | 123 456,79 LT€ | EUR 123,456.79),
* `EuroLU` (123.456,79 € | 123.456,79 LU€ | EUR 123,456.79),
* `EuroLV` (123 456,79 € | 123 456,79 LV€ | EUR 123,456.79),
* `EuroMC` (123 456,79 € | 123 456,79 MC€ | EUR 123,456.79),
* `EuroME` (123.456,79 € | 123.456,79 ME€ | EUR 123,456.79),
* `EuroMT` (€123,456.79 | MT€123,456.79 | EUR 123,456.79),
* `EuroNL` (€ 123.456,79 | NL€ 123.456,79 | EUR 123,456.79),
* `EuroPT` (€ 123.456,79 | PT€ 123.456,79 | EUR 123,456.79),
* `EuroSBA` (123.456,79 € | 123.456,79 € | EUR 123,456.79),
* `EuroSI` (123.456,79 € | 123.456,79 SI€ | EUR 123,456.79),
* `EuroSK` (123 456,79 € | 123 456,79 SK€ | EUR 123,456.79),
* `EuroSM` (123.456,79 € | 123.456,79 SM€ | EUR 123,456.79),
* `EuroVA` (€123,456.79 | VA€123,456.79 | EUR 123,456.79),
* `EuroXK` (123 456,79 € | 123 456,79 XK€ | EUR 123,456.79),
* `FalklandIslandsPound` (£123,456.79 | FK£123,456.79 | FKP 123,456.79),
* `FijiDollar` ($123,456.79 | FJ$123,456.79 | FJD 123,456.79),
* `Forint` (123 457 Ft | 123 457 Ft | HUF 123,457),
* `GibraltarPound` (£123,456.79 | GI£123,456.79 | GIP 123,456.79),
* `Gourde` (G 123,456.79 | G 123,456.79 | HTG 123,456.79),
* `Guarani` (₲ 123.457 | ₲ 123.457 | PYG 123,457),
* `GuineaFranc` (123 457 ₣ | 123 457 GN₣ | GNF 123,457),
* `GuyanaDollar` ($123,456.79 | GY$123,456.79 | GYD 123,456.79),
* `HongKongDollar` ($123,456.79 | HK$123,456.79 | HKD 123,456.79),
* `Hryvnia` (123 456,79 ₴ | 123 456,79 ₴ | UAH 123,456.79),
* `IcelandKrona` (123.457 Kr | 123.457 Kr | ISK 123,457),
* `IndianRupee` (₹123,456.79 | ₹123,456.79 | INR 123,456.79),
* `IndianRupeeBT` (₹123,456.79 | BT₹123,456.79 | INR 123,456.79),
* `IndianRupeeIN` (₹123,456.79 | IN₹123,456.79 | INR 123,456.79),
* `IranianRial` (۱۲۳٬۴۵۶٫۷۹ ﷼ | ۱۲۳٬۴۵۶٫۷۹ ﷼ | IRR 123,456.79),
* `IraqiDinar` (د.ع. ١٢٣٬٤٥٦٫٧٨٩ | د.ع. ١٢٣٬٤٥٦٫٧٨٩ | IQD 123,456.789),
* `JamaicanDollar` ($123,456.79 | JM$123,456.79 | JMD 123,456.79),
* `JordanianDinar` (د.أ. ١٢٣٬٤٥٦٫٧٨٩ | د.أ. ١٢٣٬٤٥٦٫٧٨٩ | JOD 123,456.789),
* `KenyanShilling` (Ksh 123,456.79 | Ksh 123,456.79 | KES 123,456.79),
* `Kina` (K 123,456.79 | K 123,456.79 | PGK 123,456.79),
* `Kip` (₭123.456,79 | ₭123.456,79 | LAK 123,456.79),
* `KonvertibilnaMarka` (123,456.79 КМ | 123,456.79 КМ | BAM 123,456.79),
* `KuwaitiDinar` (د.ك. ١٢٣٬٤٥٦٫٧٨٩ | د.ك. ١٢٣٬٤٥٦٫٧٨٩ | KWD 123,456.789),
* `Kwacha` (MK 123,456.79 | MK 123,456.79 | MWK 123,456.79),
* `Kwanza` (123 456,79 Kz | 123 456,79 Kz | AOA 123,456.79),
* `Kyat` (၁၂၃,၄၅၆.၇၉ K | ၁၂၃,၄၅၆.၇၉ K | MMK 123,456.79),
* `Lari` (123 456,79 ლ | 123 456,79 GEლ | GEL 123,456.79),
* `LebanesePound` (ل.ل. ١٢٣٬٤٥٧ | ل.ل. ١٢٣٬٤٥٧ | LBP 123,457),
* `Lek` (123 456,79 Lek | 123 456,79 Lek | ALL 123,456.79),
* `Lempira` (L 123,456.79 | L 123,456.79 | HNL 123,456.79),
* `Leone` (Le 123,456.79 | Le 123,456.79 | SLL 123,456.79),
* `Leu` (123.456,79 L | 123.456,79 L | RON 123,456.79),
* `LiberianDollar` ($123,456.79 | LR$123,456.79 | LRD 123,456.79),
* `LibyanDinar` (د.ل. 123.456,789 | د.ل. 123.456,789 | LYD 123,456.789),
* `Lilangeni` (L 123,456.79 | L 123,456.79 | SZL 123,456.79),
* `Loti` (L 123,456.79 | L 123,456.79 | LSL 123,456.79),
* `MalagasyAriary` (123 457 Ar | 123 457 Ar | MGA 123,457),
* `MalaysianRinggit` (RM 123,456.79 | RM 123,456.79 | MYR 123,456.79),
* `Manat` (123 456,79 m | 123 456,79 m | TMT 123,456.79),
* `MauritiusRupee` (₨ 123,456.79 | ₨ 123,456.79 | MUR 123,456.79),
* `Metical` (123.457 MTn | 123.457 MTn | MZN 123,457),
* `MexicanPeso` ($123,456.79 | MX$123,456.79 | MXN 123,456.79),
* `MoldovanLeu` (123.456,79 L | 123.456,79 L | MDL 123,456.79),
* `MoroccanDirham` (د.م. ١٢٣٬٤٥٦٫٧٩ | د.م. ١٢٣٬٤٥٦٫٧٩ | MAD 123,456.79),
* `Naira` (₦123,456.79 | ₦123,456.79 | NGN 123,456.79),
* `Nakfa` (Nfk 123,456.79 | Nfk 123,456.79 | ERN 123,456.79),
* `NamibiaDollar` ($123,456.79 | NA$123,456.79 | NAD 123,456.79),
* `NepaleseRupee` (नेरू १२३,४५६.७९ | नेरू १२३,४५६.७९ | NPR 123,456.79),
* `NewIsraeliShekel` (123,456.79 ₪ | 123,456.79 ₪ | ILS 123,456.79),
* `NewIsraeliShekelIL` (123,456.79 ₪ | 123,456.79 IL₪ | ILS 123,456.79),
* `NewIsraeliShekelPS` (123,456.79 ₪ | 123,456.79 PS₪ | ILS 123,456.79),
* `NewZealandDollar` ($123,456.79 | $123,456.79 | NZD 123,456.79),
* `NewZealandDollarCK` ($123,456.79 | CK$123,456.79 | NZD 123,456.79),
* `NewZealandDollarNU` ($123,456.79 | NU$123,456.79 | NZD 123,456.79),
* `NewZealandDollarNZ` ($123,456.79 | NZ$123,456.79 | NZD 123,456.79),
* `NewZealandDollarPN` ($123,456.79 | PN$123,456.79 | NZD 123,456.79),
* `Ngultrum` (Nu. ༡༢༣,༤༥༦.༧༩ | Nu. ༡༢༣,༤༥༦.༧༩ | BTN 123,456.79),
* `NorthKoreanWon` (₩ 123,456.79 | ₩ 123,456.79 | KPW 123,456.79),
* `NorwegianKrone` (kr 123 456,79 | kr 123 456,79 | NOK 123,456.79),
* `NuevoSol` (S/. 123,456.79 | S/. 123,456.79 | PEN 123,456.79),
* `Ouguiya` (١٢٣٬٤٥٦٫٧٩ أ.م | ١٢٣٬٤٥٦٫٧٩ أ.م | MRU 123,456.79),
* `PZloty` (123 456,79 zł | 123 456,79 zł | PLN 123,456.79),
* `Paanga` (T$ 123,456.79 | T$ 123,456.79 | TOP 123,456.79),
* `PakistanRupee` (₨ 123,456.79 | ₨ 123,456.79 | PKR 123,456.79),
* `Pataca` (P 123,456.79 | P 123,456.79 | MOP 123,456.79),
* `PesoUruguayo` ($ 123.456,79 | UY$ 123.456,79 | UYU 123,456.79),
* `PhilippinePeso` (₱123,456.79 | ₱123,456.79 | PHP 123,456.79),
* `PoundSterling` (£123,456.79 | £123,456.79 | GBP 123,456.79),
* `PoundSterlingGB` (£123,456.79 | GB£123,456.79 | GBP 123,456.79),
* `PoundSterlingGG` (£123,456.79 | GG£123,456.79 | GBP 123,456.79),
* `PoundSterlingIM` (£123,456.79 | IM£123,456.79 | GBP 123,456.79),
* `PoundSterlingIO` (£123,456.79 | IO£123,456.79 | GBP 123,456.79),
* `Pula` (P 123,456.79 | P 123,456.79 | BWP 123,456.79),
* `QatariRial` (ر.ق. ١٢٣٬٤٥٦٫٧٩ | ر.ق. ١٢٣٬٤٥٦٫٧٩ | QAR 123,456.79),
* `Quetzal` (Q 123,456.79 | Q 123,456.79 | GTQ 123,456.79),
* `Rand` (R 123 456.79 | R 123 456.79 | ZAR 123,456.79),
* `RandLS` (R 123,456.79 | LSR 123,456.79 | ZAR 123,456.79),
* `RandNA` (R 123 456.79 | NAR 123 456.79 | ZAR 123,456.79),
* `RandZA` (R 123 456.79 | ZAR 123 456.79 | ZAR 123,456.79),
* `RialOmani` (ر.ع. ١٢٣٬٤٥٦٫٧٨٩ | ر.ع. ١٢٣٬٤٥٦٫٧٨٩ | OMR 123,456.789),
* `Riel` (123.456,79៛ | 123.456,79៛ | KHR 123,456.79),
* `Rufiyaa` (ރ. 123,456.79 | ރ. 123,456.79 | MVR 123,456.79),
* `Rupiah` (Rp 123.456,79 | Rp 123.456,79 | IDR 123,456.79),
* `RussianRuble` (123 456,79 ₽ | 123 456,79 ₽ | RUB 123,456.79),
* `RussianRubleGE` (123 456,79 ₽ | 123 456,79 GE₽ | RUB 123,456.79),
* `RussianRubleRU` (123 456,79 ₽ | 123 456,79 RU₽ | RUB 123,456.79),
* `RwandaFranc` (₣ 123.457 | RW₣ 123.457 | RWF 123,457),
* `SaintHelenaPound` (£123,456.79 | SH£123,456.79 | SHP 123,456.79),
* `SaudiRiyal` (ر.س. ١٢٣٬٤٥٦٫٧٩ | ر.س. ١٢٣٬٤٥٦٫٧٩ | SAR 123,456.79),
* `SerbianDinarSR` (123 456,79 дин. | 123 456,79 дин. | RSD 123,456.79),
* `SerbianDinarXK` (123.456,79 дин. | 123.456,79 дин. | RSD 123,456.79),
* `SeychellesRupee` (₨ 123,456.79 | ₨ 123,456.79 | SCR 123,456.79),
* `SingaporeDollar` ($123,456.79 | $123,456.79 | SGD 123,456.79),
* `SingaporeDollarBN` ($123,456.79 | BN$123,456.79 | SGD 123,456.79),
* `SingaporeDollarSG` ($123,456.79 | SG$123,456.79 | SGD 123,456.79),
* `SolomonIslandsDollar` ($123,456.79 | SB$123,456.79 | SBD 123,456.79),
* `Som` (123 456,79 Лв | 123 456,79 Лв | KGS 123,456.79),
* `SomaliShilling` (SSh 123,456.79 | SSh 123,456.79 | SOS 123,456.79),
* `Somoni` (ЅМ 123,456.79 | ЅМ 123,456.79 | TJS 123,456.79),
* `SouthKoreanWon` (₩123,457 | ₩123,457 | KRW 123,457),
* `SriLankaRupee` (රු. 123,456.79 | රු. 123,456.79 | LKR 123,456.79),
* `SudanesePound` (١٢٣٬٤٥٦٫٧٩ ج.س | ١٢٣٬٤٥٦٫٧٩ ج.س | SDG 123,456.79),
* `SurinameDollar` ($ 123.456,79 | SR$ 123.456,79 | SRD 123,456.79),
* `SwedishKrona` (123 456,79 kr | 123 456,79 kr | SEK 123,456.79),
* `SwissFranc` (₣ 123'456.79 | ₣ 123'456.79 | CHF 123,456.79),
* `SwissFrancCH` (₣ 123'456.79 | CH₣ 123'456.79 | CHF 123,456.79),
* `SwissFrancLI` (₣ 123'456.79 | LI₣ 123'456.79 | CHF 123,456.79),
* `SyrianPound` (١٢٣٬٤٥٦٫٧٩ ل.س | ١٢٣٬٤٥٦٫٧٩ ل.س | SYP 123,456.79),
* `TaiwanDollar` ($123,456.79 | TW$123,456.79 | TWD 123,456.79),
* `Taka` (১২৩,৪৫৬.৭৯৳ | ১২৩,৪৫৬.৭৯৳ | BDT 123,456.79),
* `Tala` (T 123,456.79 | T 123,456.79 | WST 123,456.79),
* `TanzanianShilling` (TSh 123,456.79 | TSh 123,456.79 | TZS 123,456.79),
* `Tenge` (123 456,79 〒 | 123 456,79 〒 | KZT 123,456.79),
* `TrinidadandTobagoDollar` ($123,456.79 | TT$123,456.79 | TTD 123,456.79),
* `Tugrik` (₮ 123,456.79 | ₮ 123,456.79 | MNT 123,456.79),
* `TunisianDinar` (د.ت. 123.456,789 | د.ت. 123.456,789 | TND 123,456.789),
* `TurkishLira` (₤123.456,79 | ₤123.456,79 | TRY 123,456.79),
* `TurkishLiraCY` (₤123.456,79 | CY₤123.456,79 | TRY 123,456.79),
* `TurkishLiraTR` (₤123.456,79 | TR₤123.456,79 | TRY 123,456.79),
* `UAEDirham` (د.إ. ١٢٣٬٤٥٦٫٧٩ | د.إ. ١٢٣٬٤٥٦٫٧٩ | AED 123,456.79),
* `USDollar` ($123,456.79 | US$123,456.79 | USD 123,456.79),
* `USDollarAS` ($123,456.79 | AS$123,456.79 | USD 123,456.79),
* `USDollarFM` ($123,456.79 | FM$123,456.79 | USD 123,456.79),
* `USDollarGU` ($123,456.79 | GU$123,456.79 | USD 123,456.79),
* `USDollarHT` ($123,456.79 | HT$123,456.79 | USD 123,456.79),
* `USDollarIO` ($123,456.79 | IO$123,456.79 | USD 123,456.79),
* `USDollarMH` ($123,456.79 | MH$123,456.79 | USD 123,456.79),
* `USDollarMP` ($123,456.79 | MP$123,456.79 | USD 123,456.79),
* `USDollarPA` ($123,456.79 | PA$123,456.79 | USD 123,456.79),
* `USDollarPC` ($123,456.79 | PC$123,456.79 | USD 123,456.79),
* `USDollarPR` ($123,456.79 | PR$123,456.79 | USD 123,456.79),
* `USDollarPW` ($123,456.79 | PW$123,456.79 | USD 123,456.79),
* `USDollarTC` ($123,456.79 | TC$123,456.79 | USD 123,456.79),
* `USDollarVG` ($123,456.79 | VG$123,456.79 | USD 123,456.79),
* `USDollarVI` ($123,456.79 | VI$123,456.79 | USD 123,456.79),
* `UgandaShilling` (USh 123,457 | USh 123,457 | UGX 123,457),
* `UzbekistanSum` (123 456,79 сўм | 123 456,79 сўм | UZS 123,456.79),
* `Vatu` (Vt 123,457 | Vt 123,457 | VUV 123,457),
* `YemeniRial` (١٢٣٬٤٥٦٫٧٩ ﷼ | ١٢٣٬٤٥٦٫٧٩ ﷼ | YER 123,456.79),
* `Yen` (¥123,457 | ¥123,457 | JPY 123,457),
* `Yuan` (¥123,456.79 | ¥123,456.79 | CNY 123,456.79),
* `ZambianKwacha` (ZK 123,456.79 | ZK 123,456.79 | ZMW 123,456.79),
* `ZimbabweDollar` ($ 123,456.79 | ZW$ 123,456.79 | ZWL 123,456.79)

List of supported cryptocurrencies (and default format):

* `Bitcoin` (₿123,456.78900000 | ₿123,456.78900000 | XBT 123,456.78900000),
* `EOS` (ε123,456.7890 | ε123,456.7890 | EOS 123,456.7890),
* `Ethereum` (Ξ123,456.789000000000000000 | Ξ123,456.789000000000000000 | ETH 123,456.789000000000000000),
* `Monero` (ɱ123,456.789000000000 | ɱ123,456.789000000000 | XMR 123,456.789000000000),
* `Ripple` (✕123,456.789000 | ✕123,456.789000 | XRP 123,456.789000),
* `StellarLumens` (*123,456.7890000 | *123,456.7890000 | XLM 123,456.7890000),
* `Tezos` (ꜩ123,456.789000 | ꜩ123,456.789000 | XTZ 123,456.789000),
* `Zcash` (ⓩ123,456.78900000 | ⓩ123,456.78900000 | ZEC 123,456.78900000)

## Build (from source)

[GNU make](https://www.gnu.org/software/make/manual/make.html) is used to
automate several steps of the development process.

All of the commands described bellow are to be executed on the root folder of
this project.

A development environment can be created using the following command:

```shell
make dev
```

After creating the development environment activate the virtual enviroment
that was created using the following command:

```shell
source .venv/bin/activate
```

To build a Python package for this library use the following command:

```shell
make build
```

After this you should have a wheel file (`*.whl`) inside a folder called
`dist`.

You can now leave the virtual environment used to crete the Python package.
Use the following command for that:

```shell
deactivate
```

The library can be install using the wheel file and pip3:

```shell
pip3 --quiet install dist/multicurrency-*.whl
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request

Please read the
[CONTRIBUTING.md](https://github.com/fscm/multicurrency/blob/master/CONTRIBUTING.md)
file for more details on how to contribute to this project.

## Versioning

This project uses [SemVer](http://semver.org/) for versioning. For the versions
available, see the
[tags on this repository](https://github.com/fscm/multicurrency/tags).

## Authors

* **Frederico Martins** - [fscm](https://github.com/fscm)

See also the list of
[contributors](https://github.com/fscm/multicurrency/contributors)
who participated in this project.

## License

This project is licensed under the MIT License - see the
[LICENSE](https://github.com/fscm/multicurrency/blob/master/LICENSE)
file for details
