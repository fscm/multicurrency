# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Rand currency representation(s)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, cast

from multicurrency.pycurrency import Currency


if TYPE_CHECKING:
    from decimal import Decimal


class Rand(Currency):
    """Rand (South Africa) currency representation.

    Simple usage example:

        >>> from multicurrency import Rand
        >>> rand = Rand(
        ...     amount='123456.789')
        >>> print(rand)
        R 123 456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2. 3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2.\u202F3%s\u00A0%a',
    ) -> Self:
        """Class creator.

        Returns:
            Rand: new `Rand` object.
        """
        return cast(
            Rand,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='ZAR',
                numeric_code='710',
                symbol='R',
                localized_symbol='R',
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
            Rand: new opbject.
        """
        return self.__class__(amount, self._info[5])


class RandLS(Currency):
    """Rand (Lesotho) currency representation.

    Simple usage example:

        >>> from multicurrency import RandLS
        >>> rand_ls = RandLS(
        ...     amount='123456.789')
        >>> print(rand_ls)
        R 123,456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2.,3%s\u00A0%a',
    ) -> Self:
        """Class creator.

        Returns:
            RandLS: new `RandLS` object.
        """
        return cast(
            RandLS,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='ZAR',
                numeric_code='710',
                symbol='R',
                localized_symbol='LSR',
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
            RandLS: new opbject.
        """
        return self.__class__(amount, self._info[5])


class RandNA(Currency):
    """Rand (Namibia) currency representation.

    Simple usage example:

        >>> from multicurrency import RandNA
        >>> rand_na = RandNA(
        ...     amount='123456.789')
        >>> print(rand_na)
        R 123 456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2. 3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2.\u202F3%s\u00A0%a',
    ) -> Self:
        """Class creator.

        Returns:
            RandNA: new `RandNA` object.
        """
        return cast(
            RandNA,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='ZAR',
                numeric_code='710',
                symbol='R',
                localized_symbol='NAR',
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
            RandNA: new opbject.
        """
        return self.__class__(amount, self._info[5])


class RandZA(Currency):
    """Rand (South Africa) currency representation.

    Simple usage example:

        >>> from multicurrency import RandZA
        >>> rand_za = RandZA(
        ...     amount='123456.789')
        >>> print(rand_za)
        R 123 456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2. 3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2.\u202F3%s\u00A0%a',
    ) -> Self:
        """Class creator.

        Returns:
            RandZA: new `RandZA` object.
        """
        return cast(
            RandZA,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='ZAR',
                numeric_code='710',
                symbol='R',
                localized_symbol='ZAR',
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
            RandZA: new opbject.
        """
        return self.__class__(amount, self._info[5])
