# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Krone currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union
from .currency import Currency


class DanishKrone(Currency):
    """Danish Krone currency representation.

    Simple usage example:

        >>> from multicurrency import DanishKrone
        >>> danish_krone = DanishKrone(
        ...     amount=123456.789)
        >>> print(danish_krone)
        123.456,79 kr

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
            **other) -> 'DanishKrone':
        """Class creator.

        Returns:
            DanishKrone: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='DKK',
            numeric_code='208',
            symbol='kr',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)


class NorwegianKrone(Currency):
    """Norwegian Krone currency representation.

    Simple usage example:

        >>> from multicurrency import NorwegianKrone
        >>> norwegian_krone = NorwegianKrone(
        ...     amount=123456.789)
        >>> print(norwegian_krone)
        kr 123 456,79

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
            value. False otherwise. Defaults to True.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: Optional[int] = 2,
            decimal_sign: Optional[str] = ',',
            grouping_sign: Optional[str] = '\u202F',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '\u00A0',
            **other) -> 'NorwegianKrone':
        """Class creator.

        Returns:
            NorwegianKrone: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='NOK',
            numeric_code='578',
            symbol='kr',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)
