# multicurrency

Currency representation.

> :warning: **WARNING**:
>
> This module is still in Beta. Do not use it in production ready
> applications.
>
> Currency format (representation) is not yet implemented.

## Synopsis

The multicurrency module provides support for currency operations. It supports
several different currencies.

The currencies supported by this module were created with information
(alphabetic code, numeric code, and minor unit size) from ISO-4217.

## Prerequisites

Python, version 3.9 or above, needs to be installed on your local computer.
Python setup can be found [here](https://www.python.org/downloads/).

## Installation

The simplest way to install this library is using pip:

```shell
pip3 install multicurrency
```

## Usage

Simple usage example:

```python
>>> from multicurrency import Euro
>>> euro = Euro(1000)
>>> print(euro)
€1.000,00
>>> print(euro + Euro(0.50))
€1.000,50
```

Unsupported currencies can be represented by creating a generic `Currency`
object with the desired settings.

```python
>>> from multicurrency import Currency
>>> bitcoin = Currency(
...     amount=1000,
...     currency='XBT',
...     symbol='Ƀ',
...     code='0',
...     decimal_places=8,
...     decimal_sign='.',
...     grouping_sign=',')
>>> print(bitcoin)
Ƀ1,000.00000000
```

To help working with unsupported currencies the settings can be defined in a
dictionary and used when needed:

```python
>>> from multicurrency import Currency
>>> settings = {
...     'currency':'XBT',
...     'symbol':'Ƀ',
...     'code':'0',
...     'decimal_places':8,
...     'decimal_sign':'.',
...     'grouping_sign':','}
>>> bitcoin = Currency(1000, **settings)
>>> print(bitcoin)
Ƀ1,000.00000000
```

Currencies can also be represented with the ISO 4217 three-letter code instead
of the `symbol`.

```python
>>> from multicurrency import Euro
>>> euro = Euro(1000, international=True)
>>> print(euro)
EUR 1.000,00
```

## Precision

The multicurrency library has a user alterable precision (defaulting to 28
places) which can be as large as needed for a given problem:

```python
>>> from multicurrency import CurrencyContext, Euro
>>> for precision in [1, 2, 3, 4, 5, 6]:
...     CurrencyContext.prec = precision
...     result = Euro(1) / 7
...     print(result.pstr(precision))
...
€0,1
€0,14
€0,143
€0,1429
€0,14286
€0,142857
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
...     print(f'{rounding:16}', result.pstr(4))
...
ROUND_CEILING    €0,1429
ROUND_DOWN       €0,1428
ROUND_FLOOR      €0,1428
ROUND_HALF_DOWN  €0,1429
ROUND_HALF_EVEN  €0,1429
ROUND_HALF_UP    €0,1429
ROUND_UP         €0,1429
ROUND_05UP       €0,1428
```

Supported rounding methods are described on the `CurrencyContext` class.

## Operations

Several operations are supported by the several library classes.

* Absolute

    Produces the absolute value of a given currency.

    ```python
    >>> from multicurrency import Euro
    >>> euro = abs(Euro(-2))
    >>> print(euro)
    €2,00
    ```

* Addiction

    Addiction is supported only between currencies of the same type.

    ```python
    >>> from multicurrency import Euro
    >>> euro1 = Euro(2.5)
    >>> euro2 = Euro(3)
    >>> print(euro1 + euro2)
    €5,50
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
    €1,00
    ```

* Copy

    Produces a copy of itself.

    ```python
    >>> from multicurrency import Euro
    >>> from copy import copy
    >>> euro = copy(Euro(1/7))
    >>> print(euro)
    €0,14
    ```

* Division

    Produces a new currency with the value of the division of the currency by
    either an `int`, `float`, or `Decimal`.

    ```python
    >>> from multicurrency import Euro
    >>> euro = Euro(7) / 2
    >>> print(euro)
    €3,50
    ```

* Divmod

    Produces a tuple consisting of the currencies with the quotient and the
    remainder of the division of the currency by either an `int`, `float`, or
    `Decimal`.

    ```python
    >>> from multicurrency import Euro
    >>> q, r = divmod(Euro(7), 2)
    >>> print(q, r)
    €3,00 €1,00
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
    €3,00
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
    €1,00
    ```

* Multiplication

    Multiplication is supported only between a currency and an `int`, `float`,
    or `Decimal`.

    ```python
    >>> from multicurrency import Euro
    >>> print(Euro(2) * 2.5)
    €5,00
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
    €-1,00
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

`Afghani` (Af1.000,00),
`AlgerianDinar` (د.ج1.000,00),
`ArgentinePeso` ($1.000,00),
`ArmenianDram` (Դ1,000.00),
`ArubanFlorin` (ƒ1,000.00),
`AustralianDollar` ($1,000.00),
`AzerbaijanianManat` (ман1.000,00),
`BahamianDollar` ($1,000.00),
`BahrainiDinar` (ب.د1,000.000),
`Baht` (฿1,000.00),
`Balboa` (B/.1.000,00),
`BarbadosDollar` ($1.000,00),
`BelarusianRuble` (Br1.000,00),
`BelizeDollar` ($1,000.00),
`BermudianDollar` ($1,000.00),
`BolivarFuerte` (Bs F1.000,00),
`Boliviano` (Bs.1,000.00),
`BrazilianReal` (R$1.000,00),
`BruneiDollar` ($1,000.00),
`BulgarianLev` (лв1.000,00),
`BurundiFranc` (₣1.000),
`CFAFrancBCEAO` (₣1.000),
`CFAFrancBEAC` (₣1.000),
`CFPFranc` (₣1.000),
`CanadianDollarEN` ($1,000.00),
`CanadianDollarFR` ($1.000,00),
`CapeVerdeEscudo` ($1.000,00),
`CaymanIslandsDollar` ($1,000.00),
`Cedi` (₵1.000,00),
`ChileanPeso` ($1.000),
`ColombianPeso` ($1.000,00),
`CongoleseFranc` (₣1.000,00),
`CordobaOro` (C$1.000,00),
`CostaRicanColon` (₡1.000,00),
`CroatianKuna` (Kn1.000,00),
`CubanPeso` ($1,000.00),
`CzechKoruna` (Kč1.000,00),
`Dalasi` (D1.000,00),
`DanishKrone` (kr1.000,00),
`Denar` (ден1,000.00),
`DjiboutiFranc` (₣1.000),
`Dobra` (Db1.000,00),
`DominicanPeso` ($1,000.00),
`Dong` (₫1.000),
`EastCaribbeanDollar` ($1,000.00),
`EgyptianPound` (£1,000.00),
`EthiopianBirr` (1.000,00),
`Euro` (€1.000,00),
`FalklandIslandsPound` (£1.000,00),
`FijiDollar` ($1.000,00),
`Forint` (Ft1.000),
`GibraltarPound` (£1.000,00),
`Gourde` (G1.000,00),
`Guarani` (₲1.000),
`GuineaFranc` (₣1.000),
`GuyanaDollar` ($1.000,00),
`HongKongDollar` ($1,000.00),
`Hryvnia` (₴1.000,00),
`IcelandKrona` (Kr1.000),
`IndianRupee` (₹1,000.00),
`IranianRial` (﷼1,000.00),
`IraqiDinar` (ع.د1.000,000),
`JamaicanDollar` ($1,000.00),
`JordanianDinar` (د.ا1,000.000),
`KenyanShilling` (Sh1,000.00),
`Kina` (K1.000,00),
`Kip` (₭1.000,00),
`KonvertibilnaMarka` (КМ1,000.00),
`KuwaitiDinar` (د.ك1,000.000),
`Kwacha` (MK1.000,00),
`Kwanza` (Kz1.000,00),
`Kyat` (K1.000,00),
`Lari` (ლ1.000,00),
`LebanesePound` (ل.ل1 000),
`Lek` (L1.000,00),
`Lempira` (L1,000.00),
`Leone` (Le1.000,00),
`Leu` (L1.000,00),
`LiberianDollar` ($1.000,00),
`LibyanDinar` (ل.د1.000,000),
`Lilangeni` (L1,000.00),
`Loti` (L1.000,00),
`MalagasyAriary` (1.000),
`MalaysianRinggit` (RM1,000.00),
`Manat` (m1.000,00),
`MauritiusRupee` (₨1,000.00),
`Metical` (MTn1.000),
`MexicanPeso` ($1,000.00),
`MoldovanLeu` (L1.000,00),
`MoroccanDirham` (د.م.1.000,00),
`Naira` (₦1.000,00),
`Nakfa` (Nfk1.000,00),
`NamibiaDollar` ($1.000,00),
`NepaleseRupee` (₨1,000.00),
`NewIsraeliShekel` (₪1,000.00),
`NewZealandDollar` ($1,000.00),
`Ngultrum` (1.000,00),
`NorthKoreanWon` (₩1.000,00),
`NorwegianKrone` (kr1.000,00),
`NuevoSol` (S/.1,000.00),
`Ouguiya` (UM1.000,00),
`PZloty` (zł1.000,00),
`PakistanRupee` (₨1,000.00),
`Pataca` (P1.000,00),
`Paanga` (T$1,000.00),
`PesoUruguayo` ($1.000,00),
`PhilippinePeso` (₱1,000.00),
`PoundSterling` (£1,000.00),
`Pula` (P1.000,00),
`QatariRial` (ر.ق1.000,00),
`Quetzal` (Q1.000,00),
`Rand` (R1 000.00),
`RialOmani` (ر.ع.1,000.000),
`Riel` (៛1.000,00),
`Rufiyaa` (ރ.1.000,00),
`Rupiah` (Rp1.000,00),
`RussianRuble` (р.1.000,00),
`RwandaFranc` (₣1.000),
`SaintHelenaPound` (£1.000,00),
`SaudiRiyal` (ر.س1,000.00),
`SerbianDinar` (din1.000,00),
`SeychellesRupee` (₨1.000,00),
`SingaporeDollar` ($1,000.00),
`SolomonIslandsDollar` ($1.000,00),
`Som` (1.000,00),
`SomaliShilling` (Sh1.000,00),
`Somoni` (ЅМ1.000,00),
`SouthKoreanWon` (₩1,000),
`SriLankaRupee` (Rs1.000,00),
`SudanesePound` (£1.000,00),
`SurinameDollar` ($1.000,00),
`SwedishKrona` (kr1.000,00),
`SwissFranc` (₣1'000.00),
`SyrianPound` (ل.س1.000,00),
`TaiwanDollar` ($1.000,00),
`Taka` (৳1,000.00),
`Tala` (T1.000,00),
`TanzanianShilling` (Sh1,000.00),
`Tenge` (〒1.000,00),
`TrinidadandTobagoDollar` ($1.000,00),
`Tugrik` (₮1.000,00),
`TunisianDinar` (د.ت1.000,000),
`TurkishLira` (₤1,000.00),
`UAEDirham` (د.إ1,000.00),
`USDollar` ($1,000.00),
`UgandaShilling` (Sh1.000),
`UzbekistanSum` (1.000,00),
`Vatu` (Vt1,000),
`YemeniRial` (﷼1.000,00),
`Yen` (¥1,000),
`Yuan` (¥1,000.00),
`ZambianKwacha` (ZK1.000,00),
`ZimbabweDollar` ($1.000,00)

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
source venv/bin/activate
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
