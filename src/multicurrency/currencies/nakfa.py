# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Nakfa currency representation(s)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, cast

from multicurrency.pycurrency import Currency


if TYPE_CHECKING:
    from decimal import Decimal


class Nakfa(Currency):
    """Nakfa (Eritrea) currency representation.

    Simple usage example:

        >>> from multicurrency import Nakfa
        >>> nakfa = Nakfa(
        ...     amount='123456.789')
        >>> print(nakfa)
        Nfk 123,456.79

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
            Nakfa: new `Nakfa` object.
        """
        return cast(
            Nakfa,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='ERN',
                numeric_code='232',
                symbol='Nfk',
                localized_symbol='Nfk',
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
            Nakfa: new opbject.
        """
        return self.__class__(amount, self._info[5])
