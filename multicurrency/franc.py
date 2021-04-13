# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Franc currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union
from .currency import Currency


class BurundiFranc(Currency):
    """Burundi Franc currency representation.

    Simple usage example:

        >>> from multicurrency import BurundiFranc
        >>> burundi_franc = BurundiFranc(amount=1)
        >>> print(burundi_franc)
        ₣1

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
            **other) -> 'BurundiFranc':
        """Class creator.

        Returns:
            BurundiFranc: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='BIF',
            numeric_code='108',
            symbol='₣',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class CongoleseFranc(Currency):
    """Congolese Franc currency representation.

    Simple usage example:

        >>> from multicurrency import CongoleseFranc
        >>> congolese_franc = CongoleseFranc(amount=1)
        >>> print(congolese_franc)
        ₣1,00

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
            **other) -> 'CongoleseFranc':
        """Class creator.

        Returns:
            CongoleseFranc: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='CDF',
            numeric_code='976',
            symbol='₣',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class SwissFranc(Currency):
    """Swiss Franc currency representation.

    Simple usage example:

        >>> from multicurrency import SwissFranc
        >>> swiss_franc = SwissFranc(amount=1)
        >>> print(swiss_franc)
        ₣1.00

    For more details see `multicurrency.currency.Currency` .

    Args:
        amount (Union[int, float, Decimal]): Represented value.
        decimal_places (int, optional): Number of decimal places for the
            currency representation. Defaults to 2,
        decimal_sign (str, optional): Decimal symbol. Defaults to '.'.
        grouping_sign (str, optional): Grouping symbol. Defaults to '''.
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
            grouping_sign: Optional[str] = '\'',
            international: bool = False,
            **other) -> 'SwissFranc':
        """Class creator.

        Returns:
            SwissFranc: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='CHF',
            numeric_code='756',
            symbol='₣',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class DjiboutiFranc(Currency):
    """Djibouti Franc currency representation.

    Simple usage example:

        >>> from multicurrency import DjiboutiFranc
        >>> djibouti_franc = DjiboutiFranc(amount=1)
        >>> print(djibouti_franc)
        ₣1

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
            **other) -> 'DjiboutiFranc':
        """Class creator.

        Returns:
            DjiboutiFranc: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='DJF',
            numeric_code='262',
            symbol='₣',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class GuineaFranc(Currency):
    """Guinea Franc currency representation.

    Simple usage example:

        >>> from multicurrency import GuineaFranc
        >>> guinea_franc = GuineaFranc(amount=1)
        >>> print(guinea_franc)
        ₣1

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
            **other) -> 'GuineaFranc':
        """Class creator.

        Returns:
            GuineaFranc: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='GNF',
            numeric_code='324',
            symbol='₣',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class RwandaFranc(Currency):
    """Rwanda Franc currency representation.

    Simple usage example:

        >>> from multicurrency import RwandaFranc
        >>> rwanda_franc = RwandaFranc(amount=1)
        >>> print(rwanda_franc)
        ₣1

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
            **other) -> 'RwandaFranc':
        """Class creator.

        Returns:
            RwandaFranc: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='RWF',
            numeric_code='646',
            symbol='₣',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class CFAFrancBCEAO(Currency):
    """CFA Franc BCEAO currency representation.

    Simple usage example:

        >>> from multicurrency import CFAFrancBCEAO
        >>> cfa_franc_bceao = CFAFrancBCEAO(amount=1)
        >>> print(cfa_franc_bceao)
        ₣1

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
            **other) -> 'CFAFrancBCEAO':
        """Class creator.

        Returns:
            CFAFrancBCEAO: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='XOF',
            numeric_code='952',
            symbol='₣',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class CFAFrancBEAC(Currency):
    """CFA Franc BEAC currency representation.

    Simple usage example:

        >>> from multicurrency import CFAFrancBEAC
        >>> cfa_franc_beac = CFAFrancBEAC(amount=1)
        >>> print(cfa_franc_beac)
        ₣1

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
            **other) -> 'CFAFrancBEAC':
        """Class creator.

        Returns:
            CFAFrancBEAC: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='XAF',
            numeric_code='950',
            symbol='₣',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class CFPFranc(Currency):
    """CFP Franc currency representation.

    Simple usage example:

        >>> from multicurrency import CFPFranc
        >>> cfp_franc = CFPFranc(amount=1)
        >>> print(cfp_franc)
        ₣1

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
            **other) -> 'CFPFranc':
        """Class creator.

        Returns:
            CFPFranc: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='XPF',
            numeric_code='953',
            symbol='₣',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)
