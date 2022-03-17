# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Dinar currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union
from ._currency import Currency


class BahrainiDinar(Currency):
    """Bahraini Dinar currency representation.

    Simple usage example:

        >>> from multicurrency import BahrainiDinar
        >>> bahraini_dinar = BahrainiDinar(
        ...     amount=123456.789)
        >>> print(bahraini_dinar)
        د.ب. ١٢٣٬٤٥٦٫٧٨٩

    For more details see `multicurrency._currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 3,
        decimal_sign (str, optional): Decimal symbol. Defaults to '٫'.
        grouping_places (int, optional): Number of digits for grouping.
            Defaults to 3,
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
            grouping_places: Optional[int] = 3,
            grouping_sign: Optional[str] = '\u066C',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '\u00A0',
            **other) -> Currency:
        """Class creator.

        Returns:
            Currency: new `Currency` object.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='BHD',
            numeric_code='048',
            symbol='د.ب.',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='د.ب.',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
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
        123.456,79 د.ج.

    For more details see `multicurrency._currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 2,
        decimal_sign (str, optional): Decimal symbol. Defaults to ','.
        grouping_places (int, optional): Number of digits for grouping.
            Defaults to 3,
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
            grouping_places: Optional[int] = 3,
            grouping_sign: Optional[str] = '.',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = False,
            symbol_separator: Optional[str] = '\u00A0',
            **other) -> Currency:
        """Class creator.

        Returns:
            Currency: new `Currency` object.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='DZD',
            numeric_code='012',
            symbol='د.ج.',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='د.ج.',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
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
        د.ع. ١٢٣٬٤٥٦٫٧٨٩

    For more details see `multicurrency._currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 3,
        decimal_sign (str, optional): Decimal symbol. Defaults to '٫'.
        grouping_places (int, optional): Number of digits for grouping.
            Defaults to 3,
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
            grouping_places: Optional[int] = 3,
            grouping_sign: Optional[str] = '\u066C',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '\u00A0',
            **other) -> Currency:
        """Class creator.

        Returns:
            Currency: new `Currency` object.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='IQD',
            numeric_code='368',
            symbol='د.ع.',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='د.ع.',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
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
        د.أ. ١٢٣٬٤٥٦٫٧٨٩

    For more details see `multicurrency._currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 3,
        decimal_sign (str, optional): Decimal symbol. Defaults to '٫'.
        grouping_places (int, optional): Number of digits for grouping.
            Defaults to 3,
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
            grouping_places: Optional[int] = 3,
            grouping_sign: Optional[str] = '\u066C',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '\u00A0',
            **other) -> Currency:
        """Class creator.

        Returns:
            Currency: new `Currency` object.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='JOD',
            numeric_code='400',
            symbol='د.أ.',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='د.أ.',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
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
        د.ك. ١٢٣٬٤٥٦٫٧٨٩

    For more details see `multicurrency._currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 3,
        decimal_sign (str, optional): Decimal symbol. Defaults to '٫'.
        grouping_places (int, optional): Number of digits for grouping.
            Defaults to 3,
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
            grouping_places: Optional[int] = 3,
            grouping_sign: Optional[str] = '\u066C',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '\u00A0',
            **other) -> Currency:
        """Class creator.

        Returns:
            Currency: new `Currency` object.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='KWD',
            numeric_code='414',
            symbol='د.ك.',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='د.ك.',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
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
        د.ل. 123.456,789

    For more details see `multicurrency._currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 3,
        decimal_sign (str, optional): Decimal symbol. Defaults to ','.
        grouping_places (int, optional): Number of digits for grouping.
            Defaults to 3,
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
            grouping_places: Optional[int] = 3,
            grouping_sign: Optional[str] = '.',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '\u00A0',
            **other) -> Currency:
        """Class creator.

        Returns:
            Currency: new `Currency` object.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='LYD',
            numeric_code='434',
            symbol='د.ل.',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='د.ل.',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
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
        123.456,79 дин.

    For more details see `multicurrency._currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 2,
        decimal_sign (str, optional): Decimal symbol. Defaults to ','.
        grouping_places (int, optional): Number of digits for grouping.
            Defaults to 3,
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
            grouping_places: Optional[int] = 3,
            grouping_sign: Optional[str] = '.',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = False,
            symbol_separator: Optional[str] = '\u00A0',
            **other) -> Currency:
        """Class creator.

        Returns:
            Currency: new `Currency` object.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='RSD',
            numeric_code='941',
            symbol='дин.',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='дин.',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
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
        123 456,79 дин.

    For more details see `multicurrency._currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 2,
        decimal_sign (str, optional): Decimal symbol. Defaults to ','.
        grouping_places (int, optional): Number of digits for grouping.
            Defaults to 3,
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
            grouping_places: Optional[int] = 3,
            grouping_sign: Optional[str] = '\u202F',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = False,
            symbol_separator: Optional[str] = '\u00A0',
            **other) -> Currency:
        """Class creator.

        Returns:
            Currency: new `Currency` object.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='RSD',
            numeric_code='941',
            symbol='дин.',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='дин.',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
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
        د.ت. 123.456,789

    For more details see `multicurrency._currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 3,
        decimal_sign (str, optional): Decimal symbol. Defaults to ','.
        grouping_places (int, optional): Number of digits for grouping.
            Defaults to 3,
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
            grouping_places: Optional[int] = 3,
            grouping_sign: Optional[str] = '.',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '\u00A0',
            **other) -> Currency:
        """Class creator.

        Returns:
            Currency: new `Currency` object.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='TND',
            numeric_code='788',
            symbol='د.ت.',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='د.ت.',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)
