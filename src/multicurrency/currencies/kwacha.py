# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Kwacha currency representation(s)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, cast

from multicurrency.pycurrency import Currency


if TYPE_CHECKING:
    from decimal import Decimal


class Kwacha(Currency):
    """Kwacha (Malawi) currency representation.

    Simple usage example:

        >>> from multicurrency import Kwacha
        >>> kwacha = Kwacha(
        ...     amount='123456.789')
        >>> print(kwacha)
        MK 123,456.79

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
            Kwacha: new `Kwacha` object.
        """
        return cast(
            Kwacha,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='MWK',
                numeric_code='454',
                symbol='MK',
                localized_symbol='MK',
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
            Kwacha: new opbject.
        """
        return self.__class__(amount, self._info[5])


class ZambianKwacha(Currency):
    """Kwacha (Zambia) currency representation.

    Simple usage example:

        >>> from multicurrency import ZambianKwacha
        >>> zambian_kwacha = ZambianKwacha(
        ...     amount='123456.789')
        >>> print(zambian_kwacha)
        ZK 123,456.79

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
            ZambianKwacha: new `ZambianKwacha` object.
        """
        return cast(
            ZambianKwacha,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='ZMW',
                numeric_code='967',
                symbol='ZK',
                localized_symbol='ZK',
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
            ZambianKwacha: new opbject.
        """
        return self.__class__(amount, self._info[5])
