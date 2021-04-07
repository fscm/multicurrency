# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Pound currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union
from .currency import Currency


class EgyptianPound(Currency):
    """Egyptian Pound currency representation.

    Simple usage example:

        >>> from multicurrency import EgyptianPound
        >>> egyptian_pound = EgyptianPound(amount=1)
        >>> print(egyptian_pound)
        £1.00

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
            **other) -> 'EgyptianPound':
        """Class creator.

        Returns:
            EgyptianPound: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='EGP',
            symbol='£',
            code='818',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class FalklandIslandsPound(Currency):
    """Falkland Islands Pound currency representation.

    Simple usage example:

        >>> from multicurrency import FalklandIslandsPound
        >>> falkland_islands_pound = FalklandIslandsPound(amount=1)
        >>> print(falkland_islands_pound)
        £1,00

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
            **other) -> 'FalklandIslandsPound':
        """Class creator.

        Returns:
            FalklandIslandsPound: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='FKP',
            symbol='£',
            code='238',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class PoundSterling(Currency):
    """Pound Sterling currency representation.

    Simple usage example:

        >>> from multicurrency import PoundSterling
        >>> pound_sterling = PoundSterling(amount=1)
        >>> print(pound_sterling)
        £1.00

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
            **other) -> 'PoundSterling':
        """Class creator.

        Returns:
            PoundSterling: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='GBP',
            symbol='£',
            code='826',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class GibraltarPound(Currency):
    """Gibraltar Pound currency representation.

    Simple usage example:

        >>> from multicurrency import GibraltarPound
        >>> gibraltar_pound = GibraltarPound(amount=1)
        >>> print(gibraltar_pound)
        £1,00

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
            **other) -> 'GibraltarPound':
        """Class creator.

        Returns:
            GibraltarPound: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='GIP',
            symbol='£',
            code='292',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class LebanesePound(Currency):
    """Lebanese Pound currency representation.

    Simple usage example:

        >>> from multicurrency import LebanesePound
        >>> lebanese_pound = LebanesePound(amount=1)
        >>> print(lebanese_pound)
        ل.ل1

    For more details see `multicurrency.currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 0,
        decimal_sign (str, optional): Decimal symbol. Defaults to '.'.
        grouping_sign (str, optional): Grouping symbol. Defaults to ' '.
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
            grouping_sign: Optional[str] = ' ',
            international: bool = False,
            **other) -> 'LebanesePound':
        """Class creator.

        Returns:
            LebanesePound: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='LBP',
            symbol='ل.ل',
            code='422',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class SudanesePound(Currency):
    """Sudanese Pound currency representation.

    Simple usage example:

        >>> from multicurrency import SudanesePound
        >>> sudanese_pound = SudanesePound(amount=1)
        >>> print(sudanese_pound)
        £1,00

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
            **other) -> 'SudanesePound':
        """Class creator.

        Returns:
            SudanesePound: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='SDG',
            symbol='£',
            code='938',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class SaintHelenaPound(Currency):
    """Saint Helena Pound currency representation.

    Simple usage example:

        >>> from multicurrency import SaintHelenaPound
        >>> saint_helena_pound = SaintHelenaPound(amount=1)
        >>> print(saint_helena_pound)
        £1,00

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
            **other) -> 'SaintHelenaPound':
        """Class creator.

        Returns:
            SaintHelenaPound: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='SHP',
            symbol='£',
            code='654',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class SyrianPound(Currency):
    """Syrian Pound currency representation.

    Simple usage example:

        >>> from multicurrency import SyrianPound
        >>> syrian_pound = SyrianPound(amount=1)
        >>> print(syrian_pound)
        ل.س1,00

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
            **other) -> 'SyrianPound':
        """Class creator.

        Returns:
            SyrianPound: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='SYP',
            symbol='ل.س',
            code='760',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)
