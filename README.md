# multicurrency

Currency representation.

> :warning: **WARNING**:
>
> This module is still in Beta. Do not use it in production ready
> applications.
>
> Currency format (representation) is not yet fully implemented.

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

`Afghani` (؋ ۱۲۳٬۴۵۶٫۷۹ | AFN 123,456.79),
`AlgerianDinar` (123.456,79 د.ج | DZD 123,456.79),
`ArgentinePeso` ($ 123.456,79 | ARS 123,456.79),
`ArmenianDram` (123 456,79 Դ | AMD 123,456.79),
`ArubanFlorin` (ƒ123,456.79 | AWG 123,456.79),
`AustralianDollar` ($123,456.79 | AUD 123,456.79),
`AzerbaijanianManat` (123.456,79 ₼ | AZN 123,456.79),
`BahamianDollar` ($123,456.79 | BSD 123,456.79),
`BahrainiDinar` (١٢٣٬٤٥٦٫٧٨٩ ب.د | BHD 123,456.789),
`Baht` (฿123,456.79 | THB 123,456.79),
`Balboa` (B/. 123,456.79 | PAB 123,456.79),
`BarbadosDollar` ($123,456.79 | BBD 123,456.79),
`BelarusianRuble` (123 456,79 Br | BYN 123,456.79),
`BelizeDollar` ($123,456.79 | BZD 123,456.79),
`BermudianDollar` ($123,456.79 | BMD 123,456.79),
`BolivarFuerte` (Bs.F 123.456,79 | VEF 123,456.79),
`Boliviano` (Bs. 123.456,79 | BOB 123,456.79),
`BrazilianReal` (R$ 123.456,79 | BRL 123,456.79),
`BruneiDollar` ($ 123.456,79 | BND 123,456.79),
`BulgarianLev` (123456,79 лв | BGN 123,456.79),
`BurundiFranc` (123 457 ₣ | BIF 123,457),
`CFAFrancBCEAO` (123 457 ₣ | XOF 123,457),
`CFAFrancBEAC` (123 457 ₣ | XAF 123,457),
`CFPFranc` (123 457 ₣ | XPF 123,457),
`CanadianDollarEN` ($123,456.79 | CAD 123,456.79),
`CanadianDollarFR` (123 456,79 $ | CAD 123,456.79),
`CapeVerdeEscudo` (123 456$79 | CVE 123,456.79),
`CaymanIslandsDollar` ($123,456.79 | KYD 123,456.79),
`Cedi` (₵123,456.79 | GHS 123,456.79),
`ChileanPeso` ($123.457 | CLP 123,457),
`ColombianPeso` ($ 123.456,79 | COP 123,456.79),
`CongoleseFranc` (123 456,79 ₣ | CDF 123,456.79),
`CordobaOro` (C$123,456.79 | NIO 123,456.79),
`CostaRicanColon` (₡123 456,79 | CRC 123,456.79),
`CroatianKuna` (123.456,79 Kn | HRK 123,456.79),
`CubanPeso` ($123,456.79 | CUP 123,456.79),
`CzechKoruna` (123 456,79 Kč | CZK 123,456.79),
`Dalasi` (D 123,456.79 | GMD 123,456.79),
`DanishKrone` (123.456,79 kr | DKK 123,456.79),
`Denar` (123.456,79 ден. | MKD 123,456.79),
`DjiboutiFranc` (123 457 ₣ | DJF 123,457),
`Dobra` (123.456,79 Db | STN 123,456.79),
`DominicanPeso` ($123,456.79 | DOP 123,456.79),
`Dong` (123.457 ₫ | VND 123,457),
`EastCaribbeanDollar` ($123,456.79 | XCD 123,456.79),
`EgyptianPound` (ج.م ١٢٣٬٤٥٦٫٧٩ | EGP 123,456.79),
`EthiopianBirr` (ብር 123,456.79 | ETB 123,456.79),
`Euro` (123.456,79 € | EUR 123,456.79),
`EuroAD` (123.456,79 € | EUR 123,456.79),
`EuroAT` (€ 123.456,79 | EUR 123,456.79),
`EuroBE` (€ 123.456,79 | EUR 123,456.79),
`EuroCY` (123.456,79 € | EUR 123,456.79),
`EuroDE` (123.456,79 € | EUR 123,456.79),
`EuroEE` (123 456,79 € | EUR 123,456.79),
`EuroES` (123.456,79 € | EUR 123,456.79),
`EuroFI` (123 456,79 € | EUR 123,456.79),
`EuroFR` (123 456,79 € | EUR 123,456.79),
`EuroGR` (123.456,79 € | EUR 123,456.79),
`EuroIE` (€123,456.79 | EUR 123,456.79),
`EuroIT` (123.456,79 € | EUR 123,456.79),
`EuroLT` (123 456,79 € | EUR 123,456.79),
`EuroLU` (123.456,79 € | EUR 123,456.79),
`EuroLV` (123 456,79 € | EUR 123,456.79),
`EuroMC` (123 456,79 € | EUR 123,456.79),
`EuroME` (123.456,79 € | EUR 123,456.79),
`EuroMT` (€123,456.79 | EUR 123,456.79),
`EuroNL` (€ 123.456,79 | EUR 123,456.79),
`EuroPT` (€ 123.456,79 | EUR 123,456.79),
`EuroSI` (123.456,79 € | EUR 123,456.79),
`EuroSK` (123 456,79 € | EUR 123,456.79),
`EuroSM` (123.456,79 € | EUR 123,456.79),
`EuroVA` (€123,456.79 | EUR 123,456.79),
`EuroXK` (123 456,79 € | EUR 123,456.79),
`FalklandIslandsPound` (£123,456.79 | FKP 123,456.79),
`FijiDollar` ($123,456.79 | FJD 123,456.79),
`Forint` (123 457 Ft | HUF 123,457),
`GibraltarPound` (£123,456.79 | GIP 123,456.79),
`Gourde` (G 123,456.79 | HTG 123,456.79),
`Guarani` (₲ 123.457 | PYG 123,457),
`GuineaFranc` (123 457 ₣ | GNF 123,457),
`GuyanaDollar` ($123,456.79 | GYD 123,456.79),
`HongKongDollar` ($123,456.79 | HKD 123,456.79),
`Hryvnia` (123 456,79 ₴ | UAH 123,456.79),
`IcelandKrona` (123.457 Kr | ISK 123,457),
`IndianRupee` (₹123,456.79 | INR 123,456.79),
`IranianRial` (۱۲۳٬۴۵۶٫۷۹ ﷼ | IRR 123,456.79),
`IraqiDinar` (ع.د ١٢٣٬٤٥٦٫٧٨٩ | IQD 123,456.789),
`JamaicanDollar` ($123,456.79 | JMD 123,456.79),
`JordanianDinar` (د.ا ١٢٣٬٤٥٦٫٧٨٩ | JOD 123,456.789),
`KenyanShilling` (Ksh 123,456.79 | KES 123,456.79),
`Kina` (K 123,456.79 | PGK 123,456.79),
`Kip` (₭123.456,79 | LAK 123,456.79),
`KonvertibilnaMarka` (123,456.79 КМ | BAM 123,456.79),
`KuwaitiDinar` (د.ك ١٢٣٬٤٥٦٫٧٨٩ | KWD 123,456.789),
`Kwacha` (MK 123,456.79 | MWK 123,456.79),
`Kwanza` (123 456,79 Kz | AOA 123,456.79),
`Kyat` (၁၂၃,၄၅၆.၇၉ K | MMK 123,456.79),
`Lari` (123 456,79 ლ | GEL 123,456.79),
`LebanesePound` (ل.ل ١٢٣٬٤٥٧ | LBP 123,457),
`Lek` (123 456,79 L | ALL 123,456.79),
`Lempira` (L 123,456.79 | HNL 123,456.79),
`Leone` (Le 123,456.79 | SLL 123,456.79),
`Leu` (123.456,79 L | RON 123,456.79),
`LiberianDollar` ($123,456.79 | LRD 123,456.79),
`LibyanDinar` (ل.د 123.456,789 | LYD 123,456.789),
`Lilangeni` (L 123,456.79 | SZL 123,456.79),
`Loti` (L 123,456.79 | LSL 123,456.79),
`MalagasyAriary` (123 457 Ar | MGA 123,457),
`MalaysianRinggit` (RM 123,456.79 | MYR 123,456.79),
`Manat` (123 456,79 m | TMT 123,456.79),
`MauritiusRupee` (₨ 123,456.79 | MUR 123,456.79),
`Metical` (123.457 MTn | MZN 123,457),
`MexicanPeso` ($123,456.79 | MXN 123,456.79),
`MoldovanLeu` (123.456,79 L | MDL 123,456.79),
`MoroccanDirham` (١٢٣٬٤٥٦٫٧٩ د.م. | MAD 123,456.79),
`Naira` (₦123,456.79 | NGN 123,456.79),
`Nakfa` (Nfk 123,456.79 | ERN 123,456.79),
`NamibiaDollar` ($123,456.79 | NAD 123,456.79),
`NepaleseRupee` (नेरू १२३,४५६.७९ | NPR 123,456.79),
`NewIsraeliShekel` (123,456.79 ₪ | ILS 123,456.79),
`NewZealandDollar` ($123,456.79 | NZD 123,456.79),
`Ngultrum` (Nu. ༡༢༣,༤༥༦.༧༩ | BTN 123,456.79),
`NorthKoreanWon` (₩ 123,456.79 | KPW 123,456.79),
`NorwegianKrone` (kr 123 456,79 | NOK 123,456.79),
`NuevoSol` (S/. 123,456.79 | PEN 123,456.79),
`Ouguiya` (١٢٣٬٤٥٦٫٧٩ أ.م | MRU 123,456.79),
`PZloty` (123 456,79 zł | PLN 123,456.79),
`Paanga` (T$ 123,456.79 | TOP 123,456.79),
`PakistanRupee` (₨ 123,456.79 | PKR 123,456.79),
`Pataca` (P 123,456.79 | MOP 123,456.79),
`PesoUruguayo` ($ 123.456,79 | UYU 123,456.79),
`PhilippinePeso` (₱123,456.79 | PHP 123,456.79),
`PoundSterling` (£123,456.79 | GBP 123,456.79),
`Pula` (P 123,456.79 | BWP 123,456.79),
`QatariRial` (١٢٣٬٤٥٦٫٧٩ ر.ق | QAR 123,456.79),
`Quetzal` (Q 123,456.79 | GTQ 123,456.79),
`RandLS` (R 123,456.79 | ZAR 123,456.79),
`RandNA` (R 123 456.79 | ZAR 123,456.79),
`RandZA` (R 123 456.79 | ZAR 123,456.79),
`RialOmani` (١٢٣٬٤٥٦٫٧٨٩ ر.ع. | OMR 123,456.789),
`Riel` (123.456,79៛ | KHR 123,456.79),
`Rufiyaa` (ރ. 123,456.79 | MVR 123,456.79),
`Rupiah` (Rp 123.456,79 | IDR 123,456.79),
`RussianRuble` (123 456,79 ₽ | RUB 123,456.79),
`RwandaFranc` (₣ 123.457 | RWF 123,457),
`SaintHelenaPound` (£123,456.79 | SHP 123,456.79),
`SaudiRiyal` (١٢٣٬٤٥٦٫٧٩ ر.س | SAR 123,456.79),
`SerbianDinarSR` (123 456,79 дин | RSD 123,456.79),
`SerbianDinarXK` (123.456,79 дин | RSD 123,456.79),
`SeychellesRupee` (₨ 123,456.79 | SCR 123,456.79),
`SingaporeDollar` ($123,456.79 | SGD 123,456.79),
`SolomonIslandsDollar` ($123,456.79 | SBD 123,456.79),
`Som` (123 456,79 Лв | KGS 123,456.79),
`SomaliShilling` (Sh 123,456.79 | SOS 123,456.79),
`Somoni` (ЅМ 123,456.79 | TJS 123,456.79),
`SouthKoreanWon` (₩123,457 | KRW 123,457),
`SriLankaRupee` (රු. 123,456.79 | LKR 123,456.79),
`SudanesePound` (١٢٣٬٤٥٦٫٧٩ ج.س | SDG 123,456.79),
`SurinameDollar` ($ 123.456,79 | SRD 123,456.79),
`SwedishKrona` (123 456,79 kr | SEK 123,456.79),
`SwissFranc` (₣ 123'456.79 | CHF 123,456.79),
`SyrianPound` (١٢٣٬٤٥٦٫٧٩ ل.س | SYP 123,456.79),
`TaiwanDollar` ($123,456.79 | TWD 123,456.79),
`Taka` (১২৩,৪৫৬.৭৯৳ | BDT 123,456.79),
`Tala` (T 123,456.79 | WST 123,456.79),
`TanzanianShilling` (TSh 123,456.79 | TZS 123,456.79),
`Tenge` (123 456,79 〒 | KZT 123,456.79),
`TrinidadandTobagoDollar` ($123,456.79 | TTD 123,456.79),
`Tugrik` (₮ 123,456.79 | MNT 123,456.79),
`TunisianDinar` (د.ت 123.456,789 | TND 123,456.789),
`TurkishLira` (₤123.456,79 | TRY 123,456.79),
`UAEDirham` (١٢٣٬٤٥٦٫٧٩ د.إ | AED 123,456.79),
`USDollar` ($123,456.79 | USD 123,456.79),
`UgandaShilling` (USh 123,457 | UGX 123,457),
`UzbekistanSum` (123 456,79 сўм | UZS 123,456.79),
`Vatu` (Vt 123,457 | VUV 123,457),
`YemeniRial` (١٢٣٬٤٥٦٫٧٩ ﷼ | YER 123,456.79),
`Yen` (¥123,457 | JPY 123,457),
`Yuan` (¥123,456.79 | CNY 123,456.79),
`ZambianKwacha` (ZK 123,456.79 | ZMW 123,456.79),
`ZimbabweDollar` ($ 123,456.79 | ZWL 123,456.79)

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
