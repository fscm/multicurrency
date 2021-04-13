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
        >>> turkish_lira = TurkishLira(amount=1)
        >>> print(turkish_lira)
        ₤1.00

    For more details see `multicurrency.currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 2,
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
            decimal_places: int = 2,
            decimal_sign: Optional[str] = '.',
            grouping_sign: Optional[str] = ',',
            international: bool = False,
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
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)
