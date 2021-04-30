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
        >>> kenyan_shilling = KenyanShilling(
        ...     amount=123456.789)
        >>> print(kenyan_shilling)
        Ksh 123,456.79

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
        symbol_separator (str, optional): Separation between the symbol
            and the value. Defaults to ' '.
        symbol_ahead (bool, optional): True if symbol goes ahead of the
            value. False otherwise. Defaults to True.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: Optional[int] = 2,
            decimal_sign: Optional[str] = '.',
            grouping_sign: Optional[str] = ',',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '\u00A0',
            **other) -> 'KenyanShilling':
        """Class creator.

        Returns:
            KenyanShilling: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='KES',
            numeric_code='404',
            symbol='Ksh',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)


class SomaliShilling(Currency):
    """Somali Shilling currency representation.

    Simple usage example:

        >>> from multicurrency import SomaliShilling
        >>> somali_shilling = SomaliShilling(
        ...     amount=123456.789)
        >>> print(somali_shilling)
        Sh 123,456.79

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
        symbol_separator (str, optional): Separation between the symbol
            and the value. Defaults to ' '.
        symbol_ahead (bool, optional): True if symbol goes ahead of the
            value. False otherwise. Defaults to True.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: Optional[int] = 2,
            decimal_sign: Optional[str] = '.',
            grouping_sign: Optional[str] = ',',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '\u00A0',
            **other) -> 'SomaliShilling':
        """Class creator.

        Returns:
            SomaliShilling: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='SOS',
            numeric_code='706',
            symbol='Sh',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)


class TanzanianShilling(Currency):
    """Tanzanian Shilling currency representation.

    Simple usage example:

        >>> from multicurrency import TanzanianShilling
        >>> tanzanian_shilling = TanzanianShilling(
        ...     amount=123456.789)
        >>> print(tanzanian_shilling)
        TSh 123,456.79

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
        symbol_separator (str, optional): Separation between the symbol
            and the value. Defaults to ' '.
        symbol_ahead (bool, optional): True if symbol goes ahead of the
            value. False otherwise. Defaults to True.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: Optional[int] = 2,
            decimal_sign: Optional[str] = '.',
            grouping_sign: Optional[str] = ',',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '\u00A0',
            **other) -> 'TanzanianShilling':
        """Class creator.

        Returns:
            TanzanianShilling: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='TZS',
            numeric_code='834',
            symbol='TSh',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)


class UgandaShilling(Currency):
    """Uganda Shilling currency representation.

    Simple usage example:

        >>> from multicurrency import UgandaShilling
        >>> uganda_shilling = UgandaShilling(
        ...     amount=123456.789)
        >>> print(uganda_shilling)
        USh 123,457

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
        symbol_separator (str, optional): Separation between the symbol
            and the value. Defaults to ' '.
        symbol_ahead (bool, optional): True if symbol goes ahead of the
            value. False otherwise. Defaults to True.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: Optional[int] = 0,
            decimal_sign: Optional[str] = '.',
            grouping_sign: Optional[str] = ',',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '\u00A0',
            **other) -> 'UgandaShilling':
        """Class creator.

        Returns:
            UgandaShilling: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='UGX',
            numeric_code='800',
            symbol='USh',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)
