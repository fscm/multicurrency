# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Dram currency representation(s)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, cast

from multicurrency.pycurrency import Currency


if TYPE_CHECKING:
    from decimal import Decimal


class ArmenianDram(Currency):
    """Dram (Armenia) currency representation.

    Simple usage example:

        >>> from multicurrency import ArmenianDram
        >>> armenian_dram = ArmenianDram(
        ...     amount='123456.789')
        >>> print(armenian_dram)
        123 456,79 Դ

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
            ArmenianDram: new `ArmenianDram` object.
        """
        return cast(
            ArmenianDram,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='AMD',
                numeric_code='051',
                symbol='Դ',
                localized_symbol='Դ',
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
            ArmenianDram: new opbject.
        """
        return self.__class__(amount, self._info[5])
