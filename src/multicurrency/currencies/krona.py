# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Krona currency representation(s)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, cast

from multicurrency.pycurrency import Currency


if TYPE_CHECKING:
    from decimal import Decimal


class IcelandKrona(Currency):
    """Krona (Iceland) currency representation.

    Simple usage example:

        >>> from multicurrency import IcelandKrona
        >>> iceland_krona = IcelandKrona(
        ...     amount='123456.789')
        >>> print(iceland_krona)
        123.457 Kr

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0,.3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '0,.3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            IcelandKrona: new `IcelandKrona` object.
        """
        return cast(
            IcelandKrona,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='ISK',
                numeric_code='352',
                symbol='Kr',
                localized_symbol='Kr',
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
            IcelandKrona: new opbject.
        """
        return self.__class__(amount, self._info[5])


class SwedishKrona(Currency):
    """Krona (Sweden) currency representation.

    Simple usage example:

        >>> from multicurrency import SwedishKrona
        >>> swedish_krona = SwedishKrona(
        ...     amount='123456.789')
        >>> print(swedish_krona)
        123 456,79 kr

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2,\u202F3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            SwedishKrona: new `SwedishKrona` object.
        """
        return cast(
            SwedishKrona,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='SEK',
                numeric_code='752',
                symbol='kr',
                localized_symbol='kr',
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
            SwedishKrona: new opbject.
        """
        return self.__class__(amount, self._info[5])
