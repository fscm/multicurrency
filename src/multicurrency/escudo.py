# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Escudo currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union
from .currency import Currency


class CapeVerdeEscudo(Currency):
    """Cape Verde Escudo currency representation.

    Simple usage example:

        >>> from multicurrency import CapeVerdeEscudo
        >>> cape_verde_escudo = CapeVerdeEscudo(
        ...     amount=123456.789)
        >>> print(cape_verde_escudo)
        123 456$79

    For more details see `multicurrency.currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 2,
        decimal_sign (str, optional): Decimal symbol. Defaults to '$'.
        grouping_sign (str, optional): Grouping symbol. Defaults to ' '.
        international (bool, optional): Identifies the currency using
            the 'currency' value instead of the 'symbol'. Defaults to
            False.
        symbol_separator (str, optional): Separation between the symbol
            and the value. Defaults to ''.
        symbol_ahead (bool, optional): True if symbol goes ahead of the
            value. False otherwise. Defaults to False.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: Optional[int] = 2,
            decimal_sign: Optional[str] = '$',
            grouping_sign: Optional[str] = '\u202F',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = False,
            symbol_separator: Optional[str] = '',
            **other) -> 'CapeVerdeEscudo':
        """Class creator.

        Returns:
            CapeVerdeEscudo: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='CVE',
            numeric_code='132',
            symbol='',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)
