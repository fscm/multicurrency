# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Dollar currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union
from .currency import Currency


class AustralianDollar(Currency):
    """Australian Dollar currency representation.

    Simple usage example:

        >>> from multicurrency import AustralianDollar
        >>> australian_dollar = AustralianDollar(amount=1)
        >>> print(australian_dollar)
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
            **other) -> 'AustralianDollar':
        """Class creator.

        Returns:
            AustralianDollar: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='AUD',
            numeric_code='036',
            symbol='$',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class BarbadosDollar(Currency):
    """Barbados Dollar currency representation.

    Simple usage example:

        >>> from multicurrency import BarbadosDollar
        >>> barbados_dollar = BarbadosDollar(amount=1)
        >>> print(barbados_dollar)
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
            **other) -> 'BarbadosDollar':
        """Class creator.

        Returns:
            BarbadosDollar: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='BBD',
            numeric_code='052',
            symbol='$',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class BermudianDollar(Currency):
    """Bermudian Dollar currency representation.

    Simple usage example:

        >>> from multicurrency import BermudianDollar
        >>> bermudian_dollar = BermudianDollar(amount=1)
        >>> print(bermudian_dollar)
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
            **other) -> 'BermudianDollar':
        """Class creator.

        Returns:
            BermudianDollar: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='BMD',
            numeric_code='060',
            symbol='$',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class BruneiDollar(Currency):
    """Brunei Dollar currency representation.

    Simple usage example:

        >>> from multicurrency import BruneiDollar
        >>> brunei_dollar = BruneiDollar(amount=1)
        >>> print(brunei_dollar)
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
            **other) -> 'BruneiDollar':
        """Class creator.

        Returns:
            BruneiDollar: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='BND',
            numeric_code='096',
            symbol='$',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class BahamianDollar(Currency):
    """Bahamian Dollar currency representation.

    Simple usage example:

        >>> from multicurrency import BahamianDollar
        >>> bahamian_dollar = BahamianDollar(amount=1)
        >>> print(bahamian_dollar)
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
            **other) -> 'BahamianDollar':
        """Class creator.

        Returns:
            BahamianDollar: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='BSD',
            numeric_code='044',
            symbol='$',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class BelizeDollar(Currency):
    """Belize Dollar currency representation.

    Simple usage example:

        >>> from multicurrency import BelizeDollar
        >>> belize_dollar = BelizeDollar(amount=1)
        >>> print(belize_dollar)
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
            **other) -> 'BelizeDollar':
        """Class creator.

        Returns:
            BelizeDollar: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='BZD',
            numeric_code='084',
            symbol='$',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class CanadianDollarEN(Currency):
    """Canadian Dollar EN currency representation.

    Simple usage example:

        >>> from multicurrency import CanadianDollarEN
        >>> canadian_dollar_en = CanadianDollarEN(amount=1)
        >>> print(canadian_dollar_en)
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
            **other) -> 'CanadianDollarEN':
        """Class creator.

        Returns:
            CanadianDollarEN: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='CAD',
            numeric_code='124',
            symbol='$',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class CanadianDollarFR(Currency):
    """Canadian Dollar FR currency representation.

    Simple usage example:

        >>> from multicurrency import CanadianDollarFR
        >>> canadian_dollar_fr = CanadianDollarFR(amount=1)
        >>> print(canadian_dollar_fr)
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
            **other) -> 'CanadianDollarFR':
        """Class creator.

        Returns:
            CanadianDollarFR: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='CAD',
            numeric_code='124',
            symbol='$',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class FijiDollar(Currency):
    """Fiji Dollar currency representation.

    Simple usage example:

        >>> from multicurrency import FijiDollar
        >>> fiji_dollar = FijiDollar(amount=1)
        >>> print(fiji_dollar)
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
            **other) -> 'FijiDollar':
        """Class creator.

        Returns:
            FijiDollar: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='FJD',
            numeric_code='242',
            symbol='$',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class GuyanaDollar(Currency):
    """Guyana Dollar currency representation.

    Simple usage example:

        >>> from multicurrency import GuyanaDollar
        >>> guyana_dollar = GuyanaDollar(amount=1)
        >>> print(guyana_dollar)
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
            **other) -> 'GuyanaDollar':
        """Class creator.

        Returns:
            GuyanaDollar: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='GYD',
            numeric_code='328',
            symbol='$',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class HongKongDollar(Currency):
    """Hong Kong Dollar currency representation.

    Simple usage example:

        >>> from multicurrency import HongKongDollar
        >>> hong_kong_dollar = HongKongDollar(amount=1)
        >>> print(hong_kong_dollar)
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
            **other) -> 'HongKongDollar':
        """Class creator.

        Returns:
            HongKongDollar: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='HKD',
            numeric_code='344',
            symbol='$',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class JamaicanDollar(Currency):
    """Jamaican Dollar currency representation.

    Simple usage example:

        >>> from multicurrency import JamaicanDollar
        >>> jamaican_dollar = JamaicanDollar(amount=1)
        >>> print(jamaican_dollar)
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
            **other) -> 'JamaicanDollar':
        """Class creator.

        Returns:
            JamaicanDollar: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='JMD',
            numeric_code='388',
            symbol='$',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class CaymanIslandsDollar(Currency):
    """Cayman Islands Dollar currency representation.

    Simple usage example:

        >>> from multicurrency import CaymanIslandsDollar
        >>> cayman_islands_dollar = CaymanIslandsDollar(amount=1)
        >>> print(cayman_islands_dollar)
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
            **other) -> 'CaymanIslandsDollar':
        """Class creator.

        Returns:
            CaymanIslandsDollar: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='KYD',
            numeric_code='136',
            symbol='$',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class LiberianDollar(Currency):
    """Liberian Dollar currency representation.

    Simple usage example:

        >>> from multicurrency import LiberianDollar
        >>> liberian_dollar = LiberianDollar(amount=1)
        >>> print(liberian_dollar)
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
            **other) -> 'LiberianDollar':
        """Class creator.

        Returns:
            LiberianDollar: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='LRD',
            numeric_code='430',
            symbol='$',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class NamibiaDollar(Currency):
    """Namibia Dollar currency representation.

    Simple usage example:

        >>> from multicurrency import NamibiaDollar
        >>> namibia_dollar = NamibiaDollar(amount=1)
        >>> print(namibia_dollar)
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
            **other) -> 'NamibiaDollar':
        """Class creator.

        Returns:
            NamibiaDollar: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='NAD',
            numeric_code='516',
            symbol='$',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class NewZealandDollar(Currency):
    """New Zealand Dollar currency representation.

    Simple usage example:

        >>> from multicurrency import NewZealandDollar
        >>> new_zealand_dollar = NewZealandDollar(amount=1)
        >>> print(new_zealand_dollar)
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
            **other) -> 'NewZealandDollar':
        """Class creator.

        Returns:
            NewZealandDollar: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='NZD',
            numeric_code='554',
            symbol='$',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class SolomonIslandsDollar(Currency):
    """Solomon Islands Dollar currency representation.

    Simple usage example:

        >>> from multicurrency import SolomonIslandsDollar
        >>> solomon_islands_dollar = SolomonIslandsDollar(amount=1)
        >>> print(solomon_islands_dollar)
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
            **other) -> 'SolomonIslandsDollar':
        """Class creator.

        Returns:
            SolomonIslandsDollar: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='SBD',
            numeric_code='090',
            symbol='$',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class SingaporeDollar(Currency):
    """Singapore Dollar currency representation.

    Simple usage example:

        >>> from multicurrency import SingaporeDollar
        >>> singapore_dollar = SingaporeDollar(amount=1)
        >>> print(singapore_dollar)
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
            **other) -> 'SingaporeDollar':
        """Class creator.

        Returns:
            SingaporeDollar: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='SGD',
            numeric_code='702',
            symbol='$',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class SurinameDollar(Currency):
    """Suriname Dollar currency representation.

    Simple usage example:

        >>> from multicurrency import SurinameDollar
        >>> suriname_dollar = SurinameDollar(amount=1)
        >>> print(suriname_dollar)
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
            **other) -> 'SurinameDollar':
        """Class creator.

        Returns:
            SurinameDollar: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='SRD',
            numeric_code='968',
            symbol='$',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class TrinidadandTobagoDollar(Currency):
    """Trinidad and Tobago Dollar currency representation.

    Simple usage example:

        >>> from multicurrency import TrinidadandTobagoDollar
        >>> trinidad_and_tobago_dollar = TrinidadandTobagoDollar(amount=1)
        >>> print(trinidad_and_tobago_dollar)
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
            **other) -> 'TrinidadandTobagoDollar':
        """Class creator.

        Returns:
            TrinidadandTobagoDollar: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='TTD',
            numeric_code='780',
            symbol='$',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class TaiwanDollar(Currency):
    """Taiwan Dollar currency representation.

    Simple usage example:

        >>> from multicurrency import TaiwanDollar
        >>> taiwan_dollar = TaiwanDollar(amount=1)
        >>> print(taiwan_dollar)
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
            **other) -> 'TaiwanDollar':
        """Class creator.

        Returns:
            TaiwanDollar: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='TWD',
            numeric_code='901',
            symbol='$',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class USDollar(Currency):
    """US Dollar currency representation.

    Simple usage example:

        >>> from multicurrency import USDollar
        >>> us_dollar = USDollar(amount=1)
        >>> print(us_dollar)
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
            **other) -> 'USDollar':
        """Class creator.

        Returns:
            USDollar: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='USD',
            numeric_code='840',
            symbol='$',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class EastCaribbeanDollar(Currency):
    """East Caribbean Dollar currency representation.

    Simple usage example:

        >>> from multicurrency import EastCaribbeanDollar
        >>> east_caribbean_dollar = EastCaribbeanDollar(amount=1)
        >>> print(east_caribbean_dollar)
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
            **other) -> 'EastCaribbeanDollar':
        """Class creator.

        Returns:
            EastCaribbeanDollar: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='XCD',
            numeric_code='951',
            symbol='$',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)


class ZimbabweDollar(Currency):
    """Zimbabwe Dollar currency representation.

    Simple usage example:

        >>> from multicurrency import ZimbabweDollar
        >>> zimbabwe_dollar = ZimbabweDollar(amount=1)
        >>> print(zimbabwe_dollar)
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
            **other) -> 'ZimbabweDollar':
        """Class creator.

        Returns:
            ZimbabweDollar: new opbject.
        """
        return Currency.__new__(
            cls,
            amount=amount,
            alpha_code='ZWL',
            numeric_code='932',
            symbol='$',
            decimal_places=decimal_places,
            decimal_sign=decimal_sign,
            grouping_sign=grouping_sign,
            international=international)
