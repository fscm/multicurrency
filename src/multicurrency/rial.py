# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Rial currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union
from ._currency import Currency


class IranianRial(Currency):
    """Iranian Rial currency representation.

    Simple usage example:

        >>> from multicurrency import IranianRial
        >>> iranian_rial = IranianRial(
        ...     amount=123456.789)
        >>> print(iranian_rial)
        ۱۲۳٬۴۵۶٫۷۹ ﷼

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
            alpha_code='IRR',
            numeric_code='364',
            symbol='﷼',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='﷼',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
            grouping_sign=grouping_sign,
            convertion='۰۱۲۳۴۵۶۷۸۹-',
            international=international)


class RialOmani(Currency):
    """Rial Omani currency representation.

    Simple usage example:

        >>> from multicurrency import RialOmani
        >>> rial_omani = RialOmani(
        ...     amount=123456.789)
        >>> print(rial_omani)
        ر.ع. ١٢٣٬٤٥٦٫٧٨٩

    For more details see `multicurrency._currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 3,
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
            decimal_places: Optional[int] = 3,
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
            alpha_code='OMR',
            numeric_code='512',
            symbol='ر.ع.',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='ر.ع.',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
            grouping_sign=grouping_sign,
            convertion='٠١٢٣٤٥٦٧٨٩-',
            international=international)


class QatariRial(Currency):
    """Qatari Rial currency representation.

    Simple usage example:

        >>> from multicurrency import QatariRial
        >>> qatari_rial = QatariRial(
        ...     amount=123456.789)
        >>> print(qatari_rial)
        ر.ق. ١٢٣٬٤٥٦٫٧٩

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
            alpha_code='QAR',
            numeric_code='634',
            symbol='ر.ق.',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='ر.ق.',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
            grouping_sign=grouping_sign,
            convertion='٠١٢٣٤٥٦٧٨٩-',
            international=international)


class YemeniRial(Currency):
    """Yemeni Rial currency representation.

    Simple usage example:

        >>> from multicurrency import YemeniRial
        >>> yemeni_rial = YemeniRial(
        ...     amount=123456.789)
        >>> print(yemeni_rial)
        ١٢٣٬٤٥٦٫٧٩ ﷼

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
            alpha_code='YER',
            numeric_code='886',
            symbol='﷼',
            symbol_separator=symbol_separator,
            symbol_ahead=symbol_ahead,
            localized_symbol='﷼',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_places=grouping_places,
            grouping_sign=grouping_sign,
            convertion='٠١٢٣٤٥٦٧٨٩-',
            international=international)
