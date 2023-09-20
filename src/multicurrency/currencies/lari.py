# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Lari currency representation(s)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, cast

from multicurrency.pycurrency import Currency


if TYPE_CHECKING:
    from decimal import Decimal


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
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2,\u202F3%a\u00A0%s',
    ) -> Self:
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
            self: Self,
            amount: str | float | Decimal,
    ) -> Self:
        """Recreates self with a different `amount`.

        Args:
            amount (str | int | float | Decimal): Represented value.

        Returns:
            Lari: new opbject.
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
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2,\u202F3%a\u00A0%s',
    ) -> Self:
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
            self: Self,
            amount: str | float | Decimal,
    ) -> Self:
        """Recreates self with a different `amount`.

        Args:
            amount (str | int | float | Decimal): Represented value.

        Returns:
            GeorgiaLari: new opbject.
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
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2,\u202F3%a\u00A0%s',
    ) -> Self:
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
            self: Self,
            amount: str | float | Decimal,
    ) -> Self:
        """Recreates self with a different `amount`.

        Args:
            amount (str | int | float | Decimal): Represented value.

        Returns:
            SouthOssetiaLari: new opbject.
        """
        return self.__class__(amount, self._info[5])
