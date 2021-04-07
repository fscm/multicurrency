# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Won currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union
from .currency import Currency


class NorthKoreanWon(Currency):
    """North Korean Won currency representation.

    Simple usage example:

        >>> from multicurrency import NorthKoreanWon
        >>> north_korean_won = NorthKoreanWon(amount=1)
        >>> print(north_korean_won)
        ₩1,00

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
            **other) -> 'NorthKoreanWon':
        """Class creator.

        Returns:
            NorthKoreanWon: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='KPW',
            symbol='₩',
            code='408',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class SouthKoreanWon(Currency):
    """South Korean Won currency representation.

    Simple usage example:

        >>> from multicurrency import SouthKoreanWon
        >>> south_korean_won = SouthKoreanWon(amount=1)
        >>> print(south_korean_won)
        ₩1

    For more details see `multicurrency.currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 0,
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
            decimal_places: int = 0,
            decimal_sign: Optional[str] = '.',
            grouping_sign: Optional[str] = ',',
            international: bool = False,
            **other) -> 'SouthKoreanWon':
        """Class creator.

        Returns:
            SouthKoreanWon: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='KRW',
            symbol='₩',
            code='410',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)
