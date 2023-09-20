# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Lira currency representation(s)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, cast

from multicurrency.pycurrency import Currency


if TYPE_CHECKING:
    from decimal import Decimal


class TurkishLira(Currency):
    """Lira (Turkey) currency representation.

    Simple usage example:

        >>> from multicurrency import TurkishLira
        >>> turkish_lira = TurkishLira(
        ...     amount='123456.789')
        >>> print(turkish_lira)
        ₤123.456,79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2,.3%-%s%u'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2,.3%-%s%u',
    ) -> Self:
        """Class creator.

        Returns:
            TurkishLira: new `TurkishLira` object.
        """
        return cast(
            TurkishLira,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='TRY',
                numeric_code='949',
                symbol='₤',
                localized_symbol='₤',
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
            TurkishLira: new opbject.
        """
        return self.__class__(amount, self._info[5])


class TurkishLiraCY(Currency):
    """Lira (North Cyprus) currency representation.

    Simple usage example:

        >>> from multicurrency import TurkishLiraCY
        >>> turkish_lira_cy = TurkishLiraCY(
        ...     amount='123456.789')
        >>> print(turkish_lira_cy)
        ₤123.456,79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2,.3%-%s%u'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2,.3%-%s%u',
    ) -> Self:
        """Class creator.

        Returns:
            TurkishLiraCY: new `TurkishLiraCY` object.
        """
        return cast(
            TurkishLiraCY,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='TRY',
                numeric_code='949',
                symbol='₤',
                localized_symbol='CY₤',
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
            TurkishLiraCY: new opbject.
        """
        return self.__class__(amount, self._info[5])


class TurkishLiraTR(Currency):
    """Lira (Turkey) currency representation.

    Simple usage example:

        >>> from multicurrency import TurkishLiraTR
        >>> turkish_lira_tr = TurkishLiraTR(
        ...     amount='123456.789')
        >>> print(turkish_lira_tr)
        ₤123.456,79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2,.3%-%s%u'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2,.3%-%s%u',
    ) -> Self:
        """Class creator.

        Returns:
            TurkishLiraTR: new `TurkishLiraTR` object.
        """
        return cast(
            TurkishLiraTR,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='TRY',
                numeric_code='949',
                symbol='₤',
                localized_symbol='TR₤',
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
            TurkishLiraTR: new opbject.
        """
        return self.__class__(amount, self._info[5])
