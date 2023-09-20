# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Kyat currency representation(s)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, cast

from multicurrency.pycurrency import Currency


if TYPE_CHECKING:
    from decimal import Decimal


class Kyat(Currency):
    """Kyat (Myanmar (Burma)) currency representation.

    Simple usage example:

        >>> from multicurrency import Kyat
        >>> kyat = Kyat(
        ...     amount='123456.789')
        >>> print(kyat)
        ၁၂၃,၄၅၆.၇၉ K

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2.,3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            Kyat: new `Kyat` object.
        """
        return cast(
            Kyat,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='MMK',
                numeric_code='104',
                symbol='K',
                localized_symbol='K',
                convertion='၀၁၂၃၄၅၆၇၈၉-',
                pattern=pattern))

    def __recreate__(
            self: Self,
            amount: str | float | Decimal,
    ) -> Self:
        """Recreates self with a different `amount`.

        Args:
            amount (str | int | float | Decimal): Represented value.

        Returns:
            Kyat: new opbject.
        """
        return self.__class__(amount, self._info[5])
