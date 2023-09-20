# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Taka currency representation(s)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, cast

from multicurrency.pycurrency import Currency


if TYPE_CHECKING:
    from decimal import Decimal


class Taka(Currency):
    """Taka (Bangladesh) currency representation.

    Simple usage example:

        >>> from multicurrency import Taka
        >>> taka = Taka(
        ...     amount='123456.789')
        >>> print(taka)
        ১২৩,৪৫৬.৭৯৳

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%a%s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2.,3%a%s',
    ) -> Self:
        """Class creator.

        Returns:
            Taka: new `Taka` object.
        """
        return cast(
            Taka,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='BDT',
                numeric_code='050',
                symbol='৳',
                localized_symbol='৳',
                convertion='০১২৩৪৫৬৭৮৯-,.',
                pattern=pattern))

    def __recreate__(
            self: Self,
            amount: str | float | Decimal,
    ) -> Self:
        """Recreates self with a different `amount`.

        Args:
            amount (str | int | float | Decimal): Represented value.

        Returns:
            Taka: new opbject.
        """
        return self.__class__(amount, self._info[5])
