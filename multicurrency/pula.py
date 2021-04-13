# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Pula currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union
from .currency import Currency


class Pula(Currency):
    """Pula currency representation.

    Simple usage example:

        >>> from multicurrency import Pula
        >>> pula = Pula(amount=1)
        >>> print(pula)
        P1,00

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
            **other) -> 'Pula':
        """Class creator.

        Returns:
            Pula: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='BWP',
            numeric_code='072',
            symbol='P',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)
