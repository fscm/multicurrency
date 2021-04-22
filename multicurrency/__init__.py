# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Currency system.

The multicurrency module provides support for currency operations. It
supports several different currencies.

.. caution::
    This module is still in Beta[^beta]. Do not use it in production
    ready applications.

    [^beta]:
        An early version of a program or application that contains most
        of the major features, but is not yet complete. Sometimes these
        versions are released to the general public, for testing and
        feedback.

    Currency format (representation) is not yet implemented. Supported
    operations are described in the `multicurrency.currency` module.


The currencies supported by this module were created with information
(alphabetic code, numeric code, and minor unit size) from ISO-4217.

## Supported Currencies

List of supported currencies (and default format):

* `multicurrency.afghani.Afghani` (؋ ۱۲۳٬۴۵۶٫۷۹ | AFN 123,456.79),
* `multicurrency.dinar.AlgerianDinar` (123.456,79 د.ج | DZD 123,456.79),
* `multicurrency.peso.ArgentinePeso` ($ 123.456,79 | ARS 123,456.79),
* `multicurrency.dram.ArmenianDram` (123 456,79 Դ | AMD 123,456.79),
* `multicurrency.florin.ArubanFlorin` (ƒ123,456.79 | AWG 123,456.79),
* `multicurrency.dollar.AustralianDollar` ($123,456.79 | AUD 123,456.79),
* `multicurrency.manat.AzerbaijanianManat` (123.456,79 ₼ | AZN 123,456.79),
* `multicurrency.dollar.BahamianDollar` ($123,456.79 | BSD 123,456.79),
* `multicurrency.dinar.BahrainiDinar` (١٢٣٬٤٥٦٫٧٨٩ ب.د | BHD 123,456.789),
* `multicurrency.baht.Baht` (฿123,456.79 | THB 123,456.79),
* `multicurrency.balboa.Balboa` (B/. 123,456.79 | PAB 123,456.79),
* `multicurrency.dollar.BarbadosDollar` ($123,456.79 | BBD 123,456.79),
* `multicurrency.ruble.BelarusianRuble` (123 456,79 Br | BYN 123,456.79),
* `multicurrency.dollar.BelizeDollar` ($123,456.79 | BZD 123,456.79),
* `multicurrency.dollar.BermudianDollar` ($123,456.79 | BMD 123,456.79),
* `multicurrency.fuerte.BolivarFuerte` (Bs.F 123.456,79 | VEF 123,456.79),
* `multicurrency.boliviano.Boliviano` (Bs. 123.456,79 | BOB 123,456.79),
* `multicurrency.real.BrazilianReal` (R$ 123.456,79 | BRL 123,456.79),
* `multicurrency.dollar.BruneiDollar` ($ 123.456,79 | BND 123,456.79),
* `multicurrency.lev.BulgarianLev` (123456,79 лв | BGN 123,456.79),
* `multicurrency.franc.BurundiFranc` (123 457 ₣ | BIF 123,457),
* `multicurrency.franc.CFAFrancBCEAO` (123 457 ₣ | XOF 123,457),
* `multicurrency.franc.CFAFrancBEAC` (123 457 ₣ | XAF 123,457),
* `multicurrency.franc.CFPFranc` (123 457 ₣ | XPF 123,457),
* `multicurrency.dollar.CanadianDollarEN` ($123,456.79 | CAD 123,456.79),
* `multicurrency.dollar.CanadianDollarFR` (123 456,79 $ | CAD 123,456.79),
* `multicurrency.escudo.CapeVerdeEscudo` (123 456$79 | CVE 123,456.79),
* `multicurrency.dollar.CaymanIslandsDollar` ($123,456.79 | KYD 123,456.79),
* `multicurrency.cedi.Cedi` (₵123,456.79 | GHS 123,456.79),
* `multicurrency.peso.ChileanPeso` ($123.457 | CLP 123,457),
* `multicurrency.peso.ColombianPeso` ($ 123.456,79 | COP 123,456.79),
* `multicurrency.franc.CongoleseFranc` (123 456,79 ₣ | CDF 123,456.79),
* `multicurrency.oro.CordobaOro` (C$123,456.79 | NIO 123,456.79),
* `multicurrency.colon.CostaRicanColon` (₡123 456,79 | CRC 123,456.79),
* `multicurrency.kuna.CroatianKuna` (123.456,79 Kn | HRK 123,456.79),
* `multicurrency.peso.CubanPeso` ($123,456.79 | CUP 123,456.79),
* `multicurrency.koruna.CzechKoruna` (123 456,79 Kč | CZK 123,456.79),
* `multicurrency.dalasi.Dalasi` (D 123,456.79 | GMD 123,456.79),
* `multicurrency.krone.DanishKrone` (123.456,79 kr | DKK 123,456.79),
* `multicurrency.denar.Denar` (123.456,79 ден. | MKD 123,456.79),
* `multicurrency.franc.DjiboutiFranc` (123 457 ₣ | DJF 123,457),
* `multicurrency.dobra.Dobra` (123.456,79 Db | STN 123,456.79),
* `multicurrency.peso.DominicanPeso` ($123,456.79 | DOP 123,456.79),
* `multicurrency.dong.Dong` (123.457 ₫ | VND 123,457),
* `multicurrency.dollar.EastCaribbeanDollar` ($123,456.79 | XCD 123,456.79),
* `multicurrency.pound.EgyptianPound` (ج.م ١٢٣٬٤٥٦٫٧٩ | EGP 123,456.79),
* `multicurrency.birr.EthiopianBirr` (ብር 123,456.79 | ETB 123,456.79),
* `multicurrency.euro.Euro` (123.456,79 € | EUR 123,456.79),
* `multicurrency.euro.EuroAD` (123.456,79 € | EUR 123,456.79),
* `multicurrency.euro.EuroAT` (€ 123.456,79 | EUR 123,456.79),
* `multicurrency.euro.EuroBE` (€ 123.456,79 | EUR 123,456.79),
* `multicurrency.euro.EuroCY` (123.456,79 € | EUR 123,456.79),
* `multicurrency.euro.EuroDE` (123.456,79 € | EUR 123,456.79),
* `multicurrency.euro.EuroEE` (123 456,79 € | EUR 123,456.79),
* `multicurrency.euro.EuroES` (123.456,79 € | EUR 123,456.79),
* `multicurrency.euro.EuroFI` (123 456,79 € | EUR 123,456.79),
* `multicurrency.euro.EuroFR` (123 456,79 € | EUR 123,456.79),
* `multicurrency.euro.EuroGR` (123.456,79 € | EUR 123,456.79),
* `multicurrency.euro.EuroIE` (€123,456.79 | EUR 123,456.79),
* `multicurrency.euro.EuroIT` (123.456,79 € | EUR 123,456.79),
* `multicurrency.euro.EuroLT` (123 456,79 € | EUR 123,456.79),
* `multicurrency.euro.EuroLU` (123.456,79 € | EUR 123,456.79),
* `multicurrency.euro.EuroLV` (123 456,79 € | EUR 123,456.79),
* `multicurrency.euro.EuroMC` (123 456,79 € | EUR 123,456.79),
* `multicurrency.euro.EuroME` (123.456,79 € | EUR 123,456.79),
* `multicurrency.euro.EuroMT` (€123,456.79 | EUR 123,456.79),
* `multicurrency.euro.EuroNL` (€ 123.456,79 | EUR 123,456.79),
* `multicurrency.euro.EuroPT` (€ 123.456,79 | EUR 123,456.79),
* `multicurrency.euro.EuroSI` (123.456,79 € | EUR 123,456.79),
* `multicurrency.euro.EuroSK` (123 456,79 € | EUR 123,456.79),
* `multicurrency.euro.EuroSM` (123.456,79 € | EUR 123,456.79),
* `multicurrency.euro.EuroVA` (€123,456.79 | EUR 123,456.79),
* `multicurrency.euro.EuroXK` (123 456,79 € | EUR 123,456.79),
* `multicurrency.pound.FalklandIslandsPound` (£123,456.79 | FKP 123,456.79),
* `multicurrency.dollar.FijiDollar` ($123,456.79 | FJD 123,456.79),
* `multicurrency.forint.Forint` (123 457 Ft | HUF 123,457),
* `multicurrency.pound.GibraltarPound` (£123,456.79 | GIP 123,456.79),
* `multicurrency.gourde.Gourde` (G 123,456.79 | HTG 123,456.79),
* `multicurrency.guarani.Guarani` (₲ 123.457 | PYG 123,457),
* `multicurrency.franc.GuineaFranc` (123 457 ₣ | GNF 123,457),
* `multicurrency.dollar.GuyanaDollar` ($123,456.79 | GYD 123,456.79),
* `multicurrency.dollar.HongKongDollar` ($123,456.79 | HKD 123,456.79),
* `multicurrency.hryvnia.Hryvnia` (123 456,79 ₴ | UAH 123,456.79),
* `multicurrency.krona.IcelandKrona` (123.457 Kr | ISK 123,457),
* `multicurrency.rupee.IndianRupee` (₹123,456.79 | INR 123,456.79),
* `multicurrency.rial.IranianRial` (۱۲۳٬۴۵۶٫۷۹ ﷼ | IRR 123,456.79),
* `multicurrency.dinar.IraqiDinar` (ع.د ١٢٣٬٤٥٦٫٧٨٩ | IQD 123,456.789),
* `multicurrency.dollar.JamaicanDollar` ($123,456.79 | JMD 123,456.79),
* `multicurrency.dinar.JordanianDinar` (د.ا ١٢٣٬٤٥٦٫٧٨٩ | JOD 123,456.789),
* `multicurrency.shilling.KenyanShilling` (Ksh 123,456.79 | KES 123,456.79),
* `multicurrency.kina.Kina` (K 123,456.79 | PGK 123,456.79),
* `multicurrency.kip.Kip` (₭123.456,79 | LAK 123,456.79),
* `multicurrency.marka.KonvertibilnaMarka` (123,456.79 КМ | BAM 123,456.79),
* `multicurrency.dinar.KuwaitiDinar` (د.ك ١٢٣٬٤٥٦٫٧٨٩ | KWD 123,456.789),
* `multicurrency.kwacha.Kwacha` (MK 123,456.79 | MWK 123,456.79),
* `multicurrency.kwanza.Kwanza` (123 456,79 Kz | AOA 123,456.79),
* `multicurrency.kyat.Kyat` (၁၂၃,၄၅၆.၇၉ K | MMK 123,456.79),
* `multicurrency.lari.Lari` (123 456,79 ლ | GEL 123,456.79),
* `multicurrency.pound.LebanesePound` (ل.ل ١٢٣٬٤٥٧ | LBP 123,457),
* `multicurrency.lek.Lek` (123 456,79 L | ALL 123,456.79),
* `multicurrency.lempira.Lempira` (L 123,456.79 | HNL 123,456.79),
* `multicurrency.leone.Leone` (Le 123,456.79 | SLL 123,456.79),
* `multicurrency.leu.Leu` (123.456,79 L | RON 123,456.79),
* `multicurrency.dollar.LiberianDollar` ($123,456.79 | LRD 123,456.79),
* `multicurrency.dinar.LibyanDinar` (ل.د 123.456,789 | LYD 123,456.789),
* `multicurrency.lilangeni.Lilangeni` (L 123,456.79 | SZL 123,456.79),
* `multicurrency.loti.Loti` (L 123,456.79 | LSL 123,456.79),
* `multicurrency.ariary.MalagasyAriary` (123 457 Ar | MGA 123,457),
* `multicurrency.ringgit.MalaysianRinggit` (RM 123,456.79 | MYR 123,456.79),
* `multicurrency.manat.Manat` (123 456,79 m | TMT 123,456.79),
* `multicurrency.rupee.MauritiusRupee` (₨ 123,456.79 | MUR 123,456.79),
* `multicurrency.metical.Metical` (123.457 MTn | MZN 123,457),
* `multicurrency.peso.MexicanPeso` ($123,456.79 | MXN 123,456.79),
* `multicurrency.leu.MoldovanLeu` (123.456,79 L | MDL 123,456.79),
* `multicurrency.dirham.MoroccanDirham` (١٢٣٬٤٥٦٫٧٩ د.م. | MAD 123,456.79),
* `multicurrency.naira.Naira` (₦123,456.79 | NGN 123,456.79),
* `multicurrency.nakfa.Nakfa` (Nfk 123,456.79 | ERN 123,456.79),
* `multicurrency.dollar.NamibiaDollar` ($123,456.79 | NAD 123,456.79),
* `multicurrency.rupee.NepaleseRupee` (नेरू १२३,४५६.७९ | NPR 123,456.79),
* `multicurrency.shekel.NewIsraeliShekel` (123,456.79 ₪ | ILS 123,456.79),
* `multicurrency.dollar.NewZealandDollar` ($123,456.79 | NZD 123,456.79),
* `multicurrency.ngultrum.Ngultrum` (Nu. ༡༢༣,༤༥༦.༧༩ | BTN 123,456.79),
* `multicurrency.won.NorthKoreanWon` (₩ 123,456.79 | KPW 123,456.79),
* `multicurrency.krone.NorwegianKrone` (kr 123 456,79 | NOK 123,456.79),
* `multicurrency.nuevo_sol.NuevoSol` (S/. 123,456.79 | PEN 123,456.79),
* `multicurrency.ouguiya.Ouguiya` (١٢٣٬٤٥٦٫٧٩ أ.م | MRU 123,456.79),
* `multicurrency.pzloty.PZloty` (123 456,79 zł | PLN 123,456.79),
* `multicurrency.paanga.Paanga` (T$ 123,456.79 | TOP 123,456.79),
* `multicurrency.rupee.PakistanRupee` (₨ 123,456.79 | PKR 123,456.79),
* `multicurrency.pataca.Pataca` (P 123,456.79 | MOP 123,456.79),
* `multicurrency.peso.PesoUruguayo` ($ 123.456,79 | UYU 123,456.79),
* `multicurrency.peso.PhilippinePeso` (₱123,456.79 | PHP 123,456.79),
* `multicurrency.pound.PoundSterling` (£123,456.79 | GBP 123,456.79),
* `multicurrency.pula.Pula` (P 123,456.79 | BWP 123,456.79),
* `multicurrency.rial.QatariRial` (١٢٣٬٤٥٦٫٧٩ ر.ق | QAR 123,456.79),
* `multicurrency.quetzal.Quetzal` (Q 123,456.79 | GTQ 123,456.79),
* `multicurrency.rand.RandLS` (R 123,456.79 | ZAR 123,456.79),
* `multicurrency.rand.RandNA` (R 123 456.79 | ZAR 123,456.79),
* `multicurrency.rand.RandZA` (R 123 456.79 | ZAR 123,456.79),
* `multicurrency.rial.RialOmani` (١٢٣٬٤٥٦٫٧٨٩ ر.ع. | OMR 123,456.789),
* `multicurrency.riel.Riel` (123.456,79៛ | KHR 123,456.79),
* `multicurrency.rufiyaa.Rufiyaa` (ރ. 123,456.79 | MVR 123,456.79),
* `multicurrency.rupiah.Rupiah` (Rp 123.456,79 | IDR 123,456.79),
* `multicurrency.ruble.RussianRuble` (123 456,79 ₽ | RUB 123,456.79),
* `multicurrency.franc.RwandaFranc` (₣ 123.457 | RWF 123,457),
* `multicurrency.pound.SaintHelenaPound` (£123,456.79 | SHP 123,456.79),
* `multicurrency.riyal.SaudiRiyal` (١٢٣٬٤٥٦٫٧٩ ر.س | SAR 123,456.79),
* `multicurrency.dinar.SerbianDinarSR` (123 456,79 дин | RSD 123,456.79),
* `multicurrency.dinar.SerbianDinarXK` (123.456,79 дин | RSD 123,456.79),
* `multicurrency.rupee.SeychellesRupee` (₨ 123,456.79 | SCR 123,456.79),
* `multicurrency.dollar.SingaporeDollar` ($123,456.79 | SGD 123,456.79),
* `multicurrency.dollar.SolomonIslandsDollar` ($123,456.79 | SBD 123,456.79),
* `multicurrency.som.Som` (123 456,79 Лв | KGS 123,456.79),
* `multicurrency.shilling.SomaliShilling` (Sh 123,456.79 | SOS 123,456.79),
* `multicurrency.somoni.Somoni` (ЅМ 123,456.79 | TJS 123,456.79),
* `multicurrency.won.SouthKoreanWon` (₩123,457 | KRW 123,457),
* `multicurrency.rupee.SriLankaRupee` (රු. 123,456.79 | LKR 123,456.79),
* `multicurrency.pound.SudanesePound` (١٢٣٬٤٥٦٫٧٩ ج.س | SDG 123,456.79),
* `multicurrency.dollar.SurinameDollar` ($ 123.456,79 | SRD 123,456.79),
* `multicurrency.krona.SwedishKrona` (123 456,79 kr | SEK 123,456.79),
* `multicurrency.franc.SwissFranc` (₣ 123'456.79 | CHF 123,456.79),
* `multicurrency.pound.SyrianPound` (١٢٣٬٤٥٦٫٧٩ ل.س | SYP 123,456.79),
* `multicurrency.dollar.TaiwanDollar` ($123,456.79 | TWD 123,456.79),
* `multicurrency.taka.Taka` (১২৩,৪৫৬.৭৯৳ | BDT 123,456.79),
* `multicurrency.tala.Tala` (T 123,456.79 | WST 123,456.79),
* `multicurrency.shilling.TanzanianShilling` (TSh 123,456.79 | TZS 123,456.79),
* `multicurrency.tenge.Tenge` (123 456,79 〒 | KZT 123,456.79),
* `multicurrency.dollar.TrinidadandTobagoDollar` ($123,456.79 | TTD 123,456.79),
* `multicurrency.tugrik.Tugrik` (₮ 123,456.79 | MNT 123,456.79),
* `multicurrency.dinar.TunisianDinar` (د.ت 123.456,789 | TND 123,456.789),
* `multicurrency.lira.TurkishLira` (₤123.456,79 | TRY 123,456.79),
* `multicurrency.dirham.UAEDirham` (١٢٣٬٤٥٦٫٧٩ د.إ | AED 123,456.79),
* `multicurrency.dollar.USDollar` ($123,456.79 | USD 123,456.79),
* `multicurrency.shilling.UgandaShilling` (USh 123,457 | UGX 123,457),
* `multicurrency.sum.UzbekistanSum` (123 456,79 сўм | UZS 123,456.79),
* `multicurrency.vatu.Vatu` (Vt 123,457 | VUV 123,457),
* `multicurrency.rial.YemeniRial` (١٢٣٬٤٥٦٫٧٩ ﷼ | YER 123,456.79),
* `multicurrency.yen.Yen` (¥123,457 | JPY 123,457),
* `multicurrency.yuan.Yuan` (¥123,456.79 | CNY 123,456.79),
* `multicurrency.kwacha.ZambianKwacha` (ZK 123,456.79 | ZMW 123,456.79),
* `multicurrency.dollar.ZimbabweDollar` ($ 123,456.79 | ZWL 123,456.79)

## Usage

Simple usage example:

    >>> from multicurrency import Euro
    >>> euro = Euro(1000)
    >>> print(euro)
    €1.000,00
    >>> print(euro + Euro(0.50))
    €1.000,50

Unsupported currencies can be represented by creating a generic
`multicurrency.currency.Currency` object with the desired settings.

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

To help working with unsupported currencies the settings can be defined
in a dictionary and used when needed:

    >>> from multicurrency import Currency
    >>> settings = {
    ...     'currency':'XBT',
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

Currencies can also be represented with the ISO 4217 three-letter code
instead of the `symbol`.

    >>> from multicurrency import Euro
    >>> euro = Euro(1000, international=True)
    >>> print(euro)
    EUR 1.000,00

## Precision

The multicurrency library has a user alterable precision (defaulting to 28
places) which can be as large as needed for a given problem:

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

It also has a user alterable rounding method (defaulting to
ROUND_HALF_EVEN) which can be changed as needed:

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

Supported rounding methods are described on the
`multicurrency.currency.CurrencyContext` class.

## Operations

Several operations are supported by the several library classes.

* Absolute

    Produces the absolute value of a given currency.

        >>> from multicurrency import Euro
        >>> euro = abs(Euro(-2))
        >>> print(euro)
        €2,00

* Addiction

    Addiction is supported only between currencies of the same type.

        >>> from multicurrency import Euro
        >>> euro1 = Euro(2.5)
        >>> euro2 = Euro(3)
        >>> print(euro1 + euro2)
        €5,50

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
        €1,00

* Copy

    Produces a copy of itself.

        >>> from multicurrency import Euro
        >>> from copy import copy
        >>> euro = copy(Euro(1/7))
        >>> print(euro)
        €0,14

* Division

    Produces a new currency with the value of the division of the
    currency by either an `int`, `float`, or `decimal.Decimal`.

        >>> from multicurrency import Euro
        >>> euro = Euro(7) / 2
        >>> print(euro)
        €3,50

* Divmod

    Produces a tuple consisting of the currencies with the quotient and
    the remainder of the division of the currency by either an `int`,
    `float`, or `decimal.Decimal`.

        >>> from multicurrency import Euro
        >>> q, r = divmod(Euro(7), 2)
        >>> print(q, r)
        €3,00 €1,00

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
        €3,00

* Floordiv

    Produces a new currency with the integral part of the quotient of
    the division of the currency by either an `int`, `float`, or
    `decimal.Decimal`.

        >>> from multicurrency import Euro
        >>> q = Euro(7) // 2
        >>> print(q)
        €3,00

* Hash

    Produces a hash representation of the `multicurrency.currency.Currency`.

        >>> from multicurrency import Euro
        >>> hash(Euro(7))
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
        €1,00

* Multiplication

    Multiplication is supported only between a currency and an `int`,
    `float`, or `decimal.Decimal`.

        >>> from multicurrency import Euro
        >>> print(Euro(2) * 2.5)
        €5,00

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
        €-1,00

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

from typing import Final
from .currency import Currency, CurrencyContext
from .exceptions import (
    CurrencyException,
    CurrencyInvalidDivision,
    CurrencyInvalidMultiplication,
    CurrencyInvalidOperation,
    CurrencyMismatchException,
    CurrencyTypeException)
from .afghani import Afghani
from .ariary import MalagasyAriary
from .baht import Baht
from .balboa import Balboa
from .birr import EthiopianBirr
from .boliviano import Boliviano
from .cedi import Cedi
from .colon import CostaRicanColon
from .dalasi import Dalasi
from .denar import Denar
from .dinar import (
    BahrainiDinar,
    AlgerianDinar,
    IraqiDinar,
    JordanianDinar,
    KuwaitiDinar,
    LibyanDinar,
    SerbianDinarXK,
    SerbianDinarSR,
    TunisianDinar)
from .dirham import (
    UAEDirham,
    MoroccanDirham)
from .dobra import Dobra
from .dollar import (
    AustralianDollar,
    BarbadosDollar,
    BermudianDollar,
    BruneiDollar,
    BahamianDollar,
    BelizeDollar,
    CanadianDollarEN,
    CanadianDollarFR,
    FijiDollar,
    GuyanaDollar,
    HongKongDollar,
    JamaicanDollar,
    CaymanIslandsDollar,
    LiberianDollar,
    NamibiaDollar,
    NewZealandDollar,
    SolomonIslandsDollar,
    SingaporeDollar,
    SurinameDollar,
    TrinidadandTobagoDollar,
    TaiwanDollar,
    USDollar,
    EastCaribbeanDollar,
    ZimbabweDollar)
from .dong import Dong
from .dram import ArmenianDram
from .escudo import CapeVerdeEscudo
from .euro import (
    Euro,
    EuroAD,
    EuroAT,
    EuroBE,
    EuroCY,
    EuroEE,
    EuroFI,
    EuroFR,
    EuroDE,
    EuroGR,
    EuroIE,
    EuroIT,
    EuroXK,
    EuroLV,
    EuroLT,
    EuroLU,
    EuroMT,
    EuroMC,
    EuroME,
    EuroNL,
    EuroPT,
    EuroSM,
    EuroSK,
    EuroSI,
    EuroES,
    EuroVA)
from .florin import ArubanFlorin
from .forint import Forint
from .franc import (
    BurundiFranc,
    CongoleseFranc,
    SwissFranc,
    DjiboutiFranc,
    GuineaFranc,
    RwandaFranc,
    CFAFrancBCEAO,
    CFAFrancBEAC,
    CFPFranc)
from .fuerte import BolivarFuerte
from .gourde import Gourde
from .guarani import Guarani
from .hryvnia import Hryvnia
from .kina import Kina
from .kip import Kip
from .koruna import CzechKoruna
from .krona import (
    IcelandKrona,
    SwedishKrona)
from .krone import (
    DanishKrone,
    NorwegianKrone)
from .kuna import CroatianKuna
from .kwacha import (
    Kwacha,
    ZambianKwacha)
from .kwanza import Kwanza
from .kyat import Kyat
from .lari import Lari
from .lek import Lek
from .lempira import Lempira
from .leone import Leone
from .leu import (
    MoldovanLeu,
    Leu)
from .lev import BulgarianLev
from .lilangeni import Lilangeni
from .lira import TurkishLira
from .loti import Loti
from .manat import (
    AzerbaijanianManat,
    Manat)
from .marka import KonvertibilnaMarka
from .metical import Metical
from .naira import Naira
from .nakfa import Nakfa
from .ngultrum import Ngultrum
from .nuevo_sol import NuevoSol
from .oro import CordobaOro
from .ouguiya import Ouguiya
from .paanga import Paanga
from .pataca import Pataca
from .peso import (
    ArgentinePeso,
    ChileanPeso,
    ColombianPeso,
    CubanPeso,
    DominicanPeso,
    MexicanPeso,
    PhilippinePeso,
    PesoUruguayo)
from .pound import (
    EgyptianPound,
    FalklandIslandsPound,
    PoundSterling,
    GibraltarPound,
    LebanesePound,
    SudanesePound,
    SaintHelenaPound,
    SyrianPound)
from .pula import Pula
from .pzloty import PZloty
from .quetzal import Quetzal
from .rand import (
    RandLS,
    RandNA,
    RandZA)
from .real import BrazilianReal
from .rial import (
    IranianRial,
    RialOmani,
    QatariRial,
    YemeniRial)
from .riel import Riel
from .ringgit import MalaysianRinggit
from .riyal import SaudiRiyal
from .ruble import (
    BelarusianRuble,
    RussianRuble)
from .rufiyaa import Rufiyaa
from .rupee import (
    IndianRupee,
    SriLankaRupee,
    MauritiusRupee,
    NepaleseRupee,
    PakistanRupee,
    SeychellesRupee)
from .rupiah import Rupiah
from .shekel import NewIsraeliShekel
from .shilling import (
    KenyanShilling,
    SomaliShilling,
    TanzanianShilling,
    UgandaShilling)
from .som import Som
from .somoni import Somoni
from .sum import UzbekistanSum
from .taka import Taka
from .tala import Tala
from .tenge import Tenge
from .tugrik import Tugrik
from .vatu import Vatu
from .won import (
    NorthKoreanWon,
    SouthKoreanWon)
from .yen import Yen
from .yuan import Yuan


__all__ = [
    'Currency',
    'CurrencyContext',
    'CurrencyException',
    'CurrencyInvalidDivision',
    'CurrencyInvalidMultiplication',
    'CurrencyMismatchException',
    'CurrencyTypeException',
    'Afghani',
    'AlgerianDinar',
    'ArgentinePeso',
    'ArmenianDram',
    'ArubanFlorin',
    'AustralianDollar',
    'AzerbaijanianManat',
    'BahamianDollar',
    'BahrainiDinar',
    'Baht',
    'Balboa',
    'BarbadosDollar',
    'BelarusianRuble',
    'BelizeDollar',
    'BermudianDollar',
    'BolivarFuerte',
    'Boliviano',
    'BrazilianReal',
    'BruneiDollar',
    'BulgarianLev',
    'BurundiFranc',
    'CFAFrancBCEAO',
    'CFAFrancBEAC',
    'CFPFranc',
    'CanadianDollarEN',
    'CanadianDollarFR',
    'CapeVerdeEscudo',
    'CaymanIslandsDollar',
    'Cedi',
    'ChileanPeso',
    'ColombianPeso',
    'CongoleseFranc',
    'CordobaOro',
    'CostaRicanColon',
    'CroatianKuna',
    'CubanPeso',
    'CzechKoruna',
    'Dalasi',
    'DanishKrone',
    'Denar',
    'DjiboutiFranc',
    'Dobra',
    'DominicanPeso',
    'Dong',
    'EastCaribbeanDollar',
    'EgyptianPound',
    'EthiopianBirr',
    'Euro',
    'EuroAD',
    'EuroAT',
    'EuroBE',
    'EuroCY',
    'EuroDE',
    'EuroEE',
    'EuroES',
    'EuroFI',
    'EuroFR',
    'EuroGR',
    'EuroIE',
    'EuroIT',
    'EuroLT',
    'EuroLU',
    'EuroLV',
    'EuroMC',
    'EuroME',
    'EuroMT',
    'EuroNL',
    'EuroPT',
    'EuroSI',
    'EuroSK',
    'EuroSM',
    'EuroVA',
    'EuroXK',
    'FalklandIslandsPound',
    'FijiDollar',
    'Forint',
    'GibraltarPound',
    'Gourde',
    'Guarani',
    'GuineaFranc',
    'GuyanaDollar',
    'HongKongDollar',
    'Hryvnia',
    'IcelandKrona',
    'IndianRupee',
    'IranianRial',
    'IraqiDinar',
    'JamaicanDollar',
    'JordanianDinar',
    'KenyanShilling',
    'Kina',
    'Kip',
    'KonvertibilnaMarka',
    'KuwaitiDinar',
    'Kwacha',
    'Kwanza',
    'Kyat',
    'Lari',
    'LebanesePound',
    'Lek',
    'Lempira',
    'Leone',
    'Leu',
    'LiberianDollar',
    'LibyanDinar',
    'Lilangeni',
    'Loti',
    'MalagasyAriary',
    'MalaysianRinggit',
    'Manat',
    'MauritiusRupee',
    'Metical',
    'MexicanPeso',
    'MoldovanLeu',
    'MoroccanDirham',
    'Naira',
    'Nakfa',
    'NamibiaDollar',
    'NepaleseRupee',
    'NewIsraeliShekel',
    'NewZealandDollar',
    'Ngultrum',
    'NorthKoreanWon',
    'NorwegianKrone',
    'NuevoSol',
    'Ouguiya',
    'PZloty',
    'Paanga',
    'PakistanRupee',
    'Pataca',
    'PesoUruguayo',
    'PhilippinePeso',
    'PoundSterling',
    'Pula',
    'QatariRial',
    'Quetzal',
    'RandLS',
    'RandNA',
    'RandZA',
    'RialOmani',
    'Riel',
    'Rufiyaa',
    'Rupiah',
    'RussianRuble',
    'RwandaFranc',
    'SaintHelenaPound',
    'SaudiRiyal',
    'SerbianDinarSR',
    'SerbianDinarXK',
    'SeychellesRupee',
    'SingaporeDollar',
    'SolomonIslandsDollar',
    'Som',
    'SomaliShilling',
    'Somoni',
    'SouthKoreanWon',
    'SriLankaRupee',
    'SudanesePound',
    'SurinameDollar',
    'SwedishKrona',
    'SwissFranc',
    'SyrianPound',
    'TaiwanDollar',
    'Taka',
    'Tala',
    'TanzanianShilling',
    'Tenge',
    'TrinidadandTobagoDollar',
    'Tugrik',
    'TunisianDinar',
    'TurkishLira',
    'UAEDirham',
    'USDollar',
    'UgandaShilling',
    'UzbekistanSum',
    'Vatu',
    'YemeniRial',
    'Yen',
    'Yuan',
    'ZambianKwacha',
    'ZimbabweDollar']


__author__: Final[str] = 'Frederico Martins'
__license__: Final[str] = 'MIT'
__project__: Final[str] = __package__
__version__: Final[str] = '0.4.0'
