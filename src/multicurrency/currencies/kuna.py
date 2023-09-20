# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Kuna currency representation(s)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, cast

from multicurrency.pycurrency import Currency


if TYPE_CHECKING:
    from decimal import Decimal


class CroatianKuna(Currency):
    """Kuna (Croatia) currency representation.

    Simple usage example:

        >>> from multicurrency import CroatianKuna
        >>> croatian_kuna = CroatianKuna(
        ...     amount='123456.789')
        >>> print(croatian_kuna)
        123.456,79 Kn

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2,.3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2,.3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            CroatianKuna: new `CroatianKuna` object.
        """
        return cast(
            CroatianKuna,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='HRK',
                numeric_code='191',
                symbol='Kn',
                localized_symbol='Kn',
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
            CroatianKuna: new opbject.
        """
        return self.__class__(amount, self._info[5])
