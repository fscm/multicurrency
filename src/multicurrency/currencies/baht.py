# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Baht currency representation(s)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, cast

from multicurrency.pycurrency import Currency


if TYPE_CHECKING:
    from decimal import Decimal


class Baht(Currency):
    """Baht (Thailand) currency representation.

    Simple usage example:

        >>> from multicurrency import Baht
        >>> baht = Baht(
        ...     amount='123456.789')
        >>> print(baht)
        ฿123,456.79

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
            Baht: new `Baht` object.
        """
        return cast(
            Baht,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='THB',
                numeric_code='764',
                symbol='฿',
                localized_symbol='฿',
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
            Baht: new opbject.
        """
        return self.__class__(amount, self._info[5])
