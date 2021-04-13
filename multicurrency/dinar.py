# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Dinar currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union
from .currency import Currency


class BahrainiDinar(Currency):
    """Bahraini Dinar currency representation.

    Simple usage example:

        >>> from multicurrency import BahrainiDinar
        >>> bahraini_dinar = BahrainiDinar(amount=1)
        >>> print(bahraini_dinar)
        ب.د1.000

    For more details see `multicurrency.currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 3,
        decimal_sign (str, optional): Decimal symbol. Defaults to '.'.
        grouping_sign (str, optional): Grouping symbol. Defaults to ','.
        international (bool, optional): Identifies the currency using
            the 'currency' value instead of the 'symbol'. Defaults to
            False.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: int = 3,
            decimal_sign: Optional[str] = '.',
            grouping_sign: Optional[str] = ',',
            international: bool = False,
            **other) -> 'BahrainiDinar':
        """Class creator.

        Returns:
            BahrainiDinar: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='BHD',
            numeric_code='048',
            symbol='ب.د',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class AlgerianDinar(Currency):
    """Algerian Dinar currency representation.

    Simple usage example:

        >>> from multicurrency import AlgerianDinar
        >>> algerian_dinar = AlgerianDinar(amount=1)
        >>> print(algerian_dinar)
        د.ج1,00

    For more details see `multicurrency.currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 2,
        decimal_sign (str, optional): Decimal symbol. Defaults to ','.
        grouping_sign (str, optional): Grouping symbol. Defaults to '.'.
        international (bool, optional): Identifies the currency using
            the 'currency' value instead of the 'symbol'. Defaults to
            False.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: int = 2,
            decimal_sign: Optional[str] = ',',
            grouping_sign: Optional[str] = '.',
            international: bool = False,
            **other) -> 'AlgerianDinar':
        """Class creator.

        Returns:
            AlgerianDinar: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='DZD',
            numeric_code='012',
            symbol='د.ج',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class IraqiDinar(Currency):
    """Iraqi Dinar currency representation.

    Simple usage example:

        >>> from multicurrency import IraqiDinar
        >>> iraqi_dinar = IraqiDinar(amount=1)
        >>> print(iraqi_dinar)
        ع.د1,000

    For more details see `multicurrency.currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 3,
        decimal_sign (str, optional): Decimal symbol. Defaults to ','.
        grouping_sign (str, optional): Grouping symbol. Defaults to '.'.
        international (bool, optional): Identifies the currency using
            the 'currency' value instead of the 'symbol'. Defaults to
            False.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: int = 3,
            decimal_sign: Optional[str] = ',',
            grouping_sign: Optional[str] = '.',
            international: bool = False,
            **other) -> 'IraqiDinar':
        """Class creator.

        Returns:
            IraqiDinar: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='IQD',
            numeric_code='368',
            symbol='ع.د',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class JordanianDinar(Currency):
    """Jordanian Dinar currency representation.

    Simple usage example:

        >>> from multicurrency import JordanianDinar
        >>> jordanian_dinar = JordanianDinar(amount=1)
        >>> print(jordanian_dinar)
        د.ا1.000

    For more details see `multicurrency.currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 3,
        decimal_sign (str, optional): Decimal symbol. Defaults to '.'.
        grouping_sign (str, optional): Grouping symbol. Defaults to ','.
        international (bool, optional): Identifies the currency using
            the 'currency' value instead of the 'symbol'. Defaults to
            False.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: int = 3,
            decimal_sign: Optional[str] = '.',
            grouping_sign: Optional[str] = ',',
            international: bool = False,
            **other) -> 'JordanianDinar':
        """Class creator.

        Returns:
            JordanianDinar: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='JOD',
            numeric_code='400',
            symbol='د.ا',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class KuwaitiDinar(Currency):
    """Kuwaiti Dinar currency representation.

    Simple usage example:

        >>> from multicurrency import KuwaitiDinar
        >>> kuwaiti_dinar = KuwaitiDinar(amount=1)
        >>> print(kuwaiti_dinar)
        د.ك1.000

    For more details see `multicurrency.currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 3,
        decimal_sign (str, optional): Decimal symbol. Defaults to '.'.
        grouping_sign (str, optional): Grouping symbol. Defaults to ','.
        international (bool, optional): Identifies the currency using
            the 'currency' value instead of the 'symbol'. Defaults to
            False.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: int = 3,
            decimal_sign: Optional[str] = '.',
            grouping_sign: Optional[str] = ',',
            international: bool = False,
            **other) -> 'KuwaitiDinar':
        """Class creator.

        Returns:
            KuwaitiDinar: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='KWD',
            numeric_code='414',
            symbol='د.ك',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class LibyanDinar(Currency):
    """Libyan Dinar currency representation.

    Simple usage example:

        >>> from multicurrency import LibyanDinar
        >>> libyan_dinar = LibyanDinar(amount=1)
        >>> print(libyan_dinar)
        ل.د1,000

    For more details see `multicurrency.currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 3,
        decimal_sign (str, optional): Decimal symbol. Defaults to ','.
        grouping_sign (str, optional): Grouping symbol. Defaults to '.'.
        international (bool, optional): Identifies the currency using
            the 'currency' value instead of the 'symbol'. Defaults to
            False.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: int = 3,
            decimal_sign: Optional[str] = ',',
            grouping_sign: Optional[str] = '.',
            international: bool = False,
            **other) -> 'LibyanDinar':
        """Class creator.

        Returns:
            LibyanDinar: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='LYD',
            numeric_code='434',
            symbol='ل.د',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class SerbianDinar(Currency):
    """Serbian Dinar currency representation.

    Simple usage example:

        >>> from multicurrency import SerbianDinar
        >>> serbian_dinar = SerbianDinar(amount=1)
        >>> print(serbian_dinar)
        din1,00

    For more details see `multicurrency.currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 2,
        decimal_sign (str, optional): Decimal symbol. Defaults to ','.
        grouping_sign (str, optional): Grouping symbol. Defaults to '.'.
        international (bool, optional): Identifies the currency using
            the 'currency' value instead of the 'symbol'. Defaults to
            False.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: int = 2,
            decimal_sign: Optional[str] = ',',
            grouping_sign: Optional[str] = '.',
            international: bool = False,
            **other) -> 'SerbianDinar':
        """Class creator.

        Returns:
            SerbianDinar: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='RSD',
            numeric_code='941',
            symbol='din',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class TunisianDinar(Currency):
    """Tunisian Dinar currency representation.

    Simple usage example:

        >>> from multicurrency import TunisianDinar
        >>> tunisian_dinar = TunisianDinar(amount=1)
        >>> print(tunisian_dinar)
        د.ت1,000

    For more details see `multicurrency.currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 3,
        decimal_sign (str, optional): Decimal symbol. Defaults to ','.
        grouping_sign (str, optional): Grouping symbol. Defaults to '.'.
        international (bool, optional): Identifies the currency using
            the 'currency' value instead of the 'symbol'. Defaults to
            False.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: int = 3,
            decimal_sign: Optional[str] = ',',
            grouping_sign: Optional[str] = '.',
            international: bool = False,
            **other) -> 'TunisianDinar':
        """Class creator.

        Returns:
            TunisianDinar: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='TND',
            numeric_code='788',
            symbol='د.ت',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)
