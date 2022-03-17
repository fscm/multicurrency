# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Pound currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union
from ._currency import Currency


class EgyptianPound(Currency):
    """Egyptian Pound currency representation.

    Simple usage example:

        >>> from multicurrency import EgyptianPound
        >>> egyptian_pound = EgyptianPound(
        ...     amount=123456.789)
        >>> print(egyptian_pound)
        ج.م. ١٢٣٬٤٥٦٫٧٩

    For more details see `multicurrency._currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 2,
        decimal_sign (str, optional): Decimal symbol. Defaults to '٫'.
        grouping_places (int, optional): Number of digits for grouping.
            Defaults to 3,
        grouping_sign (str, optional): Grouping symbol. Defaults to '٬'.
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
            decimal_sign: Optional[str] = '\u066B',
            grouping_places: Optional[int] = 3,
            grouping_sign: Optional[str] = '\u066C',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '\u00A0',
            **other) -> Currency:
        """Class creator.

        Returns:
            Currency: new `Currency` object.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='EGP',
            numeric_code='818',
            symbol='ج.م.',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='ج.م.',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
            grouping_sign=grouping_sign,
            convertion='٠١٢٣٤٥٦٧٨٩-',
            international=international)


class FalklandIslandsPound(Currency):
    """Falkland Islands Pound currency representation.

    Simple usage example:

        >>> from multicurrency import FalklandIslandsPound
        >>> falkland_islands_pound = FalklandIslandsPound(
        ...     amount=123456.789)
        >>> print(falkland_islands_pound)
        £123,456.79

    For more details see `multicurrency._currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 2,
        decimal_sign (str, optional): Decimal symbol. Defaults to '.'.
        grouping_places (int, optional): Number of digits for grouping.
            Defaults to 3,
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
            decimal_places: Optional[int] = 2,
            decimal_sign: Optional[str] = '.',
            grouping_places: Optional[int] = 3,
            grouping_sign: Optional[str] = ',',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '',
            **other) -> Currency:
        """Class creator.

        Returns:
            Currency: new `Currency` object.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='FKP',
            numeric_code='238',
            symbol='£',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='FK£',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)


class PoundSterling(Currency):
    """Pound Sterling currency representation.

    Simple usage example:

        >>> from multicurrency import PoundSterling
        >>> pound_sterling = PoundSterling(
        ...     amount=123456.789)
        >>> print(pound_sterling)
        £123,456.79

    For more details see `multicurrency._currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 2,
        decimal_sign (str, optional): Decimal symbol. Defaults to '.'.
        grouping_places (int, optional): Number of digits for grouping.
            Defaults to 3,
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
            decimal_places: Optional[int] = 2,
            decimal_sign: Optional[str] = '.',
            grouping_places: Optional[int] = 3,
            grouping_sign: Optional[str] = ',',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '',
            **other) -> Currency:
        """Class creator.

        Returns:
            Currency: new `Currency` object.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='GBP',
            numeric_code='826',
            symbol='£',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='£',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)


class PoundSterlingGG(Currency):
    """Pound Sterling GG currency representation.

    Simple usage example:

        >>> from multicurrency import PoundSterlingGG
        >>> pound_sterling_gg = PoundSterlingGG(
        ...     amount=123456.789)
        >>> print(pound_sterling_gg)
        £123,456.79

    For more details see `multicurrency._currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 2,
        decimal_sign (str, optional): Decimal symbol. Defaults to '.'.
        grouping_places (int, optional): Number of digits for grouping.
            Defaults to 3,
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
            decimal_places: Optional[int] = 2,
            decimal_sign: Optional[str] = '.',
            grouping_places: Optional[int] = 3,
            grouping_sign: Optional[str] = ',',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '',
            **other) -> Currency:
        """Class creator.

        Returns:
            Currency: new `Currency` object.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='GBP',
            numeric_code='826',
            symbol='£',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='GG£',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)


class PoundSterlingIO(Currency):
    """Pound Sterling IO currency representation.

    Simple usage example:

        >>> from multicurrency import PoundSterlingIO
        >>> pound_sterling_io = PoundSterlingIO(
        ...     amount=123456.789)
        >>> print(pound_sterling_io)
        £123,456.79

    For more details see `multicurrency._currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 2,
        decimal_sign (str, optional): Decimal symbol. Defaults to '.'.
        grouping_places (int, optional): Number of digits for grouping.
            Defaults to 3,
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
            decimal_places: Optional[int] = 2,
            decimal_sign: Optional[str] = '.',
            grouping_places: Optional[int] = 3,
            grouping_sign: Optional[str] = ',',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '',
            **other) -> Currency:
        """Class creator.

        Returns:
            Currency: new `Currency` object.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='GBP',
            numeric_code='826',
            symbol='£',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='IO£',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)


class PoundSterlingGB(Currency):
    """Pound Sterling GB currency representation.

    Simple usage example:

        >>> from multicurrency import PoundSterlingGB
        >>> pound_sterling_gb = PoundSterlingGB(
        ...     amount=123456.789)
        >>> print(pound_sterling_gb)
        £123,456.79

    For more details see `multicurrency._currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 2,
        decimal_sign (str, optional): Decimal symbol. Defaults to '.'.
        grouping_places (int, optional): Number of digits for grouping.
            Defaults to 3,
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
            decimal_places: Optional[int] = 2,
            decimal_sign: Optional[str] = '.',
            grouping_places: Optional[int] = 3,
            grouping_sign: Optional[str] = ',',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '',
            **other) -> Currency:
        """Class creator.

        Returns:
            Currency: new `Currency` object.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='GBP',
            numeric_code='826',
            symbol='£',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='GB£',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)


class PoundSterlingIM(Currency):
    """Pound Sterling IM currency representation.

    Simple usage example:

        >>> from multicurrency import PoundSterlingIM
        >>> pound_sterling_im = PoundSterlingIM(
        ...     amount=123456.789)
        >>> print(pound_sterling_im)
        £123,456.79

    For more details see `multicurrency._currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 2,
        decimal_sign (str, optional): Decimal symbol. Defaults to '.'.
        grouping_places (int, optional): Number of digits for grouping.
            Defaults to 3,
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
            decimal_places: Optional[int] = 2,
            decimal_sign: Optional[str] = '.',
            grouping_places: Optional[int] = 3,
            grouping_sign: Optional[str] = ',',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '',
            **other) -> Currency:
        """Class creator.

        Returns:
            Currency: new `Currency` object.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='GBP',
            numeric_code='826',
            symbol='£',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='IM£',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)


class GibraltarPound(Currency):
    """Gibraltar Pound currency representation.

    Simple usage example:

        >>> from multicurrency import GibraltarPound
        >>> gibraltar_pound = GibraltarPound(
        ...     amount=123456.789)
        >>> print(gibraltar_pound)
        £123,456.79

    For more details see `multicurrency._currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 2,
        decimal_sign (str, optional): Decimal symbol. Defaults to '.'.
        grouping_places (int, optional): Number of digits for grouping.
            Defaults to 3,
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
            decimal_places: Optional[int] = 2,
            decimal_sign: Optional[str] = '.',
            grouping_places: Optional[int] = 3,
            grouping_sign: Optional[str] = ',',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '',
            **other) -> Currency:
        """Class creator.

        Returns:
            Currency: new `Currency` object.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='GIP',
            numeric_code='292',
            symbol='£',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='GI£',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)


class LebanesePound(Currency):
    """Lebanese Pound currency representation.

    Simple usage example:

        >>> from multicurrency import LebanesePound
        >>> lebanese_pound = LebanesePound(
        ...     amount=123456.789)
        >>> print(lebanese_pound)
        ل.ل. ١٢٣٬٤٥٧

    For more details see `multicurrency._currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 0,
        decimal_sign (str, optional): Decimal symbol. Defaults to '٫'.
        grouping_places (int, optional): Number of digits for grouping.
            Defaults to 3,
        grouping_sign (str, optional): Grouping symbol. Defaults to '٬'.
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
            decimal_sign: Optional[str] = '\u066B',
            grouping_places: Optional[int] = 3,
            grouping_sign: Optional[str] = '\u066C',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '\u00A0',
            **other) -> Currency:
        """Class creator.

        Returns:
            Currency: new `Currency` object.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='LBP',
            numeric_code='422',
            symbol='ل.ل.',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='ل.ل.',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
            grouping_sign=grouping_sign,
            convertion='٠١٢٣٤٥٦٧٨٩-',
            international=international)


class SudanesePound(Currency):
    """Sudanese Pound currency representation.

    Simple usage example:

        >>> from multicurrency import SudanesePound
        >>> sudanese_pound = SudanesePound(
        ...     amount=123456.789)
        >>> print(sudanese_pound)
        ١٢٣٬٤٥٦٫٧٩ ج.س

    For more details see `multicurrency._currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 2,
        decimal_sign (str, optional): Decimal symbol. Defaults to '٫'.
        grouping_places (int, optional): Number of digits for grouping.
            Defaults to 3,
        grouping_sign (str, optional): Grouping symbol. Defaults to '٬'.
        international (bool, optional): Identifies the currency using
            the 'currency' value instead of the 'symbol'. Defaults to
            False.
        symbol_separator (str, optional): Separation between the symbol
            and the value. Defaults to ' '.
        symbol_ahead (bool, optional): True if symbol goes ahead of the
            value. False otherwise. Defaults to False.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: Optional[int] = 2,
            decimal_sign: Optional[str] = '\u066B',
            grouping_places: Optional[int] = 3,
            grouping_sign: Optional[str] = '\u066C',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = False,
            symbol_separator: Optional[str] = '\u00A0',
            **other) -> Currency:
        """Class creator.

        Returns:
            Currency: new `Currency` object.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='SDG',
            numeric_code='938',
            symbol='ج.س',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='ج.س',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
            grouping_sign=grouping_sign,
            convertion='٠١٢٣٤٥٦٧٨٩-',
            international=international)


class SaintHelenaPound(Currency):
    """Saint Helena Pound currency representation.

    Simple usage example:

        >>> from multicurrency import SaintHelenaPound
        >>> saint_helena_pound = SaintHelenaPound(
        ...     amount=123456.789)
        >>> print(saint_helena_pound)
        £123,456.79

    For more details see `multicurrency._currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 2,
        decimal_sign (str, optional): Decimal symbol. Defaults to '.'.
        grouping_places (int, optional): Number of digits for grouping.
            Defaults to 3,
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
            decimal_places: Optional[int] = 2,
            decimal_sign: Optional[str] = '.',
            grouping_places: Optional[int] = 3,
            grouping_sign: Optional[str] = ',',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = True,
            symbol_separator: Optional[str] = '',
            **other) -> Currency:
        """Class creator.

        Returns:
            Currency: new `Currency` object.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='SHP',
            numeric_code='654',
            symbol='£',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='SH£',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
            grouping_sign=grouping_sign,
            convertion='',
            international=international)


class SyrianPound(Currency):
    """Syrian Pound currency representation.

    Simple usage example:

        >>> from multicurrency import SyrianPound
        >>> syrian_pound = SyrianPound(
        ...     amount=123456.789)
        >>> print(syrian_pound)
        ١٢٣٬٤٥٦٫٧٩ ل.س

    For more details see `multicurrency._currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 2,
        decimal_sign (str, optional): Decimal symbol. Defaults to '٫'.
        grouping_places (int, optional): Number of digits for grouping.
            Defaults to 3,
        grouping_sign (str, optional): Grouping symbol. Defaults to '٬'.
        international (bool, optional): Identifies the currency using
            the 'currency' value instead of the 'symbol'. Defaults to
            False.
        symbol_separator (str, optional): Separation between the symbol
            and the value. Defaults to ' '.
        symbol_ahead (bool, optional): True if symbol goes ahead of the
            value. False otherwise. Defaults to False.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs,disable=unused-argument
            cls,
            amount: Union[int, float, Decimal],
            decimal_places: Optional[int] = 2,
            decimal_sign: Optional[str] = '\u066B',
            grouping_places: Optional[int] = 3,
            grouping_sign: Optional[str] = '\u066C',
            international: Optional[bool] = False,
            symbol_ahead: Optional[bool] = False,
            symbol_separator: Optional[str] = '\u00A0',
            **other) -> Currency:
        """Class creator.

        Returns:
            Currency: new `Currency` object.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='SYP',
            numeric_code='760',
            symbol='ل.س',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='ل.س',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
            grouping_sign=grouping_sign,
            convertion='٠١٢٣٤٥٦٧٨٩-',
            international=international)
