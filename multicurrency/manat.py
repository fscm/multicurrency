# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Manat currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union
from .currency import Currency


class AzerbaijanianManat(Currency):
    """Azerbaijanian Manat currency representation.

    Simple usage example:

        >>> from multicurrency import AzerbaijanianManat
        >>> azerbaijanian_manat = AzerbaijanianManat(amount=1)
        >>> print(azerbaijanian_manat)
        ман1,00

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
            **other) -> 'AzerbaijanianManat':
        """Class creator.

        Returns:
            AzerbaijanianManat: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='AZN',
            symbol='ман',
            code='944',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class Manat(Currency):
    """Manat currency representation.

    Simple usage example:

        >>> from multicurrency import Manat
        >>> manat = Manat(amount=1)
        >>> print(manat)
        m1,00

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
            **other) -> 'Manat':
        """Class creator.

        Returns:
            Manat: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='TMT',
            symbol='m',
            code='934',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)
