# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Dirham currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union
from .currency import Currency


class UAEDirham(Currency):
    """UAE Dirham currency representation.

    Simple usage example:

        >>> from multicurrency import UAEDirham
        >>> uae_dirham = UAEDirham(
        ...     amount=123456.789)
        >>> print(uae_dirham)
        ١٢٣٬٤٥٦٫٧٩ د.إ

    For more details see `multicurrency.currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 2,
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
            decimal_places: Optional[int] = 2,
            decimal_sign: Optional[str] = '\u066B',
            grouping_sign: Optional[str] = '\u066C',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = False,
            symbol_separator: Optional[str] = '\u00A0',
            **other) -> 'UAEDirham':
        """Class creator.

        Returns:
            UAEDirham: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='AED',
            numeric_code='784',
            symbol='د.إ',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            convertion='٠١٢٣٤٥٦٧٨٩-',
            international=international)


class MoroccanDirham(Currency):
    """Moroccan Dirham currency representation.

    Simple usage example:

        >>> from multicurrency import MoroccanDirham
        >>> moroccan_dirham = MoroccanDirham(
        ...     amount=123456.789)
        >>> print(moroccan_dirham)
        ١٢٣٬٤٥٦٫٧٩ د.م.

    For more details see `multicurrency.currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 2,
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
            decimal_places: Optional[int] = 2,
            decimal_sign: Optional[str] = '\u066B',
            grouping_sign: Optional[str] = '\u066C',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = False,
            symbol_separator: Optional[str] = '\u00A0',
            **other) -> 'MoroccanDirham':
        """Class creator.

        Returns:
            MoroccanDirham: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='MAD',
            numeric_code='504',
            symbol='د.م.',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            convertion='٠١٢٣٤٥٦٧٨٩-',
            international=international)
