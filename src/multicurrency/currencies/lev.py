# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Lev currency representation(s)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, cast

from multicurrency.pycurrency import Currency


if TYPE_CHECKING:
    from decimal import Decimal


class BulgarianLev(Currency):
    """Lev (Bulgaria) currency representation.

    Simple usage example:

        >>> from multicurrency import BulgarianLev
        >>> bulgarian_lev = BulgarianLev(
        ...     amount='123456.789')
        >>> print(bulgarian_lev)
        123 456,79 лв.

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2,\u00A03%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            BulgarianLev: new `BulgarianLev` object.
        """
        return cast(
            BulgarianLev,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='BGN',
                numeric_code='975',
                symbol='лв.',
                localized_symbol='лв.',
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
            BulgarianLev: new opbject.
        """
        return self.__class__(amount, self._info[5])
