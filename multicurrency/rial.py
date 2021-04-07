# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Rial currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union
from .currency import Currency


class IranianRial(Currency):
    """Iranian Rial currency representation.

    Simple usage example:

        >>> from multicurrency import IranianRial
        >>> iranian_rial = IranianRial(amount=1)
        >>> print(iranian_rial)
        ﷼1.00

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
            **other) -> 'IranianRial':
        """Class creator.

        Returns:
            IranianRial: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='IRR',
            symbol='﷼',
            code='364',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class RialOmani(Currency):
    """Rial Omani currency representation.

    Simple usage example:

        >>> from multicurrency import RialOmani
        >>> rial_omani = RialOmani(amount=1)
        >>> print(rial_omani)
        ر.ع.1.000

    For more details see `multicurrency.currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 3,
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
            decimal_places: int = 3,
            decimal_sign: Optional[str] = '.',
            grouping_sign: Optional[str] = ',',
            international: bool = False,
            **other) -> 'RialOmani':
        """Class creator.

        Returns:
            RialOmani: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='OMR',
            symbol='ر.ع.',
            code='512',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class QatariRial(Currency):
    """Qatari Rial currency representation.

    Simple usage example:

        >>> from multicurrency import QatariRial
        >>> qatari_rial = QatariRial(amount=1)
        >>> print(qatari_rial)
        ر.ق1,00

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
            **other) -> 'QatariRial':
        """Class creator.

        Returns:
            QatariRial: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='QAR',
            symbol='ر.ق',
            code='634',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class YemeniRial(Currency):
    """Yemeni Rial currency representation.

    Simple usage example:

        >>> from multicurrency import YemeniRial
        >>> yemeni_rial = YemeniRial(amount=1)
        >>> print(yemeni_rial)
        ﷼1,00

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
            **other) -> 'YemeniRial':
        """Class creator.

        Returns:
            YemeniRial: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='YER',
            symbol='﷼',
            code='886',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)
