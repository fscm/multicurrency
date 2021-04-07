# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Peso currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union
from .currency import Currency


class ArgentinePeso(Currency):
    """Argentine Peso currency representation.

    Simple usage example:

        >>> from multicurrency import ArgentinePeso
        >>> argentine_peso = ArgentinePeso(amount=1)
        >>> print(argentine_peso)
        $1,00

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
            **other) -> 'ArgentinePeso':
        """Class creator.

        Returns:
            ArgentinePeso: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='ARS',
            symbol='$',
            code='032',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class ChileanPeso(Currency):
    """Chilean Peso currency representation.

    Simple usage example:

        >>> from multicurrency import ChileanPeso
        >>> chilean_peso = ChileanPeso(amount=1)
        >>> print(chilean_peso)
        $1

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
            **other) -> 'ChileanPeso':
        """Class creator.

        Returns:
            ChileanPeso: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='CLP',
            symbol='$',
            code='152',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class ColombianPeso(Currency):
    """Colombian Peso currency representation.

    Simple usage example:

        >>> from multicurrency import ColombianPeso
        >>> colombian_peso = ColombianPeso(amount=1)
        >>> print(colombian_peso)
        $1,00

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
            **other) -> 'ColombianPeso':
        """Class creator.

        Returns:
            ColombianPeso: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='COP',
            symbol='$',
            code='170',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class CubanPeso(Currency):
    """Cuban Peso currency representation.

    Simple usage example:

        >>> from multicurrency import CubanPeso
        >>> cuban_peso = CubanPeso(amount=1)
        >>> print(cuban_peso)
        $1.00

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
            **other) -> 'CubanPeso':
        """Class creator.

        Returns:
            CubanPeso: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='CUP',
            symbol='$',
            code='192',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class DominicanPeso(Currency):
    """Dominican Peso currency representation.

    Simple usage example:

        >>> from multicurrency import DominicanPeso
        >>> dominican_peso = DominicanPeso(amount=1)
        >>> print(dominican_peso)
        $1.00

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
            **other) -> 'DominicanPeso':
        """Class creator.

        Returns:
            DominicanPeso: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='DOP',
            symbol='$',
            code='214',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class MexicanPeso(Currency):
    """Mexican Peso currency representation.

    Simple usage example:

        >>> from multicurrency import MexicanPeso
        >>> mexican_peso = MexicanPeso(amount=1)
        >>> print(mexican_peso)
        $1.00

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
            **other) -> 'MexicanPeso':
        """Class creator.

        Returns:
            MexicanPeso: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='MXN',
            symbol='$',
            code='484',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class PhilippinePeso(Currency):
    """Philippine Peso currency representation.

    Simple usage example:

        >>> from multicurrency import PhilippinePeso
        >>> philippine_peso = PhilippinePeso(amount=1)
        >>> print(philippine_peso)
        ₱1.00

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
            **other) -> 'PhilippinePeso':
        """Class creator.

        Returns:
            PhilippinePeso: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='PHP',
            symbol='₱',
            code='608',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class PesoUruguayo(Currency):
    """Peso Uruguayo currency representation.

    Simple usage example:

        >>> from multicurrency import PesoUruguayo
        >>> peso_uruguayo = PesoUruguayo(amount=1)
        >>> print(peso_uruguayo)
        $1,00

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
            **other) -> 'PesoUruguayo':
        """Class creator.

        Returns:
            PesoUruguayo: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            currency='UYU',
            symbol='$',
            code='858',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)
