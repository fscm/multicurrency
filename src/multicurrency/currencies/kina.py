# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Kina currency representation(s)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, cast

from multicurrency.pycurrency import Currency


if TYPE_CHECKING:
    from decimal import Decimal


class Kina(Currency):
    """Kina (Papua New Guinea) currency representation.

    Simple usage example:

        >>> from multicurrency import Kina
        >>> kina = Kina(
        ...     amount='123456.789')
        >>> print(kina)
        K 123,456.79

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
            Kina: new `Kina` object.
        """
        return cast(
            Kina,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='PGK',
                numeric_code='598',
                symbol='K',
                localized_symbol='K',
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
            Kina: new opbject.
        """
        return self.__class__(amount, self._info[5])
