# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Crypto currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union
from .currency import Currency


class EOS(Currency):
    """EOS currency representation.

    Simple usage example:

        >>> from multicurrency import EOS
        >>> eos = EOS(
        ...     amount=123456.789)
        >>> print(eos)
        ε123,456.7890

    For more details see `multicurrency.currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 4,
        decimal_sign (str, optional): Decimal symbol. Defaults to '.'.
        grouping_sign (str, optional): Grouping symbol. Defaults to ','.
        international (bool, optional): Identifies the currency using
            the 'currency' value instead of the 'symbol'. Defaults to
            False.
        symbol_separator (str, optional): Separation between the symbol
            and the value. Defaults to ''.
        symbol_ahead (bool, optional): True if symbol goes ahead of the
            value. False otherwise. Defaults to True.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: Optional[int] = 4,
            decimal_sign: Optional[str] = '.',
            grouping_sign: Optional[str] = ',',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '',
            **other) -> 'EOS':
        """Class creator.

        Returns:
            EOS: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='EOS',
            numeric_code='0',
            symbol='ε',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)


class Bitcoin(Currency):
    """Bitcoin currency representation.

    Simple usage example:

        >>> from multicurrency import Bitcoin
        >>> bitcoin = Bitcoin(
        ...     amount=123456.789)
        >>> print(bitcoin)
        ₿123,456.78900000

    For more details see `multicurrency.currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 8,
        decimal_sign (str, optional): Decimal symbol. Defaults to '.'.
        grouping_sign (str, optional): Grouping symbol. Defaults to ','.
        international (bool, optional): Identifies the currency using
            the 'currency' value instead of the 'symbol'. Defaults to
            False.
        symbol_separator (str, optional): Separation between the symbol
            and the value. Defaults to ''.
        symbol_ahead (bool, optional): True if symbol goes ahead of the
            value. False otherwise. Defaults to True.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: Optional[int] = 8,
            decimal_sign: Optional[str] = '.',
            grouping_sign: Optional[str] = ',',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '',
            **other) -> 'Bitcoin':
        """Class creator.

        Returns:
            Bitcoin: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='XBT',
            numeric_code='0',
            symbol='₿',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)


class StellarLumens(Currency):
    """Stellar Lumens currency representation.

    Simple usage example:

        >>> from multicurrency import StellarLumens
        >>> stellar_lumens = StellarLumens(
        ...     amount=123456.789)
        >>> print(stellar_lumens)
        *123,456.78900

    For more details see `multicurrency.currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 5,
        decimal_sign (str, optional): Decimal symbol. Defaults to '.'.
        grouping_sign (str, optional): Grouping symbol. Defaults to ','.
        international (bool, optional): Identifies the currency using
            the 'currency' value instead of the 'symbol'. Defaults to
            False.
        symbol_separator (str, optional): Separation between the symbol
            and the value. Defaults to ''.
        symbol_ahead (bool, optional): True if symbol goes ahead of the
            value. False otherwise. Defaults to True.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: Optional[int] = 5,
            decimal_sign: Optional[str] = '.',
            grouping_sign: Optional[str] = ',',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '',
            **other) -> 'StellarLumens':
        """Class creator.

        Returns:
            StellarLumens: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='XLM',
            numeric_code='0',
            symbol='*',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)


class Monero(Currency):
    """Monero currency representation.

    Simple usage example:

        >>> from multicurrency import Monero
        >>> monero = Monero(
        ...     amount=123456.789)
        >>> print(monero)
        ɱ123,456.789000000000

    For more details see `multicurrency.currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 12,
        decimal_sign (str, optional): Decimal symbol. Defaults to '.'.
        grouping_sign (str, optional): Grouping symbol. Defaults to ','.
        international (bool, optional): Identifies the currency using
            the 'currency' value instead of the 'symbol'. Defaults to
            False.
        symbol_separator (str, optional): Separation between the symbol
            and the value. Defaults to ''.
        symbol_ahead (bool, optional): True if symbol goes ahead of the
            value. False otherwise. Defaults to True.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: Optional[int] = 12,
            decimal_sign: Optional[str] = '.',
            grouping_sign: Optional[str] = ',',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '',
            **other) -> 'Monero':
        """Class creator.

        Returns:
            Monero: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='XMR',
            numeric_code='0',
            symbol='ɱ',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)


class Ripple(Currency):
    """Ripple currency representation.

    Simple usage example:

        >>> from multicurrency import Ripple
        >>> ripple = Ripple(
        ...     amount=123456.789)
        >>> print(ripple)
        ✕123,456.789000

    For more details see `multicurrency.currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 6,
        decimal_sign (str, optional): Decimal symbol. Defaults to '.'.
        grouping_sign (str, optional): Grouping symbol. Defaults to ','.
        international (bool, optional): Identifies the currency using
            the 'currency' value instead of the 'symbol'. Defaults to
            False.
        symbol_separator (str, optional): Separation between the symbol
            and the value. Defaults to ''.
        symbol_ahead (bool, optional): True if symbol goes ahead of the
            value. False otherwise. Defaults to True.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: Optional[int] = 6,
            decimal_sign: Optional[str] = '.',
            grouping_sign: Optional[str] = ',',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '',
            **other) -> 'Ripple':
        """Class creator.

        Returns:
            Ripple: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='XRP',
            numeric_code='0',
            symbol='✕',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)


class Tezos(Currency):
    """Tezos currency representation.

    Simple usage example:

        >>> from multicurrency import Tezos
        >>> tezos = Tezos(
        ...     amount=123456.789)
        >>> print(tezos)
        ꜩ123,456.789000

    For more details see `multicurrency.currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 6,
        decimal_sign (str, optional): Decimal symbol. Defaults to '.'.
        grouping_sign (str, optional): Grouping symbol. Defaults to ','.
        international (bool, optional): Identifies the currency using
            the 'currency' value instead of the 'symbol'. Defaults to
            False.
        symbol_separator (str, optional): Separation between the symbol
            and the value. Defaults to ''.
        symbol_ahead (bool, optional): True if symbol goes ahead of the
            value. False otherwise. Defaults to True.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: Optional[int] = 6,
            decimal_sign: Optional[str] = '.',
            grouping_sign: Optional[str] = ',',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '',
            **other) -> 'Tezos':
        """Class creator.

        Returns:
            Tezos: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='XTZ',
            numeric_code='0',
            symbol='ꜩ',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)


class Zcash(Currency):
    """Zcash currency representation.

    Simple usage example:

        >>> from multicurrency import Zcash
        >>> zcash = Zcash(
        ...     amount=123456.789)
        >>> print(zcash)
        ⓩ123,456.78900000

    For more details see `multicurrency.currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 8,
        decimal_sign (str, optional): Decimal symbol. Defaults to '.'.
        grouping_sign (str, optional): Grouping symbol. Defaults to ','.
        international (bool, optional): Identifies the currency using
            the 'currency' value instead of the 'symbol'. Defaults to
            False.
        symbol_separator (str, optional): Separation between the symbol
            and the value. Defaults to ''.
        symbol_ahead (bool, optional): True if symbol goes ahead of the
            value. False otherwise. Defaults to True.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: Optional[int] = 8,
            decimal_sign: Optional[str] = '.',
            grouping_sign: Optional[str] = ',',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '',
            **other) -> 'Zcash':
        """Class creator.

        Returns:
            Zcash: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='ZEC',
            numeric_code='0',
            symbol='ⓩ',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)
