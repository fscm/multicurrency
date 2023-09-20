# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Dobra currency representation(s)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, cast

from multicurrency.pycurrency import Currency


if TYPE_CHECKING:
    from decimal import Decimal


class Dobra(Currency):
    """Dobra (Sao Tome and Principe) currency representation.

    Simple usage example:

        >>> from multicurrency import Dobra
        >>> dobra = Dobra(
        ...     amount='123456.789')
        >>> print(dobra)
        123.456,79 Db

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
            Dobra: new `Dobra` object.
        """
        return cast(
            Dobra,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='STN',
                numeric_code='930',
                symbol='Db',
                localized_symbol='Db',
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
            Dobra: new opbject.
        """
        return self.__class__(amount, self._info[5])
