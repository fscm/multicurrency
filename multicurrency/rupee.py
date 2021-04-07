# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Rupee currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union
from .currency import Currency


class IndianRupee(Currency):
    """Indian Rupee currency representation.

    Simple usage example:

        >>> from multicurrency import IndianRupee
        >>> indian_rupee = IndianRupee(amount=1)
        >>> print(indian_rupee)
        ₹1.00

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
            **other) -> 'IndianRupee':
        """Class creator.

        Returns:
            IndianRupee: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='INR',
            symbol='₹',
            code='356',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class SriLankaRupee(Currency):
    """Sri Lanka Rupee currency representation.

    Simple usage example:

        >>> from multicurrency import SriLankaRupee
        >>> sri_lanka_rupee = SriLankaRupee(amount=1)
        >>> print(sri_lanka_rupee)
        Rs1,00

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
            **other) -> 'SriLankaRupee':
        """Class creator.

        Returns:
            SriLankaRupee: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='LKR',
            symbol='Rs',
            code='144',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class MauritiusRupee(Currency):
    """Mauritius Rupee currency representation.

    Simple usage example:

        >>> from multicurrency import MauritiusRupee
        >>> mauritius_rupee = MauritiusRupee(amount=1)
        >>> print(mauritius_rupee)
        ₨1.00

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
            **other) -> 'MauritiusRupee':
        """Class creator.

        Returns:
            MauritiusRupee: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='MUR',
            symbol='₨',
            code='480',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class NepaleseRupee(Currency):
    """Nepalese Rupee currency representation.

    Simple usage example:

        >>> from multicurrency import NepaleseRupee
        >>> nepalese_rupee = NepaleseRupee(amount=1)
        >>> print(nepalese_rupee)
        ₨1.00

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
            **other) -> 'NepaleseRupee':
        """Class creator.

        Returns:
            NepaleseRupee: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='NPR',
            symbol='₨',
            code='524',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class PakistanRupee(Currency):
    """Pakistan Rupee currency representation.

    Simple usage example:

        >>> from multicurrency import PakistanRupee
        >>> pakistan_rupee = PakistanRupee(amount=1)
        >>> print(pakistan_rupee)
        ₨1.00

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
            **other) -> 'PakistanRupee':
        """Class creator.

        Returns:
            PakistanRupee: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='PKR',
            symbol='₨',
            code='586',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class SeychellesRupee(Currency):
    """Seychelles Rupee currency representation.

    Simple usage example:

        >>> from multicurrency import SeychellesRupee
        >>> seychelles_rupee = SeychellesRupee(amount=1)
        >>> print(seychelles_rupee)
        ₨1,00

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
            **other) -> 'SeychellesRupee':
        """Class creator.

        Returns:
            SeychellesRupee: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='SCR',
            symbol='₨',
            code='690',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)
