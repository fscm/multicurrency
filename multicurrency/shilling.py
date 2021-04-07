# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Shilling currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union
from .currency import Currency


class KenyanShilling(Currency):
    """Kenyan Shilling currency representation.

    Simple usage example:

        >>> from multicurrency import KenyanShilling
        >>> kenyan_shilling = KenyanShilling(amount=1)
        >>> print(kenyan_shilling)
        Sh1.00

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
            **other) -> 'KenyanShilling':
        """Class creator.

        Returns:
            KenyanShilling: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='KES',
            symbol='Sh',
            code='404',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class SomaliShilling(Currency):
    """Somali Shilling currency representation.

    Simple usage example:

        >>> from multicurrency import SomaliShilling
        >>> somali_shilling = SomaliShilling(amount=1)
        >>> print(somali_shilling)
        Sh1,00

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
            **other) -> 'SomaliShilling':
        """Class creator.

        Returns:
            SomaliShilling: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='SOS',
            symbol='Sh',
            code='706',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class TanzanianShilling(Currency):
    """Tanzanian Shilling currency representation.

    Simple usage example:

        >>> from multicurrency import TanzanianShilling
        >>> tanzanian_shilling = TanzanianShilling(amount=1)
        >>> print(tanzanian_shilling)
        Sh1.00

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
            **other) -> 'TanzanianShilling':
        """Class creator.

        Returns:
            TanzanianShilling: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='TZS',
            symbol='Sh',
            code='834',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class UgandaShilling(Currency):
    """Uganda Shilling currency representation.

    Simple usage example:

        >>> from multicurrency import UgandaShilling
        >>> uganda_shilling = UgandaShilling(amount=1)
        >>> print(uganda_shilling)
        Sh1

    For more details see `multicurrency.currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 0,
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
            decimal_places: int = 0,
            decimal_sign: Optional[str] = ',',
            grouping_sign: Optional[str] = '.',
            international: bool = False,
            **other) -> 'UgandaShilling':
        """Class creator.

        Returns:
            UgandaShilling: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='UGX',
            symbol='Sh',
            code='800',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)
