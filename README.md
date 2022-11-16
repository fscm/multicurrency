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
...     localized_symbol='₿',
...     convertion='',
...     pattern='8.,3%-%s%u')
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
...     'localized_symbol':'₿',
...     'convertion':'',
...     'pattern':'8.,3%-%s%u'}
>>> bitcoin = Currency(1000, **settings)
>>> print(bitcoin)
₿1,000.00000000
```

Currencies can also be represented with the ISO 4217 three-letter code instead
of the `symbol`.

```python
>>> from multicurrency import Euro
>>> euro = Euro(1000)
>>> print(euro.international())
1,000.00 EUR
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

The multicurrency library uses `decimal.Decimal` (to represent the `amount`
value) which has a user alterable precision and rounding settings (defaulting
to `28` places and `ROUND_HALF_EVEN` respectively).

To change the default precision value of a currency one can simply use the
`precision` method provided by that currency (up to the value of the
`decimal.Decimal` precision minus 3):

```python
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
```

If a larger precision is required the default `decimal.Context` precision value
will have to be changed:

```python
>>> from decimal import localcontext
>>> from multicurrency import Euro
>>> with localcontext() as context:
...     precision = 50
...     context.prec = precision + 3
...     result = Euro(1_000/7)
...     print(result.precision(50))
142,85714285714286120310134720057249069213867187500000 €
```

To change the rounding method the default `decimal.Context` rounding
value needs to be changed:

```python
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
```

## Formatting

The `Currency` class allows you to create and customize your own value
formatting behaviors using the same implementation as the built-in `format()`
method.

The specification for the formatting feature is as follows:

```null
[dp][ds][gs][gp][format]
```

The meaning of the various alignment options is as follows:

| Option   | Type    | Meaning                                                                                                                   |
|:---------|:--------|:--------------------------------------------------------------------------------------------------------------------------|
| [dp]     | int+    | The number of decimal places (integer number with one or more digits). Must be grater or equal to 0 (zero.)               |
| [ds]     | char{1} | The decimal sign (single non-digit character).                                                                            |
| [gs]     | char{1} | The grouping sign (single non-digit character).                                                                           |
| [gp]     | int+    | The number of digits to group the number by (integer number with one or more digits).Must be grater or equal to 0 (zero.) |
| [format] | str     | The formatting pattern (a string with the order of the currency parts).                                                   |

All fields are optional although for the first four fields when setting one the
fields on the left of that are required to be set as well.

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

Table of supported currencies (and default format):

| Currency                                                   | Country                                         |          Default |        Localized |   International |
|:-----------------------------------------------------------|:------------------------------------------------|-----------------:|-----------------:|----------------:|
| `multicurrency.currencies.afghani.Afghani`                 | Afghanistan                                     |     ؋ ۱۲۳٬۴۵۶٫۷۹ |     ؋ ۱۲۳٬۴۵۶٫۷۹ |  123,456.79 AFN |
| `multicurrency.currencies.dinar.AlgerianDinar`             | Algeria                                         |  123.456,79 د.ج. |  123.456,79 د.ج. |  123,456.79 DZD |
| `multicurrency.currencies.peso.ArgentinePeso`              | Argentina                                       |     $ 123.456,79 |   AR$ 123.456,79 |  123,456.79 ARS |
| `multicurrency.currencies.dram.ArmenianDram`               | Armenia                                         |     123 456,79 Դ |     123 456,79 Դ |  123,456.79 AMD |
| `multicurrency.currencies.florin.ArubanFlorin`             | Aruba                                           |      ƒ123,456.79 |      ƒ123,456.79 |  123,456.79 AWG |
| `multicurrency.currencies.dollar.AustralianDollar`         | Australia                                       |     $ 123,456.79 |     $ 123,456.79 |  123,456.79 AUD |
| `multicurrency.currencies.dollar.AustralianDollarAU`       | Australia                                       |      $123,456.79 |    AU$123,456.79 |  123,456.79 AUD |
| `multicurrency.currencies.dollar.AustralianDollarCC`       | Coconut Islands                                 |      $123,456.79 |    CC$123,456.79 |  123,456.79 AUD |
| `multicurrency.currencies.dollar.AustralianDollarKI`       | Kiribati                                        |      $123,456.79 |    KI$123,456.79 |  123,456.79 AUD |
| `multicurrency.currencies.dollar.AustralianDollarMR`       | Nauru                                           |      $123,456.79 |    NR$123,456.79 |  123,456.79 AUD |
| `multicurrency.currencies.dollar.AustralianDollarTV`       | Tuvalu                                          |      $123,456.79 |    TV$123,456.79 |  123,456.79 AUD |
| `multicurrency.currencies.manat.AzerbaijanianManat`        | Azerbaijan                                      |     123.456,79 ₼ |     123.456,79 ₼ |  123,456.79 AZN |
| `multicurrency.currencies.dollar.BahamianDollar`           | Bahamas                                         |      $123,456.79 |    BS$123,456.79 |  123,456.79 BSD |
| `multicurrency.currencies.dinar.BahrainiDinar`             | Bahrain                                         | د.ب. ١٢٣٬٤٥٦٫٧٨٩ | د.ب. ١٢٣٬٤٥٦٫٧٨٩ | 123,456.789 BHD |
| `multicurrency.currencies.baht.Baht`                       | Thailand                                        |      ฿123,456.79 |      ฿123,456.79 |  123,456.79 THB |
| `multicurrency.currencies.balboa.Balboa`                   | Panama                                          |   B/. 123,456.79 |   B/. 123,456.79 |  123,456.79 PAB |
| `multicurrency.currencies.dollar.BarbadosDollar`           | Barbados                                        |      $123,456.79 |    BB$123,456.79 |  123,456.79 BBD |
| `multicurrency.currencies.ruble.BelarusianRuble`           | Belarus                                         |    123 456,79 Br |    123 456,79 Br |  123,456.79 BYN |
| `multicurrency.currencies.dollar.BelizeDollar`             | Belize                                          |      $123,456.79 |    BZ$123,456.79 |  123,456.79 BZD |
| `multicurrency.currencies.dollar.BermudianDollar`          | Bermuda                                         |      $123,456.79 |    BM$123,456.79 |  123,456.79 BMD |
| `multicurrency.currencies.fuerte.BolivarFuerte`            | Venezuela                                       | Bs.F. 123.456,79 | Bs.F. 123.456,79 |  123,456.79 VEF |
| `multicurrency.currencies.boliviano.Boliviano`             | Bolivia                                         |   Bs. 123.456,79 |   Bs. 123.456,79 |  123,456.79 BOB |
| `multicurrency.currencies.real.BrazilianReal`              | Brazil                                          |    R$ 123.456,79 |    R$ 123.456,79 |  123,456.79 BRL |
| `multicurrency.currencies.dollar.BruneiDollar`             | Brunei                                          |     $ 123.456,79 |     $ 123.456,79 |  123,456.79 BND |
| `multicurrency.currencies.dollar.BruneiDollarBN`           | Brunei                                          |     $ 123.456,79 |   BN$ 123.456,79 |  123,456.79 BND |
| `multicurrency.currencies.dollar.BruneiDollarSG`           | Singapore                                       |     $ 123.456,79 |   SG$ 123.456,79 |  123,456.79 BND |
| `multicurrency.currencies.lev.BulgarianLev`                | Bulgaria                                        |   123 456,79 лв. |   123 456,79 лв. |  123,456.79 BGN |
| `multicurrency.currencies.franc.BurundiFranc`              | Burundi                                         |        123 457 ₣ |      123 457 BI₣ |     123,457 BIF |
| `multicurrency.currencies.franc.CFAFrancBCEAO`             | Senegal                                         |        123 457 ₣ |        123 457 ₣ |     123,457 XOF |
| `multicurrency.currencies.franc.CFAFrancBCEAOBF`           | Burkina Faso                                    |        123 457 ₣ |      123 457 BF₣ |     123,457 XOF |
| `multicurrency.currencies.franc.CFAFrancBCEAOBJ`           | Benin                                           |        123 457 ₣ |      123 457 BJ₣ |     123,457 XOF |
| `multicurrency.currencies.franc.CFAFrancBCEAOCI`           | Côte d'Ivoire                                   |        123 457 ₣ |      123 457 CI₣ |     123,457 XOF |
| `multicurrency.currencies.franc.CFAFrancBCEAOGW`           | Guinea-Bissau                                   |        123 457 ₣ |      123 457 GW₣ |     123,457 XOF |
| `multicurrency.currencies.franc.CFAFrancBCEAOML`           | Mali                                            |        123 457 ₣ |      123 457 ML₣ |     123,457 XOF |
| `multicurrency.currencies.franc.CFAFrancBCEAONG`           | Niger                                           |        123 457 ₣ |      123 457 NG₣ |     123,457 XOF |
| `multicurrency.currencies.franc.CFAFrancBCEAOSN`           | Senegal                                         |        123 457 ₣ |      123 457 SN₣ |     123,457 XOF |
| `multicurrency.currencies.franc.CFAFrancBCEAOTG`           | Togo                                            |        123 457 ₣ |      123 457 TG₣ |     123,457 XOF |
| `multicurrency.currencies.franc.CFAFrancBEAC`              | Cameroon                                        |        123 457 ₣ |        123 457 ₣ |     123,457 XAF |
| `multicurrency.currencies.franc.CFAFrancBEACCD`            | Congo (Brazzaville)                             |        123 457 ₣ |      123 457 CD₣ |     123,457 XAF |
| `multicurrency.currencies.franc.CFAFrancBEACCF`            | Central African Republic                        |        123 457 ₣ |      123 457 CF₣ |     123,457 XAF |
| `multicurrency.currencies.franc.CFAFrancBEACCM`            | Cameroon                                        |        123 457 ₣ |      123 457 CM₣ |     123,457 XAF |
| `multicurrency.currencies.franc.CFAFrancBEACGA`            | Gabon                                           |        123 457 ₣ |      123 457 GA₣ |     123,457 XAF |
| `multicurrency.currencies.franc.CFAFrancBEACGQ`            | Equatorial Guinea                               |        123 457 ₣ |      123 457 GQ₣ |     123,457 XAF |
| `multicurrency.currencies.franc.CFAFrancBEACTD`            | Chad                                            |        123 457 ₣ |      123 457 TD₣ |     123,457 XAF |
| `multicurrency.currencies.franc.CFPFranc`                  | French Polynesia                                |        123 457 ₣ |        123 457 ₣ |     123,457 XPF |
| `multicurrency.currencies.franc.CFPFrancNC`                | New Caledonia                                   |        123 457 ₣ |      123 457 NC₣ |     123,457 XPF |
| `multicurrency.currencies.franc.CFPFrancPF`                | French Polynesia                                |        123 457 ₣ |      123 457 PF₣ |     123,457 XPF |
| `multicurrency.currencies.franc.CFPFrancWF`                | Wallis and Futuna                               |        123 457 ₣ |      123 457 WF₣ |     123,457 XPF |
| `multicurrency.currencies.dollar.CanadianDollarEN`         | Canada                                          |      $123,456.79 |    CA$123,456.79 |  123,456.79 CAD |
| `multicurrency.currencies.dollar.CanadianDollarFR`         | Canada                                          |     123 456,79 $ |   123 456,79 CA$ |  123,456.79 CAD |
| `multicurrency.currencies.escudo.CapeVerdeEscudo`          | Cape Verde                                      |       123 456$79 |       123 456$79 |  123,456.79 CVE |
| `multicurrency.currencies.dollar.CaymanIslandsDollar`      | Cayman Islands                                  |      $123,456.79 |    KY$123,456.79 |  123,456.79 KYD |
| `multicurrency.currencies.cedi.Cedi`                       | Ghana                                           |      ₵123,456.79 |      ₵123,456.79 |  123,456.79 GHS |
| `multicurrency.currencies.peso.ChileanPeso`                | Chile                                           |         $123.457 |       CL$123.457 |     123,457 CLP |
| `multicurrency.currencies.peso.ColombianPeso`              | Colombia                                        |     $ 123.456,79 |   CO$ 123.456,79 |  123,456.79 COP |
| `multicurrency.currencies.franc.CongoleseFranc`            | Congo (Kinshasa)                                |     123 456,79 ₣ |   123 456,79 CD₣ |  123,456.79 CDF |
| `multicurrency.currencies.oro.CordobaOro`                  | Nicaragua                                       |     C$123,456.79 |     C$123,456.79 |  123,456.79 NIO |
| `multicurrency.currencies.colon.CostaRicanColon`           | Costa Rica                                      |      ₡123 456,79 |      ₡123 456,79 |  123,456.79 CRC |
| `multicurrency.currencies.kuna.CroatianKuna`               | Croatia                                         |    123.456,79 Kn |    123.456,79 Kn |  123,456.79 HRK |
| `multicurrency.currencies.peso.CubanPeso`                  | Cuba                                            |      $123,456.79 |    CU$123,456.79 |  123,456.79 CUP |
| `multicurrency.currencies.koruna.CzechKoruna`              | Czech Republic                                  |    123 456,79 Kč |    123 456,79 Kč |  123,456.79 CZK |
| `multicurrency.currencies.dalasi.Dalasi`                   | Gambia                                          |     D 123,456.79 |     D 123,456.79 |  123,456.79 GMD |
| `multicurrency.currencies.krone.DanishKrone`               | Denmark                                         |    123.456,79 kr |    123.456,79 kr |  123,456.79 DKK |
| `multicurrency.currencies.denar.Denar`                     | Macedonia                                       |  123.456,79 ден. |  123.456,79 ден. |  123,456.79 MKD |
| `multicurrency.currencies.franc.DjiboutiFranc`             | Djibouti                                        |        123 457 ₣ |      123 457 DJ₣ |     123,457 DJF |
| `multicurrency.currencies.dobra.Dobra`                     | Sao Tome and Principe                           |    123.456,79 Db |    123.456,79 Db |  123,456.79 STN |
| `multicurrency.currencies.peso.DominicanPeso`              | Dominican Republic                              |      $123,456.79 |    DO$123,456.79 |  123,456.79 DOP |
| `multicurrency.currencies.dong.Dong`                       | Vietnam                                         |        123.457 ₫ |        123.457 ₫ |     123,457 VND |
| `multicurrency.currencies.dollar.EasternCaribbeanDollar`   | Organisation of Eastern Caribbean States (OECS) |      $123,456.79 |      $123,456.79 |  123,456.79 XCD |
| `multicurrency.currencies.dollar.EasternCaribbeanDollarAG` | Antigua and Barbuda                             |      $123,456.79 |    AG$123,456.79 |  123,456.79 XCD |
| `multicurrency.currencies.dollar.EasternCaribbeanDollarAI` | Anguilla                                        |      $123,456.79 |    AI$123,456.79 |  123,456.79 XCD |
| `multicurrency.currencies.dollar.EasternCaribbeanDollarDM` | Dominica                                        |      $123,456.79 |    DM$123,456.79 |  123,456.79 XCD |
| `multicurrency.currencies.dollar.EasternCaribbeanDollarGD` | Grenada                                         |      $123,456.79 |    GD$123,456.79 |  123,456.79 XCD |
| `multicurrency.currencies.dollar.EasternCaribbeanDollarKN` | Saint Kitts and Nevis                           |      $123,456.79 |    KN$123,456.79 |  123,456.79 XCD |
| `multicurrency.currencies.dollar.EasternCaribbeanDollarLC` | Saint Lucia                                     |      $123,456.79 |    LC$123,456.79 |  123,456.79 XCD |
| `multicurrency.currencies.dollar.EasternCaribbeanDollarMS` | Montserrat                                      |      $123,456.79 |    MS$123,456.79 |  123,456.79 XCD |
| `multicurrency.currencies.dollar.EasternCaribbeanDollarVC` | Saint Vincent and Grenadine                     |      $123,456.79 |    VC$123,456.79 |  123,456.79 XCD |
| `multicurrency.currencies.pound.EgyptianPound`             | Egypt                                           |  ج.م. ١٢٣٬٤٥٦٫٧٩ |  ج.م. ١٢٣٬٤٥٦٫٧٩ |  123,456.79 EGP |
| `multicurrency.currencies.birr.EthiopianBirr`              | Ethiopia                                        |    ብር 123,456.79 |    ብር 123,456.79 |  123,456.79 ETB |
| `multicurrency.currencies.euro.Euro`                       |                                                 |     123.456,79 € |     123.456,79 € |  123,456.79 EUR |
| `multicurrency.currencies.euro.EuroAD`                     | Andorra                                         |     123.456,79 € |   123.456,79 AD€ |  123,456.79 EUR |
| `multicurrency.currencies.euro.EuroAT`                     | Austria                                         |     € 123.456,79 |   AT€ 123.456,79 |  123,456.79 EUR |
| `multicurrency.currencies.euro.EuroBE`                     | Belgium                                         |     € 123.456,79 |   BE€ 123.456,79 |  123,456.79 EUR |
| `multicurrency.currencies.euro.EuroCY`                     | Cyprus                                          |     123.456,79 € |   123.456,79 CY€ |  123,456.79 EUR |
| `multicurrency.currencies.euro.EuroDE`                     | Germany                                         |     123.456,79 € |   123.456,79 DE€ |  123,456.79 EUR |
| `multicurrency.currencies.euro.EuroEE`                     | Estonia                                         |     123 456,79 € |   123 456,79 EE€ |  123,456.79 EUR |
| `multicurrency.currencies.euro.EuroES`                     | Spain                                           |     123.456,79 € |   123.456,79 ES€ |  123,456.79 EUR |
| `multicurrency.currencies.euro.EuroFI`                     | Finland                                         |     123 456,79 € |   123 456,79 FI€ |  123,456.79 EUR |
| `multicurrency.currencies.euro.EuroFR`                     | France                                          |     123 456,79 € |   123 456,79 FR€ |  123,456.79 EUR |
| `multicurrency.currencies.euro.EuroGR`                     | Greece                                          |     123.456,79 € |   123.456,79 GR€ |  123,456.79 EUR |
| `multicurrency.currencies.euro.EuroIE`                     | Ireland                                         |      €123,456.79 |    IR€123,456.79 |  123,456.79 EUR |
| `multicurrency.currencies.euro.EuroIT`                     | Italy                                           |     123.456,79 € |   123.456,79 IT€ |  123,456.79 EUR |
| `multicurrency.currencies.euro.EuroLT`                     | Lithuania                                       |     123 456,79 € |   123 456,79 LT€ |  123,456.79 EUR |
| `multicurrency.currencies.euro.EuroLU`                     | Luxembourg                                      |     123.456,79 € |   123.456,79 LU€ |  123,456.79 EUR |
| `multicurrency.currencies.euro.EuroLV`                     | Latvia                                          |     123 456,79 € |   123 456,79 LV€ |  123,456.79 EUR |
| `multicurrency.currencies.euro.EuroMC`                     | Monaco                                          |     123 456,79 € |   123 456,79 MC€ |  123,456.79 EUR |
| `multicurrency.currencies.euro.EuroME`                     | Montenegro                                      |     123.456,79 € |   123.456,79 ME€ |  123,456.79 EUR |
| `multicurrency.currencies.euro.EuroMT`                     | Malta                                           |      €123,456.79 |    MT€123,456.79 |  123,456.79 EUR |
| `multicurrency.currencies.euro.EuroNL`                     | Netherlands                                     |     € 123.456,79 |   NL€ 123.456,79 |  123,456.79 EUR |
| `multicurrency.currencies.euro.EuroPT`                     | Portugal                                        |     € 123.456,79 |   PT€ 123.456,79 |  123,456.79 EUR |
| `multicurrency.currencies.euro.EuroSBA`                    | Akrotiri and Dhekelia                           |     123.456,79 € |     123.456,79 € |  123,456.79 EUR |
| `multicurrency.currencies.euro.EuroSI`                     | Slovenia                                        |     123.456,79 € |   123.456,79 SI€ |  123,456.79 EUR |
| `multicurrency.currencies.euro.EuroSK`                     | Slovakia                                        |     123 456,79 € |   123 456,79 SK€ |  123,456.79 EUR |
| `multicurrency.currencies.euro.EuroSM`                     | San-Marino                                      |     123.456,79 € |   123.456,79 SM€ |  123,456.79 EUR |
| `multicurrency.currencies.euro.EuroVA`                     | Vatican                                         |      €123,456.79 |    VA€123,456.79 |  123,456.79 EUR |
| `multicurrency.currencies.euro.EuroXK`                     | Kosovo                                          |     123 456,79 € |   123 456,79 XK€ |  123,456.79 EUR |
| `multicurrency.currencies.pound.FalklandIslandsPound`      | Falkland Islands                                |      £123,456.79 |    FK£123,456.79 |  123,456.79 FKP |
| `multicurrency.currencies.dollar.FijiDollar`               | Fiji                                            |      $123,456.79 |    FJ$123,456.79 |  123,456.79 FJD |
| `multicurrency.currencies.forint.Forint`                   | Hungary                                         |       123 457 Ft |       123 457 Ft |     123,457 HUF |
| `multicurrency.currencies.lari.GeorgiaLari`                | Georgia                                         |     123 456,79 ლ |   123 456,79 GEლ |  123,456.79 GEL |
| `multicurrency.currencies.pound.GibraltarPound`            | Gibraltar                                       |      £123,456.79 |    GI£123,456.79 |  123,456.79 GIP |
| `multicurrency.currencies.gourde.Gourde`                   | Haiti                                           |     G 123,456.79 |     G 123,456.79 |  123,456.79 HTG |
| `multicurrency.currencies.guarani.Guarani`                 | Paraguay                                        |        ₲ 123.457 |        ₲ 123.457 |     123,457 PYG |
| `multicurrency.currencies.franc.GuineaFranc`               | Guinea                                          |        123 457 ₣ |      123 457 GN₣ |     123,457 GNF |
| `multicurrency.currencies.dollar.GuyanaDollar`             | Guyana                                          |      $123,456.79 |    GY$123,456.79 |  123,456.79 GYD |
| `multicurrency.currencies.dollar.HongKongDollar`           | Hong Kong                                       |      $123,456.79 |    HK$123,456.79 |  123,456.79 HKD |
| `multicurrency.currencies.hryvnia.Hryvnia`                 | Ukraine                                         |     123 456,79 ₴ |     123 456,79 ₴ |  123,456.79 UAH |
| `multicurrency.currencies.krona.IcelandKrona`              | Iceland                                         |       123.457 Kr |       123.457 Kr |     123,457 ISK |
| `multicurrency.currencies.rupee.IndianRupee`               | India                                           |      ₹123,456.79 |      ₹123,456.79 |  123,456.79 INR |
| `multicurrency.currencies.rupee.IndianRupeeBT`             | Bhutan                                          |      ₹123,456.79 |    BT₹123,456.79 |  123,456.79 INR |
| `multicurrency.currencies.rupee.IndianRupeeIN`             | India                                           |      ₹123,456.79 |    IN₹123,456.79 |  123,456.79 INR |
| `multicurrency.currencies.rial.IranianRial`                | Iran                                            |     ۱۲۳٬۴۵۶٫۷۹ ﷼ |     ۱۲۳٬۴۵۶٫۷۹ ﷼ |  123,456.79 IRR |
| `multicurrency.currencies.dinar.IraqiDinar`                | Iraq                                            | د.ع. ١٢٣٬٤٥٦٫٧٨٩ | د.ع. ١٢٣٬٤٥٦٫٧٨٩ | 123,456.789 IQD |
| `multicurrency.currencies.dollar.JamaicanDollar`           | Jamaica                                         |      $123,456.79 |    JM$123,456.79 |  123,456.79 JMD |
| `multicurrency.currencies.dinar.JordanianDinar`            | Jordan                                          | د.أ. ١٢٣٬٤٥٦٫٧٨٩ | د.أ. ١٢٣٬٤٥٦٫٧٨٩ | 123,456.789 JOD |
| `multicurrency.currencies.shilling.KenyanShilling`         | Kenya                                           |   Ksh 123,456.79 |   Ksh 123,456.79 |  123,456.79 KES |
| `multicurrency.currencies.kina.Kina`                       | Papua New Guinea                                |     K 123,456.79 |     K 123,456.79 |  123,456.79 PGK |
| `multicurrency.currencies.kip.Kip`                         | Laos                                            |      ₭123.456,79 |      ₭123.456,79 |  123,456.79 LAK |
| `multicurrency.currencies.marka.KonvertibilnaMarka`        | Bosnia and Herzegovina                          |    123,456.79 КМ |    123,456.79 КМ |  123,456.79 BAM |
| `multicurrency.currencies.dinar.KuwaitiDinar`              | Kuwait                                          | د.ك. ١٢٣٬٤٥٦٫٧٨٩ | د.ك. ١٢٣٬٤٥٦٫٧٨٩ | 123,456.789 KWD |
| `multicurrency.currencies.kwacha.Kwacha`                   | Malawi                                          |    MK 123,456.79 |    MK 123,456.79 |  123,456.79 MWK |
| `multicurrency.currencies.kwanza.Kwanza`                   | Angola                                          |    123 456,79 Kz |    123 456,79 Kz |  123,456.79 AOA |
| `multicurrency.currencies.kyat.Kyat`                       | Myanmar (Burma)                                 |     ၁၂၃,၄၅၆.၇၉ K |     ၁၂၃,၄၅၆.၇၉ K |  123,456.79 MMK |
| `multicurrency.currencies.lari.Lari`                       |                                                 |     123 456,79 ლ |   123 456,79 GEლ |  123,456.79 GEL |
| `multicurrency.currencies.pound.LebanesePound`             | Lebanon                                         |     ل.ل. ١٢٣٬٤٥٧ |     ل.ل. ١٢٣٬٤٥٧ |     123,457 LBP |
| `multicurrency.currencies.lek.Lek`                         | Albania                                         |   123 456,79 Lek |   123 456,79 Lek |  123,456.79 ALL |
| `multicurrency.currencies.lempira.Lempira`                 | Honduras                                        |     L 123,456.79 |     L 123,456.79 |  123,456.79 HNL |
| `multicurrency.currencies.leone.Leone`                     | Sierra Leone                                    |    Le 123,456.79 |    Le 123,456.79 |  123,456.79 SLL |
| `multicurrency.currencies.leu.Leu`                         | Romania                                         |     123.456,79 L |     123.456,79 L |  123,456.79 RON |
| `multicurrency.currencies.dollar.LiberianDollar`           | Liberia                                         |      $123,456.79 |    LR$123,456.79 |  123,456.79 LRD |
| `multicurrency.currencies.dinar.LibyanDinar`               | Libya                                           | د.ل. 123.456,789 | د.ل. 123.456,789 | 123,456.789 LYD |
| `multicurrency.currencies.lilangeni.Lilangeni`             | Swaziland                                       |     L 123,456.79 |     L 123,456.79 |  123,456.79 SZL |
| `multicurrency.currencies.loti.Loti`                       | Lesotho                                         |     L 123,456.79 |     L 123,456.79 |  123,456.79 LSL |
| `multicurrency.currencies.ariary.MalagasyAriary`           | Madagascar                                      |       123 457 Ar |       123 457 Ar |     123,457 MGA |
| `multicurrency.currencies.ringgit.MalaysianRinggit`        | Malaysia                                        |    RM 123,456.79 |    RM 123,456.79 |  123,456.79 MYR |
| `multicurrency.currencies.manat.Manat`                     | Turkmenistan                                    |     123 456,79 m |     123 456,79 m |  123,456.79 TMT |
| `multicurrency.currencies.rupee.MauritiusRupee`            | Mauritius                                       |     ₨ 123,456.79 |     ₨ 123,456.79 |  123,456.79 MUR |
| `multicurrency.currencies.metical.Metical`                 | Mozambique                                      |      123.457 MTn |      123.457 MTn |     123,457 MZN |
| `multicurrency.currencies.peso.MexicanPeso`                | Mexico                                          |      $123,456.79 |    MX$123,456.79 |  123,456.79 MXN |
| `multicurrency.currencies.leu.MoldovanLeu`                 | Moldova                                         |     123.456,79 L |     123.456,79 L |  123,456.79 MDL |
| `multicurrency.currencies.dirham.MoroccanDirham`           | Morocco                                         |  ١٢٣٬٤٥٦٫٧٩ د.م. |  ١٢٣٬٤٥٦٫٧٩ د.م. |  123,456.79 MAD |
| `multicurrency.currencies.naira.Naira`                     | Nigeria                                         |      ₦123,456.79 |      ₦123,456.79 |  123,456.79 NGN |
| `multicurrency.currencies.nakfa.Nakfa`                     | Eritrea                                         |   Nfk 123,456.79 |   Nfk 123,456.79 |  123,456.79 ERN |
| `multicurrency.currencies.dollar.NamibiaDollar`            | Namibia                                         |      $123,456.79 |    NA$123,456.79 |  123,456.79 NAD |
| `multicurrency.currencies.rupee.NepaleseRupee`             | Nepal                                           |  नेरू १२३,४५६.७९ |  नेरू १२३,४५६.७९ |  123,456.79 NPR |
| `multicurrency.currencies.shekel.NewIsraeliShekel`         | Israel                                          |     123,456.79 ₪ |     123,456.79 ₪ |  123,456.79 ILS |
| `multicurrency.currencies.shekel.NewIsraeliShekelIL`       | Israel                                          |     123,456.79 ₪ |   123,456.79 IL₪ |  123,456.79 ILS |
| `multicurrency.currencies.shekel.NewIsraeliShekelPS`       | Palestine                                       |     123,456.79 ₪ |   123,456.79 PS₪ |  123,456.79 ILS |
| `multicurrency.currencies.dollar.NewZealandDollar`         | New Zealand                                     |      $123,456.79 |      $123,456.79 |  123,456.79 NZD |
| `multicurrency.currencies.dollar.NewZealandDollarCK`       | Cook Islands                                    |      $123,456.79 |    CK$123,456.79 |  123,456.79 NZD |
| `multicurrency.currencies.dollar.NewZealandDollarNU`       | Niue                                            |      $123,456.79 |    NU$123,456.79 |  123,456.79 NZD |
| `multicurrency.currencies.dollar.NewZealandDollarNZ`       | New Zealand                                     |      $123,456.79 |    NZ$123,456.79 |  123,456.79 NZD |
| `multicurrency.currencies.dollar.NewZealandDollarPN`       | Pitcairn Island                                 |      $123,456.79 |    PN$123,456.79 |  123,456.79 NZD |
| `multicurrency.currencies.ngultrum.Ngultrum`               | Bhutan                                          |   Nu. ༡༢༣,༤༥༦.༧༩ |   Nu. ༡༢༣,༤༥༦.༧༩ |  123,456.79 BTN |
| `multicurrency.currencies.won.NorthKoreanWon`              | North Korea                                     |     ₩ 123,456.79 |     ₩ 123,456.79 |  123,456.79 KPW |
| `multicurrency.currencies.krone.NorwegianKrone`            | Norway                                          |    kr 123 456,79 |    kr 123 456,79 |  123,456.79 NOK |
| `multicurrency.currencies.nuevo_sol.NuevoSol`              | Peru                                            |   S/. 123,456.79 |   S/. 123,456.79 |  123,456.79 PEN |
| `multicurrency.currencies.ouguiya.Ouguiya`                 | Mauritania                                      |   ١٢٣٬٤٥٦٫٧٩ أ.م |   ١٢٣٬٤٥٦٫٧٩ أ.م |  123,456.79 MRU |
| `multicurrency.currencies.pzloty.PZloty`                   | Poland                                          |    123 456,79 zł |    123 456,79 zł |  123,456.79 PLN |
| `multicurrency.currencies.paanga.Paanga`                   | Tonga                                           |    T$ 123,456.79 |    T$ 123,456.79 |  123,456.79 TOP |
| `multicurrency.currencies.rupee.PakistanRupee`             | Pakistan                                        |     ₨ 123,456.79 |     ₨ 123,456.79 |  123,456.79 PKR |
| `multicurrency.currencies.pataca.Pataca`                   | Macao                                           |     P 123,456.79 |     P 123,456.79 |  123,456.79 MOP |
| `multicurrency.currencies.peso.PesoUruguayo`               | Uruguay                                         |     $ 123.456,79 |   UY$ 123.456,79 |  123,456.79 UYU |
| `multicurrency.currencies.peso.PhilippinePeso`             | Philippines                                     |      ₱123,456.79 |      ₱123,456.79 |  123,456.79 PHP |
| `multicurrency.currencies.pound.PoundSterling`             | Great Britain                                   |      £123,456.79 |      £123,456.79 |  123,456.79 GBP |
| `multicurrency.currencies.pound.PoundSterlingGB`           | Great Britain                                   |      £123,456.79 |    GB£123,456.79 |  123,456.79 GBP |
| `multicurrency.currencies.pound.PoundSterlingGG`           | Alderney                                        |      £123,456.79 |    GG£123,456.79 |  123,456.79 GBP |
| `multicurrency.currencies.pound.PoundSterlingIM`           | Isle of Man                                     |      £123,456.79 |    IM£123,456.79 |  123,456.79 GBP |
| `multicurrency.currencies.pound.PoundSterlingIO`           | British Indian Ocean Territory                  |      £123,456.79 |    IO£123,456.79 |  123,456.79 GBP |
| `multicurrency.currencies.pula.Pula`                       | Botswana                                        |     P 123,456.79 |     P 123,456.79 |  123,456.79 BWP |
| `multicurrency.currencies.rial.QatariRial`                 | Qatar                                           |  ر.ق. ١٢٣٬٤٥٦٫٧٩ |  ر.ق. ١٢٣٬٤٥٦٫٧٩ |  123,456.79 QAR |
| `multicurrency.currencies.quetzal.Quetzal`                 | Guatemala                                       |     Q 123,456.79 |     Q 123,456.79 |  123,456.79 GTQ |
| `multicurrency.currencies.rand.Rand`                       | South Africa                                    |     R 123 456.79 |     R 123 456.79 |  123,456.79 ZAR |
| `multicurrency.currencies.rand.RandLS`                     | Lesotho                                         |     R 123,456.79 |   LSR 123,456.79 |  123,456.79 ZAR |
| `multicurrency.currencies.rand.RandNA`                     | Namibia                                         |     R 123 456.79 |   NAR 123 456.79 |  123,456.79 ZAR |
| `multicurrency.currencies.rand.RandZA`                     | South Africa                                    |     R 123 456.79 |   ZAR 123 456.79 |  123,456.79 ZAR |
| `multicurrency.currencies.rial.RialOmani`                  | Oman                                            | ر.ع. ١٢٣٬٤٥٦٫٧٨٩ | ر.ع. ١٢٣٬٤٥٦٫٧٨٩ | 123,456.789 OMR |
| `multicurrency.currencies.riel.Riel`                       | Cambodia                                        |      123.456,79៛ |      123.456,79៛ |  123,456.79 KHR |
| `multicurrency.currencies.rufiyaa.Rufiyaa`                 | Maldives                                        |    ރ. 123,456.79 |    ރ. 123,456.79 |  123,456.79 MVR |
| `multicurrency.currencies.rupiah.Rupiah`                   | Indonesia                                       |    Rp 123.456,79 |    Rp 123.456,79 |  123,456.79 IDR |
| `multicurrency.currencies.ruble.RussianRuble`              | Russia                                          |     123 456,79 ₽ |     123 456,79 ₽ |  123,456.79 RUB |
| `multicurrency.currencies.ruble.RussianRubleGE`            | South Ossetia                                   |     123 456,79 ₽ |   123 456,79 GE₽ |  123,456.79 RUB |
| `multicurrency.currencies.ruble.RussianRubleRU`            | Russia                                          |     123 456,79 ₽ |   123 456,79 RU₽ |  123,456.79 RUB |
| `multicurrency.currencies.franc.RwandaFranc`               | Rwanda                                          |        ₣ 123.457 |      RW₣ 123.457 |     123,457 RWF |
| `multicurrency.currencies.pound.SaintHelenaPound`          | Saint Helena                                    |      £123,456.79 |    SH£123,456.79 |  123,456.79 SHP |
| `multicurrency.currencies.pound.SaintHelenaPoundAI`        | Ascension Island                                |      £123,456.79 |    SH£123,456.79 |  123,456.79 SHP |
| `multicurrency.currencies.pound.SaintHelenaPoundTC`        | Tristan da Cunha                                |      £123,456.79 |    SH£123,456.79 |  123,456.79 SHP |
| `multicurrency.currencies.riyal.SaudiRiyal`                | Saudi Arabia                                    |  ر.س. ١٢٣٬٤٥٦٫٧٩ |  ر.س. ١٢٣٬٤٥٦٫٧٩ |  123,456.79 SAR |
| `multicurrency.currencies.dinar.SerbianDinarSR`            | Serbia                                          |  123 456,79 дин. |  123 456,79 дин. |  123,456.79 RSD |
| `multicurrency.currencies.dinar.SerbianDinarXK`            | Kosovo                                          |  123.456,79 дин. |  123.456,79 дин. |  123,456.79 RSD |
| `multicurrency.currencies.rupee.SeychellesRupee`           | Seychelles                                      |     ₨ 123,456.79 |     ₨ 123,456.79 |  123,456.79 SCR |
| `multicurrency.currencies.dollar.SingaporeDollar`          | Singapore                                       |      $123,456.79 |      $123,456.79 |  123,456.79 SGD |
| `multicurrency.currencies.dollar.SingaporeDollarBN`        | Brunei                                          |      $123,456.79 |    BN$123,456.79 |  123,456.79 SGD |
| `multicurrency.currencies.dollar.SingaporeDollarSG`        | Singapore                                       |      $123,456.79 |    SG$123,456.79 |  123,456.79 SGD |
| `multicurrency.currencies.dollar.SolomonIslandsDollar`     | Solomon Islands                                 |      $123,456.79 |    SB$123,456.79 |  123,456.79 SBD |
| `multicurrency.currencies.som.Som`                         | Kyrgyzstan                                      |    123 456,79 Лв |    123 456,79 Лв |  123,456.79 KGS |
| `multicurrency.currencies.shilling.SomaliShilling`         | Somalia                                         |   SSh 123,456.79 |   SSh 123,456.79 |  123,456.79 SOS |
| `multicurrency.currencies.somoni.Somoni`                   | Tajikistan                                      |    ЅМ 123,456.79 |    ЅМ 123,456.79 |  123,456.79 TJS |
| `multicurrency.currencies.won.SouthKoreanWon`              | South Korea                                     |         ₩123,457 |         ₩123,457 |     123,457 KRW |
| `multicurrency.currencies.lari.SouthOssetiaLari`           | South Ossetia                                   |     123 456,79 ლ |   123 456,79 GEლ |  123,456.79 GEL |
| `multicurrency.currencies.rupee.SriLankaRupee`             | Sri Lanka                                       |   රු. 123,456.79 |   රු. 123,456.79 |  123,456.79 LKR |
| `multicurrency.currencies.pound.SudanesePound`             | Sudan                                           |   ١٢٣٬٤٥٦٫٧٩ ج.س |   ١٢٣٬٤٥٦٫٧٩ ج.س |  123,456.79 SDG |
| `multicurrency.currencies.dollar.SurinameDollar`           | Suriname                                        |     $ 123.456,79 |   SR$ 123.456,79 |  123,456.79 SRD |
| `multicurrency.currencies.krona.SwedishKrona`              | Sweden                                          |    123 456,79 kr |    123 456,79 kr |  123,456.79 SEK |
| `multicurrency.currencies.franc.SwissFranc`                | Switzerland                                     |     ₣ 123'456.79 |     ₣ 123'456.79 |  123,456.79 CHF |
| `multicurrency.currencies.franc.SwissFrancCH`              | Switzerland                                     |     ₣ 123'456.79 |   CH₣ 123'456.79 |  123,456.79 CHF |
| `multicurrency.currencies.franc.SwissFrancLI`              | Liechtenstein                                   |     ₣ 123'456.79 |   LI₣ 123'456.79 |  123,456.79 CHF |
| `multicurrency.currencies.pound.SyrianPound`               | Syria                                           |   ١٢٣٬٤٥٦٫٧٩ ل.س |   ١٢٣٬٤٥٦٫٧٩ ل.س |  123,456.79 SYP |
| `multicurrency.currencies.dollar.TaiwanDollar`             | Taiwan                                          |      $123,456.79 |    TW$123,456.79 |  123,456.79 TWD |
| `multicurrency.currencies.taka.Taka`                       | Bangladesh                                      |      ১২৩,৪৫৬.৭৯৳ |      ১২৩,৪৫৬.৭৯৳ |  123,456.79 BDT |
| `multicurrency.currencies.tala.Tala`                       | Samoa                                           |     T 123,456.79 |     T 123,456.79 |  123,456.79 WST |
| `multicurrency.currencies.shilling.TanzanianShilling`      | Tanzania                                        |   TSh 123,456.79 |   TSh 123,456.79 |  123,456.79 TZS |
| `multicurrency.currencies.tenge.Tenge`                     | Kazakhstan                                      |     123 456,79 〒 |     123 456,79 〒 |  123,456.79 KZT |
| `multicurrency.currencies.dollar.TrinidadandTobagoDollar`  | Trinidad and Tobago                             |      $123,456.79 |    TT$123,456.79 |  123,456.79 TTD |
| `multicurrency.currencies.tugrik.Tugrik`                   | Mongolia                                        |     ₮ 123,456.79 |     ₮ 123,456.79 |  123,456.79 MNT |
| `multicurrency.currencies.dinar.TunisianDinar`             | Tunisia                                         | د.ت. 123.456,789 | د.ت. 123.456,789 | 123,456.789 TND |
| `multicurrency.currencies.lira.TurkishLira`                | Turkey                                          |      ₤123.456,79 |      ₤123.456,79 |  123,456.79 TRY |
| `multicurrency.currencies.lira.TurkishLiraCY`              | North Cyprus                                    |      ₤123.456,79 |    CY₤123.456,79 |  123,456.79 TRY |
| `multicurrency.currencies.lira.TurkishLiraTR`              | Turkey                                          |      ₤123.456,79 |    TR₤123.456,79 |  123,456.79 TRY |
| `multicurrency.currencies.dirham.UAEDirham`                | UAE                                             |  د.إ. ١٢٣٬٤٥٦٫٧٩ |  د.إ. ١٢٣٬٤٥٦٫٧٩ |  123,456.79 AED |
| `multicurrency.currencies.dollar.USDollar`                 | United States of America                        |      $123,456.79 |    US$123,456.79 |  123,456.79 USD |
| `multicurrency.currencies.dollar.USDollarAS`               | American Samoa                                  |      $123,456.79 |    AS$123,456.79 |  123,456.79 USD |
| `multicurrency.currencies.dollar.USDollarFM`               | Micronesia                                      |      $123,456.79 |    FM$123,456.79 |  123,456.79 USD |
| `multicurrency.currencies.dollar.USDollarGU`               | Guam                                            |      $123,456.79 |    GU$123,456.79 |  123,456.79 USD |
| `multicurrency.currencies.dollar.USDollarHT`               | Haiti                                           |      $123,456.79 |    HT$123,456.79 |  123,456.79 USD |
| `multicurrency.currencies.dollar.USDollarIO`               | British Indian Ocean Territory                  |      $123,456.79 |    IO$123,456.79 |  123,456.79 USD |
| `multicurrency.currencies.dollar.USDollarMH`               | Marshall Islands                                |      $123,456.79 |    MH$123,456.79 |  123,456.79 USD |
| `multicurrency.currencies.dollar.USDollarMP`               | Northern Mariana Islands                        |      $123,456.79 |    MP$123,456.79 |  123,456.79 USD |
| `multicurrency.currencies.dollar.USDollarPA`               | Panama                                          |      $123,456.79 |    PA$123,456.79 |  123,456.79 USD |
| `multicurrency.currencies.dollar.USDollarPC`               | Pacific Remote Islands                          |      $123,456.79 |    PC$123,456.79 |  123,456.79 USD |
| `multicurrency.currencies.dollar.USDollarPR`               | Puerto Rico                                     |      $123,456.79 |    PR$123,456.79 |  123,456.79 USD |
| `multicurrency.currencies.dollar.USDollarPW`               | Palau                                           |      $123,456.79 |    PW$123,456.79 |  123,456.79 USD |
| `multicurrency.currencies.dollar.USDollarTC`               | Turks and Caicos Islands                        |      $123,456.79 |    TC$123,456.79 |  123,456.79 USD |
| `multicurrency.currencies.dollar.USDollarVG`               | British Virgin Islands                          |      $123,456.79 |    VG$123,456.79 |  123,456.79 USD |
| `multicurrency.currencies.dollar.USDollarVI`               | US Virgin Islands                               |      $123,456.79 |    VI$123,456.79 |  123,456.79 USD |
| `multicurrency.currencies.shilling.UgandaShilling`         | Uganda                                          |      USh 123,457 |      USh 123,457 |     123,457 UGX |
| `multicurrency.currencies.sum.UzbekistanSum`               | Uzbekistan                                      |   123 456,79 сўм |   123 456,79 сўм |  123,456.79 UZS |
| `multicurrency.currencies.vatu.Vatu`                       | Vanuatu                                         |       Vt 123,457 |       Vt 123,457 |     123,457 VUV |
| `multicurrency.currencies.rial.YemeniRial`                 | Yemen                                           |     ١٢٣٬٤٥٦٫٧٩ ﷼ |     ١٢٣٬٤٥٦٫٧٩ ﷼ |  123,456.79 YER |
| `multicurrency.currencies.yen.Yen`                         | Japan                                           |         ¥123,457 |         ¥123,457 |     123,457 JPY |
| `multicurrency.currencies.yuan.Yuan`                       | China                                           |      ¥123,456.79 |      ¥123,456.79 |  123,456.79 CNY |
| `multicurrency.currencies.kwacha.ZambianKwacha`            | Zambia                                          |    ZK 123,456.79 |    ZK 123,456.79 |  123,456.79 ZMW |
| `multicurrency.currencies.dollar.ZimbabweDollar`           | Zimbabwe                                        |     $ 123,456.79 |   ZW$ 123,456.79 |  123,456.79 ZWL |

## Supported Cryptocurrencies

Table of supported cryptocurrencies (and default format):

| Cryptocurrency                                  |                     Default |                   Localized |                  International |
|:------------------------------------------------|----------------------------:|----------------------------:|-------------------------------:|
| `multicurrency.currencies.crypto.Bitcoin`       |           ₿123,456.78900000 |           ₿123,456.78900000 |           123,456.78900000 XBT |
| `multicurrency.currencies.crypto.EOS`           |               ε123,456.7890 |               ε123,456.7890 |               123,456.7890 EOS |
| `multicurrency.currencies.crypto.Ethereum`      | Ξ123,456.789000000000000000 | Ξ123,456.789000000000000000 | 123,456.789000000000000000 ETH |
| `multicurrency.currencies.crypto.Monero`        |       ɱ123,456.789000000000 |       ɱ123,456.789000000000 |       123,456.789000000000 XMR |
| `multicurrency.currencies.crypto.Ripple`        |             ✕123,456.789000 |             ✕123,456.789000 |             123,456.789000 XRP |
| `multicurrency.currencies.crypto.StellarLumens` |            *123,456.7890000 |            *123,456.7890000 |            123,456.7890000 XLM |
| `multicurrency.currencies.crypto.Tezos`         |             ꜩ123,456.789000 |             ꜩ123,456.789000 |             123,456.789000 XTZ |
| `multicurrency.currencies.crypto.Zcash`         |           ⓩ123,456.78900000 |           ⓩ123,456.78900000 |           123,456.78900000 ZEC |

## Build (from source)

[GNU make](https://www.gnu.org/software/make/manual/make.html) is used to
automate several steps of the development process.

All of the commands described bellow are to be executed on the root folder of
this project.

A development environment can be created using the following command:

```shell
make dev
```

To build a Python package for this library use the following command:

```shell
make build
```

After this you should have a wheel file (`*.whl`) inside a folder called
`dist`.

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
