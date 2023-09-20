# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Cedi currency representation(s)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, cast

from multicurrency.pycurrency import Currency


if TYPE_CHECKING:
    from decimal import Decimal


class Cedi(Currency):
    """Cedi (Ghana) currency representation.

    Simple usage example:

        >>> from multicurrency import Cedi
        >>> cedi = Cedi(
        ...     amount='123456.789')
        >>> print(cedi)
        ₵123,456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%-%s%u'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2.,3%-%s%u',
    ) -> Self:
        """Class creator.

        Returns:
            Cedi: new `Cedi` object.
        """
        return cast(
            Cedi,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='GHS',
                numeric_code='936',
                symbol='₵',
                localized_symbol='₵',
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
            Cedi: new opbject.
        """
        return self.__class__(amount, self._info[5])
