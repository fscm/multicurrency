# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Kwacha currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union
from .currency import Currency


class Kwacha(Currency):
    """Kwacha currency representation.

    Simple usage example:

        >>> from multicurrency import Kwacha
        >>> kwacha = Kwacha(amount=1)
        >>> print(kwacha)
        MK1,00

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
            **other) -> 'Kwacha':
        """Class creator.

        Returns:
            Kwacha: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='MWK',
            numeric_code='454',
            symbol='MK',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class ZambianKwacha(Currency):
    """Zambian Kwacha currency representation.

    Simple usage example:

        >>> from multicurrency import ZambianKwacha
        >>> zambian_kwacha = ZambianKwacha(amount=1)
        >>> print(zambian_kwacha)
        ZK1,00

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
            **other) -> 'ZambianKwacha':
        """Class creator.

        Returns:
            ZambianKwacha: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='ZMW',
            numeric_code='967',
            symbol='ZK',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)
