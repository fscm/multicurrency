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
        >>> uae_dirham = UAEDirham(amount=1)
        >>> print(uae_dirham)
        د.إ1.00

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
            **other) -> 'UAEDirham':
        """Class creator.

        Returns:
            UAEDirham: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='AED',
            symbol='د.إ',
            code='784',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class MoroccanDirham(Currency):
    """Moroccan Dirham currency representation.

    Simple usage example:

        >>> from multicurrency import MoroccanDirham
        >>> moroccan_dirham = MoroccanDirham(amount=1)
        >>> print(moroccan_dirham)
        د.م.1,00

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
            **other) -> 'MoroccanDirham':
        """Class creator.

        Returns:
            MoroccanDirham: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='MAD',
            symbol='د.م.',
            code='504',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)
