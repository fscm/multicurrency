# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Vatu currency representation(s)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, cast

from multicurrency.pycurrency import Currency


if TYPE_CHECKING:
    from decimal import Decimal


class Vatu(Currency):
    """Vatu (Vanuatu) currency representation.

    Simple usage example:

        >>> from multicurrency import Vatu
        >>> vatu = Vatu(
        ...     amount='123456.789')
        >>> print(vatu)
        Vt 123,457

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0.,3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '0.,3%s\u00A0%a',
    ) -> Self:
        """Class creator.

        Returns:
            Vatu: new `Vatu` object.
        """
        return cast(
            Vatu,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='VUV',
                numeric_code='548',
                symbol='Vt',
                localized_symbol='Vt',
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
            Vatu: new opbject.
        """
        return self.__class__(amount, self._info[5])
