# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Metical currency representation(s)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, cast

from multicurrency.pycurrency import Currency


if TYPE_CHECKING:
    from decimal import Decimal


class Metical(Currency):
    """Metical (Mozambique) currency representation.

    Simple usage example:

        >>> from multicurrency import Metical
        >>> metical = Metical(
        ...     amount='123456.789')
        >>> print(metical)
        123.457 MTn

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0,.3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '0,.3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            Metical: new `Metical` object.
        """
        return cast(
            Metical,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='MZN',
                numeric_code='943',
                symbol='MTn',
                localized_symbol='MTn',
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
            Metical: new opbject.
        """
        return self.__class__(amount, self._info[5])
