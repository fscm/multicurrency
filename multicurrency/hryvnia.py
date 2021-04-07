# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Hryvnia currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union
from .currency import Currency


class Hryvnia(Currency):
    """Hryvnia currency representation.

    Simple usage example:

        >>> from multicurrency import Hryvnia
        >>> hryvnia = Hryvnia(amount=1)
        >>> print(hryvnia)
        ₴1,00

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
            **other) -> 'Hryvnia':
        """Class creator.

        Returns:
            Hryvnia: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='UAH',
            symbol='₴',
            code='980',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)
