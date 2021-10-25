# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Lira currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union
from .currency import Currency


class TurkishLira(Currency):
    """Turkish Lira currency representation.

    Simple usage example:

        >>> from multicurrency import TurkishLira
        >>> turkish_lira = TurkishLira(
        ...     amount=123456.789)
        >>> print(turkish_lira)
        ₤123.456,79

    For more details see `multicurrency.currency.Currency` .

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
            and the value. Defaults to ''.
        symbol_ahead (bool, optional): True if symbol goes ahead of the
            value. False otherwise. Defaults to True.
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
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '',
            **other) -> 'TurkishLira':
        """Class creator.

        Returns:
            TurkishLira: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='TRY',
            numeric_code='949',
            symbol='₤',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='₤',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)


class TurkishLiraCY(Currency):
    """Turkish Lira CY currency representation.

    Simple usage example:

        >>> from multicurrency import TurkishLiraCY
        >>> turkish_lira_cy = TurkishLiraCY(
        ...     amount=123456.789)
        >>> print(turkish_lira_cy)
        ₤123.456,79

    For more details see `multicurrency.currency.Currency` .

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
            and the value. Defaults to ''.
        symbol_ahead (bool, optional): True if symbol goes ahead of the
            value. False otherwise. Defaults to True.
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
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '',
            **other) -> 'TurkishLiraCY':
        """Class creator.

        Returns:
            TurkishLiraCY: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='TRY',
            numeric_code='949',
            symbol='₤',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='CY₤',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)


class TurkishLiraTR(Currency):
    """Turkish Lira TR currency representation.

    Simple usage example:

        >>> from multicurrency import TurkishLiraTR
        >>> turkish_lira_tr = TurkishLiraTR(
        ...     amount=123456.789)
        >>> print(turkish_lira_tr)
        ₤123.456,79

    For more details see `multicurrency.currency.Currency` .

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
            and the value. Defaults to ''.
        symbol_ahead (bool, optional): True if symbol goes ahead of the
            value. False otherwise. Defaults to True.
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
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '',
            **other) -> 'TurkishLiraTR':
        """Class creator.

        Returns:
            TurkishLiraTR: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='TRY',
            numeric_code='949',
            symbol='₤',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='TR₤',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)
