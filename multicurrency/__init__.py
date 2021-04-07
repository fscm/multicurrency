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

`multicurrency.afghani.Afghani` (Af1.000,00),
`multicurrency.dinar.AlgerianDinar` (د.ج1.000,00),
`multicurrency.peso.ArgentinePeso` ($1.000,00),
`multicurrency.dram.ArmenianDram` (Դ1,000.00),
`multicurrency.florin.ArubanFlorin` (ƒ1,000.00),
`multicurrency.dollar.AustralianDollar` ($1,000.00),
`multicurrency.manat.AzerbaijanianManat` (ман1.000,00),
`multicurrency.dollar.BahamianDollar` ($1,000.00),
`multicurrency.dinar.BahrainiDinar` (ب.د1,000.000),
`multicurrency.baht.Baht` (฿1,000.00),
`multicurrency.balboa.Balboa` (B/.1.000,00),
`multicurrency.dollar.BarbadosDollar` ($1.000,00),
`multicurrency.ruble.BelarusianRuble` (Br1.000,00),
`multicurrency.dollar.BelizeDollar` ($1,000.00),
`multicurrency.dollar.BermudianDollar` ($1,000.00),
`multicurrency.fuerte.BolivarFuerte` (Bs F1.000,00),
`multicurrency.boliviano.Boliviano` (Bs.1,000.00),
`multicurrency.real.BrazilianReal` (R$1.000,00),
`multicurrency.dollar.BruneiDollar` ($1,000.00),
`multicurrency.lev.BulgarianLev` (лв1.000,00),
`multicurrency.franc.BurundiFranc` (₣1.000),
`multicurrency.franc.CFAFrancBCEAO` (₣1.000),
`multicurrency.franc.CFAFrancBEAC` (₣1.000),
`multicurrency.franc.CFPFranc` (₣1.000),
`multicurrency.dollar.CanadianDollarEN` ($1,000.00),
`multicurrency.dollar.CanadianDollarFR` ($1.000,00),
`multicurrency.escudo.CapeVerdeEscudo` ($1.000,00),
`multicurrency.dollar.CaymanIslandsDollar` ($1,000.00),
`multicurrency.cedi.Cedi` (₵1.000,00),
`multicurrency.peso.ChileanPeso` ($1.000),
`multicurrency.peso.ColombianPeso` ($1.000,00),
`multicurrency.franc.CongoleseFranc` (₣1.000,00),
`multicurrency.oro.CordobaOro` (C$1.000,00),
`multicurrency.colon.CostaRicanColon` (₡1.000,00),
`multicurrency.kuna.CroatianKuna` (Kn1.000,00),
`multicurrency.peso.CubanPeso` ($1,000.00),
`multicurrency.koruna.CzechKoruna` (Kč1.000,00),
`multicurrency.dalasi.Dalasi` (D1.000,00),
`multicurrency.krone.DanishKrone` (kr1.000,00),
`multicurrency.denar.Denar` (ден1,000.00),
`multicurrency.franc.DjiboutiFranc` (₣1.000),
`multicurrency.dobra.Dobra` (Db1.000,00),
`multicurrency.peso.DominicanPeso` ($1,000.00),
`multicurrency.dong.Dong` (₫1.000),
`multicurrency.dollar.EastCaribbeanDollar` ($1,000.00),
`multicurrency.pound.EgyptianPound` (£1,000.00),
`multicurrency.birr.EthiopianBirr` (1.000,00),
`multicurrency.euro.Euro` (€1.000,00),
`multicurrency.pound.FalklandIslandsPound` (£1.000,00),
`multicurrency.dollar.FijiDollar` ($1.000,00),
`multicurrency.forint.Forint` (Ft1.000),
`multicurrency.pound.GibraltarPound` (£1.000,00),
`multicurrency.gourde.Gourde` (G1.000,00),
`multicurrency.guarani.Guarani` (₲1.000),
`multicurrency.franc.GuineaFranc` (₣1.000),
`multicurrency.dollar.GuyanaDollar` ($1.000,00),
`multicurrency.dollar.HongKongDollar` ($1,000.00),
`multicurrency.hryvnia.Hryvnia` (₴1.000,00),
`multicurrency.krona.IcelandKrona` (Kr1.000),
`multicurrency.rupee.IndianRupee` (₹1,000.00),
`multicurrency.rial.IranianRial` (﷼1,000.00),
`multicurrency.dinar.IraqiDinar` (ع.د1.000,000),
`multicurrency.dollar.JamaicanDollar` ($1,000.00),
`multicurrency.dinar.JordanianDinar` (د.ا1,000.000),
`multicurrency.shilling.KenyanShilling` (Sh1,000.00),
`multicurrency.kina.Kina` (K1.000,00),
`multicurrency.kip.Kip` (₭1.000,00),
`multicurrency.marka.KonvertibilnaMarka` (КМ1,000.00),
`multicurrency.dinar.KuwaitiDinar` (د.ك1,000.000),
`multicurrency.kwacha.Kwacha` (MK1.000,00),
`multicurrency.kwanza.Kwanza` (Kz1.000,00),
`multicurrency.kyat.Kyat` (K1.000,00),
`multicurrency.lari.Lari` (ლ1.000,00),
`multicurrency.pound.LebanesePound` (ل.ل1 000),
`multicurrency.lek.Lek` (L1.000,00),
`multicurrency.lempira.Lempira` (L1,000.00),
`multicurrency.leone.Leone` (Le1.000,00),
`multicurrency.leu.Leu` (L1.000,00),
`multicurrency.dollar.LiberianDollar` ($1.000,00),
`multicurrency.dinar.LibyanDinar` (ل.د1.000,000),
`multicurrency.lilangeni.Lilangeni` (L1,000.00),
`multicurrency.loti.Loti` (L1.000,00),
`multicurrency.ariary.MalagasyAriary` (1.000),
`multicurrency.ringgit.MalaysianRinggit` (RM1,000.00),
`multicurrency.manat.Manat` (m1.000,00),
`multicurrency.rupee.MauritiusRupee` (₨1,000.00),
`multicurrency.metical.Metical` (MTn1.000),
`multicurrency.peso.MexicanPeso` ($1,000.00),
`multicurrency.leu.MoldovanLeu` (L1.000,00),
`multicurrency.dirham.MoroccanDirham` (د.م.1.000,00),
`multicurrency.naira.Naira` (₦1.000,00),
`multicurrency.nakfa.Nakfa` (Nfk1.000,00),
`multicurrency.dollar.NamibiaDollar` ($1.000,00),
`multicurrency.rupee.NepaleseRupee` (₨1,000.00),
`multicurrency.shekel.NewIsraeliShekel` (₪1,000.00),
`multicurrency.dollar.NewZealandDollar` ($1,000.00),
`multicurrency.ngultrum.Ngultrum` (1.000,00),
`multicurrency.won.NorthKoreanWon` (₩1.000,00),
`multicurrency.krone.NorwegianKrone` (kr1.000,00),
`multicurrency.nuevo_sol.NuevoSol` (S/.1,000.00),
`multicurrency.ouguiya.Ouguiya` (UM1.000,00),
`multicurrency.pzloty.PZloty` (zł1.000,00),
`multicurrency.paanga.Paanga` (T$1,000.00),
`multicurrency.rupee.PakistanRupee` (₨1,000.00),
`multicurrency.pataca.Pataca` (P1.000,00),
`multicurrency.peso.PesoUruguayo` ($1.000,00),
`multicurrency.peso.PhilippinePeso` (₱1,000.00),
`multicurrency.pound.PoundSterling` (£1,000.00),
`multicurrency.pula.Pula` (P1.000,00),
`multicurrency.rial.QatariRial` (ر.ق1.000,00),
`multicurrency.quetzal.Quetzal` (Q1.000,00),
`multicurrency.rand.Rand` (R1 000.00),
`multicurrency.rial.RialOmani` (ر.ع.1,000.000),
`multicurrency.riel.Riel` (៛1.000,00),
`multicurrency.rufiyaa.Rufiyaa` (ރ.1.000,00),
`multicurrency.rupiah.Rupiah` (Rp1.000,00),
`multicurrency.ruble.RussianRuble` (р.1.000,00),
`multicurrency.franc.RwandaFranc` (₣1.000),
`multicurrency.pound.SaintHelenaPound` (£1.000,00),
`multicurrency.riyal.SaudiRiyal` (ر.س1,000.00),
`multicurrency.dinar.SerbianDinar` (din1.000,00),
`multicurrency.rupee.SeychellesRupee` (₨1.000,00),
`multicurrency.dollar.SingaporeDollar` ($1,000.00),
`multicurrency.dollar.SolomonIslandsDollar` ($1.000,00),
`multicurrency.som.Som` (1.000,00),
`multicurrency.shilling.SomaliShilling` (Sh1.000,00),
`multicurrency.somoni.Somoni` (ЅМ1.000,00),
`multicurrency.won.SouthKoreanWon` (₩1,000),
`multicurrency.rupee.SriLankaRupee` (Rs1.000,00),
`multicurrency.pound.SudanesePound` (£1.000,00),
`multicurrency.dollar.SurinameDollar` ($1.000,00),
`multicurrency.krona.SwedishKrona` (kr1.000,00),
`multicurrency.franc.SwissFranc` (₣1'000.00),
`multicurrency.pound.SyrianPound` (ل.س1.000,00),
`multicurrency.dollar.TaiwanDollar` ($1.000,00),
`multicurrency.taka.Taka` (৳1,000.00),
`multicurrency.tala.Tala` (T1.000,00),
`multicurrency.shilling.TanzanianShilling` (Sh1,000.00),
`multicurrency.tenge.Tenge` (〒1.000,00),
`multicurrency.dollar.TrinidadandTobagoDollar` ($1.000,00),
`multicurrency.tugrik.Tugrik` (₮1.000,00),
`multicurrency.dinar.TunisianDinar` (د.ت1.000,000),
`multicurrency.lira.TurkishLira` (₤1,000.00),
`multicurrency.dirham.UAEDirham` (د.إ1,000.00),
`multicurrency.dollar.USDollar` ($1,000.00),
`multicurrency.shilling.UgandaShilling` (Sh1.000),
`multicurrency.sum.UzbekistanSum` (1.000,00),
`multicurrency.vatu.Vatu` (Vt1,000),
`multicurrency.rial.YemeniRial` (﷼1.000,00),
`multicurrency.yen.Yen` (¥1,000),
`multicurrency.yuan.Yuan` (¥1,000.00),
`multicurrency.kwacha.ZambianKwacha` (ZK1.000,00),
`multicurrency.dollar.ZimbabweDollar` ($1.000,00)

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
    ...     currency='XBT',
    ...     symbol='Ƀ',
    ...     code='0',
    ...     decimal_places=8,
    ...     decimal_sign='.',
    ...     grouping_sign=',')
    >>> print(bitcoin)
    Ƀ1,000.00000000

To help working with unsupported currencies the settings can be defined
in a dictionary and used when needed:

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

        >>> euro = abs(Euro(-2))
        >>> print(euro)
        €2,00

* Addiction

    Addiction is supported only between currencies of the same type.

        >>> euro1 = Euro(2.5)
        >>> euro2 = Euro(3)
        >>> print(euro1 + euro2)
        €5,50

* Boolean

    Produces 'True' for values of currency other than zero. 'False'
    otherwise.

        >>> bool(Euro(0))
        False
        >>> bool(Euro(1))
        True

* Ceiling

    Produces a new currency rounded up to the nearest integer.

        >>> from math import ceil
        >>> print(ceil(Euro(1/7)))
        €1,00

* Copy

    Produces a copy of itself.

        >>> from copy import copy
        >>> euro = copy(Euro(1/7))
        >>> print(euro)
        €0,14

* Division

    Produces a new currency with the value of the division of the
    currency by either an `int`, `float`, or `decimal.Decimal`.

        >>> euro = Euro(7) / 2
        >>> print(euro)
        €3,50

* Divmod

    Produces a tuple consisting of the currencies with the quotient and
    the remainder of the division of the currency by either an `int`,
    `float`, or `decimal.Decimal`.

        >>> q, r = divmod(Euro(7), 2)
        >>> print(q, r)
        €3,00 €1,00

* Float
    Produces a `float` with the value of the currency amount.

        >>> float(Euro(1/7))
        0.14285714285714285

* Flooring

    Produces a new currency rounded down to the nearest integer.

        >>> from math import floor
        >>> print(floor(Euro(7/2)))
        €3,00

* Floordiv

    Produces a new currency with the integral part of the quotient of
    the division of the currency by either an `int`, `float`, or
    `decimal.Decimal`.

        >>> q = Euro(7) // 2
        >>> print(q)
        €3,00

* Hash

    Produces a hash representation of the `multicurrency.currency.Currency`.

        >>> hash(Euro(7))
        1166476495300974230

* Int
    Produces an `int` with the value of the currency amount.

        >>> int(Euro(7/2))
        3

* Mod

    Produces a new currency with the value of the remainder of the
    division of the currency by either an `int`, `float`, or
    `decimal.Decimal`.

        >>> r = Euro(7) % 2
        >>> print(r)
        €1,00

* Multiplication

    Multiplication is supported only between a currency and an `int`,
    `float`, or `decimal.Decimal`.

        >>> print(Euro(2) * 2.5)
        €5,00

* Round

    Produces a new currency with the amount of the currency rounded to
    a given precision.

        >>> r = round(Euro(1/7), 3)
        >>> print(r.amount)
        0.143

* Subtraction

    Subtraction is supported only between currencies of the same type.

        >>> euro1 = Euro(2)
        >>> euro2 = Euro(3)
        >>> print(euro1 - euro2)
        €-1,00

* Other Operations

    This library also supports the basic comparison operations between
    two objects of the same currency.

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
    SerbianDinar,
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
from .euro import Euro
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
from .rand import Rand
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
    'Rand',
    'RialOmani',
    'Riel',
    'Rufiyaa',
    'Rupiah',
    'RussianRuble',
    'RwandaFranc',
    'SaintHelenaPound',
    'SaudiRiyal',
    'SerbianDinar',
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
__author_email__: Final[str] = 'fscm@users.noreply.github.com'
__license__: Final[str] = 'MIT'
__project__: Final[str] = __package__
__version__: Final[str] = '0.2.0'
