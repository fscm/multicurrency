# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Won currency representation(s)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, cast

from multicurrency.pycurrency import Currency


if TYPE_CHECKING:
    from decimal import Decimal


class NorthKoreanWon(Currency):
    """Won (North Korea) currency representation.

    Simple usage example:

        >>> from multicurrency import NorthKoreanWon
        >>> north_korean_won = NorthKoreanWon(
        ...     amount='123456.789')
        >>> print(north_korean_won)
        ₩ 123,456.79

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
            NorthKoreanWon: new `NorthKoreanWon` object.
        """
        return cast(
            NorthKoreanWon,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='KPW',
                numeric_code='408',
                symbol='₩',
                localized_symbol='₩',
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
            NorthKoreanWon: new opbject.
        """
        return self.__class__(amount, self._info[5])


class SouthKoreanWon(Currency):
    """Won (South Korea) currency representation.

    Simple usage example:

        >>> from multicurrency import SouthKoreanWon
        >>> south_korean_won = SouthKoreanWon(
        ...     amount='123456.789')
        >>> print(south_korean_won)
        ₩123,457

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0.,3%-%s%u'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '0.,3%-%s%u',
    ) -> Self:
        """Class creator.

        Returns:
            SouthKoreanWon: new `SouthKoreanWon` object.
        """
        return cast(
            SouthKoreanWon,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='KRW',
                numeric_code='410',
                symbol='₩',
                localized_symbol='₩',
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
            SouthKoreanWon: new opbject.
        """
        return self.__class__(amount, self._info[5])
