# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Shilling currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class KenyanShilling(Currency):
    """Shilling (Kenya) currency representation.

    Simple usage example:

        >>> from multicurrency import KenyanShilling
        >>> kenyan_shilling = KenyanShilling(
        ...     amount='123456.789')
        >>> print(kenyan_shilling)
        Ksh 123,456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2.,3%s\u00A0%a'
    ) -> 'KenyanShilling':
        """Class creator.

        Returns:
            KenyanShilling: new `KenyanShilling` object.
        """
        return cast(
            KenyanShilling,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='KES',
                numeric_code='404',
                symbol='Ksh',
                localized_symbol='Ksh',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'KenyanShilling':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class SomaliShilling(Currency):
    """Shilling (Somalia) currency representation.

    Simple usage example:

        >>> from multicurrency import SomaliShilling
        >>> somali_shilling = SomaliShilling(
        ...     amount='123456.789')
        >>> print(somali_shilling)
        SSh 123,456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2.,3%s\u00A0%a'
    ) -> 'SomaliShilling':
        """Class creator.

        Returns:
            SomaliShilling: new `SomaliShilling` object.
        """
        return cast(
            SomaliShilling,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='SOS',
                numeric_code='706',
                symbol='SSh',
                localized_symbol='SSh',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'SomaliShilling':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class TanzanianShilling(Currency):
    """Shilling (Tanzania) currency representation.

    Simple usage example:

        >>> from multicurrency import TanzanianShilling
        >>> tanzanian_shilling = TanzanianShilling(
        ...     amount='123456.789')
        >>> print(tanzanian_shilling)
        TSh 123,456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2.,3%s\u00A0%a'
    ) -> 'TanzanianShilling':
        """Class creator.

        Returns:
            TanzanianShilling: new `TanzanianShilling` object.
        """
        return cast(
            TanzanianShilling,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='TZS',
                numeric_code='834',
                symbol='TSh',
                localized_symbol='TSh',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'TanzanianShilling':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class UgandaShilling(Currency):
    """Shilling (Uganda) currency representation.

    Simple usage example:

        >>> from multicurrency import UgandaShilling
        >>> uganda_shilling = UgandaShilling(
        ...     amount='123456.789')
        >>> print(uganda_shilling)
        USh 123,457

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0.,3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '0.,3%s\u00A0%a'
    ) -> 'UgandaShilling':
        """Class creator.

        Returns:
            UgandaShilling: new `UgandaShilling` object.
        """
        return cast(
            UgandaShilling,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='UGX',
                numeric_code='800',
                symbol='USh',
                localized_symbol='USh',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'UgandaShilling':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
