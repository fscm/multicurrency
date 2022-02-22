# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Shekel currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union
from ._currency import Currency


class NewIsraeliShekel(Currency):
    """New Israeli Shekel currency representation.

    Simple usage example:

        >>> from multicurrency import NewIsraeliShekel
        >>> new_israeli_shekel = NewIsraeliShekel(
        ...     amount=123456.789)
        >>> print(new_israeli_shekel)
        123,456.79 ₪

    For more details see `multicurrency._currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 2,
        decimal_sign (str, optional): Decimal symbol. Defaults to '.'.
        grouping_places (int, optional): Number of digits for grouping.
            Defaults to 3,
        grouping_sign (str, optional): Grouping symbol. Defaults to ','.
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
            decimal_sign: Optional[str] = '.',
            grouping_places: Optional[int] = 3,
            grouping_sign: Optional[str] = ',',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = False,
            symbol_separator: Optional[str] = '\u00A0',
            **other) -> 'NewIsraeliShekel':
        """Class creator.

        Returns:
            NewIsraeliShekel: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='ILS',
            numeric_code='376',
            symbol='₪',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='₪',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)


class NewIsraeliShekelIL(Currency):
    """New Israeli Shekel IL currency representation.

    Simple usage example:

        >>> from multicurrency import NewIsraeliShekelIL
        >>> new_israeli_shekel_il = NewIsraeliShekelIL(
        ...     amount=123456.789)
        >>> print(new_israeli_shekel_il)
        123,456.79 ₪

    For more details see `multicurrency._currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 2,
        decimal_sign (str, optional): Decimal symbol. Defaults to '.'.
        grouping_places (int, optional): Number of digits for grouping.
            Defaults to 3,
        grouping_sign (str, optional): Grouping symbol. Defaults to ','.
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
            decimal_sign: Optional[str] = '.',
            grouping_places: Optional[int] = 3,
            grouping_sign: Optional[str] = ',',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = False,
            symbol_separator: Optional[str] = '\u00A0',
            **other) -> 'NewIsraeliShekelIL':
        """Class creator.

        Returns:
            NewIsraeliShekelIL: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='ILS',
            numeric_code='376',
            symbol='₪',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='IL₪',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)


class NewIsraeliShekelPS(Currency):
    """New Israeli Shekel PS currency representation.

    Simple usage example:

        >>> from multicurrency import NewIsraeliShekelPS
        >>> new_israeli_shekel_ps = NewIsraeliShekelPS(
        ...     amount=123456.789)
        >>> print(new_israeli_shekel_ps)
        123,456.79 ₪

    For more details see `multicurrency._currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 2,
        decimal_sign (str, optional): Decimal symbol. Defaults to '.'.
        grouping_places (int, optional): Number of digits for grouping.
            Defaults to 3,
        grouping_sign (str, optional): Grouping symbol. Defaults to ','.
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
            decimal_sign: Optional[str] = '.',
            grouping_places: Optional[int] = 3,
            grouping_sign: Optional[str] = ',',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = False,
            symbol_separator: Optional[str] = '\u00A0',
            **other) -> 'NewIsraeliShekelPS':
        """Class creator.

        Returns:
            NewIsraeliShekelPS: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='ILS',
            numeric_code='376',
            symbol='₪',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='PS₪',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)