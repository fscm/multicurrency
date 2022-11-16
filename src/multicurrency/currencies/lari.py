# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Lari currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class Lari(Currency):
    """Lari currency representation.

    Simple usage example:

        >>> from multicurrency import Lari
        >>> lari = Lari(
        ...     amount='123456.789')
        >>> print(lari)
        123 456,79 ლ

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2,\u202F3%a\u00A0%s'
    ) -> 'Lari':
        """Class creator.

        Returns:
            Lari: new `Lari` object.
        """
        return cast(
            Lari,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='GEL',
                numeric_code='981',
                symbol='ლ',
                localized_symbol='GEლ',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'Lari':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class GeorgiaLari(Currency):
    """Lari (Georgia) currency representation.

    Simple usage example:

        >>> from multicurrency import GeorgiaLari
        >>> georgia_lari = GeorgiaLari(
        ...     amount='123456.789')
        >>> print(georgia_lari)
        123 456,79 ლ

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2,\u202F3%a\u00A0%s'
    ) -> 'GeorgiaLari':
        """Class creator.

        Returns:
            GeorgiaLari: new `GeorgiaLari` object.
        """
        return cast(
            GeorgiaLari,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='GEL',
                numeric_code='981',
                symbol='ლ',
                localized_symbol='GEლ',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'GeorgiaLari':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class SouthOssetiaLari(Currency):
    """Lari (South Ossetia) currency representation.

    Simple usage example:

        >>> from multicurrency import SouthOssetiaLari
        >>> south_ossetia_lari = SouthOssetiaLari(
        ...     amount='123456.789')
        >>> print(south_ossetia_lari)
        123 456,79 ლ

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2,\u202F3%a\u00A0%s'
    ) -> 'SouthOssetiaLari':
        """Class creator.

        Returns:
            SouthOssetiaLari: new `SouthOssetiaLari` object.
        """
        return cast(
            SouthOssetiaLari,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='GEL',
                numeric_code='981',
                symbol='ლ',
                localized_symbol='GEლ',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'SouthOssetiaLari':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
