# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Somoni currency representation(s)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, cast

from multicurrency.pycurrency import Currency


if TYPE_CHECKING:
    from decimal import Decimal


class Somoni(Currency):
    """Somoni (Tajikistan) currency representation.

    Simple usage example:

        >>> from multicurrency import Somoni
        >>> somoni = Somoni(
        ...     amount='123456.789')
        >>> print(somoni)
        ЅМ 123,456.79

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
            Somoni: new `Somoni` object.
        """
        return cast(
            Somoni,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='TJS',
                numeric_code='972',
                symbol='ЅМ',
                localized_symbol='ЅМ',
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
            Somoni: new opbject.
        """
        return self.__class__(amount, self._info[5])
