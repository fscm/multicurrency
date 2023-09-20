# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Denar currency representation(s)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, cast

from multicurrency.pycurrency import Currency


if TYPE_CHECKING:
    from decimal import Decimal


class Denar(Currency):
    """Denar (Macedonia) currency representation.

    Simple usage example:

        >>> from multicurrency import Denar
        >>> denar = Denar(
        ...     amount='123456.789')
        >>> print(denar)
        123.456,79 ден.

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
            Denar: new `Denar` object.
        """
        return cast(
            Denar,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='MKD',
                numeric_code='807',
                symbol='ден.',
                localized_symbol='ден.',
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
            Denar: new opbject.
        """
        return self.__class__(amount, self._info[5])
