# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Krone currency representation(s)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, cast

from multicurrency.pycurrency import Currency


if TYPE_CHECKING:
    from decimal import Decimal


class DanishKrone(Currency):
    """Krone (Denmark) currency representation.

    Simple usage example:

        >>> from multicurrency import DanishKrone
        >>> danish_krone = DanishKrone(
        ...     amount='123456.789')
        >>> print(danish_krone)
        123.456,79 kr

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
            DanishKrone: new `DanishKrone` object.
        """
        return cast(
            DanishKrone,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='DKK',
                numeric_code='208',
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
            DanishKrone: new opbject.
        """
        return self.__class__(amount, self._info[5])


class NorwegianKrone(Currency):
    """Krone (Norway) currency representation.

    Simple usage example:

        >>> from multicurrency import NorwegianKrone
        >>> norwegian_krone = NorwegianKrone(
        ...     amount='123456.789')
        >>> print(norwegian_krone)
        kr 123 456,79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2, 3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2,\u202F3%s\u00A0%a',
    ) -> Self:
        """Class creator.

        Returns:
            NorwegianKrone: new `NorwegianKrone` object.
        """
        return cast(
            NorwegianKrone,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='NOK',
                numeric_code='578',
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
            NorwegianKrone: new opbject.
        """
        return self.__class__(amount, self._info[5])
