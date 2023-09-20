# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Oro currency representation(s)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, cast

from multicurrency.pycurrency import Currency


if TYPE_CHECKING:
    from decimal import Decimal


class CordobaOro(Currency):
    """Oro (Nicaragua) currency representation.

    Simple usage example:

        >>> from multicurrency import CordobaOro
        >>> cordoba_oro = CordobaOro(
        ...     amount='123456.789')
        >>> print(cordoba_oro)
        C$123,456.79

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
            CordobaOro: new `CordobaOro` object.
        """
        return cast(
            CordobaOro,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='NIO',
                numeric_code='558',
                symbol='C$',
                localized_symbol='C$',
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
            CordobaOro: new opbject.
        """
        return self.__class__(amount, self._info[5])
