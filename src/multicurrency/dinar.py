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
        >>> bahraini_dinar = BahrainiDinar(
        ...     amount=123456.789)
        >>> print(bahraini_dinar)
        ١٢٣٬٤٥٦٫٧٨٩ ب.د

    For more details see `multicurrency.currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 3,
        decimal_sign (str, optional): Decimal symbol. Defaults to '٫'.
        grouping_sign (str, optional): Grouping symbol. Defaults to '٬'.
        international (bool, optional): Identifies the currency using
            the 'currency' value instead of the 'symbol'. Defaults to
            False.
        symbol_separator (str, optional): Separation between the symbol
            and the value. Defaults to ' '.
        symbol_ahead (bool, optional): True if symbol goes ahead of the
            value. False otherwise. Defaults to False.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: Optional[int] = 3,
            decimal_sign: Optional[str] = '\u066B',
            grouping_sign: Optional[str] = '\u066C',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = False,
            symbol_separator: Optional[str] = '\u00A0',
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
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            convertion='٠١٢٣٤٥٦٧٨٩-',
            international=international)


class AlgerianDinar(Currency):
    """Algerian Dinar currency representation.

    Simple usage example:

        >>> from multicurrency import AlgerianDinar
        >>> algerian_dinar = AlgerianDinar(
        ...     amount=123456.789)
        >>> print(algerian_dinar)
        123.456,79 د.ج

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
        symbol_separator (str, optional): Separation between the symbol
            and the value. Defaults to ' '.
        symbol_ahead (bool, optional): True if symbol goes ahead of the
            value. False otherwise. Defaults to False.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: Optional[int] = 2,
            decimal_sign: Optional[str] = ',',
            grouping_sign: Optional[str] = '.',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = False,
            symbol_separator: Optional[str] = '\u00A0',
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
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)


class IraqiDinar(Currency):
    """Iraqi Dinar currency representation.

    Simple usage example:

        >>> from multicurrency import IraqiDinar
        >>> iraqi_dinar = IraqiDinar(
        ...     amount=123456.789)
        >>> print(iraqi_dinar)
        ع.د ١٢٣٬٤٥٦٫٧٨٩

    For more details see `multicurrency.currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 3,
        decimal_sign (str, optional): Decimal symbol. Defaults to '٫'.
        grouping_sign (str, optional): Grouping symbol. Defaults to '٬'.
        international (bool, optional): Identifies the currency using
            the 'currency' value instead of the 'symbol'. Defaults to
            False.
        symbol_separator (str, optional): Separation between the symbol
            and the value. Defaults to ' '.
        symbol_ahead (bool, optional): True if symbol goes ahead of the
            value. False otherwise. Defaults to True.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: Optional[int] = 3,
            decimal_sign: Optional[str] = '\u066B',
            grouping_sign: Optional[str] = '\u066C',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '\u00A0',
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
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            convertion='٠١٢٣٤٥٦٧٨٩-',
            international=international)


class JordanianDinar(Currency):
    """Jordanian Dinar currency representation.

    Simple usage example:

        >>> from multicurrency import JordanianDinar
        >>> jordanian_dinar = JordanianDinar(
        ...     amount=123456.789)
        >>> print(jordanian_dinar)
        د.ا ١٢٣٬٤٥٦٫٧٨٩

    For more details see `multicurrency.currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 3,
        decimal_sign (str, optional): Decimal symbol. Defaults to '٫'.
        grouping_sign (str, optional): Grouping symbol. Defaults to '٬'.
        international (bool, optional): Identifies the currency using
            the 'currency' value instead of the 'symbol'. Defaults to
            False.
        symbol_separator (str, optional): Separation between the symbol
            and the value. Defaults to ' '.
        symbol_ahead (bool, optional): True if symbol goes ahead of the
            value. False otherwise. Defaults to True.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: Optional[int] = 3,
            decimal_sign: Optional[str] = '\u066B',
            grouping_sign: Optional[str] = '\u066C',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '\u00A0',
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
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            convertion='٠١٢٣٤٥٦٧٨٩-',
            international=international)


class KuwaitiDinar(Currency):
    """Kuwaiti Dinar currency representation.

    Simple usage example:

        >>> from multicurrency import KuwaitiDinar
        >>> kuwaiti_dinar = KuwaitiDinar(
        ...     amount=123456.789)
        >>> print(kuwaiti_dinar)
        د.ك ١٢٣٬٤٥٦٫٧٨٩

    For more details see `multicurrency.currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 3,
        decimal_sign (str, optional): Decimal symbol. Defaults to '٫'.
        grouping_sign (str, optional): Grouping symbol. Defaults to '٬'.
        international (bool, optional): Identifies the currency using
            the 'currency' value instead of the 'symbol'. Defaults to
            False.
        symbol_separator (str, optional): Separation between the symbol
            and the value. Defaults to ' '.
        symbol_ahead (bool, optional): True if symbol goes ahead of the
            value. False otherwise. Defaults to True.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: Optional[int] = 3,
            decimal_sign: Optional[str] = '\u066B',
            grouping_sign: Optional[str] = '\u066C',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '\u00A0',
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
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            convertion='٠١٢٣٤٥٦٧٨٩-',
            international=international)


class LibyanDinar(Currency):
    """Libyan Dinar currency representation.

    Simple usage example:

        >>> from multicurrency import LibyanDinar
        >>> libyan_dinar = LibyanDinar(
        ...     amount=123456.789)
        >>> print(libyan_dinar)
        ل.د 123.456,789

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
        symbol_separator (str, optional): Separation between the symbol
            and the value. Defaults to ' '.
        symbol_ahead (bool, optional): True if symbol goes ahead of the
            value. False otherwise. Defaults to True.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: Optional[int] = 3,
            decimal_sign: Optional[str] = ',',
            grouping_sign: Optional[str] = '.',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '\u00A0',
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
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)


class SerbianDinarXK(Currency):
    """Serbian Dinar XK currency representation.

    Simple usage example:

        >>> from multicurrency import SerbianDinarXK
        >>> serbian_dinar_xk = SerbianDinarXK(
        ...     amount=123456.789)
        >>> print(serbian_dinar_xk)
        123.456,79 дин

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
        symbol_separator (str, optional): Separation between the symbol
            and the value. Defaults to ' '.
        symbol_ahead (bool, optional): True if symbol goes ahead of the
            value. False otherwise. Defaults to False.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: Optional[int] = 2,
            decimal_sign: Optional[str] = ',',
            grouping_sign: Optional[str] = '.',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = False,
            symbol_separator: Optional[str] = '\u00A0',
            **other) -> 'SerbianDinarXK':
        """Class creator.

        Returns:
            SerbianDinarXK: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='RSD',
            numeric_code='941',
            symbol='дин',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)


class SerbianDinarSR(Currency):
    """Serbian Dinar SR currency representation.

    Simple usage example:

        >>> from multicurrency import SerbianDinarSR
        >>> serbian_dinar_sr = SerbianDinarSR(
        ...     amount=123456.789)
        >>> print(serbian_dinar_sr)
        123 456,79 дин

    For more details see `multicurrency.currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 2,
        decimal_sign (str, optional): Decimal symbol. Defaults to ','.
        grouping_sign (str, optional): Grouping symbol. Defaults to ' '.
        international (bool, optional): Identifies the currency using
            the 'currency' value instead of the 'symbol'. Defaults to
            False.
        symbol_separator (str, optional): Separation between the symbol
            and the value. Defaults to ' '.
        symbol_ahead (bool, optional): True if symbol goes ahead of the
            value. False otherwise. Defaults to False.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: Optional[int] = 2,
            decimal_sign: Optional[str] = ',',
            grouping_sign: Optional[str] = '\u202F',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = False,
            symbol_separator: Optional[str] = '\u00A0',
            **other) -> 'SerbianDinarSR':
        """Class creator.

        Returns:
            SerbianDinarSR: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='RSD',
            numeric_code='941',
            symbol='дин',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)


class TunisianDinar(Currency):
    """Tunisian Dinar currency representation.

    Simple usage example:

        >>> from multicurrency import TunisianDinar
        >>> tunisian_dinar = TunisianDinar(
        ...     amount=123456.789)
        >>> print(tunisian_dinar)
        د.ت 123.456,789

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
        symbol_separator (str, optional): Separation between the symbol
            and the value. Defaults to ' '.
        symbol_ahead (bool, optional): True if symbol goes ahead of the
            value. False otherwise. Defaults to True.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: Optional[int] = 3,
            decimal_sign: Optional[str] = ',',
            grouping_sign: Optional[str] = '.',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '\u00A0',
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
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)
