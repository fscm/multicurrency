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
`multicurrency.algerian_dinar.AlgerianDinar` (د.ج1.000,00),
`multicurrency.argentine_peso.ArgentinePeso` ($1.000,00),
`multicurrency.armenian_dram.ArmenianDram` (Դ1,000.00),
`multicurrency.aruban_florin.ArubanFlorin` (ƒ1,000.00),
`multicurrency.australian_dollar.AustralianDollar` ($1,000.00),
`multicurrency.azerbaijanian_manat.AzerbaijanianManat` (ман1.000,00),
`multicurrency.bahamian_dollar.BahamianDollar` ($1,000.00),
`multicurrency.bahraini_dinar.BahrainiDinar` (ب.د1,000.000),
`multicurrency.baht.Baht` (฿1,000.00),
`multicurrency.balboa.Balboa` (B/.1.000,00),
`multicurrency.barbados_dollar.BarbadosDollar` ($1.000,00),
`multicurrency.belarusian_ruble.BelarusianRuble` (Br1.000,00),
`multicurrency.belize_dollar.BelizeDollar` ($1,000.00),
`multicurrency.bermudian_dollar.BermudianDollar` ($1,000.00),
`multicurrency.bolivar_fuerte.BolivarFuerte` (Bs F1.000,00),
`multicurrency.boliviano.Boliviano` (Bs.1,000.00),
`multicurrency.brazilian_real.BrazilianReal` (R$1.000,00),
`multicurrency.brunei_dollar.BruneiDollar` ($1,000.00),
`multicurrency.bulgarian_lev.BulgarianLev` (лв1.000,00),
`multicurrency.burundi_franc.BurundiFranc` (₣1.000),
`multicurrency.cfa_franc_bceao.CFAFrancBCEAO` (₣1.000),
`multicurrency.cfa_franc_beac.CFAFrancBEAC` (₣1.000),
`multicurrency.cfp_franc.CFPFranc` (₣1.000),
`multicurrency.canadian_dollar_en.CanadianDollarEN` ($1,000.00),
`multicurrency.canadian_dollar_fr.CanadianDollarFR` ($1.000,00),
`multicurrency.cape_verde_escudo.CapeVerdeEscudo` ($1.000,00),
`multicurrency.cayman_islands_dollar.CaymanIslandsDollar` ($1,000.00),
`multicurrency.cedi.Cedi` (₵1.000,00),
`multicurrency.chilean_peso.ChileanPeso` ($1.000),
`multicurrency.colombian_peso.ColombianPeso` ($1.000,00),
`multicurrency.congolese_franc.CongoleseFranc` (₣1.000,00),
`multicurrency.cordoba_oro.CordobaOro` (C$1.000,00),
`multicurrency.costa_rican_colon.CostaRicanColon` (₡1.000,00),
`multicurrency.croatian_kuna.CroatianKuna` (Kn1.000,00),
`multicurrency.cuban_peso.CubanPeso` ($1,000.00),
`multicurrency.czech_koruna.CzechKoruna` (Kč1.000,00),
`multicurrency.dalasi.Dalasi` (D1.000,00),
`multicurrency.danish_krone.DanishKrone` (kr1.000,00),
`multicurrency.denar.Denar` (ден1,000.00),
`multicurrency.djibouti_franc.DjiboutiFranc` (₣1.000),
`multicurrency.dobra.Dobra` (Db1.000,00),
`multicurrency.dominican_peso.DominicanPeso` ($1,000.00),
`multicurrency.dong.Dong` (₫1.000),
`multicurrency.east_caribbean_dollar.EastCaribbeanDollar` ($1,000.00),
`multicurrency.egyptian_pound.EgyptianPound` (£1,000.00),
`multicurrency.ethiopian_birr.EthiopianBirr` (1.000,00),
`multicurrency.euro.Euro` (€1.000,00),
`multicurrency.falkland_islands_pound.FalklandIslandsPound` (£1.000,00),
`multicurrency.fiji_dollar.FijiDollar` ($1.000,00),
`multicurrency.forint.Forint` (Ft1.000),
`multicurrency.gibraltar_pound.GibraltarPound` (£1.000,00),
`multicurrency.gourde.Gourde` (G1.000,00),
`multicurrency.guarani.Guarani` (₲1.000),
`multicurrency.guinea_franc.GuineaFranc` (₣1.000),
`multicurrency.guyana_dollar.GuyanaDollar` ($1.000,00),
`multicurrency.hong_kong_dollar.HongKongDollar` ($1,000.00),
`multicurrency.hryvnia.Hryvnia` (₴1.000,00),
`multicurrency.iceland_krona.IcelandKrona` (Kr1.000),
`multicurrency.indian_rupee.IndianRupee` (₹1,000.00),
`multicurrency.iranian_rial.IranianRial` (﷼1,000.00),
`multicurrency.iraqi_dinar.IraqiDinar` (ع.د1.000,000),
`multicurrency.jamaican_dollar.JamaicanDollar` ($1,000.00),
`multicurrency.jordanian_dinar.JordanianDinar` (د.ا1,000.000),
`multicurrency.kenyan_shilling.KenyanShilling` (Sh1,000.00),
`multicurrency.kina.Kina` (K1.000,00),
`multicurrency.kip.Kip` (₭1.000,00),
`multicurrency.konvertibilna_marka.KonvertibilnaMarka` (КМ1,000.00),
`multicurrency.kuwaiti_dinar.KuwaitiDinar` (د.ك1,000.000),
`multicurrency.kwacha.Kwacha` (MK1.000,00),
`multicurrency.kwanza.Kwanza` (Kz1.000,00),
`multicurrency.kyat.Kyat` (K1.000,00),
`multicurrency.lari.Lari` (ლ1.000,00),
`multicurrency.lebanese_pound.LebanesePound` (ل.ل1 000),
`multicurrency.lek.Lek` (L1.000,00),
`multicurrency.lempira.Lempira` (L1,000.00),
`multicurrency.leone.Leone` (Le1.000,00),
`multicurrency.leu.Leu` (L1.000,00),
`multicurrency.liberian_dollar.LiberianDollar` ($1.000,00),
`multicurrency.libyan_dinar.LibyanDinar` (ل.د1.000,000),
`multicurrency.lilangeni.Lilangeni` (L1,000.00),
`multicurrency.loti.Loti` (L1.000,00),
`multicurrency.malagasy_ariary.MalagasyAriary` (1.000),
`multicurrency.malaysian_ringgit.MalaysianRinggit` (RM1,000.00),
`multicurrency.manat.Manat` (m1.000,00),
`multicurrency.mauritius_rupee.MauritiusRupee` (₨1,000.00),
`multicurrency.metical.Metical` (MTn1.000),
`multicurrency.mexican_peso.MexicanPeso` ($1,000.00),
`multicurrency.moldovan_leu.MoldovanLeu` (L1.000,00),
`multicurrency.moroccan_dirham.MoroccanDirham` (د.م.1.000,00),
`multicurrency.naira.Naira` (₦1.000,00),
`multicurrency.nakfa.Nakfa` (Nfk1.000,00),
`multicurrency.namibia_dollar.NamibiaDollar` ($1.000,00),
`multicurrency.nepalese_rupee.NepaleseRupee` (₨1,000.00),
`multicurrency.new_israeli_shekel.NewIsraeliShekel` (₪1,000.00),
`multicurrency.new_zealand_dollar.NewZealandDollar` ($1,000.00),
`multicurrency.ngultrum.Ngultrum` (1.000,00),
`multicurrency.north_korean_won.NorthKoreanWon` (₩1.000,00),
`multicurrency.norwegian_krone.NorwegianKrone` (kr1.000,00),
`multicurrency.nuevo_sol.NuevoSol` (S/.1,000.00),
`multicurrency.ouguiya.Ouguiya` (UM1.000,00),
`multicurrency.pzloty.PZloty` (zł1.000,00),
`multicurrency.pakistan_rupee.PakistanRupee` (₨1,000.00),
`multicurrency.pataca.Pataca` (P1.000,00),
`multicurrency.paanga.Paanga` (T$1,000.00),
`multicurrency.peso_uruguayo.PesoUruguayo` ($1.000,00),
`multicurrency.philippine_peso.PhilippinePeso` (₱1,000.00),
`multicurrency.pound_sterling.PoundSterling` (£1,000.00),
`multicurrency.pula.Pula` (P1.000,00),
`multicurrency.qatari_rial.QatariRial` (ر.ق1.000,00),
`multicurrency.quetzal.Quetzal` (Q1.000,00),
`multicurrency.rand.Rand` (R1 000.00),
`multicurrency.rial_omani.RialOmani` (ر.ع.1,000.000),
`multicurrency.riel.Riel` (៛1.000,00),
`multicurrency.rufiyaa.Rufiyaa` (ރ.1.000,00),
`multicurrency.rupiah.Rupiah` (Rp1.000,00),
`multicurrency.russian_ruble.RussianRuble` (р.1.000,00),
`multicurrency.rwanda_franc.RwandaFranc` (₣1.000),
`multicurrency.saint_helena_pound.SaintHelenaPound` (£1.000,00),
`multicurrency.saudi_riyal.SaudiRiyal` (ر.س1,000.00),
`multicurrency.serbian_dinar.SerbianDinar` (din1.000,00),
`multicurrency.seychelles_rupee.SeychellesRupee` (₨1.000,00),
`multicurrency.singapore_dollar.SingaporeDollar` ($1,000.00),
`multicurrency.solomon_islands_dollar.SolomonIslandsDollar` ($1.000,00),
`multicurrency.som.Som` (1.000,00),
`multicurrency.somali_shilling.SomaliShilling` (Sh1.000,00),
`multicurrency.somoni.Somoni` (ЅМ1.000,00),
`multicurrency.south_korean_won.SouthKoreanWon` (₩1,000),
`multicurrency.sri_lanka_rupee.SriLankaRupee` (Rs1.000,00),
`multicurrency.sudanese_pound.SudanesePound` (£1.000,00),
`multicurrency.suriname_dollar.SurinameDollar` ($1.000,00),
`multicurrency.swedish_krona.SwedishKrona` (kr1.000,00),
`multicurrency.swiss_franc.SwissFranc` (₣1'000.00),
`multicurrency.syrian_pound.SyrianPound` (ل.س1.000,00),
`multicurrency.taiwan_dollar.TaiwanDollar` ($1.000,00),
`multicurrency.taka.Taka` (৳1,000.00),
`multicurrency.tala.Tala` (T1.000,00),
`multicurrency.tanzanian_shilling.TanzanianShilling` (Sh1,000.00),
`multicurrency.tenge.Tenge` (〒1.000,00),
`multicurrency.trinidad_and_tobago_dollar.TrinidadandTobagoDollar` ($1.000,00),
`multicurrency.tugrik.Tugrik` (₮1.000,00),
`multicurrency.tunisian_dinar.TunisianDinar` (د.ت1.000,000),
`multicurrency.turkish_lira.TurkishLira` (₤1,000.00),
`multicurrency.uae_dirham.UAEDirham` (د.إ1,000.00),
`multicurrency.us_dollar.USDollar` ($1,000.00),
`multicurrency.uganda_shilling.UgandaShilling` (Sh1.000),
`multicurrency.uzbekistan_sum.UzbekistanSum` (1.000,00),
`multicurrency.vatu.Vatu` (Vt1,000),
`multicurrency.yemeni_rial.YemeniRial` (﷼1.000,00),
`multicurrency.yen.Yen` (¥1,000),
`multicurrency.yuan.Yuan` (¥1,000.00),
`multicurrency.zambian_kwacha.ZambianKwacha` (ZK1.000,00),
`multicurrency.zimbabwe_dollar.ZimbabweDollar` ($1.000,00)

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
from .algerian_dinar import AlgerianDinar
from .argentine_peso import ArgentinePeso
from .armenian_dram import ArmenianDram
from .aruban_florin import ArubanFlorin
from .australian_dollar import AustralianDollar
from .azerbaijanian_manat import AzerbaijanianManat
from .bahamian_dollar import BahamianDollar
from .bahraini_dinar import BahrainiDinar
from .baht import Baht
from .balboa import Balboa
from .barbados_dollar import BarbadosDollar
from .belarusian_ruble import BelarusianRuble
from .belize_dollar import BelizeDollar
from .bermudian_dollar import BermudianDollar
from .bolivar_fuerte import BolivarFuerte
from .boliviano import Boliviano
from .brazilian_real import BrazilianReal
from .brunei_dollar import BruneiDollar
from .bulgarian_lev import BulgarianLev
from .burundi_franc import BurundiFranc
from .cfa_franc_bceao import CFAFrancBCEAO
from .cfa_franc_beac import CFAFrancBEAC
from .cfp_franc import CFPFranc
from .canadian_dollar_en import CanadianDollarEN
from .canadian_dollar_fr import CanadianDollarFR
from .cape_verde_escudo import CapeVerdeEscudo
from .cayman_islands_dollar import CaymanIslandsDollar
from .cedi import Cedi
from .chilean_peso import ChileanPeso
from .colombian_peso import ColombianPeso
from .congolese_franc import CongoleseFranc
from .cordoba_oro import CordobaOro
from .costa_rican_colon import CostaRicanColon
from .croatian_kuna import CroatianKuna
from .cuban_peso import CubanPeso
from .czech_koruna import CzechKoruna
from .dalasi import Dalasi
from .danish_krone import DanishKrone
from .denar import Denar
from .djibouti_franc import DjiboutiFranc
from .dobra import Dobra
from .dominican_peso import DominicanPeso
from .dong import Dong
from .east_caribbean_dollar import EastCaribbeanDollar
from .egyptian_pound import EgyptianPound
from .ethiopian_birr import EthiopianBirr
from .euro import Euro
from .falkland_islands_pound import FalklandIslandsPound
from .fiji_dollar import FijiDollar
from .forint import Forint
from .gibraltar_pound import GibraltarPound
from .gourde import Gourde
from .guarani import Guarani
from .guinea_franc import GuineaFranc
from .guyana_dollar import GuyanaDollar
from .hong_kong_dollar import HongKongDollar
from .hryvnia import Hryvnia
from .iceland_krona import IcelandKrona
from .indian_rupee import IndianRupee
from .iranian_rial import IranianRial
from .iraqi_dinar import IraqiDinar
from .jamaican_dollar import JamaicanDollar
from .jordanian_dinar import JordanianDinar
from .kenyan_shilling import KenyanShilling
from .kina import Kina
from .kip import Kip
from .konvertibilna_marka import KonvertibilnaMarka
from .kuwaiti_dinar import KuwaitiDinar
from .kwacha import Kwacha
from .kwanza import Kwanza
from .kyat import Kyat
from .lari import Lari
from .lebanese_pound import LebanesePound
from .lek import Lek
from .lempira import Lempira
from .leone import Leone
from .leu import Leu
from .liberian_dollar import LiberianDollar
from .libyan_dinar import LibyanDinar
from .lilangeni import Lilangeni
from .loti import Loti
from .malagasy_ariary import MalagasyAriary
from .malaysian_ringgit import MalaysianRinggit
from .manat import Manat
from .mauritius_rupee import MauritiusRupee
from .metical import Metical
from .mexican_peso import MexicanPeso
from .moldovan_leu import MoldovanLeu
from .moroccan_dirham import MoroccanDirham
from .naira import Naira
from .nakfa import Nakfa
from .namibia_dollar import NamibiaDollar
from .nepalese_rupee import NepaleseRupee
from .new_israeli_shekel import NewIsraeliShekel
from .new_zealand_dollar import NewZealandDollar
from .ngultrum import Ngultrum
from .north_korean_won import NorthKoreanWon
from .norwegian_krone import NorwegianKrone
from .nuevo_sol import NuevoSol
from .ouguiya import Ouguiya
from .pzloty import PZloty
from .pakistan_rupee import PakistanRupee
from .pataca import Pataca
from .paanga import Paanga
from .peso_uruguayo import PesoUruguayo
from .philippine_peso import PhilippinePeso
from .pound_sterling import PoundSterling
from .pula import Pula
from .qatari_rial import QatariRial
from .quetzal import Quetzal
from .rand import Rand
from .rial_omani import RialOmani
from .riel import Riel
from .rufiyaa import Rufiyaa
from .rupiah import Rupiah
from .russian_ruble import RussianRuble
from .rwanda_franc import RwandaFranc
from .saint_helena_pound import SaintHelenaPound
from .saudi_riyal import SaudiRiyal
from .serbian_dinar import SerbianDinar
from .seychelles_rupee import SeychellesRupee
from .singapore_dollar import SingaporeDollar
from .solomon_islands_dollar import SolomonIslandsDollar
from .som import Som
from .somali_shilling import SomaliShilling
from .somoni import Somoni
from .south_korean_won import SouthKoreanWon
from .sri_lanka_rupee import SriLankaRupee
from .sudanese_pound import SudanesePound
from .suriname_dollar import SurinameDollar
from .swedish_krona import SwedishKrona
from .swiss_franc import SwissFranc
from .syrian_pound import SyrianPound
from .taiwan_dollar import TaiwanDollar
from .taka import Taka
from .tala import Tala
from .tanzanian_shilling import TanzanianShilling
from .tenge import Tenge
from .trinidad_and_tobago_dollar import TrinidadandTobagoDollar
from .tugrik import Tugrik
from .tunisian_dinar import TunisianDinar
from .turkish_lira import TurkishLira
from .uae_dirham import UAEDirham
from .us_dollar import USDollar
from .uganda_shilling import UgandaShilling
from .uzbekistan_sum import UzbekistanSum
from .vatu import Vatu
from .yemeni_rial import YemeniRial
from .yen import Yen
from .yuan import Yuan
from .zambian_kwacha import ZambianKwacha
from .zimbabwe_dollar import ZimbabweDollar


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
    'PakistanRupee',
    'Pataca',
    'Paanga',
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
__version__: Final[str] = '0.1.0'
