# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Manat currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union
from ._currency import Currency


class AzerbaijanianManat(Currency):
    """Azerbaijanian Manat currency representation.

    Simple usage example:

        >>> from multicurrency import AzerbaijanianManat
        >>> azerbaijanian_manat = AzerbaijanianManat(
        ...     amount=123456.789)
        >>> print(azerbaijanian_manat)
        123.456,79 ₼

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
            **other) -> 'AzerbaijanianManat':
        """Class creator.

        Returns:
            AzerbaijanianManat: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='AZN',
            numeric_code='944',
            symbol='₼',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='₼',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)


class Manat(Currency):
    """Manat currency representation.

    Simple usage example:

        >>> from multicurrency import Manat
        >>> manat = Manat(
        ...     amount=123456.789)
        >>> print(manat)
        123 456,79 m

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
            **other) -> 'Manat':
        """Class creator.

        Returns:
            Manat: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='TMT',
            numeric_code='934',
            symbol='m',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='m',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)
